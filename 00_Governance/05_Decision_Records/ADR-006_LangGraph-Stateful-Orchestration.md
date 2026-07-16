# ADR-006: Use LangGraph as the durable stateful orchestration runtime

**Status:** Proposed
**Date:** 2026-07-16
**Owner:** HANA-X AI Architecture
**Derived from:** ICE-SRC-008 and ICE-ARCH-001

## Context

SAP workflows are multi-step, stateful, failure-prone, and often require clarification, approval, retries, and resumability.

## Decision

Use LangGraph to model explicit subgraphs for intake, clarification, retrieval, planning, approval, governed tool execution, validation, and exception handling. Do not rely on an unconstrained agent loop for high-risk writes.

## Consequences

- Workflow state can be checkpointed and resumed.
- Policy and approval gates become explicit nodes.
- Graph and state migrations require versioning and backward-compatibility tests.

## Validation and follow-up

- Select and benchmark a production checkpointer.
- Define graph versioning, migration, and recovery procedures.

## References

- `05_Architecture/02_Component_Architecture/ICE-ARCH-001_HANA-X-Copilot-Solution-Architecture/References/ICE-ARCH-001_References.md`
