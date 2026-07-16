# ICE-FIG-001 v0.1 Design Review

## Submitted concept

The submitted raster diagram communicates the intended architecture effectively and is preserved unchanged under `Source/Received/`.

## Strengths

- Clear intent-to-action sequence from user experience to SAP S/4HANA.
- Correct separation of CopilotKit, AG-UI, LangGraph, context services, MCP tools, and SAP interfaces.
- Strong Clean Core message.
- Explicit on-premises Ollama and human-in-the-loop concepts.

## Corrections applied in the governed render

- Separated CopilotKit and AG-UI into distinct experience and protocol nodes.
- Reframed the prompt enhancer as the Intent Refinement and Clarification Service.
- Marked preference memory as optional rather than baseline.
- Added policy and approval controls inside the planning layer.
- Added Docling and Crawl4AI as governed ingestion services.
- Clarified PostgreSQL as the authoritative record and Qdrant as a rebuildable retrieval index.
- Added cross-cutting identity, authorization, audit, observability, and provenance controls.
- Replaced direct component-to-SAP side arrows with the governed tool-execution path.
- Omitted the SAP logo from the governed render pending brand and trademark review; the unmodified submitted concept remains preserved.

## Publication decision

Use the governed SVG render for the architecture specification. Retain the submitted image only as design provenance unless a later brand review approves it for publication.
