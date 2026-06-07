---
id: criterion.4_2
type: Criterion
label: "4.2 Harness, Skills & Runtime Strategy"
aliases: ["4.2", "Harness, Skills & Runtime Strategy"]
tags: ["criterion", "dim-4"]
sources: ["dimensions.json"]
---

# 4.2 Harness, Skills & Runtime Strategy

**Type:** Criterion  ·  **ID:** `criterion.4_2`

**Also known as:** 4.2, Harness, Skills & Runtime Strategy

~75-80% of value is in skill-based augmentation agents, and they are the on-ramp to autonomy.

## Attributes

- **dimension:** 4
- **criterion_id:** 4.2
- **anchors:** {'L1': 'Bespoke autonomous builds; skills not leveraged', 'L2': 'Some harness/skill use; ad-hoc', 'L3': 'Helper skills built upward into closed loops; portable skills', 'L4': 'Skill-based agents the primary engine; local->centralized promotion path', 'L5': 'Local agents promoted to a centralized runtime where justified; skills portable/build-to-delete'}
- **probing_questions:** [{'q': 'Are you leveraging harness agents (Claude Code/Cowork + plugins + skills) as a primary value engine?', 'looking_for': 'Tests capture of the ~75-80% near-term value. Strong: skill-based agents are a primary engine. Weak: chasing bespoke autonomous builds → misses the real value.'}, {'q': "Do you build UPWARD from small, genuinely-used helper skills into a worker's closed loop, or script big agents top-down?", 'looking_for': 'Tests build direction. Strong: upward from used helpers. Weak: top-down process scripting → stalls (tacit knowledge never captured).'}, {'q': 'Are skills/plugins portable and tool-independent (build-to-delete)?', 'looking_for': 'Tests durability of the asset vs the tool. Strong: skills move across tools intact. Weak: locked to one platform → rework when the tool turns over.'}, {'q': 'Is there a path to assemble local agents and promote them to a centralized/managed runtime as they mature?', 'looking_for': 'Tests the on-ramp to autonomy. Strong: a clear local->centralized promotion path. Weak: no path → local agents never graduate safely.'}]

## Relationships (incoming)

- [Dimension 4: Agent Platform, Harness Engineering & Operations (incl. Autonomy)](./dim__4.md) → has_criterion
- [Harness](./concept__harness.md) → references_criterion
- [Agent](./concept__agent.md) → references_criterion
- [Build-to-Delete](./concept__build_to_delete.md) → references_criterion
- [The Agent Spectrum & the 90% Rule](./craft__the_agent_spectrum_the_90_rule.md) → references_criterion

## Sources

- dimensions.json
