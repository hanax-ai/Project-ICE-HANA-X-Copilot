# Project ICE — HANA-X Copilot

## Working publication title

**HANA-X Copilot, The First Commercially Available SAP S/4HANA Copilot**

Project ICE is the governed publication, architecture, requirements, and knowledge repository for HANA-X Copilot. The program introduces **Intent-Centric Enterprise Computing (ICE)** and positions HANA-X Copilot as the **Enterprise Intent Layer** for SAP S/4HANA.

## Repository purpose

This repository provides a controlled lifecycle for:

- source intake and evidence preservation;
- knowledge normalization and retrieval grounding;
- chapter-by-chapter white-paper authoring;
- enterprise architecture and SAP integration specifications;
- product requirements and traceability;
- Agent Zero and Claude authoring runs;
- editorial, technical, claims, security, and executive review;
- publication builds, deliverables, releases, and archival records.

## Governing principle

> Original sources are immutable, working documents are version-controlled, and published deliverables are never overwritten.

## Repository map

| Directory | Purpose |
|---|---|
| `00_Governance/` | Project charter, authoring rules, terminology, decisions, change control, and templates |
| `01_Registers/` | Source, artifact, claims, figure, requirements, decision, risk, and issue registers |
| `02_Source_Materials/` | Immutable internal and external source evidence |
| `03_Knowledge_Base/` | Normalized sources, summaries, topic knowledge, citations, and RAG inputs |
| `04_White_Paper/` | Front matter, chapter authoring, appendices, assembly, and publication builds |
| `05_Architecture/` | Reference architecture and subsystem specifications |
| `06_Requirements/` | Product, functional, non-functional, security, SAP, AI, UX, and acceptance requirements |
| `07_Use_Cases/` | Procurement flagship use case and future business-domain cases |
| `08_Agent_Zero/` | Claude instructions, prompts, context packs, jobs, outputs, logs, and evaluations |
| `09_Reviews_and_Approvals/` | Formal quality gates and signed approvals |
| `10_Visual_and_Brand_Assets/` | Brand assets, editable figure sources, renders, licenses, and alt text |
| `11_Deliverables/` | Approved web, print, accessible, archival, presentation, and product outputs |
| `12_Releases/` | Immutable versioned release snapshots and checksums |
| `90_Archive/` | Superseded, rejected, withdrawn, and historical materials |
| `99_Workspace/` | Non-authoritative temporary work |

## Lifecycle

```text
Source intake
    -> Knowledge preparation
    -> Authoring
    -> Architecture and requirements
    -> Review and approval
    -> Publication
    -> Release and archival
```

## Naming convention

```text
<Program>-<ArtifactType>-<ID>_<Short-Title>_v<Major.Minor>_<Status>_<Date>.<ext>
```

Example:

```text
HXC-ICE-FM-001_Letter-from-the-Founder_v1.0_PUBLISHED_2026-07-14.pdf
```

Approved status values are `DRAFT`, `IN-REVIEW`, `APPROVED`, `PUBLISHED`, `SUPERSEDED`, and `WITHDRAWN`. Do not use `FINAL` as a status.

## Versioning

| Version | Meaning |
|---|---|
| `v0.1` | Initial working draft |
| `v0.5` | Substantive draft under review |
| `v0.9` | Release candidate |
| `v1.0` | First approved publication |
| `v1.1` | Minor approved revision |
| `v2.0` | Major structural or strategic revision |

## Current source set

The initial register includes the HANA-X Agentic OS white paper, Query Response, HANA-X Copilot Business Case, Letter from the Founder, and Procurement Agent Specification. See `01_Registers/ICE_Source_Register.csv`.

## Current status

Repository governance and publication scaffolding initialized on 2026-07-14. The next governed artifact is the **HANA-X Copilot Master Authoring Guide**.
