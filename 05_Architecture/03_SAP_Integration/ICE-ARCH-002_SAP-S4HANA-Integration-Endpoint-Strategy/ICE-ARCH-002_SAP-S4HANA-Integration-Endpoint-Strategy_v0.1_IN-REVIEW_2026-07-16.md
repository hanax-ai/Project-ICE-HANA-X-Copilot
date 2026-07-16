---
artifact_id: ICE-ARCH-002
title: SAP S/4HANA Integration Endpoint Strategy
subtitle: Governed Interface Patterns for HANA-X Copilot
version: "0.1"
status: IN-REVIEW
owner: HANA-X AI Architecture
date: 2026-07-16
derived_from:
  - ICE-SRC-010
related_artifacts:
  - ICE-ARCH-001
  - ADR-003
  - ADR-009
---

# SAP S/4HANA Integration Endpoint Strategy

## Governed Interface Patterns for HANA-X Copilot

**Artifact:** ICE-ARCH-002  
**Version:** 0.1  
**Status:** IN-REVIEW  
**Owner:** HANA-X AI Architecture  
**Date:** 16 July 2026

> This document defines how HANA-X Copilot identifies, classifies, governs, and consumes SAP S/4HANA integration interfaces. It replaces an informal list of endpoints with a Clean Core-aligned interface strategy and a repeatable endpoint-registration model.

## 1. Purpose

SAP S/4HANA exposes multiple integration technologies. The term **endpoint** means a network-addressable service location through which a client invokes an API, service, event channel, or integration adapter. OData, SOAP, RFC, IDoc, and business events are interface technologies or patterns; each may expose one or more concrete endpoints.

For HANA-X Copilot, an SAP endpoint is not merely a URL. It is a governed execution contract containing the supported business object, operations, schemas, authorization context, approval rules, edition and release compatibility, error behavior, lifecycle state, and audit requirements.

## 2. Scope and compatibility baseline

The endpoint strategy covers SAP S/4HANA Cloud Public Edition, SAP S/4HANA Cloud Private Edition, and on-premises deployments where released interfaces are available.

Compatibility follows an **N-1 policy**: each endpoint catalog release pins and validates the release immediately preceding the current supported release for each edition. The catalog must record the actual tested release identifiers rather than retaining `N-1` as an unresolved label.

The baseline supports the complete governed operation lifecycle:

- read and search;
- draft creation;
- deterministic validation;
- transactional create, update, action, and delete where approved;
- human and policy approval;
- asynchronous and event-driven operations; and
- exception, retry, compensation, and reconciliation handling.

## 3. Architectural principles

1. **Released interfaces first.** Prefer released and supported SAP APIs, services, and events appropriate to the customer edition and release.
2. **Clean Core alignment.** Keep Copilot logic outside the ERP core; avoid direct database access and ungoverned modifications.
3. **Endpoint allowlisting.** The agent may invoke only registered, versioned, and authorized tools mapped to approved SAP interfaces.
4. **Edition and release awareness.** Availability and behavior must be validated for the target edition and pinned release.
5. **Read/write separation.** Reads, drafts, reversible updates, high-impact writes, and event subscriptions receive different controls.
6. **Principal-aware execution.** Every operation carries an approved identity pattern and produces auditable attribution.
7. **Contract-driven agents.** SAP schemas, code lists, required fields, and documented errors shape tool definitions, validation, and clarification questions.
8. **Knowledge and execution separation.** Documentation-retrieval services may assist discovery but may never authorize or execute SAP transactions.

## 4. Formal interface tiers

