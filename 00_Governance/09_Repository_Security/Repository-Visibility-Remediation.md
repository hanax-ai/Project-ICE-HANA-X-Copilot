# Repository Visibility and Public Source-Corpus Policy

## Decision update

The Project ICE canonical repository is approved to remain public and non-redacted for the current governed source corpus. The founder has authorized this public repository model for Project ICE.

The public authorization does **not** permit secrets, SAP credentials, access tokens, customer data, private third-party licensed material, or confidential customer implementation data to be committed.

## Current policy

- The canonical repository may remain public.
- Approved Project ICE source materials may remain visible in the repository.
- Original evidence remains immutable after intake.
- Every source must have an ID, manifest, register entry, authority tier, and SHA-256 hash.
- Publication claims continue to require evidence or an active risk-acceptance record.
- New source files still require confidentiality and rights review before intake.

## Public distribution model

The repository itself is the governed public source of truth for Project ICE. Website pages, PDFs, executive presentations, or other assets may also be published through HANA-X distribution channels after approval.

A sanitized mirror is no longer required for the current Project ICE corpus, but the mirror tooling remains available if a future distribution channel needs a subset-only publication package.

## Important history rule

Do not attempt ad hoc redaction or force-push history rewrites unless a future security incident requires it. Any future removal decision must be handled through a formal governance record.

## Verification checklist

- [x] Public repository authorization is recorded in `PROJECT_MANIFEST.yaml`.
- [x] Source-integrity and register-validation workflows enforce register and hash consistency.
- [x] Original evidence remains immutable.
- [ ] Branch protection is enabled on `main` after all required checks are green.
- [ ] New sources are screened for credentials, customer data, and publication rights before intake.
