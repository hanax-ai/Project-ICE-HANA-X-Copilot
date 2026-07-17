---
artifact_id: ICE-GOV-006
title: HANA-X Copilot Detailed Table of Contents
version: "1.0"
status: IN-REVIEW
owner: Project ICE Publication Office
created: 2026-07-16
related_artifacts:
  - ICE-GOV-002
  - ICE-GOV-007
  - ICE-FM-001
  - ICE-FM-002
  - ICE-BIZ-001
  - ICE-ARCH-001
  - ICE-ARCH-002
---

# HANA-X Copilot Detailed Table of Contents

**Artifact:** ICE-GOV-006  
**Version:** 1.0  
**Status:** IN-REVIEW  
**Owner:** Project ICE Publication Office  
**Date:** 16 July 2026

## 1. Publication design

### 1.1 Working title

**HANA-X Copilot: The Enterprise Intent Layer for SAP S/4HANA**  
**Subtitle:** Intent-Centric Enterprise Computing, Governed Agentic AI, and the Future of SAP Operations

### 1.2 Publication objective

Produce a 60–80-page flagship technical publication that introduces HANA-X Copilot, formally defines Intent-Centric Enterprise Computing, establishes the Enterprise Intent Layer, documents the reference architecture and SAP execution boundary, demonstrates the procurement proof point, and provides a governed foundation for implementation and product requirements.

### 1.3 Narrative arc

```text
Why enterprise interaction must change
→ What Intent-Centric Enterprise Computing means
→ Why HANA-X Copilot is needed now
→ How the product works
→ Why the architecture is credible
→ How it integrates with SAP S/4HANA
→ How procurement proves the model
→ How governance makes agentic execution safe
→ How the platform expands across the enterprise
```

### 1.4 Page budget

| Section | Target pages |
|---|---:|
| Front matter | 5–7 |
| Part I — Evolution and business rationale | 6–8 |
| Part II — Product vision and experience | 6–8 |
| Part III — Reference architecture | 15–18 |
| Part IV — SAP integration architecture | 8–10 |
| Part V — Procurement reference implementation | 8–10 |
| Part VI — Governance, security, and operations | 7–9 |
| Part VII — Roadmap and strategic outlook | 3–4 |
| Appendices | 6–8 |
| **Total** | **64–82** |

The assembly target is 60–80 pages. Page budgets may be compressed during production without removing required evidence, controls, or traceability.

## 2. Front matter

### FM-001 — Cover and publication identity

**Objective:** Establish product identity, publication title, version, status, ownership, and visual system.

**Content:**

- HANA-X Copilot title and subtitle.
- Project ICE and Intent-Centric Enterprise Computing identity.
- Version, publication date, and status.
- HANA-X AI ownership.
- Approved cover figure or conceptual illustration.

**Primary inputs:** brand assets, publication manifest, approved claims wording.  
**Target:** 1 page.

### FM-002 — Publication control, legal notice, and reading guidance

**Objective:** State scope, evidence limitations, trademarks, version control, and how to use the publication.

**Content:**

- Publication control table.
- Copyright and trademark notice.
- SAP relationship and non-endorsement language where required.
- Status of product capabilities and roadmap statements.
- Reader guide for executives, architects, security leaders, and implementation teams.

**Target:** 1–2 pages.

### FM-003 — Letter from the Founder

**Artifact:** `ICE-FM-001`  
**Objective:** Introduce the vision, paradigm, and strategic voice of Project ICE.

**Key messages:**

- Enterprise software should adapt to people.
- Intent-Centric Enterprise Computing is the next interaction paradigm.
- SAP remains the System of Record; HANA-X becomes the System of Intent.
- HANA-X strengthens rather than replaces SAP.
- Procurement is the flagship demonstration.

**Target:** 2 pages.

### FM-004 — Executive Summary

**Artifact:** `ICE-FM-002`  
**Objective:** Allow an executive reader to understand the entire proposition in five minutes.

**Required sections:**

1. The enterprise interaction problem.
2. The shift to agentic enterprise systems.
3. Definition of Intent-Centric Enterprise Computing.
4. Business urgency and value realization.
5. HANA-X Copilot and the Enterprise Intent Layer.
6. Governed intent-to-action operating model.
7. Clean Core and SAP execution boundary.
8. Procurement proof point.
9. On-premises and customer-controlled deployment.
10. Cross-domain expansion and call to action.

**Primary inputs:** `ICE-FM-001`, `ICE-BIZ-001`, `ICE-ARCH-001`, `ICE-ARCH-002`, `ICE-SRC-003`, `ICE-SRC-005`.  
**Target:** 3–4 pages.  
**Priority:** first formal chapter.

