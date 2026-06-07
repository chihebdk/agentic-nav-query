---
id: criterion.4_3
type: Criterion
label: "4.3 Agent Architecture & Context Engineering"
aliases: ["4.3", "Agent Architecture & Context Engineering"]
tags: ["criterion", "dim-4"]
keywords: ["agent", "architecture", "context", "criterion", "dim-4", "engineering"]
status: current
sources: ["dimensions.json"]
entity_page: ../../knowledge-base/entities/criterion__4_3.md
---

# 4.3 Agent Architecture & Context Engineering  ·  _Criterion_

Architecture determines reliability; accuracy compounds negatively across chained agents; it's all context.

**Key facts:** dimension=4; criterion_id=4.3; anchors={'L1': 'Monolithic or prematurely multi-agent; infra-first', 'L2': 'Some decomposition; ad-hoc context', 'L3': 'Single-agent-first; hybrid extraction; context designed first', 'L4': 'Deliberate patterns; function/events/MCP/durable-execution used correctly', 'L5': 'Reliable hybrid architectures; context-first; reusable, observable design'}; probing_questions=[{'q': 'Do you start with a single agent and maximize it before adding agents, and avoid chaining within a domain?', 'looking_for': "'Accuracy compounds negatively across chained agents.' Strong: single-first, no needless chaining. Weak: agent sprawl → context loss at handoffs."}, {'q': 'Do you extract deterministic steps into a workflow and keep the agent only at judgment points (hybrid)?', 'looking_for': 'Tests the hybrid pattern. Strong: deterministic steps in code, agent at judgment. Weak: agent does everything → fragile, costly.'}, {'q': 'Is context engineering treated as the primary lever (what the model sees), with memory/RAG/tools as utilities?', 'looking_for': "'It's all context.' Strong: context designed first. Weak: infrastructure built first, context an afterthought → poor quality."}, {'q': 'How do agents integrate — function calling for actions, events for outcomes, MCP for shared tools, durable execution for orchestration?', 'looking_for': 'Tests integration design. Strong: right mechanism per job; ambient agents event-driven. Weak: brittle synchronous chains / API rebuilds for agents.'}].

**Connected to:** Dimension 4: Agent Platform, Harness Engineering & Operations (incl. Autonomy) → has_criterion; Agent Memory → supports_craft; Agent → references_criterion; Durable Execution → references_criterion; The 90% Rule → references_criterion; Capability Ladder → references_criterion; Build-to-Delete → references_criterion; Retrieval Craft → references_criterion; The Agent Spectrum & the 90% Rule → references_criterion; Tool Design & Permissioning → references_criterion; Model Selection → references_criterion.

**Sourced from:** dimensions.json.
