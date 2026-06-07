---
id: criterion.4_3
type: Criterion
label: "4.3 Agent Architecture & Context Engineering"
aliases: ["4.3", "Agent Architecture & Context Engineering"]
tags: ["criterion", "dim-4"]
sources: ["dimensions.json"]
---

# 4.3 Agent Architecture & Context Engineering

**Type:** Criterion  ·  **ID:** `criterion.4_3`

**Also known as:** 4.3, Agent Architecture & Context Engineering

Architecture determines reliability; accuracy compounds negatively across chained agents; it's all context.

## Attributes

- **dimension:** 4
- **criterion_id:** 4.3
- **anchors:** {'L1': 'Monolithic or prematurely multi-agent; infra-first', 'L2': 'Some decomposition; ad-hoc context', 'L3': 'Single-agent-first; hybrid extraction; context designed first', 'L4': 'Deliberate patterns; function/events/MCP/durable-execution used correctly', 'L5': 'Reliable hybrid architectures; context-first; reusable, observable design'}
- **probing_questions:** [{'q': 'Do you start with a single agent and maximize it before adding agents, and avoid chaining within a domain?', 'looking_for': "'Accuracy compounds negatively across chained agents.' Strong: single-first, no needless chaining. Weak: agent sprawl → context loss at handoffs."}, {'q': 'Do you extract deterministic steps into a workflow and keep the agent only at judgment points (hybrid)?', 'looking_for': 'Tests the hybrid pattern. Strong: deterministic steps in code, agent at judgment. Weak: agent does everything → fragile, costly.'}, {'q': 'Is context engineering treated as the primary lever (what the model sees), with memory/RAG/tools as utilities?', 'looking_for': "'It's all context.' Strong: context designed first. Weak: infrastructure built first, context an afterthought → poor quality."}, {'q': 'How do agents integrate — function calling for actions, events for outcomes, MCP for shared tools, durable execution for orchestration?', 'looking_for': 'Tests integration design. Strong: right mechanism per job; ambient agents event-driven. Weak: brittle synchronous chains / API rebuilds for agents.'}]

## Relationships (incoming)

- [Dimension 4: Agent Platform, Harness Engineering & Operations (incl. Autonomy)](./dim__4.md) → has_criterion
- [Agent Memory](./craft__agent_memory.md) → supports_craft
- [Agent](./concept__agent.md) → references_criterion
- [Durable Execution](./concept__durable_execution.md) → references_criterion
- [The 90% Rule](./concept__the_90_rule.md) → references_criterion
- [Capability Ladder](./concept__capability_ladder.md) → references_criterion
- [Build-to-Delete](./concept__build_to_delete.md) → references_criterion
- [Retrieval Craft](./craft__retrieval_craft.md) → references_criterion
- [The Agent Spectrum & the 90% Rule](./craft__the_agent_spectrum_the_90_rule.md) → references_criterion
- [Tool Design & Permissioning](./craft__tool_design_permissioning.md) → references_criterion
- [Model Selection](./template__model_selection.md) → references_criterion

## Sources

- dimensions.json
