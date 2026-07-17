---
artifact_id: ICE-GOV-002
title: HANA-X Copilot Master Authoring Guide
version: "1.0"
status: IN-REVIEW
owner: Project ICE Editorial Team
created: 2026-07-16
related_artifacts:
  - ICE-GOV-003
  - ICE-GOV-004
  - ICE-GOV-005
  - ICE-GOV-006
  - ICE-GOV-007
  - ICE-FM-002
---

# HANA-X Copilot Master Authoring Guide

**Artifact:** ICE-GOV-002  
**Version:** 1.0  
**Status:** IN-REVIEW  
**Owner:** Project ICE Editorial Team  
**Date:** 16 July 2026

## 1. Purpose and authority

This guide is the governing authoring constitution for the HANA-X Copilot Technical Publication. It controls mission, audience, narrative architecture, terminology, evidence, claims, citations, chapter structure, diagrams, AI-assisted authoring, review gates, traceability, production, and release.

When this guide conflicts with an informal working note, AI-generated draft, or unapproved chapter convention, this guide prevails. Approved architecture decisions, official SAP documentation, the Source Register, Claims Register, Artifact Register, and publication-specific approval records remain authoritative within their respective scopes.

## 2. Publication mission

The publication shall:

1. Formally define Intent-Centric Enterprise Computing (ICE).
2. Introduce HANA-X Copilot as the Enterprise Intent Layer for SAP S/4HANA.
3. Explain why SAP customers need an AI-native, governed intent-to-action experience.
4. Present a credible enterprise reference architecture.
5. Define a Clean Core-aligned SAP integration and endpoint strategy.
6. Demonstrate the architecture through a procurement reference implementation.
7. Establish security, governance, observability, data, model, and operating controls.
8. Provide requirements, decisions, figures, references, and implementation guidance that remain traceable to governed sources.

The target is a 60–80-page flagship publication written for SAP leadership and enterprise decision-makers first, while retaining sufficient technical depth for architects and implementation teams.

## 3. Audience and reader journeys

### 3.1 Primary audience

- SAP leadership and product stakeholders.
- SAP S/4HANA customers and enterprise executives.
- Chief information, technology, data, digital, and AI officers.
- Enterprise and SAP architects.
- Transformation, procurement, finance, supply-chain, and operations leaders.

### 3.2 Secondary audience

- SAP implementation partners and systems integrators.
- AI engineering, platform, security, and governance teams.
- Product managers and domain-agent developers.
- Analysts, investors, and strategic ecosystem partners.

### 3.3 Reader journeys

| Reader | Principal question | Required outcome |
|---|---|---|
| Executive | Why does this matter now? | Understand urgency, value, differentiation, and strategic fit |
| SAP leader | Does this strengthen SAP and preserve Clean Core? | Understand ecosystem alignment and integration discipline |
| Architect | Is the design coherent and implementable? | Understand components, boundaries, data flows, identity, and controls |
| Security or governance leader | Can agentic execution be trusted? | Understand authorization, policy, approval, audit, and evidence |
| Implementation partner | How would we build and extend it? | Understand endpoints, MCP tools, workflows, requirements, and roadmap |

## 4. Core thesis and narrative architecture

The publication shall consistently establish the following narrative:

1. Enterprise computing evolved from transaction-centric to process-centric interaction.
2. Agentic AI creates the opportunity for intent-centric collaboration.
3. SAP S/4HANA remains the trusted System of Record.
4. HANA-X Copilot provides the governed System of Intent.
5. The Enterprise Intent Layer interprets, clarifies, plans, applies policy, obtains approval, and executes through registered tools.
6. Released SAP interfaces and Clean Core-aligned extension patterns preserve the ERP core.
7. Customer-controlled model deployment provides an on-premises baseline while retaining interoperability.
8. Procurement proves the reusable architecture before expansion to other domains.

## 5. Approved terminology

Use the terminology standard and glossary as the canonical vocabulary. The following terms require exact and consistent treatment:

- **Intent-Centric Enterprise Computing (ICE):** the paradigm in which users express desired outcomes and governed systems translate those intentions into authorized enterprise action.
- **Enterprise Intent Layer:** the architectural layer between human intent and enterprise execution.
- **System of Intent:** HANA-X Copilot's role in interpreting, refining, planning, and governing intended work.
- **System of Record:** SAP S/4HANA's role as the authoritative transactional platform.
- **Agentic AI:** systems capable of planning, tool invocation, workflow coordination, and controlled execution.
- **Governed autonomy:** autonomous capability constrained by identity, policy, approval thresholds, registered tools, and audit.
- **Intent Refinement and Clarification Service:** the component that resolves missing, ambiguous, or conflicting business information.
- **Clean Core-aligned:** designed to use released and supported interfaces while avoiding intrusive ERP core modification; not a universal guarantee without landscape validation.
- **MCP tool:** a registered and governed capability exposed through the Model Context Protocol.

