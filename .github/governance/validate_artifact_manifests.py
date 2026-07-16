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


def manifest_paths(root: Path):
    paths = set(root.glob("04_White_Paper/**/artifact-manifest.yaml"))
    paths.update(root.glob("05_Architecture/**/artifact-manifest.yaml"))
    return sorted(paths)


def main():
    root = Path.cwd()
    errors = []
    artifacts = {
        row["Artifact ID"]: row
        for row in csv.DictReader(
            (root / "01_Registers/ICE_Artifact_Register.csv").open(
                encoding="utf-8", newline=""
            )
        )
    }
    manifests = manifest_paths(root)

    for path in manifests:
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as exc:
            errors.append(f"Invalid YAML in {path}: {exc}")
            continue

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

        governed_paths = {}
        for field in ("publication_paths", "canonical_paths"):
            value = data.get(field, {}) or {}
            if not isinstance(value, dict):
                errors.append(f"{field} must be a mapping for {artifact_id}")
                continue
            governed_paths.update(value)

        hashes = data.get("sha256", {}) or {}
        if hashes and not isinstance(hashes, dict):
            errors.append(f"sha256 must be a mapping for {artifact_id}")
            hashes = {}

        for key, relative in governed_paths.items():
            target = root / str(relative)
            if not target.exists():
                errors.append(f"Missing governed path for {artifact_id}: {relative}")
                continue
            expected = hashes.get(key)
            if expected and sha256(target) != expected:
                errors.append(f"Hash mismatch for {artifact_id} {key}")

        # Requirement files may be stored outside canonical_paths but still hashed.
        requirements_path = data.get("requirements_path")
        if requirements_path:
            target = root / requirements_path
            if not target.exists():
                errors.append(
                    f"Missing requirements path for {artifact_id}: {requirements_path}"
                )
            elif hashes.get("requirements") and sha256(target) != hashes["requirements"]:
                errors.append(f"Hash mismatch for {artifact_id} requirements")

        claims_status = str(
            (data.get("review_status", {}) or {}).get("claims_and_legal", "")
        ).lower()
        if data.get("status") == "PUBLISHED" and "outstanding" in claims_status:
            record = data.get("risk_acceptance_record")
            if not record:
                errors.append(
                    f"Published artifact with outstanding claims lacks risk_acceptance_record: {artifact_id}"
                )
            elif not (root / record).exists():
                errors.append(
                    f"Risk acceptance record missing for {artifact_id}: {record}"
                )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Artifact manifest validation passed for {len(manifests)} manifests.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
