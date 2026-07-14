#!/usr/bin/env python3
import hashlib
from pathlib import Path
import sys
import yaml


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    root = Path.cwd()
    errors = []
    releases = list(root.glob("12_Releases/**/Release_Manifest.yaml"))

    for manifest in releases:
        release_dir = manifest.parent
        data = yaml.safe_load(manifest.read_text(encoding="utf-8")) or {}
        checksum_path = release_dir / "SHA256SUMS.txt"
        if not checksum_path.exists():
            errors.append(f"Missing SHA256SUMS.txt: {release_dir}")
            continue
        checksums = {}
        for line in checksum_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            digest, relative = line.split(None, 1)
            checksums[relative.strip()] = digest
        manifest_files = {item["path"]: item["sha256"] for item in data.get("files", [])}
        if checksums != manifest_files:
            errors.append(f"Manifest/checksum file list mismatch: {release_dir}")
        for relative, expected in manifest_files.items():
            target = release_dir / relative
            if not target.exists():
                errors.append(f"Missing release file: {target}")
            elif sha256(target) != expected:
                errors.append(f"Release hash mismatch: {target}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Release integrity passed for {len(releases)} release manifests.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
