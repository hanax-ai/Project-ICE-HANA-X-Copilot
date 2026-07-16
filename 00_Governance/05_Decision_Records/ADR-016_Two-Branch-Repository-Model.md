# ADR-016: Operate Project ICE with Main and Working Branches Only

**Status:** Accepted  
**Date:** 2026-07-16  
**Owner:** HANA-X AI

## Context

Project ICE previously used short-lived `agent/`, `author/`, and `review/` branches. As the publication repository evolved, completed and superseded branches accumulated and made it harder to identify the authoritative work in progress.

The repository owner directed that Project ICE retain only one production branch and one active working branch.

## Decision

Project ICE will use exactly two persistent branches:

1. `main` is the protected production-truth branch.
2. `working` is the sole authoring, integration, and review-preparation branch.

All changes are developed on `working`. Governed change sets move from `working` to `main` through a pull request. After merge, `working` is synchronized to the resulting `main` commit before the next workstream begins.

No `feature/`, `agent/`, `author/`, `review/`, release, or personal branches are permitted. The branch-hygiene workflow removes every branch other than `main` and `working` after a push to `main` and may also be run manually.

## Controls

- `PROJECT_MANIFEST.yaml` records `main` and `working` as the only allowed branches.
- `CONTRIBUTING.md` defines the working-to-main lifecycle.
- `.github/PULL_REQUEST_TEMPLATE.md` requires `working` as head and `main` as base.
- `.github/workflows/branch-hygiene.yml` enforces the allowed branch set.
- The register and manifest validator checks the declared two-branch policy.

## Consequences

### Benefits

- One clearly identifiable body of active work.
- No abandoned feature branches.
- Simpler pull-request and review coordination.
- Easier synchronization for Agent Zero, Claude, and human contributors.
- Reduced risk of publishing or reviewing the wrong branch.

### Tradeoffs

- Parallel workstreams must coordinate within `working` rather than using separate branches.
- Only one principal pull request should normally be open at a time.
- `working` must be synchronized immediately after every merge to prevent divergence.

## Supersedes

This decision supersedes the branch-prefix guidance previously recorded in `CONTRIBUTING.md` and `PROJECT_MANIFEST.yaml`.
