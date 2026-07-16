# ADR-015: Support a matrix of SAP identity and principal-propagation patterns

**Status:** Proposed
**Date:** 2026-07-16
**Owner:** HANA-X AI Architecture
**Derived from:** ICE-SRC-008 and ICE-ARCH-001

## Context

Authentication and user delegation vary by S/4HANA edition, identity provider, SAP Gateway configuration, network topology, and customer policy.

## Decision

Support documented pattern families: direct on-premises delegation, user-bound OAuth, SAML/token exchange, tightly constrained service identity with compensating controls, and optional customer-selected BTP/Cloud Connector integration.

## Consequences

- No single authentication flow is assumed universally.
- Every pattern must preserve attribution, authorization, token lifecycle, revocation, and failure behavior.
- Service identity use requires explicit risk and policy controls.

## Validation and follow-up

- Validate at least one end-to-end user-bound pattern in the procurement sandbox.
- Create an edition/release/authentication compatibility matrix.

## References

- `05_Architecture/02_Component_Architecture/ICE-ARCH-001_HANA-X-Copilot-Solution-Architecture/References/ICE-ARCH-001_References.md`
