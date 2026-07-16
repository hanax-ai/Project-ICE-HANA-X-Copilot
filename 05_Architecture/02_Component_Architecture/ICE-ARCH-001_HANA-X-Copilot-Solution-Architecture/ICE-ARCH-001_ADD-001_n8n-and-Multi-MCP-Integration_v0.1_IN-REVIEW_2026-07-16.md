---
artifact_id: ICE-ARCH-001
addendum_id: ICE-ARCH-001-ADD-001
title: n8n and Multi-MCP Integration Architecture
version: "0.1"
status: IN-REVIEW
owner: HANA-X AI Architecture
derived_from:
  - ICE-SRC-009
related_sources:
  - ICE-SRC-008
---

# n8n and Multi-MCP Integration Architecture

## 1. Decision summary

HANA-X Copilot adopts a **governed multi-MCP integration gateway**. LangGraph remains the system-level orchestration, policy-routing, clarification, planning, approval, and recovery authority. It connects to multiple MCP server domains through independently governed client profiles rather than requiring every server to sit behind one hub.

The baseline server domains are:

1. **FastMCP-managed custom services** — local Python tools, domain logic, SAP metadata utilities, security helpers, and low-latency internal functions.
2. **n8n workflow automation** — visual multi-system workflows, transformations, asynchronous execution, event triggers, waits, retries, and notifications.
3. **Standalone specialized MCP servers** — independently operated services such as Docling MCP, Crawl4AI MCP, and Shadcn MCP when direct access is operationally preferable.

## 2. Architectural placement

```text
CopilotKit Experience Layer
        │
        │ AG-UI
        ▼
LangGraph Agent Runtime
        │
        ├── Policy, clarification, planning, approval, checkpointing
        │
        ▼
Governed Multi-MCP Integration Gateway
        ├── FastMCP client profile → FastMCP-managed custom tools
        ├── n8n client profile → n8n MCP Server Trigger / workflow tools
        └── Standalone profiles → Docling, Crawl4AI, Shadcn, other approved servers
        │
        ▼
SAP S/4HANA and approved enterprise systems
```

The gateway is a logical control plane implemented within the HANA-X backend. It maintains server registration, health, capabilities, tool namespaces, authorization requirements, policy classes, and audit mappings. It is not a requirement that every server share the same process, transport, authentication scheme, or lifecycle.

## 3. Division of labor

| Capability | LangGraph | FastMCP | n8n | Standalone MCP |
|---|---|---|---|---|
| Business intent state | Authoritative | No | No | No |
| Clarification and HITL | Authoritative | Supporting tools only | Workflow pause only when delegated | Supporting tools only |
| Policy and approval decision | Authoritative | Enforces tool-local controls | Enforces workflow-local controls | Enforces server-local controls |
| Stateful agent routing | Authoritative | No | No | No |
| Custom Python domain logic | May invoke | Primary | Possible but not preferred | Service-specific |
| Visual multi-system orchestration | Supervises | No | Primary | No |
| Long-running waits and retries | Coordinates | Limited | Primary for delegated workflows | Service-specific |
| Enterprise event triggers | Receives/resumes work | May emit | Primary | May emit |
| Specialized parsing or acquisition | Routes | May proxy | May coordinate | Primary |

n8n does not replace LangGraph. A workflow exposed by n8n is treated as a registered tool or delegated execution plan. It cannot independently broaden scope, bypass approval, alter policy, or invoke unregistered SAP operations.

## 4. n8n use cases

### 4.1 Multi-system context aggregation

Use n8n when one governed operation must collect or transform data across SAP and other enterprise services. The workflow returns a normalized response contract and provenance for each contributing system.

### 4.2 Long-running asynchronous execution

Use n8n for workflows that exceed the interactive request window or require waits, retries, rate limiting, scheduled continuation, or external-system completion.

The launch contract returns:

- workflow definition ID and version;
- execution ID;
- HANA-X correlation ID;
- accepted timestamp;
- expected completion or timeout policy;
- callback or event contract; and
- user-visible status link.

Completion processing must be authenticated and idempotent. LangGraph resumes from a persisted checkpoint only after validating the correlation ID, execution identity, workflow version, payload digest, and current policy state.

### 4.3 Proactive enterprise events

