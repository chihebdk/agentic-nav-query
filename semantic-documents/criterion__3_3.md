---
id: criterion.3_3
type: Criterion
label: "3.3 Data Accessibility & Integration (fit-for-purpose)"
aliases: ["3.3", "Data Accessibility & Integration (fit-for-purpose)"]
tags: ["criterion", "dim-3"]
keywords: ["accessibility", "criterion", "data", "dim-3", "fit-for-purpose", "integration"]
status: current
sources: ["dimensions.json"]
entity_page: ../../knowledge-base/entities/criterion__3_3.md
---

# 3.3 Data Accessibility & Integration (fit-for-purpose)  ·  _Criterion_

MCP, APIs and event streaming solve different layers; maturity is fit-for-purpose selection, not 'everything via MCP.'

**Key facts:** dimension=3; criterion_id=3.3; anchors={'L1': "Siloed; or naive 'MCP-for-everything' experiments", 'L2': 'Some sources connected for pilots; pattern ad-hoc', 'L3': 'Key sources accessible; APIs managed; MCP for agent tool-use over existing APIs', 'L4': 'Fit-for-purpose: event backbone + managed APIs + MCP agent layer + A2A; unstructured accessible; data products', 'L5': 'Standardized, governed, observable agent-access layer over a durable event/API backbone; right pattern per job'}; probing_questions=[{'q': 'Can agents access structured AND unstructured data across systems?', 'looking_for': 'Tests reach across the ~80% that is unstructured. Strong: both accessible. Weak: only structured/siloed → agents see a fraction of context.'}, {'q': 'Do you select integration patterns by fit — event backbone for async/high-volume, managed APIs for deterministic/compliance, MCP for agent tool-use (rule of thumb: MCP when 3+ integrations feed an AI workflow)?', 'looking_for': 'Tests architectural judgment. Strong: fit-for-purpose pattern selection. Weak: one-size-fits-all → wrong tool for the job.'}, {'q': 'Is MCP layered OVER your existing API/event backbone (wrapping APIs), or are you trying to replace integration with MCP?', 'looking_for': "Catches the 'MCP-for-everything' anti-pattern. Strong: MCP as the agent-access layer over a sound backbone. Weak: routing deterministic/high-volume/compliance flows through MCP → latency, cost, non-determinism, compliance risk."}, {'q': 'How do you handle async, reliability, and LLM-specific failures (queues, dead-letter queues) in agent workflows?', 'looking_for': 'Tests resilience of the integration substrate. Strong: durable event backbone + DLQs. Weak: brittle synchronous chains → data loss, stalls.'}].

**Connected to:** Dimension 3: Data, Knowledge Sources & Retrieval → has_criterion; MCP / A2A → references_criterion; Agent-Washing → references_criterion; Retrieval Craft → references_criterion.

**Sourced from:** dimensions.json.
