---
source_id: ICE-SRC-009
title: n8n and Multi-MCP Architecture Supplement
authority_tier: Contextual
status: Proposed
related_sources:
  - ICE-SRC-008
---

# n8n and Multi-MCP Architecture Supplement

## Owner-provided direction

The development environment contains:

- n8n and an n8n MCP server;
- FastMCP as the primary management plane for custom MCP servers;
- specialized standalone MCP servers, including Docling MCP, Crawl4AI MCP, and Shadcn MCP; and
- a requirement to support n8n independently rather than forcing it behind the FastMCP hub.

## Normalized architectural interpretation

HANA-X Copilot should use a **governed multi-MCP integration gateway** rather than assume a single MCP server or transport. LangGraph remains the stateful orchestration and governance authority. It may connect through separate client profiles to:

1. **FastMCP-managed servers** for custom Python tools and internal domain logic.
2. **n8n MCP** for visual workflow automation, multi-system integration, asynchronous jobs, event triggers, transformation, and notifications.
3. **Standalone specialized servers** for capabilities best operated independently, including document parsing, web acquisition, and UI-generation support.

## Recommended division of responsibilities

| Component | Responsibility |
|---|---|
| LangGraph | Intent state, clarification, planning, policy routing, human interrupts, approvals, compensation decisions, and workflow-level audit |
| FastMCP | Custom Python tools, domain utilities, low-latency internal services, SAP metadata helpers, and security utilities |
| n8n | Visual multi-system workflows, long-running execution, retries, waits, event triggers, transformation, and enterprise notifications |
| Standalone MCP servers | Specialized capabilities whose lifecycle or protocol is operationally cleaner outside FastMCP |

## Primary use cases for n8n

- Aggregate SAP and non-SAP context into a normalized tool response.
- Execute long-running asynchronous workflows without holding an interactive agent request open.
- Receive enterprise events and create proactive Copilot work items or notifications.
- Coordinate approved changes across SAP, repositories, messaging, CRM, ticketing, and other enterprise services.

## Required controls

- deny-by-default server and tool allowlists;
- namespaced tool identifiers;
- permanent tool and workflow versions;
- typed input and output contracts;
- authentication and authorization profiles per server;
- approval classification and policy mapping;
- correlation IDs for asynchronous execution;
- idempotent callback and completion processing;
- timeout, retry, compensation, and dead-letter behavior;
- secrets isolation within the owning integration runtime;
- linked LangGraph, MCP, n8n, and SAP audit identifiers; and
- health, capability, and version discovery for every configured server.

## Verification notes

n8n officially provides an MCP Server Trigger and documents URL, authentication, path, limitations, and reverse-proxy considerations. The exact transport and authentication configuration must be validated against the installed n8n release and deployment topology. FastMCP supports client-side connections to MCP servers; HANA-X should not assume that every server is aggregated behind one hub. Illustrative code from the original source is conceptual and is not an implementation contract.
