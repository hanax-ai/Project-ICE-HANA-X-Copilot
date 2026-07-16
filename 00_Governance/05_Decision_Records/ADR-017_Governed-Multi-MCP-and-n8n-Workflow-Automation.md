# ADR-017 — Governed Multi-MCP Gateway and n8n Workflow Automation

**Status:** Proposed  
**Date:** 2026-07-16  
**Owner:** HANA-X AI Architecture  
**Derived from:** ICE-SRC-009; ICE-ARCH-001-ADD-001

## Context

The HANA-X development environment uses FastMCP for most custom MCP services, n8n with its own MCP endpoint for visual workflow automation, and standalone specialized MCP servers such as Docling, Crawl4AI, and Shadcn. Forcing all servers behind one hub would create unnecessary coupling and may not match their transport, authentication, or lifecycle requirements.

## Decision

HANA-X Copilot will use a governed multi-MCP integration gateway in the LangGraph backend.

- LangGraph remains authoritative for intent state, clarification, planning, policy routing, approval, checkpointing, and recovery.
- FastMCP-managed services provide custom Python and domain tools.
- n8n provides registered visual workflows, asynchronous jobs, event triggers, transformations, and multi-system automation.
- Approved standalone MCP servers may be connected directly through dedicated client profiles.
- Dynamic discovery is filtered through a deny-by-default registry before tools are exposed to models or graphs.
- Tools are namespaced, versioned, typed, authorized, audited, and lifecycle managed.

## Consequences

### Positive

- Preserves the best operational role for each runtime.
- Avoids coupling all MCP services to one server implementation.
- Supports long-running and event-driven work without blocking interactive sessions.
- Allows specialized services to evolve independently.
- Creates one policy and audit model across heterogeneous tool servers.

### Costs and risks

- Requires server-specific transport and authentication profiles.
- Increases health, version, discovery, and observability complexity.
- Tool collisions and inconsistent schemas must be normalized.
- Asynchronous callbacks require replay protection and durable correlation.
- n8n workflow governance must be integrated with HANA-X change control.

## Required controls

- deny-by-default server and tool allowlists;
- namespaced permanent tool IDs;
- typed contracts and schema validation;
- identity, authorization, and approval metadata;
- secrets isolation;
- timeout, retry, idempotency, compensation, and cancellation rules;
- authenticated callbacks for asynchronous work;
- linked LangGraph, MCP, n8n, and SAP trace identifiers; and
- versioned workflow promotion across environments.

## Validation

The decision remains Proposed until a proof of concept demonstrates:

1. FastMCP and n8n tools can be discovered and registered without collision.
2. An asynchronous n8n workflow resumes LangGraph exactly once.
3. A proactive event creates a governed Copilot work item rather than bypassing policy.
4. Audit traces link the user request through the final SAP or external-system outcome.
5. Failure, timeout, cancellation, retry, and callback-replay tests pass.
