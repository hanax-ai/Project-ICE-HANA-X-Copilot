# ADR-005: Adopt CopilotKit and AG-UI for the agent experience boundary

**Status:** Proposed
**Date:** 2026-07-16
**Owner:** HANA-X AI Architecture
**Derived from:** ICE-SRC-008 and ICE-ARCH-001

## Context

HANA-X Copilot requires a decoupled user experience that supports streaming, shared state, generative UI, structured tool activity, and human-in-the-loop interactions.

## Decision

Use React/Next.js with CopilotKit for the user experience and AG-UI as the bidirectional event protocol between the client and agent runtime. Keep SAP business logic and authorization in backend services.

## Consequences

- The frontend can evolve independently of the orchestration runtime.
- Typed events replace brittle parsing of model text.
- Backend policy and authorization remain mandatory because AG-UI events are transport, not authorization.

## Validation and follow-up

- Proof of concept for shared state, interruption, cancellation, and approval flows.
- Accessibility and performance testing for generated SAP business-object views.

## References

- `05_Architecture/02_Component_Architecture/ICE-ARCH-001_HANA-X-Copilot-Solution-Architecture/References/ICE-ARCH-001_References.md`
