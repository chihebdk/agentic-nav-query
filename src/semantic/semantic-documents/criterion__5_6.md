---
id: criterion.5_6
type: Criterion
label: "5.6 Orchestration, Durable-Execution Runtime & Tooling/Connector Catalog"
aliases: ["5.6", "Orchestration, Durable-Execution Runtime & Tooling/Connector Catalog"]
tags: ["criterion", "dim-5"]
keywords: ["catalog", "criterion", "dim-5", "durable-execution", "orchestration", "runtime", "tooling/connector"]
status: current
sources: ["dimensions.json"]
entity_page: ../../knowledge-base/entities/criterion__5_6.md
---

# 5.6 Orchestration, Durable-Execution Runtime & Tooling/Connector Catalog  ·  _Criterion_

Long-running/Deep agents must survive failures via durable execution; shared orchestration + a governed tool catalog let agents act and coordinate reliably at scale.

**Key facts:** dimension=5; criterion_id=5.6; anchors={'L1': 'No orchestration runtime; agents restart on failure; bespoke tools per agent', 'L2': 'Some workflow glue; tools duplicated; no durable execution', 'L3': 'Orchestration for priority flows; a tool/connector catalog emerging', 'L4': 'Managed orchestration + durable execution (state persistence/resume) for long-running agents; governed shared tool/MCP-server catalog with standards', 'L5': 'Platform durable-execution runtime (Deep agents survive failures); discoverable, versioned tool catalog; orchestration + reasoning as clean complementary layers'}; probing_questions=[{'q': 'Does the platform provide a managed orchestration runtime for multi-step / multi-agent (A2A) coordination, or does each team build its own?', 'looking_for': 'Tests shared orchestration. Strong: a platform orchestration runtime. Weak: bespoke orchestration per team → fragmentation.'}, {'q': 'For long-running / Deep agents, is there a durable-execution platform so they survive failures and resume (state persistence, recovery) rather than restart?', 'looking_for': 'THE key primitive for Deep agents. Strong: durable execution (e.g., Temporal-style or managed runtime with resumable state). Weak: long-running agents restart from scratch / must be babysat → unreliable.'}, {'q': 'Is there a shared, governed tool/connector/MCP-server catalog (adapters, discovery, versioning)?', 'looking_for': 'Tests the tool catalog. Strong: a discoverable, versioned catalog of vetted tools/connectors. Weak: bespoke tools rebuilt per agent.'}, {'q': "Are tool sets kept small and task-relevant, with tool-design standards (clear function signatures, designed from the agent's perspective)?", 'looking_for': 'Tests tool-design discipline (adapters are the primary driver of agent reliability). Strong: small, task-scoped tools with standards. Weak: agents handed large API catalogs → worse performance.'}, {'q': "Is durable execution / orchestration treated as a complementary layer to the agent's reasoning loop, not conflated with it?", 'looking_for': 'Tests architectural clarity. Strong: durable-execution platform + agent framework as separate, complementary layers. Weak: orchestration and reasoning tangled → brittle, hard to operate.'}].

**Connected to:** Dimension 5: Agentic Platform & Control Plane (Operating Model) → has_criterion; Control Plane → references_criterion; Durable Execution → references_criterion; Agent Memory → references_criterion.

**Sourced from:** dimensions.json.
