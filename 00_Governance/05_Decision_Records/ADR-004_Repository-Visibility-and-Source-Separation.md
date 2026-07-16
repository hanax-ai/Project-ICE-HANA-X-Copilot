# ADR-004: Public Canonical Repository With Governed Source Controls

**Status:** Accepted
**Date:** 2026-07-16
**Owner:** HANA-X AI

## Context

Project ICE contains governed publication assets, internal source evidence, working records, specifications, and architecture discovery material.

An earlier remediation path recommended a private canonical repository plus a sanitized public mirror. The founder has since authorized the canonical Project ICE repository to remain public and non-redacted for the current source corpus.

Public repository authorization does not reduce the need for confidentiality review, source immutability, evidence tracking, or claim governance.

## Decision

The Project ICE repository may remain public as the canonical governed repository, provided that the following controls remain in force:

- public repository authorization is recorded in `PROJECT_MANIFEST.yaml`;
- original source evidence remains immutable after intake;
- every source has an ID, manifest, register entry, authority tier, and SHA-256 hash;
- secrets, SAP credentials, access tokens, customer data, and unauthorized third-party material are prohibited;
- AI-generated and exploratory material is clearly labeled by authority tier;
- published claims require evidence or a recorded risk-acceptance exception;
- all substantive changes pass governance workflows and code-owner review.

## Consequences

- The source-integrity workflow must permit the founder-authorized public source-corpus model when the Project Manifest explicitly allows it.
- The workflow must continue to fail if public restricted-source exposure occurs without manifest authorization.
- Confidentiality screening remains mandatory for new source intake.
- A sanitized mirror remains available as an optional downstream distribution mechanism, not the canonical source of truth.
