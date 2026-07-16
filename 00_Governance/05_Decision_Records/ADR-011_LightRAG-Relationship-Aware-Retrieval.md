# ADR-011: Evaluate LightRAG for relationship-aware retrieval

**Status:** Proposed
**Date:** 2026-07-16
**Owner:** HANA-X AI Architecture
**Derived from:** ICE-SRC-008 and ICE-ARCH-001

## Context

Vector retrieval alone may miss multi-hop relationships across documents, messages, and SAP-related entities.

## Decision

Evaluate LightRAG as an optional graph-assisted retrieval layer. Its exact storage adapters, identifiers, deletion semantics, citation behavior, and overlap with PostgreSQL/Qdrant must be validated before production adoption.

## Consequences

- LightRAG may improve multi-hop context assembly.
- Uncontrolled duplication and ambiguous data ownership must be avoided.
- The component remains optional until benchmarked.

## Validation and follow-up

- Benchmark retrieval quality against hybrid Qdrant retrieval.
- Document storage ownership, deletion, re-indexing, and citation provenance.

## References

- `05_Architecture/02_Component_Architecture/ICE-ARCH-001_HANA-X-Copilot-Solution-Architecture/References/ICE-ARCH-001_References.md`
