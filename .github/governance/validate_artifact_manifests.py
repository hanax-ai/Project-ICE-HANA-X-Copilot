#!/usr/bin/env python3
import csv
import hashlib
from pathlib import Path
import sys
import yaml

REQUIRED = {"artifact_id", "title", "status", "version", "owner", "source_ids"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    root = Path.cwd()
    errors = []
    artifacts = {row["Artifact ID"]: row for row in csv.DictReader((root / "01_Registers/ICE_Artifact_Register.csv").open(encoding="utf-8", newline=""))}
    manifests = list(root.glob("04_White_Paper/**/artifact-manifest.yaml"))

    for path in manifests:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        missing = sorted(REQUIRED - data.keys())
        if missing:
            errors.append(f"Missing keys in {path}: {', '.join(missing)}")
            continue
        artifact_id = data["artifact_id"]
        row = artifacts.get(artifact_id)
        if row is None:
            errors.append(f"Manifest has no Artifact Register row: {artifact_id}")
            continue
        if str(row["Version"]) != str(data["version"]):
            errors.append(f"Version mismatch for {artifact_id}")
        if row["Status"] != data["status"]:
            errors.append(f"Status mismatch for {artifact_id}")

        publication_paths = data.get("publication_paths", {}) or {}
        hashes = data.get("sha256", {}) or {}
        for key, relative in publication_paths.items():
            target = root / relative
            if not target.exists():
                errors.append(f"Missing publication path for {artifact_id}: {relative}")
            if key in {"approved_docx", "published_pdf"} and hashes.get(key) and target.exists():
                if sha256(target) != hashes[key]:
                    errors.append(f"Hash mismatch for {artifact_id} {key}")

        claims_status = str((data.get("review_status", {}) or {}).get("claims_and_legal", "")).lower()
        if data.get("status") == "PUBLISHED" and "outstanding" in claims_status:
            record = data.get("risk_acceptance_record")
            if not record:
                errors.append(f"Published artifact with outstanding claims lacks risk_acceptance_record: {artifact_id}")
            elif not (root / record).exists():
                errors.append(f"Risk acceptance record missing for {artifact_id}: {record}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Artifact manifest validation passed for {len(manifests)} manifests.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
