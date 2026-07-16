# ICE-ARCH-001 Derived Requirements

**Artifact:** ICE-ARCH-001  
**Version:** 0.1  
**Status:** IN-REVIEW  
**Source:** ICE-SRC-008

These requirements were extracted from the governed solution architecture and remain proposed until reviewed and accepted in the product requirements baseline.

| Requirement ID | Category | Requirement | Acceptance criterion |
|---|---|---|---|
| ICE-UX-001 | User experience | The Copilot shall accept natural-language requests and maintain conversational context. | A multi-turn test resolves references from prior turns without requiring repetition. |
| ICE-UX-002 | User experience | The Copilot shall ask targeted clarification questions when required business fields are missing or ambiguous. | An ambiguous procurement request produces a grounded question and does not execute a write. |
| ICE-UX-003 | User experience | The Copilot shall support open-text, multiple-choice, correction, confirmation, and approval interactions. | Each interaction type renders and returns a typed backend event. |
| ICE-UX-004 | User experience | The clarification budget shall be configurable by business process and risk. | A policy configuration changes the permitted clarification turns without code modification. |
| ICE-AI-001 | AI and agent | The baseline model runtime shall operate on premises through Ollama without requiring a hosted frontier-model service. | A complete reference workflow runs with network egress to hosted LLM services disabled. |
| ICE-AI-002 | AI and agent | Model selection shall be configuration and benchmark driven rather than hard-coded into business logic. | A model version can be changed through approved configuration and the benchmark record identifies the selected model. |
| ICE-AI-003 | AI and agent | All model-generated structured data shall pass deterministic structural and business validation before tool execution. | Malformed, invalid-code, and unauthorized payload tests are rejected before the SAP tool call. |
| ICE-SAP-002 | SAP integration | SAP operations shall execute only through registered, versioned, and authorized tools. | An arbitrary or unregistered SAP URL cannot be invoked by the agent. |
| ICE-SAP-003 | SAP integration | Each SAP tool shall declare edition, release, service, entity, schema, authorization, approval, idempotency, and error behavior. | Tool-contract validation fails when a required declaration is missing. |
| ICE-SAP-004 | SAP integration | The integration shall use released and supported SAP APIs, OData services, events, or separately governed approved interfaces. | Endpoint inventory maps every tool to a governed SAP interface and supported release. |
| ICE-SEC-002 | Security | The system shall preserve the initiating user identity and applicable SAP authorization context for transaction execution. | SAP and Copilot audit records attribute a test transaction to the initiating user or documented compensating identity pattern. |
| ICE-SEC-003 | Security | A changed write payload shall invalidate any prior human approval. | Editing an approved payload forces a new approval before execution. |
| ICE-SEC-004 | Security | The system shall not place access tokens, credentials, or unrestricted enterprise records in model prompts. | Prompt and trace inspection finds no secrets or raw bearer tokens. |
| ICE-DATA-001 | Data and memory | PostgreSQL shall remain the authoritative record for artifacts, workflow state, indexing state, policies, and audit evidence. | All Qdrant and graph records can be traced to a canonical PostgreSQL record. |
| ICE-DATA-002 | Data and memory | Qdrant and graph retrieval stores shall be rebuildable indexes rather than authoritative records. | A clean index rebuild from canonical records produces complete searchable coverage. |
| ICE-DATA-003 | Data and memory | PostgreSQL-to-retrieval-index synchronization shall use a transactional outbox and idempotent workers. | Failure and retry tests produce no lost canonical record and no duplicate active index point. |
| ICE-DATA-004 | Data and memory | User preferences shall be inspectable, correctable, removable, and unable to override current SAP values or policy. | A user can view/delete a preference and a conflicting SAP value or policy takes precedence. |
| ICE-ING-001 | Ingestion | Original uploaded files shall be preserved immutably before normalization and indexing. | The source hash remains verifiable and the original is not modified during reprocessing. |
| ICE-ING-002 | Ingestion | Web acquisition shall enforce domain policy, SSRF protection, provenance, page hashing, rights review, and user approval before permanent ingestion. | Blocked/private addresses are denied and a retained page has URL, retrieval time, hash, and approval evidence. |
| ICE-OBS-001 | Observability | Every workflow shall produce an auditable trace of intent, clarification, context, plan, policy, approval, tools, SAP results, errors, and final response. | A completed procurement test can be reconstructed from linked trace and audit identifiers. |
| ICE-NFR-001 | Non-functional | The agent runtime shall support checkpointing, interruption, safe resumption, and idempotent retry for long-running workflows. | A paused workflow resumes after restart without duplicate write execution. |
| ICE-NFR-002 | Non-functional | Vector, graph, prompt, model, tool, and workflow versions shall be recorded for reproducibility. | A prior execution can be associated with the exact component versions used. |