### FM-005 — Table of contents and figure index

**Objective:** Provide navigable publication structure and controlled figure listing.

**Target:** 1–2 pages, generated during assembly.

## 3. Part I — The Evolution of Enterprise Computing

### Chapter 1 — From Transactions to Processes to Intent

**Objective:** Establish the historical progression that makes ICE understandable and credible.

**Key content:**

- Transaction-centric enterprise computing.
- Process-centric integration and SAP Fiori.
- Limits of application-centric interaction.
- Agentic systems as the enabling transition.
- Intent-centric collaboration as the third paradigm.

**Required figure:** Three Eras of Enterprise Computing.  
**Primary inputs:** `ICE-FM-001`, ADR-002, official SAP history and Fiori sources.  
**Target:** 2–3 pages.

### Chapter 2 — Defining Intent-Centric Enterprise Computing

**Objective:** Provide the formal definition, principles, boundaries, and terminology of ICE.

**Key content:**

- Definition of intent.
- Intent refinement and structured business instructions.
- System of Intent versus System of Record.
- Enterprise Intent Layer.
- Governed autonomy.
- Human accountability.
- ICE beyond SAP while remaining SAP-first.

**Required figure:** Enterprise Intent Layer conceptual model.  
**Primary inputs:** ADR-001, ADR-002, `ICE-ARCH-001`, terminology standard.  
**Target:** 2–3 pages.

### Chapter 3 — Business Drivers and Strategic Urgency

**Objective:** Explain why the product and paradigm are needed now.

**Key content:**

- AI-native user expectations.
- Enterprise-software agentic competition.
- SAP adoption and value-realization friction.
- Process velocity, training, trust, and control.
- Clean Core and upgrade risk.
- Data sovereignty and cost predictability.
- Why HANA-X strengthens the SAP ecosystem.

**Primary input:** `ICE-BIZ-001`.  
**Claims:** ICE-CLM-006 through ICE-CLM-011.  
**Target:** 2–3 pages.

## 4. Part II — HANA-X Copilot Product Vision

### Chapter 4 — Product Definition and Positioning

**Objective:** Define exactly what HANA-X Copilot is and is not.

**Key content:**

- Agentic enterprise copilot for SAP S/4HANA.
- Enterprise Intent Layer product role.
- Difference from chatbot, search assistant, workflow bot, and generic agent framework.
- SAP-first and extensible positioning.
- Relationship among HANA-X Agentic OS, HANA-X Copilot, and SAP S/4HANA.

**Primary inputs:** `ICE-FM-001`, `ICE-BIZ-001`, `ICE-ARCH-001`.  
**Target:** 2 pages.

### Chapter 5 — Human–AI Co-Working and Intent Refinement

**Objective:** Explain the user experience that turns imperfect requests into governed instructions.

**Key content:**

- Natural-language request intake.
- Entity resolution and missing-field detection.
- Open-text, multiple-choice, and confirmation interactions.
- Clarification budgets and loop termination.
- Plan preview and user correction.
- Policy-driven human approval.
- Explainable results and exceptions.

**Required figures:** clarification state machine; approval interaction.  
**Primary inputs:** `ICE-ARCH-001`, ADR-007, UX requirements.  
**Target:** 2–3 pages.

### Chapter 6 — Product Capabilities and Domain Expansion

**Objective:** Connect the initial procurement proof point to a reusable enterprise platform.

**Key content:**

- Read, search, recommend, draft, validate, execute, approve, and monitor.
- Context and conversational continuity.
- Document and web knowledge acquisition.
- Event-driven and proactive work.
- Future Finance, Sales, Manufacturing, Supply Chain, HR, and Executive agents.
- Partner-built tools and workflows.

**Target:** 2–3 pages.

## 5. Part III — Reference Architecture

### Chapter 7 — End-to-End Intent-to-Action Architecture

**Objective:** Present the complete layered architecture and the responsibility of each layer.

**Layers:**

1. User and channel.
2. CopilotKit experience layer.
3. AG-UI interaction protocol.
4. LangGraph agent runtime.
5. Intent Refinement and Clarification Service.
6. Policy, context, and planning.
7. Governed multi-MCP tool execution.
8. Released SAP APIs and events.
9. SAP S/4HANA System of Record.

**Cross-cutting controls:** identity, authorization, human approval, audit, observability, provenance, security, retention, and claims governance.

**Required figure:** end-to-end reference architecture.  
**Primary input:** `ICE-ARCH-001`.  
**Target:** 3 pages.

