# ADR-010: Use PostgreSQL as the authoritative context record and Qdrant as a rebuildable retrieval index

**Status:** Proposed
**Date:** 2026-07-16
**Owner:** HANA-X AI Architecture
**Derived from:** ICE-SRC-008 and ICE-ARCH-001

## Context

The solution requires exact structured queries, transactional state, artifact provenance, and semantic retrieval. PostgreSQL and Qdrant do not share one ordinary atomic transaction.

## Decision

Store canonical artifacts, metadata, jobs, state, entities, policies, and audit evidence in PostgreSQL. Store dense/sparse vectors and filterable payloads in Qdrant. Synchronize through a transactional outbox and idempotent indexing workers.

## Consequences

- PostgreSQL remains the source of truth.
- Qdrant can be rebuilt and reconciled.
- Indexing becomes eventually consistent and must expose status and retry state.

## Validation and follow-up

- Define chunking and embedding version strategy.
- Implement reconciliation, re-indexing, deletion, and recovery tests.

## References

- `05_Architecture/02_Component_Architecture/ICE-ARCH-001_HANA-X-Copilot-Solution-Architecture/References/ICE-ARCH-001_References.md`
