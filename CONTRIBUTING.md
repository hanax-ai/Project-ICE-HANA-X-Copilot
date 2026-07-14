# Contributing to Project ICE

## Branching

Create focused branches using `agent/<description>`, `author/<artifact-id>-<description>`, or `review/<artifact-id>-<review-type>`. Do not author directly on `main`.

## Pull requests

Every pull request must identify the affected artifact IDs, source IDs, claim IDs, requirement IDs, figures, and review gates. Use the repository pull-request template.

## Content controls

- Never edit files under an `Originals/` directory.
- Never overwrite a published artifact or release.
- Update the relevant register when adding, superseding, or withdrawing an artifact.
- Keep binary originals and delivery formats separate from canonical Markdown and metadata.
- Retain editable source files for every published figure.
- Do not commit secrets, SAP credentials, tokens, customer data, or proprietary third-party material without documented rights.

## Review gates

At minimum, substantive publication content requires editorial, technical, citation, and executive review. SAP integration, security, competitive, cost, licensing, and market claims require their specialist reviews.

## Commit messages

Use short, intentional messages that describe the governed change, for example:

```text
Add Project ICE source and claims registers
Draft ICE-CH-03 enterprise intent architecture
Approve ICE-FIG-005 procurement workflow
```