| Tier | Interface pattern | HANA-X treatment | Key controls |
|---|---|---|---|
| Tier 1 | Released REST/OData APIs and business events | Preferred baseline | Release status, schemas, authorization, CSRF, ETags, idempotency, event replay |
| Tier 2 | Released SOAP APIs and supported integration services | Supported when appropriate | WSDL version, certificates, message security, fault normalization |
| Tier 3 | Released IDoc/ALE interfaces | Supported for asynchronous, EDI, and established high-volume patterns | Partner profiles, message types, retries, status monitoring, reconciliation |
| Tier 4 | Released RFC/BAPI interfaces | Formal compatibility tier with enhanced review | Released status, remote-enabled function, authorization objects, commit behavior, statefulness, successor API, sunset plan |
| Tier 5 | Customer-governed custom APIs | Allowed only with documented ownership and lifecycle | API owner, release contract, compatibility tests, support and deprecation plan |
| Exception | File and batch interfaces | Controlled exception pattern | Encryption, integrity, duplicate detection, schedule, reconciliation |
| Prohibited | Direct database access, screen scraping, arbitrary URLs, ungoverned internal calls | Not permitted | Block and audit |

RFC/BAPI is retained as a formal tier, not a default new-development choice. Every RFC/BAPI registration must document upgrade impact, recommended successor, exception approval, and sunset strategy.

## 5. Endpoint selection hierarchy

Use this order of preference:

1. Released SAP REST/OData API or business event for the target edition and pinned release.
2. Released SAP SOAP service when no suitable Tier 1 contract exists or the scenario requires it.
3. Released IDoc interface for asynchronous or EDI processes.
4. Released RFC/BAPI interface under Tier 4 controls.
5. Customer-owned custom API implemented through an approved extension pattern.
6. File or batch exchange only when the requirement cannot be met safely through the preceding tiers.

## 6. Endpoint Registry

Every SAP tool exposed through the governed MCP boundary must map to an Endpoint Registry entry.

| Field | Description |
|---|---|
| Endpoint ID | Permanent HANA-X identifier |
| Business domain and object | Procurement, finance, sales, manufacturing, supplier, purchase order, and so on |
| SAP interface | API, service, event, IDoc, RFC/BAPI, or custom technical name |
| Interface tier and type | Tier 1-5 and OData, REST, SOAP, event, IDoc, RFC/BAPI, custom API, or file |
| Edition and pinned release | Public, Private, or on-premises compatibility evidence |
| Operations | Read, search, draft, validate, create, update, delete, action, approve, subscribe |
| Tool identity | Permanent MCP tool ID and version |
| Schemas and code lists | Versioned input/output contracts and SAP value domains |
| Authorization | SAP roles, scopes, user delegation, or compensating service controls |
| Approval class | Informational, draft, reversible write, high-impact write, event-triggered work item |
| Concurrency and idempotency | ETag, duplicate prevention, idempotency key, retry safety |
| Error model | SAP errors, protocol faults, remediation and user guidance |
| Data classification | Public, internal, confidential, regulated |
| Audit fields | Initiator, effective identity, plan version, payload digest, timestamps, correlation IDs |
| Lifecycle status | Proposed, validated, approved, deprecated, withdrawn |
| Evidence | Official SAP references and customer-system validation |

### Example logical record

```yaml
endpoint_id: HXC-SAP-MM-PO-001
business_domain: Procurement
business_object: Purchase Order
interface_tier: 1
interface_type: OData
sap_interface: API_PURCHASEORDER_PROCESS_SRV
edition_release:
  edition: customer-validated
  pinned_release: pending-catalog-baseline
operations: [read, search, draft, validate, create, update, approve]
approval_class: policy-driven
mcp_tool_id: sap.procurement.purchase_order.v1
status: proposed
```

## 7. HANA-X execution model

```text
Natural-language intent
  -> Intent Refinement and Clarification Service
  -> policy and authorization evaluation
  -> registered MCP tool selection
  -> Endpoint Registry validation
  -> approved SAP interface invocation
  -> result and error normalization
  -> audit, trace, and user explanation
```

The model may select only registered tools. It may not construct arbitrary SAP URLs, bypass the tool layer, or infer undocumented fields.

