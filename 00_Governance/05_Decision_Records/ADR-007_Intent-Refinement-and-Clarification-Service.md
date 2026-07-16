# ADR-007: Create an Intent Refinement and Clarification Service

**Status:** Proposed
**Date:** 2026-07-16
**Owner:** HANA-X AI Architecture
**Derived from:** ICE-SRC-008 and ICE-ARCH-001

## Context

Natural-language business requests are frequently incomplete or ambiguous. A hidden prompt rewriter does not provide sufficient transparency or control for enterprise execution.

## Decision

Implement a dedicated service/subgraph that resolves entities, checks registered tool schemas, asks targeted questions, presents governed choices, enforces a configurable clarification budget, and shows the final plan before sensitive execution.

## Consequences

- Clarification becomes a first-class collaboration experience.
- Questions and options must be grounded in authorized data.
- The workflow stops safely when required fields remain unresolved.

## Validation and follow-up

- Validate question quality and user completion rates.
- Define process-specific clarification budgets and fallback behavior.

## References

- `05_Architecture/02_Component_Architecture/ICE-ARCH-001_HANA-X-Copilot-Solution-Architecture/References/ICE-ARCH-001_References.md`
