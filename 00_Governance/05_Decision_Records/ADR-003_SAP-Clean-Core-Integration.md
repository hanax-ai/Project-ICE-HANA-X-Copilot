# ADR-003 — Use released SAP interfaces to preserve Clean Core

**Status:** Accepted  
**Date:** 2026-07-14  
**Decision owner:** HANA-X AI

## Context

The Copilot must extend the value of SAP S/4HANA without intrusive modifications to the ERP core.

## Decision

HANA-X Copilot will integrate through released and supported SAP S/4HANA APIs, OData services, business events, and other approved interfaces appropriate to the deployed edition and release. Direct database writes and undocumented interfaces are excluded.

## Consequences

Each SAP tool must map to a supported interface, authorization model, validation rule, audit trail, and release-specific compatibility statement.

## Traceability

ICE-SRC-002; ICE-SRC-003; ICE-SRC-005; ICE-CLM-003
