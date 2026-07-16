# ADR-009: Use MCP as the governed SAP tool-adaptation boundary

**Status:** Proposed
**Date:** 2026-07-16
**Owner:** HANA-X AI Architecture
**Derived from:** ICE-SRC-008 and ICE-ARCH-001

## Context

The agent requires a standard and reusable way to discover and execute enterprise capabilities without constructing arbitrary SAP URLs.

## Decision

Expose versioned SAP business capabilities through an MCP tool service that performs schema mapping, validation, identity and policy enforcement, CSRF/ETag handling, idempotency, retries, SAP error normalization, audit evidence, and response minimization.

## Consequences

- Agent orchestration is decoupled from SAP transport details.
- Tools become explicit, testable contracts.
- The MCP service is not the sole security boundary; backend authorization remains mandatory.

## Validation and follow-up

- Define procurement tool contracts and endpoint compatibility matrix.
- Threat-model tool discovery, prompt injection, and confused-deputy risks.

## References

- `05_Architecture/02_Component_Architecture/ICE-ARCH-001_HANA-X-Copilot-Solution-Architecture/References/ICE-ARCH-001_References.md`
