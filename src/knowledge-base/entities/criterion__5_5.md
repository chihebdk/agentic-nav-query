---
id: criterion.5_5
type: Criterion
label: "5.5 Control-Plane Primitives: Registry, Identity, Gateways & Observability"
aliases: ["5.5", "Control-Plane Primitives: Registry, Identity, Gateways & Observability"]
tags: ["criterion", "dim-5"]
sources: ["dimensions.json"]
---

# 5.5 Control-Plane Primitives: Registry, Identity, Gateways & Observability

**Type:** Criterion  ·  **ID:** `criterion.5_5`

**Also known as:** 5.5, Control-Plane Primitives: Registry, Identity, Gateways & Observability

Registry, identity, gateways and multi-purpose observability make a fleet governable, affordable and safe.

## Attributes

- **dimension:** 5
- **criterion_id:** 5.5
- **anchors:** {'L1': 'No registry/identity/gateway; logs only', 'L2': 'Partial inventory; basic logging; ad-hoc gateway', 'L3': 'Registry + per-agent identity for priority agents; an AI gateway in place', 'L4': 'AI gateway (cost/routing/policy) + MCP gateway; observability serves monitoring/evals/cost', 'L5': 'Consolidated gateways (AI/MCP/API); least-privilege identity; observability serves monitoring, logging, security, evals, cost, drift fleet-wide'}
- **probing_questions:** [{'q': 'Is there an agent registry/inventory (what agents exist, owners, scope, status)?', 'looking_for': 'Tests fleet visibility. Strong: a maintained registry. Weak: no inventory → shadow agents.'}, {'q': 'Do agents have managed identity and least-privilege access as a platform primitive?', 'looking_for': 'Tests the access primitive (security DEPTH = Dim 8). Strong: per-agent identity/least-privilege from the platform. Weak: shared/blanket credentials.'}, {'q': 'Do you have an AI/LLM gateway, and what is it leveraged for (cost attribution, routing, caching, rate-limiting, policy/guardrail enforcement)?', 'looking_for': 'Tests the central chokepoint. Strong: a gateway used for cost + routing + policy. Weak: fragmented LLM access, cost blind spots, no policy enforcement point.'}, {'q': 'Which gateways are in place (AI/LLM, MCP, API), and does the AI gateway also serve as the MCP gateway (e.g., via plugins) — how consolidated are they?', 'looking_for': 'Tests gateway taxonomy & consolidation. Strong: deliberate set of gateways (incl. an MCP gateway governing tool/MCP-server traffic), consciously consolidated. Weak: only a traditional API gateway, no MCP-traffic governance, accidental sprawl.'}, {'q': 'What is your agentic observability leveraged for — continuous monitoring, logging, security, evals, cost, and drift?', 'looking_for': 'Tests observability BREADTH. Strong: observability feeds monitoring, evals, security, cost, and drift. Weak: latency/logs only → blind to silent failures, drift, abuse.'}]

## Relationships (incoming)

- [Dimension 5: Agentic Platform & Control Plane (Operating Model)](./dim__5.md) → has_criterion
- [8.2 Agent Identity & Least-Privilege Access](./criterion__8_2.md) → cross_references
- [9.6 Agent Registry, Intake & Lifecycle Governance](./criterion__9_6.md) → cross_references
- [Tool Design & Permissioning](./craft__tool_design_permissioning.md) → supports_craft
- [Observability Minimum](./craft__observability_minimum.md) → supports_craft
- [Control Plane](./concept__control_plane.md) → references_criterion
- [MCP / A2A](./concept__mcp_a2a.md) → references_criterion
- [Production Readiness](./craft__production_readiness.md) → references_criterion
- [Guardrail Stack](./template__guardrail_stack.md) → references_criterion

## Sources

- dimensions.json