n8n may receive approved SAP or non-SAP events, enrich them, and submit a proactive work item to HANA-X Copilot. The event does not directly create a privileged agent action. The Copilot evaluates identity, policy, urgency, duplication, and approval requirements before presenting or executing the resulting plan.

## 5. Tool registration and discovery

Dynamic discovery is permitted, but discovered tools are not automatically exposed to a model. Every tool passes through a deny-by-default registry.

Each server and tool record includes:

- server ID, type, owner, environment, version, and health;
- transport and authentication profile;
- namespaced tool ID, such as `fastmcp.sap.get_purchase_order` or `n8n.procurement.expedite_shipment`;
- business purpose and risk classification;
- typed input and output schemas;
- data-classification and egress rules;
- required identity and authorization context;
- approval and segregation-of-duties rules;
- timeout, retry, idempotency, and compensation behavior;
- asynchronous callback contract where applicable;
- audit and observability fields; and
- lifecycle status and deprecation date.

Tool-name collisions are resolved through namespaces, never by first-discovered precedence.

## 6. Security and secrets

- Credentials remain in the runtime that owns the integration.
- FastMCP, n8n, and standalone servers receive only the minimum scoped credentials required for the registered tool.
- Raw credentials and bearer tokens are never placed in model prompts.
- Server-to-server calls use authenticated transport appropriate to the deployment.
- Callbacks include replay protection, expiry, signature or token validation, and correlation checks.
- Direct standalone connections use the same registration, allowlist, policy, and audit controls as hub-managed tools.

## 7. Audit and observability

A delegated workflow must be reconstructable across systems. The trace links:

```text
user request
→ LangGraph run ID
→ plan and approval record
→ MCP server and tool ID/version
→ n8n workflow and execution ID, when used
→ SAP or external-system request IDs
→ callback/event ID
→ final result and user notification
```

Logs record business identifiers with masking rules. Secrets and unrestricted payloads are excluded.

## 8. Technical corrections to the exploratory source

- The exact n8n transport, URL, authentication mode, and reverse-proxy configuration are deployment-specific and must be confirmed against the installed n8n version.
- The architecture does not assume an npm package or stdio command named `@n8n/mcp-server`; n8n's documented MCP Server Trigger exposes workflows through its configured MCP endpoint.
- MCP tool descriptions returned by a server are not trusted authorization policy.
- Combining tool lists in memory is insufficient; tools must be adapted, namespaced, filtered, and registered.
- Direct calls to Docling, Crawl4AI, or Shadcn are allowed only when a registered standalone client profile is approved.
- CopilotKit and AG-UI remain the user-agent interaction boundary; they do not authorize n8n or MCP execution.

## 9. Proposed requirements

- `ICE-MCP-001` — The platform shall support multiple independently configured MCP server connections.
- `ICE-MCP-002` — All discovered tools shall pass a deny-by-default registration and allowlist process.
- `ICE-MCP-003` — Tool IDs shall be globally unique and namespaced by server domain.
- `ICE-N8N-001` — n8n workflows exposed as tools shall have versioned contracts and governance metadata.
- `ICE-N8N-002` — Asynchronous n8n execution shall use durable correlation, authenticated callbacks, and idempotent completion.
- `ICE-N8N-003` — n8n event triggers shall create governed work items rather than bypass agent policy.
- `ICE-OBS-002` — Traces shall link LangGraph, MCP, n8n, and SAP execution identifiers.

## 10. Open decisions

1. Which transport and authentication profiles are enabled for the installed n8n MCP endpoint?
2. Will the HANA-X backend use one multi-server client library or dedicated adapters per server class?
3. Which workflows are eligible for n8n versus native LangGraph or FastMCP implementation?
4. What maximum execution duration and retention period apply to delegated n8n jobs?
5. What callback endpoint and signing mechanism will resume LangGraph safely?
6. Is Shadcn MCP permitted to provide only design-time component scaffolding, or may it participate at runtime?
7. Which SAP events are available in the initial customer landscape, and how will n8n receive them?

## 11. Recommendation

Adopt the multi-MCP gateway as a proposed baseline and run a proof of concept with three workflows:

1. **Read aggregation:** SAP purchase-order context plus an approved external system.
2. **Asynchronous operation:** a long-running workflow with callback, timeout, retry, and cancellation.
3. **Proactive event:** an SAP or simulated exception event that creates a governed Copilot work item.

Promotion from `IN-REVIEW` requires successful security, identity, failure-recovery, audit, and versioning tests.