### Chapter 8 — Experience and Agent Interaction

**Objective:** Explain the browser experience, generative UI, streaming, shared state, and user-agent protocol.

**Key content:** CopilotKit, React/Next.js, AG-UI, structured progress, interrupts, approvals, generated result views, and separation of presentation from authorization.

**Primary inputs:** ADR-005, UX requirements.  
**Target:** 2 pages.

### Chapter 9 — Stateful Orchestration and Planning

**Objective:** Explain how long-running, resumable, controlled workflows are executed.

**Key content:** LangGraph state, checkpoints, deterministic state transitions, planning, bounded loops, retries, compensation, interrupts, correlation IDs, and failure recovery.

**Primary inputs:** ADR-006, orchestration requirements.  
**Target:** 2 pages.

### Chapter 10 — Local Model and AI Runtime

**Objective:** Define the on-premises model-serving baseline and model governance.

**Key content:** Ollama, open-weight models, model routing, structured outputs, schema validation, benchmark criteria, embeddings, prompt templates, model lifecycle, and limitations.

**Required figure:** model selection and validation flow.  
**Primary inputs:** ADR-008, AI requirements, Claims Register.  
**Target:** 2 pages.

### Chapter 11 — Context, Knowledge, and Memory

**Objective:** Define authoritative state, retrieval indexes, relationship-aware retrieval, and curated preferences.

**Key content:**

- PostgreSQL as authoritative application and ingestion state.
- Qdrant as a rebuildable vector and hybrid index.
- Transactional outbox and idempotent indexing.
- LightRAG and relationship-aware retrieval.
- Optional preference memory.
- Conversation, session, business, and organizational context.

**Required figure:** context and memory architecture.  
**Primary inputs:** ADR-010, ADR-011, ADR-014, data requirements.  
**Target:** 2–3 pages.

### Chapter 12 — Governed Knowledge Acquisition

**Objective:** Explain how enterprise files and approved web content enter the knowledge system.

**Key content:** Docling, Crawl4AI, immutable originals, source IDs, malware and rights checks, provenance, sensitive-content classification, extraction quality, refresh policy, and retrieval readiness.

**Primary inputs:** ADR-012, ADR-013, ingestion requirements.  
**Target:** 2 pages.

### Chapter 13 — Multi-MCP and Workflow Automation

**Objective:** Define the governed tool plane and relationship among custom tools, workflow automation, and specialist servers.

**Key content:**

- Governed multi-MCP gateway.
- FastMCP custom-tool plane.
- n8n workflow-automation plane.
- Standalone specialist MCP servers.
- Namespacing, registration, health, authorization, and audit.
- Asynchronous execution and callback-driven LangGraph resume.

**Required figure:** multi-MCP gateway and n8n workflow plane.  
**Primary inputs:** `ICE-ARCH-001-ADD-001`, ADR-017.  
**Target:** 2–3 pages.

### Chapter 14 — Observability and Operational Evidence

**Objective:** Show how every workflow becomes traceable from user intent to SAP outcome.

**Key content:** correlation IDs, prompts and model versions, retrieved sources, plans, policies, approvals, tool calls, SAP objects, exceptions, latency, resources, and final response.

**Required figure:** intent-to-outcome audit trace.  
**Target:** 1–2 pages.

## 6. Part IV — SAP Integration Architecture

### Chapter 15 — SAP S/4HANA as the System of Record

**Objective:** Explain the product's SAP-first boundary and why HANA-X does not replace the ERP core.

**Key content:** transaction integrity, master data, authorization, business rules, document lifecycle, and controlled external orchestration.

**Target:** 1–2 pages.

### Chapter 16 — Endpoint and Interface Strategy

**Objective:** Define the governed interface hierarchy and compatibility model.

**Interface tiers:**

1. Released REST/OData APIs and business events.
2. Released SOAP services.
3. IDoc/ALE.
4. RFC/BAPI compatibility tier.
5. Governed custom APIs.
6. Prohibited direct database or ungoverned internal access.

**Compatibility:** Public Edition, Private Edition, and on-premises; actual releases pinned under the N-1 policy.

**Primary input:** `ICE-ARCH-002`.  
**Target:** 2 pages.

### Chapter 17 — SAP MCP Server and Tool Contracts

**Objective:** Explain how SAP business capabilities become registered agent tools.

**Key content:** tool discovery, schema normalization, metadata mapping, authorization context, validation, approval requirements, CSRF, ETags, concurrency, idempotency, retries, errors, redaction, rate limiting, and audit evidence.

**Required figure:** SAP endpoint-to-MCP-tool mapping.  
**Target:** 2–3 pages.

