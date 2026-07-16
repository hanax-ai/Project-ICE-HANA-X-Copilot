# ADR-008: Use Ollama as the on-premises model-serving boundary

**Status:** Proposed
**Date:** 2026-07-16
**Owner:** HANA-X AI Architecture
**Derived from:** ICE-SRC-008 and ICE-ARCH-001

## Context

The baseline product must support local inference without requiring a hosted frontier-model service.

## Decision

Serve benchmark-selected open-weight models through Ollama. Keep model selection configurable and evaluate models for SAP entity extraction, tool selection, schema adherence, clarification quality, multilingual performance, latency, and hardware use.

## Consequences

- The model layer remains replaceable.
- Structured output reduces malformed payloads but does not guarantee business correctness.
- All generated data remains subject to deterministic validation, policy, authorization, and approval.

## Validation and follow-up

- Run model and embedding benchmarks on target hardware.
- Define model lifecycle, rollback, quantization, and provenance controls.

## References

- `05_Architecture/02_Component_Architecture/ICE-ARCH-001_HANA-X-Copilot-Solution-Architecture/References/ICE-ARCH-001_References.md`
