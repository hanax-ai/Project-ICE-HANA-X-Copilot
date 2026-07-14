# Repository Security and Source Handling

This area governs repository visibility, source confidentiality, branch protection, public-mirror generation, and the automated controls that protect Project ICE evidence and releases.

## Required posture

- The canonical repository must be private while restricted source evidence is present.
- Approved public deliverables may be distributed independently.
- A public Git repository must be a sanitized mirror, not the canonical evidence repository.
- Files under an `Originals/` directory are immutable after intake.

## Administrative tools

- `scripts/make_repository_private.sh` - preferred immediate remediation.
- `scripts/create_sanitized_public_mirror.sh` - produces a new public-safe working tree.
- `scripts/configure_branch_protection.sh` - configures the required protection for `main`.

Read `Repository-Visibility-Remediation.md` before running an administrative script.