### Chapter 18 — Identity, Authorization, and Principal Propagation

**Objective:** Define supported identity patterns and end-to-end accountability.

**Patterns:** direct user delegation, OAuth user-bound access, SAML or token exchange, controlled service identity, and customer-selected hybrid integration.

**Required figure:** identity and principal-propagation patterns.  
**Primary input:** ADR-015.  
**Target:** 2 pages.

### Chapter 19 — Clean Core and Lifecycle Governance

**Objective:** Show how released interfaces, endpoint registration, versioning, deprecation, and compatibility reduce extension risk.

**Key content:** edition/release validation, endpoint registry, successor APIs, custom-interface exceptions, regression testing, and change management.

**Primary inputs:** ADR-003, `ICE-ARCH-002`.  
**Target:** 1–2 pages.

## 7. Part V — Procurement Agent Reference Implementation

### Chapter 20 — Procurement Business Problem and Value Case

**Objective:** Establish the measurable customer problem and the reasons procurement is the flagship proof point.

**Key content:** cycle time, manual effort, incomplete requests, maverick spend, supplier performance, inventory shortages, approvals, invoice exceptions, and audit burden.

**Primary inputs:** `ICE-SRC-003`, `ICE-SRC-005`, `ICE-BIZ-001`.  
**Target:** 2 pages.

### Chapter 21 — Procurement Capabilities and SAP Business Objects

**Objective:** Define the reference domain model and supported capabilities.

**Business objects:** purchase requisitions, purchase orders, suppliers, products/materials, stock, contracts, inbound deliveries, goods receipts, and supplier invoices.

**Operations:** read, search, recommend, draft, validate, create, update, approve, reject, release, monitor, and diagnose.

**Primary input:** `ICE-SAP-CAT-001` when available.  
**Target:** 2 pages.

### Chapter 22 — Intent-to-Action Workflow

**Objective:** Demonstrate the complete procurement co-working experience.

**Reference scenario:** “Create a purchase order for 250 laptops from our preferred supplier.”

**Workflow:** interpret intent, resolve material and organization context, check inventory, identify approved supplier and contract, validate price and policy, prepare requisition or PO draft, request approval, execute through registered SAP tools, and return the business-object identifier.

**Required figures:** procurement workflow timeline; protected-write sequence.  
**Target:** 2–3 pages.

### Chapter 23 — Procurement Exceptions and Recovery

**Objective:** Demonstrate safe behavior when business or technical conditions prevent execution.

**Examples:** missing organizational data, blocked supplier, insufficient authorization, unavailable endpoint, pricing conflict, stale ETag, approval rejection, duplicate request, and partial external workflow failure.

**Target:** 1–2 pages.

### Chapter 24 — Proof-of-Value and Success Measures

**Objective:** Define how the reference implementation will prove business and control value.

**Measures:** adoption, task time, clarification turns, handoffs, invalid payloads, correction rates, approval compliance, unauthorized-tool blocks, audit completeness, infrastructure cost, and user trust.

Source-provided numeric targets remain hypotheses until baseline and pilot evidence exist.

**Target:** 1–2 pages.

## 8. Part VI — Governance, Security, and Operations

### Chapter 25 — Enterprise AI Governance

**Objective:** Define accountability, policy ownership, approval classes, registered tools, model and prompt governance, and change control.

**Target:** 2 pages.

### Chapter 26 — Security and Data Protection

**Objective:** Define authentication, authorization, least privilege, secrets, data classification, prompt-injection defenses, retrieval security, retention, deletion, and legal hold.

**Required figure:** trust boundaries and security controls.  
**Target:** 2–3 pages.

### Chapter 27 — Deployment and Operating Model

**Objective:** Explain the customer-controlled on-premises baseline and operational responsibilities.

**Key content:** logical services, containers or Kubernetes, model nodes, PostgreSQL, Qdrant, MCP servers, identity integration, secrets, monitoring, backups, high availability, recovery, patching, and support.

**Target:** 2 pages.

### Chapter 28 — Testing, Evaluation, and Release Management

**Objective:** Define how the product and publication establish evidence.

**Key content:** model benchmarks, tool contract tests, SAP integration tests, security tests, workflow evaluation, red-team testing, performance baselines, regression gates, release evidence, and requirements traceability.

**Target:** 1–2 pages.

## 9. Part VII — Roadmap and Strategic Outlook

### Chapter 29 — Product Delivery Roadmap

**Objective:** Present the staged path from procurement proof of value to commercial product and cross-domain expansion.

**Stages:** discovery, read-only pilot, draft mode, governed write, event-driven workflows, multi-domain agents, partner ecosystem.