### 5.1 Prohibited or qualified formulations

Do not use the following without approved evidence or qualification:

- “Zero hallucination.”
- “Fully deterministic AI.”
- “Guaranteed savings.”
- “Reverses SAP backlog deceleration.”
- “No cost” or “free AI.”
- “Works with every SAP release.”
- “Completely autonomous” where policy or approval applies.
- “SAP-certified,” “SAP-endorsed,” or similar language without formal authorization.
- New first-to-market or market-leadership categories not present in the Claims Register.

## 6. Editorial voice and style

The publication shall be:

- Executive-accessible but technically credible.
- Confident without overstating evidence.
- Specific about architecture, controls, and customer outcomes.
- Respectful of SAP and its ecosystem.
- Clear about assumptions, proposed decisions, optional components, and open questions.
- Written in active voice with direct sentences and meaningful headings.

Avoid conversational transcripts, promotional exaggeration, unexplained acronyms, dense vendor catalogs, and implementation details that obscure the business or architectural purpose.

### 6.1 Chapter opening pattern

Each chapter should open with:

1. The problem or question being addressed.
2. Why it matters to the reader.
3. The HANA-X position or architectural response.
4. What the chapter will establish.

### 6.2 Chapter closing pattern

Each chapter should close with:

- Key conclusions.
- Dependencies or open questions.
- Relationship to the next chapter.
- Claims, decisions, requirements, or figures requiring register updates.

## 7. Chapter authoring package

No chapter enters drafting without a governed authoring package containing:

- Permanent chapter or artifact ID.
- Chapter title and objective.
- Target audience and reader outcome.
- Page or word budget.
- Approved source set and authority tiers.
- Required claims and evidence status.
- Applicable ADRs and architecture artifacts.
- Required figures and figure IDs.
- Required requirements or traceability outputs.
- Known exclusions and prohibited claims.
- Reviewers and acceptance criteria.

## 8. Standard chapter structure

Use this structure unless the Detailed Table of Contents specifies otherwise:

```text
Title and control metadata
Executive takeaway
Problem and context
HANA-X position
Architecture or operating model
Business and technical implications
Example or reference workflow
Risks, assumptions, and controls
Key conclusions
References and traceability
```

The canonical chapter source is Markdown. DOCX, PDF, HTML, and presentation outputs are derivatives produced through the approved publication pipeline.

## 9. Source and evidence governance

### 9.1 Authority order

Use evidence in this order:

1. Verified technical facts and official SAP or standards documentation.
2. Approved HANA-X architecture decisions and governed specifications.
3. Approved founder vision and strategic terminology.
4. Accepted business cases and implementation evidence.
5. Contextual research and working notes.
6. Exploratory or AI-generated material requiring independent verification.

### 9.2 Source rules

- Every source must have a permanent Source ID.
- Original evidence is immutable.
- Every factual assertion must be traceable to a source, decision, requirement, test, or clearly marked inference.
- AI-generated research is never elevated to primary authority merely because it is polished or repeated.
- Time-sensitive facts require retrieval or publication dates.
- SAP capabilities must be qualified by edition and release when relevant.

## 10. Claims governance

Every material competitive, financial, commercial, architectural, performance, licensing, or product-capability assertion must be evaluated against the Claims Register.

Claims are classified by risk:

| Risk | Treatment |
|---|---|
| Low | Source validation and editorial review |
| Medium | Primary evidence and specialist review |
| High | Primary evidence, claims/legal review, and explicit approval or recorded exception |

A chapter cannot be approved with an unsupported high-risk claim. Proposed benefits must be expressed as design intent or testable hypotheses until measured evidence exists.

## 11. Citation and reference standards

- Cite the most authoritative available source.
- Prefer primary product documentation, standards, filings, and controlled HANA-X artifacts.
- Preserve source title, publisher, date, URL or repository path, and retrieval date where applicable.
- Do not use raw search-result snippets as evidence.
- Do not use inaccessible internal URLs as public references.
- Separate primary evidence from secondary context.
- Maintain chapter references in the governed reference catalog and update the Source Register when a new source enters the corpus.

## 12. Architecture-writing standards

Architecture content must:

- Define the business or control problem before naming technology.
- Distinguish accepted decisions, proposed decisions, alternatives, optional components, and open questions.
- Identify system boundaries, ownership, authoritative state, derivative indexes, trust boundaries, and failure behavior.
- Avoid treating a protocol, framework, or model as the security boundary.
- State edition-, release-, or deployment-specific assumptions.
- Trace component descriptions to ADRs and requirements.

