---
id: concept.agent
type: Concept
label: "Agent"
aliases: []
tags: ["concept", "glossary"]
sources: ["glossary.md"]
---

# Agent

**Type:** Concept  ·  **ID:** `concept.agent`

An LLM that selects tools, calls them in a loop, and decides when to stop (prompt + tools + loop + stop conditions). Not every 'agent' pitched is one.

## Relationships (outgoing)

- references_criterion → [4.1 Use-Case Selection & Pattern Fit](./criterion__4_1.md)
- references_criterion → [4.2 Harness, Skills & Runtime Strategy](./criterion__4_2.md)
- references_criterion → [4.3 Agent Architecture & Context Engineering](./criterion__4_3.md)
- references_criterion → [4.4 Graduation to Autonomy (in-loop -> operator -> out-of-loop)](./criterion__4_4.md)
- references_criterion → [4.5 Evaluation & Quality (Evals)](./criterion__4_5.md)
- references_criterion → [4.6 AgentOps: Observability, Reliability, Cost & Trajectory Capture](./criterion__4_6.md)
- references_criterion → [5.4 Reference Patterns & Architectural Governance by Agent Type/Autonomy](./criterion__5_4.md)
- related_to → [The Agent Spectrum & the 90% Rule](./craft__the_agent_spectrum_the_90_rule.md)
- related_to → [Evals & Guardrails](./craft__evals_guardrails.md)

## Relationships (incoming)

- [Harness](./concept__harness.md) → related_to
- [Capability Ladder](./concept__capability_ladder.md) → related_to
- [Agent-Washing](./concept__agent_washing.md) → related_to
- [The 90% Rule](./concept__the_90_rule.md) → related_to

## Sources

- glossary.md