**Required figure:** product roadmap.  
**Target:** 1–2 pages.

### Chapter 30 — The Future of Intent-Centric Enterprise Computing

**Objective:** Close the publication with the long-term strategic vision.

**Key content:** multi-agent collaboration, enterprise-system interoperability, intent-based operating models, human accountability, partner opportunities, and HANA-X's role in defining the category.

**Target:** 1–2 pages.

## 10. Appendices

### Appendix A — Architecture decision summary

Summarize ADR-001 through the current approved or proposed decision set.  
**Target:** 1–2 pages.

### Appendix B — SAP endpoint catalog extract

Provide selected procurement endpoint records from `ICE-SAP-CAT-001`, including edition, release, tool ID, operations, authorization, approval class, idempotency, evidence, and lifecycle status.  
**Target:** 2 pages.

### Appendix C — Requirements traceability extract

Show representative source-to-requirement-to-test mappings.  
**Target:** 1–2 pages.

### Appendix D — Glossary and terminology

Provide definitions for ICE, Enterprise Intent Layer, System of Intent, governed autonomy, MCP, AG-UI, Clean Core, and other essential terms.  
**Target:** 1–2 pages.

### Appendix E — Reference and claims methodology

Explain source authority, claim risk, evidence packages, versioning, and citation controls.  
**Target:** 1 page.

## 11. Figure plan

| Figure | Working title | Primary chapter | Status |
|---|---|---|---|
| ICE-FIG-001 | Three Eras of Enterprise Computing | Chapter 1 | Planned |
| ICE-FIG-002 | Enterprise Intent Layer | Chapter 2 | Planned |
| ICE-FIG-003 | HANA-X Copilot End-to-End Architecture | Chapter 7 | Existing concept; redraw required |
| ICE-FIG-004 | Intent Refinement and Clarification Loop | Chapter 5 | Planned |
| ICE-FIG-005 | Policy-Driven Human Approval | Chapter 5 | Planned |
| ICE-FIG-006 | Context, Knowledge, and Memory Architecture | Chapter 11 | Planned |
| ICE-FIG-007 | Multi-MCP Gateway and n8n Workflow Plane | Chapter 13 | Planned |
| ICE-FIG-008 | Intent-to-Outcome Audit Trace | Chapter 14 | Planned |
| ICE-FIG-009 | SAP Endpoint and Clean Core Integration | Chapter 16 | Planned |
| ICE-FIG-010 | SAP Tool Contract and Execution Boundary | Chapter 17 | Planned |
| ICE-FIG-011 | Identity and Principal Propagation | Chapter 18 | Planned |
| ICE-FIG-012 | Procurement Intent-to-Action Workflow | Chapter 22 | Planned |
| ICE-FIG-013 | Procurement Protected-Write Sequence | Chapter 22 | Planned |
| ICE-FIG-014 | Security Trust Boundaries | Chapter 26 | Planned |
| ICE-FIG-015 | Product Delivery Roadmap | Chapter 29 | Planned |

Additional figures require Figure Register entries and may not cause the total publication figure count to exceed the limits in `ICE-GOV-002` and `ICE-GOV-007` without approved change control.

## 12. Chapter dependencies

```text
ICE-GOV-002 + ICE-GOV-006 + ICE-GOV-007
        ↓
ICE-FM-002 Executive Summary
        ↓
Parts I and II
        ↓
ICE-ARCH-001 chapters
        ↓
ICE-ARCH-002 + ICE-SAP-CAT-001 chapters
        ↓
Procurement reference implementation
        ↓
Governance, security, and operations
        ↓
Roadmap, conclusion, and full assembly
```

## 13. Authoring priority

1. Approve the publication blueprint artifacts.
2. Draft and review `ICE-FM-002`.
3. Complete Part I and Part II narrative chapters.
4. Convert `ICE-ARCH-001` into Part III.
5. Complete `ICE-SAP-CAT-001` and Part IV.
6. Develop the procurement workflows and Part V.
7. Complete governance, security, and operating chapters.
8. Assemble, review, approve, and publish.

## 14. Acceptance criteria

This Detailed Table of Contents is ready for approval when:

- Every required publication section has a defined objective.
- Page budgets support a 60–80-page target after production editing.
- Each chapter identifies primary governed inputs.
- Required figures are registered or planned.
- Claims-sensitive chapters identify evidence requirements.
- Dependencies align with the Project ICE Roadmap.
- The Master Authoring Guide and terminology standards are consistent with the structure.
- Editorial, architecture, SAP, claims, and executive reviewers approve the blueprint.