Vendor or framework descriptions belong in the main narrative only when they explain a meaningful architectural role. Installation commands, long schemas, and implementation code belong in appendices or companion guides.

## 13. Figure and diagram standards

The publication targets 12–18 core figures and no more than 20–25 figures including appendices.

Every figure requires:

- Permanent Figure ID.
- Editable deterministic source.
- Rendered output.
- Title and caption.
- Short alt text and long description where needed.
- Source provenance.
- Review and publication status.

Technical architecture, sequence, data-flow, security, endpoint, and workflow diagrams must use controlled editable sources such as Mermaid, Graphviz, PlantUML, Draw.io, SVG, or PowerPoint. Generative-image tools may support covers and conceptual illustrations but are not the technical source of truth.

## 14. AI-assisted authoring protocol

Agent Zero, Claude, ChatGPT, or other authoring agents may draft, normalize, compare, or review content only within a governed job package.

### 14.1 Required AI job inputs

- Chapter brief and acceptance criteria.
- Approved source list with authority classification.
- Approved terminology and claims constraints.
- Applicable architecture artifacts and ADRs.
- Required figures and requirements outputs.
- Word or page budget.
- Review instructions.

### 14.2 Required AI behavior

The authoring agent shall:

- Cite or trace substantive claims.
- Separate source fact from inference and recommendation.
- Flag missing evidence and contradictions.
- Preserve artifact and source identities.
- Avoid inventing SAP endpoint behavior, release support, benchmarks, or licensing conclusions.
- Produce structured review notes when uncertain.
- Never overwrite immutable evidence or published artifacts.

### 14.3 Human accountability

AI output remains draft material until reviewed. Human owners approve strategy, architecture, SAP integration, security, claims, and publication status.

## 15. Review lifecycle

Every chapter follows:

```text
Research
→ Source validation
→ Chapter brief
→ Outline
→ Draft
→ Editorial review
→ Technical architecture review
→ SAP integration review
→ Security and data review
→ Source and citation review
→ Claims and legal review
→ Visual and accessibility review
→ Executive approval
→ Publication
```

Comment classifications are:

- BLOCKER
- MAJOR
- MINOR
- EDITORIAL
- QUESTION
- DEFERRED

Approval requires zero unresolved blockers and an explicit disposition for all major comments.

## 16. Artifact statuses

Use only:

- DRAFT
- IN-REVIEW
- APPROVED
- PUBLISHED
- SUPERSEDED
- WITHDRAWN

Do not use `FINAL`. Published artifacts are immutable; any subsequent change requires a new version.

## 17. Requirements and traceability

Architecture and product chapters shall extract testable requirements where appropriate. Each requirement must include:

- Requirement ID.
- Normative statement using “shall.”
- Source and architecture origin.
- Acceptance criterion.
- Planned test or evidence.
- Status and owner.

Traceability should connect:

```text
Source
→ Claim or decision
→ Architecture component
→ Requirement
→ Acceptance criterion
→ Test evidence
→ Published statement
```

## 18. Publication production

The canonical Markdown set shall be assembled into publication derivatives through the approved build process.

Release readiness includes:

- Complete table of contents and cross-references.
- Approved figures, captions, and alt text.
- Citation and hyperlink validation.
- Copyediting and proofreading.
- PDF, DOCX, and web rendering review.
- Accessibility review.
- Register and manifest updates.
- SHA-256 hashes and release notes.
- Immutable snapshot under `12_Releases/`.

## 19. Repository workflow

Project ICE uses only `main` and `working`.

```text
Author on working
→ Run governance validation
→ Open working-to-main pull request
→ Complete review and checks
→ Merge to main
→ Synchronize working to main
```

Direct publication work on `main` is prohibited.

## 20. Quality acceptance criteria

A chapter is ready for approval only when it is:

- Correct and internally consistent.
- Appropriate for the target reader.
- Traceable to governed sources.
- Consistent with approved terminology and architecture.
- Free of unsupported high-risk claims.
- Clear about assumptions and limitations.
- Supported by approved figures where required.
- Accessible and publication-ready.
- Integrated with adjacent chapters without duplication or contradiction.

## 21. Change control

Changes to this guide require:

1. A documented reason and affected artifacts.
2. Editorial and governance review.
3. Artifact Register and change-log updates.
4. A new version when the approved guide changes materially.
5. Reassessment of affected chapters or release candidates.

## 22. Immediate application

This guide shall govern the creation of `ICE-FM-002 — Executive Summary`. Its authoring package must use `ICE-FM-001`, `ICE-BIZ-001`, `ICE-ARCH-001`, `ICE-ARCH-002`, `ICE-SRC-003`, and `ICE-SRC-005`, with the Detailed Table of Contents and Project ICE Publication Roadmap controlling scope and sequencing.