## 8. SAP endpoint knowledge and discovery architecture

### 8.1 Authoritative hierarchy

1. **SAP Business Accelerator Hub** — primary public catalog for APIs, events, schemas, and integration content: https://api.sap.com/
2. **SAP Help Portal** — edition- and release-specific product documentation: https://help.sap.com/
3. **Target-system metadata and configuration** — service catalogs, communication arrangements, SAP Gateway activation, event configuration, and authorization roles.
4. **SAP-managed public documentation repositories** — machine-readable public documentation where relevant: https://github.com/SAP-docs
5. **ABAP Keyword Documentation and released-object information** — ABAP platform and released API guidance: https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/index.htm
6. **SAP Developer Tutorials** — implementation examples and setup guidance: https://developers.sap.com/tutorial-navigator.html
7. **SAP Community and third-party discovery sources** — secondary research only; never sole evidence of support or compatibility.

### 8.2 SAP Documentation MCP Server

The community SAP Documentation MCP Server referenced by the source draft is retained as an optional research accelerator:

- discovery location: https://mcpservers.org/servers/marianfoo/mcp-sap-docs
- component classification: `ICE-MCP-EXT-001`
- role: documentation search, retrieval, and released-object research;
- authority: secondary;
- baseline status: optional;
- SAP transaction access: prohibited;
- independent validation: required.

It is distinct from the HANA-X SAP MCP execution server:

```text
SAP Documentation MCP Server -> discovers and retrieves SAP knowledge
HANA-X SAP MCP Server        -> invokes governed SAP business operations
```

Results from the documentation MCP server must preserve the underlying source URL, publisher, retrieval time, and authority classification. A result becomes authoritative only when the underlying evidence is an official SAP source or is independently validated against the target system.

### 8.3 Multi-MCP placement

The documentation MCP server may be connected through the governed multi-MCP gateway defined by `ICE-ARCH-001-ADD-001` and `ADR-017`. It receives no transaction credentials and cannot bypass the Endpoint Registry, policy service, or SAP execution boundary.

## 9. Source-link disposition

- Internal `wdf.sap.corp` locations are excluded from the public authoritative catalog.
- SAP Commerce Cloud API Registry is outside the S/4HANA endpoint scope.
- BTP platform endpoints belong only to an optional BTP deployment profile.
- Third-party Q&A, Cognite, and MCP listing pages are discovery sources only.
- Malformed or duplicate links are removed and replaced with canonical official locations.

## 10. Catalog lifecycle

```text
Discover
-> retrieve official documentation
-> validate edition and pinned N-1 release
-> inspect target-system metadata
-> classify interface tier
-> define MCP tool contract
-> validate authorization and approval
-> test read, draft, write, event, failure, concurrency, and idempotency behavior
-> record evidence
-> approve
-> monitor lifecycle and deprecation
```

## 11. Next governed deliverables

1. Create `ICE-SAP-CAT-001`, the SAP S/4HANA Endpoint Catalog, beginning with procurement.
2. Pin the actual N-1 release identifiers for Public Edition, Private Edition, and the initial on-premises compatibility baseline.
3. Map each endpoint to an MCP tool ID, interface tier, and policy classification.
4. Define acceptance tests for all supported operation classes.
5. Register `ICE-MCP-EXT-001` as an optional secondary documentation-retrieval component.
6. Maintain endpoint deprecation, compatibility, and successor-interface records.

## References

- SAP Business Accelerator Hub. https://api.sap.com/
- SAP Help Portal. https://help.sap.com/
- SAP S/4HANA documentation. https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE
- SAP Developer Tutorials. https://developers.sap.com/tutorial-navigator.html
- SAP Documentation GitHub organization. https://github.com/SAP-docs
- ABAP Keyword Documentation. https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/index.htm
- Community SAP Documentation MCP Server listing. https://mcpservers.org/servers/marianfoo/mcp-sap-docs
