# ADR-004: Separate Restricted Source Evidence from Public Publication Assets

**Status:** Accepted
**Date:** 2026-07-14
**Owner:** HANA-X AI

## Context

Project ICE contains two classes of information:

1. approved publication assets intended for external distribution; and
2. internal source evidence, working records, specifications, and conversation history that may be restricted to project use.

A public repository cannot safely contain restricted source evidence. Removing a file in a later commit does not remove it from Git history.

## Decision

The canonical Project ICE repository must be private whenever it contains restricted source evidence. Public distribution must occur through approved deliverables or a separately generated sanitized public mirror.

The repository must enforce the following controls:

- restricted originals are prohibited in a public repository;
- original evidence is immutable after intake;
- every source has an ID, manifest, register entry, authority tier, and hash;
- public mirrors exclude restricted source packages and private working records;
- changing repository visibility or creating a public mirror requires an explicit administrative action and verification;
- publication artifacts may be public only after their review status and any accepted exceptions are recorded.

## Supported implementation paths

### Path A - Private canonical repository (preferred)

Make the existing canonical repository private. Continue to store governed source evidence and publication work in the same repository. Publish approved PDFs, HTML, and other approved outputs separately.

### Path B - Sanitized public mirror

Keep the canonical repository private and generate a separate public mirror containing only approved public artifacts, non-sensitive governance material, and sanitized metadata. Do not copy restricted originals, normalized restricted content, internal working notes, or private review records.

## Consequences

- The current public repository must be made private before additional restricted material is imported.
- A public mirror, if required, is a derived distribution channel and not the source of truth.
- Source-intake and repository-visibility checks must run in CI.
- Any history containing restricted material must remain private or be replaced by a sanitized mirror; deleting files from the current branch is insufficient.
