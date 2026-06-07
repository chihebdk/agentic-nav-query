---
id: criterion.1_7
type: Criterion
label: "1.7 Sourcing & Stack Strategy (2026)"
aliases: ["1.7", "Sourcing & Stack Strategy (2026)"]
tags: ["criterion", "dim-1"]
sources: ["dimensions.json"]
---

# 1.7 Sourcing & Stack Strategy (2026)

**Type:** Criterion  ·  **ID:** `criterion.1_7`

**Also known as:** 1.7, Sourcing & Stack Strategy (2026)

Build-vs-buy is now a placement decision; standardizing is where scaling leverage lives — and where you avoid paying agent prices for relabeled RPA.

## Attributes

- **dimension:** 1
- **criterion_id:** 1.7
- **anchors:** {'L1': 'Every team improvises; buys on labels', 'L2': 'Awareness, no standard', 'L3': 'Documented build/buy/managed rule; capability assessed beyond labels', 'L4': 'Standard harness + managed/self-host policy; MCP/A2A stance', 'L5': 'Deliberate, vendor-agnostic stack; advantage parked in the knowledge layer'}
- **probing_questions:** [{'q': 'Have you standardized a harness/runtime, or does each team build its own?', 'looking_for': 'Tests for an operating-model standard vs. fragmentation. Strong: a chosen standard with rationale. Weak: every team improvises → sprawl, rework.'}, {'q': 'Can you distinguish genuine agentic capability from relabeled RPA/workflow when you buy or build?', 'looking_for': "Anti-'agent-washing' discernment at sourcing. Strong: buys capability, not a label; knows what's under the hood. Weak: accepts vendor framing → overpays for workflow automation."}, {'q': 'Managed vs. self-hosted, and what is your interoperability stance (MCP / A2A)?', 'looking_for': 'Probes deliberate placement and lock-in awareness. Strong: a clear rule by sensitivity/scale + standards posture. Weak: no view → accidental architecture and lock-in.'}, {'q': 'Is there a build-vs-buy-vs-managed decision rule?', 'looking_for': 'Tests for repeatable sourcing discipline. Strong: a documented rule applied consistently. Weak: case-by-case improvisation.'}]

## Relationships (incoming)

- [Dimension 1: Strategy, Leadership & Value Realization](./dim__1.md) → has_criterion
- [Harness](./concept__harness.md) → references_criterion
- [MCP / A2A](./concept__mcp_a2a.md) → references_criterion
- [Agent-Washing](./concept__agent_washing.md) → references_criterion
- [Model Selection](./template__model_selection.md) → references_criterion

## Sources

- dimensions.json
