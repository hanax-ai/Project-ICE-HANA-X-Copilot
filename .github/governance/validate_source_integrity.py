#!/usr/bin/env python3
import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import yaml

ALLOWED_SOURCE_STATUSES = {"Proposed", "Accepted", "Verified", "Superseded", "Withdrawn"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def fail(errors):
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


def repository_is_public() -> bool:
    value = os.environ.get("GITHUB_REPOSITORY_PRIVATE", "").strip().lower()
    if value in {"true", "false"}:
        return value == "false"
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if event_path and Path(event_path).exists():
        data = json.loads(Path(event_path).read_text(encoding="utf-8"))
        private = data.get("repository", {}).get("private")
        if isinstance(private, bool):
            return not private
    return False


def changed_originals(base_ref: str):
    command = ["git", "diff", "--name-status", f"{base_ref}...HEAD", "--", "02_Source_Materials"]
    result = subprocess.run(command, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        return [], [f"Unable to inspect Git diff against {base_ref}: {result.stderr.strip()}"]
    violations = []
    for line in result.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        status, path = parts[0], parts[-1]
        if "/Originals/" in path and status[0] in {"M", "D", "R"}:
            violations.append(f"Immutable original changed or deleted: {status} {path}")
    return violations, []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", default="")
    args = parser.parse_args()
    root = Path.cwd()
    errors = []

    register_path = root / "01_Registers/ICE_Source_Register.csv"
    rows = list(csv.DictReader(register_path.open(encoding="utf-8", newline="")))
    ids = {row["Source ID"] for row in rows}

    restricted = [row for row in rows if "restricted" in row.get("License or rights", "").lower()]
    if repository_is_public() and restricted:
        errors.append("Repository is public while restricted source records are present: " + ", ".join(row["Source ID"] for row in restricted))

    manifests = list(root.glob("02_Source_Materials/**/Metadata/ICE-SRC-*_manifest.yaml"))
    manifest_ids = set()
    for manifest_path in manifests:
        data = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
        source_id = data.get("source_id")
        manifest_ids.add(source_id)
        if source_id not in ids:
            errors.append(f"Manifest has no Source Register entry: {manifest_path}")
        if data.get("status") not in ALLOWED_SOURCE_STATUSES:
            errors.append(f"Invalid source status in {manifest_path}: {data.get('status')}")
        if data.get("originals_immutable") is not True:
            errors.append(f"originals_immutable must be true: {manifest_path}")

        checks = []
        if isinstance(data.get("current_original"), dict):
            checks.append(data["current_original"])
        for item in data.get("previous_originals", []) or []:
            if isinstance(item, dict):
                checks.append(item)
        if data.get("sha256"):
            package = manifest_path.parent.parent
            originals = [p for p in (package / "Originals").iterdir() if p.is_file() and p.name not in {"README.md", "SOURCE-LOCATION.md"}]
            if len(originals) == 1:
                checks.append({"path": str(originals[0].relative_to(root)), "sha256": data["sha256"]})
            elif len(originals) > 1:
                errors.append(f"Top-level sha256 is ambiguous because multiple originals exist: {manifest_path}")

        for item in checks:
            path = root / str(item.get("path", ""))
            expected = str(item.get("sha256", ""))
            if not path.exists():
                errors.append(f"Registered original does not exist: {path}")
            elif expected and sha256(path) != expected:
                errors.append(f"SHA-256 mismatch: {path}")

    for source_id in ids:
        if source_id != "ICE-SRC-001" and source_id not in manifest_ids:
            errors.append(f"Source Register entry has no manifest: {source_id}")

    if args.base_ref:
        violations, diff_errors = changed_originals(args.base_ref)
        errors.extend(violations)
        errors.extend(diff_errors)

    if not errors:
        print(f"Source integrity passed for {len(rows)} registered sources and {len(manifests)} manifests.")
    return fail(errors)


if __name__ == "__main__":
    sys.exit(main())
