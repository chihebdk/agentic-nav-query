---
id: criterion.7_1
type: Criterion
label: "7.1 AI Fluency & Role-Based Training (enterprise-wide)"
aliases: ["7.1", "AI Fluency & Role-Based Training (enterprise-wide)"]
tags: ["criterion", "dim-7"]
sources: ["dimensions.json"]
---

# 7.1 AI Fluency & Role-Based Training (enterprise-wide)

**Type:** Criterion  ·  **ID:** `criterion.7_1`

**Also known as:** 7.1, AI Fluency & Role-Based Training (enterprise-wide)

Talent readiness is the lowest AI-readiness dimension; enterprise-wide, role-appropriate enablement is foundational to the transformation.

## Attributes

- **dimension:** 7
- **criterion_id:** 7.1
- **anchors:** {'L1': 'No structured AI training, or only a few technical people', 'L2': 'Ad-hoc training for technical teams', 'L3': 'Role-based learning paths; agentic skills targeted; citizen-builder enablement', 'L4': 'Enterprise-wide enablement (every function/level) with role-appropriate depth; continuous reskilling', 'L5': 'Enterprise-wide, continuous, MEASURED capability uplift; AI fluency a baseline expectation for all'}
- **probing_questions:** [{'q': 'Is AI/agent fluency treated as table stakes ACROSS THE WHOLE ENTERPRISE (every function and level), with role-appropriate depth — or only for technical teams?', 'looking_for': "Tests breadth of enablement. Strong: enterprise-wide, role-appropriate enablement for everyone. Weak: training confined to technical/specialist teams → the rest of the org can't use/guide AI."}, {'q': 'Are there role-differentiated learning paths (leaders, builders, citizen developers, end users), and does training target AGENTIC skills (orchestration, skill-building, supervising agents) rather than only classical data-science/ML?', 'looking_for': 'Tests role-fit and agentic focus. Strong: differentiated paths targeting agentic skills. Weak: one generic course, or classical-ML training that misses the agentic shift.'}, {'q': 'Is there a continuous reskilling cadence as roles and tools change, plus enablement for citizen builders?', 'looking_for': 'Tests sustainability. Strong: continuous reskilling + citizen-builder enablement. Weak: one-time training that goes stale.'}, {'q': 'How do you measure enablement reach and capability uplift (coverage, fluency, active builders) — not just course completions?', 'looking_for': 'Tests outcome focus. Strong: measured reach + capability uplift. Weak: vanity metrics (completions) or no measurement.'}]

## Relationships (incoming)

- [Dimension 7: Workforce, Talent & Operating Model](./dim__7.md) → has_criterion
- [Role-Based Enablement](./craft__role_based_enablement.md) → supports_craft
- [UX of AI](./craft__ux_of_ai.md) → references_criterion

## Sources

- dimensions.json
