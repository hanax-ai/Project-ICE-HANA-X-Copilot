# Contributing to Project ICE

## Branching

Project ICE uses exactly two persistent branches:

- `main` — the protected production-truth branch containing reviewed and accepted repository state.
- `working` — the sole authoring, integration, and review-preparation branch.

All repository changes must be committed to `working`. When a governed change set is ready, open a pull request from `working` into `main`. After the pull request is merged, synchronize `working` to the resulting `main` commit before beginning the next change set.

Do not create `feature/`, `agent/`, `author/`, `review/`, release, or personal branches. Additional branches are not part of the Project ICE operating model and are removed automatically by the branch-hygiene workflow.

Do not author directly on `main`.

## Pull requests

Every pull request must:

- use `working` as the head branch and `main` as the base branch;
- identify the affected artifact IDs, source IDs, claim IDs, requirement IDs, figures, and review gates;
- use the repository pull-request template;
- pass all required governance checks before merge.

Only one Project ICE pull request should normally be open at a time because `working` is the single integration branch.

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
