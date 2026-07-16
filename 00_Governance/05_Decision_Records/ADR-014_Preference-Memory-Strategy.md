# ADR-014: Keep preference memory optional and begin with explicit PostgreSQL records

**Status:** Proposed
**Date:** 2026-07-16
**Owner:** HANA-X AI Architecture
**Derived from:** ICE-SRC-008 and ICE-ARCH-001

## Context

The Copilot may benefit from recurring user defaults, but opaque memory extraction can introduce stale, conflicting, or unauthorized values.

## Decision

Start with explicit, inspectable preference records in PostgreSQL. Evaluate Mem0 or another specialized memory service only if benchmarks show material improvement in extraction, conflict resolution, retrieval relevance, deletion, privacy, and local operation.

## Consequences

- Users can inspect and correct remembered preferences.
- Preferences cannot override current SAP data, required values, or policy.
- An additional memory service is not required for the baseline.

## Validation and follow-up

- Define preference ownership, confidence, expiration, and correction flows.
- Benchmark native records against a specialized memory service.

## References

- `05_Architecture/02_Component_Architecture/ICE-ARCH-001_HANA-X-Copilot-Solution-Architecture/References/ICE-ARCH-001_References.md`
