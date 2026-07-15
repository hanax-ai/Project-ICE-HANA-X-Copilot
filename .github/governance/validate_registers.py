#!/usr/bin/env python3
import csv
from pathlib import Path
import re
import sys

import yaml

SOURCE_STATUSES = {"Proposed", "Accepted", "Verified", "Superseded", "Withdrawn"}
ARTIFACT_STATUSES = {"PLANNED", "SCAFFOLDED", "DRAFT", "IN-REVIEW", "APPROVED", "PUBLISHED", "SUPERSEDED", "WITHDRAWN"}


class UniqueKeyLoader(yaml.SafeLoader):
    """YAML loader that rejects duplicate mapping keys."""


def construct_unique_mapping(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key: {key}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    construct_unique_mapping,
)


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


def validate_project_manifest(root, errors):
    path = root / "PROJECT_MANIFEST.yaml"
    try:
        data = yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f"PROJECT_MANIFEST.yaml is invalid: {exc}")
        return

    if not isinstance(data, dict):
        errors.append("PROJECT_MANIFEST.yaml must contain a top-level mapping")
        return

    for key in ("project", "repository", "publication", "source_register", "controls", "governance_automation"):
        if key not in data:
            errors.append(f"PROJECT_MANIFEST.yaml missing top-level key: {key}")

    repository = data.get("repository", {}) or {}
    prefixes = repository.get("working_branch_prefixes")
    if prefixes != ["agent/", "author/", "review/"]:
        errors.append("PROJECT_MANIFEST.yaml working_branch_prefixes must be agent/, author/, review/")

    visibility = repository.get("visibility_policy", {}) or {}
    if visibility.get("restricted_sources_allowed_when_public") is not False:
        errors.append("PROJECT_MANIFEST.yaml must prohibit restricted sources in a public repository")


def main():
    root = Path.cwd()
    errors = []

    validate_project_manifest(root, errors)

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
    print(
        "Register and project-manifest validation passed: "
        f"{len(sources)} sources, {len(artifacts)} artifacts, "
        f"{len(claims)} claims, {len(decisions)} decisions."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
