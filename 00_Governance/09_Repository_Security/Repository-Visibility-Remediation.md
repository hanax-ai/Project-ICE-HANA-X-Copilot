# Repository Visibility Remediation

## Risk

The canonical repository contains source records classified as internal and restricted to project use. A public repository exposes those files and their Git history.

## Immediate preferred action

Make `hanax-ai/Project-ICE-HANA-X-Copilot` private before importing any additional internal, customer, conversation-history, or AI research source documents.

Run:

```bash
CONFIRM_VISIBILITY_CHANGE=YES \
  bash 00_Governance/09_Repository_Security/scripts/make_repository_private.sh
```

Verify the result in GitHub repository settings and with:

```bash
gh repo view hanax-ai/Project-ICE-HANA-X-Copilot --json visibility
```

## Public distribution model

Approved PDFs, HTML pages, product sheets, and other intentionally public assets may be published through the HANA-X website, a release channel, or a separate sanitized public mirror.

To build a sanitized mirror working tree:

```bash
bash 00_Governance/09_Repository_Security/scripts/create_sanitized_public_mirror.sh \
  /path/to/Project-ICE-HANA-X-Copilot \
  /path/to/Project-ICE-HANA-X-Copilot-Public
```

Review the generated tree before publishing it. The script does not create or push a GitHub repository.

## Important history rule

Deleting restricted files in a new commit does not remove them from previous commits. Do not attempt an ad hoc force-push. Preserve the canonical history in a private repository and create a new sanitized mirror for public use.

## Verification checklist

- [ ] Canonical repository visibility is private.
- [ ] Branch protection is enabled on `main`.
- [ ] Source-integrity and register-validation workflows pass.
- [ ] Public mirrors contain no restricted original, normalized source, summary, working note, credential, customer record, or private review artifact.
- [ ] Published claims have evidence or an active risk-acceptance record.
