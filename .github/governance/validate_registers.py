#!/usr/bin/env python3
import csv
from pathlib import Path
import re
import sys

SOURCE_STATUSES = {"Proposed", "Accepted", "Verified", "Superseded", "Withdrawn"}
ARTIFACT_STATUSES = {"PLANNED", "SCAFFOLDED", "DRAFT", "IN-REVIEW", "APPROVED", "PUBLISHED", "SUPERSEDED", "WITHDRAWN"}


def load(path):
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def unique(rows, field, errors, label):
    seen = set()
    for row in rows:
        value = row.get(field, "").strip()
        if not value:
            errors.append(f"{label}: empty {field}")
        elif value in seen:
            errors.append(f"{label}: duplicate {field} {value}")
        seen.add(value)


def main():
    root = Path.cwd()
    errors = []

    sources = load(root / "01_Registers/ICE_Source_Register.csv")
    unique(sources, "Source ID", errors, "Source Register")
    for row in sources:
        if not re.fullmatch(r"ICE-SRC-[0-9]{3}", row["Source ID"]):
            errors.append(f"Invalid Source ID: {row['Source ID']}")
        if row["Status"] not in SOURCE_STATUSES:
            errors.append(f"Invalid source status for {row['Source ID']}: {row['Status']}")
        path = row.get("Repository path", "").strip()
        if path and not (root / path).exists():
            errors.append(f"Registered source path missing for {row['Source ID']}: {path}")

    artifacts = load(root / "01_Registers/ICE_Artifact_Register.csv")
    unique(artifacts, "Artifact ID", errors, "Artifact Register")
    for row in artifacts:
        if row["Status"] not in ARTIFACT_STATUSES:
            errors.append(f"Invalid artifact status for {row['Artifact ID']}: {row['Status']}")
        path = row.get("Repository path", "").strip()
        if path and not (root / path).exists():
            errors.append(f"Registered artifact path missing for {row['Artifact ID']}: {path}")

    claims = load(root / "01_Registers/ICE_Claims_Register.csv")
    unique(claims, "Claim ID", errors, "Claims Register")

    decisions = load(root / "01_Registers/ICE_Decision_Register.csv")
    unique(decisions, "Decision ID", errors, "Decision Register")
    for row in decisions:
        path = row.get("Path", "").strip()
        if path and not (root / path).exists():
            errors.append(f"Decision path missing for {row['Decision ID']}: {path}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Register validation passed: {len(sources)} sources, {len(artifacts)} artifacts, {len(claims)} claims, {len(decisions)} decisions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
