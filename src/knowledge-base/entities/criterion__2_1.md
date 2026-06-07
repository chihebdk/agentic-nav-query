---
id: criterion.2_1
type: Criterion
label: "2.1 Knowledge Capture & Codification"
aliases: ["2.1", "Knowledge Capture & Codification"]
tags: ["criterion", "dim-2"]
sources: ["dimensions.json"]
---

# 2.1 Knowledge Capture & Codification

**Type:** Criterion  ·  **ID:** `criterion.2_1`

**Also known as:** 2.1, Knowledge Capture & Codification

Uncodified tacit knowledge is invisible to agents; codified expertise is the moat.

## Attributes

- **dimension:** 2
- **criterion_id:** 2.1
- **anchors:** {'L1': 'Knowledge in heads (all functions); not mapped', 'L2': 'Some docs; ad-hoc capture', 'L3': 'Sources mapped; expert procedures across functions codified into skills for priority areas', 'L4': 'Systematic codification pipeline; tacit knowledge routinely externalized', 'L5': 'Continuous capture; codified expertise is a managed, expanding moat'}
- **probing_questions:** [{'q': 'Where does your most valuable expertise live across functions (PM, ops, projects, eng, analysts) — and have you mapped it?', 'looking_for': "Tests whether the org knows where its tacit knowledge sits — the prerequisite to codifying it. Strong: a deliberate map of critical expertise and who holds it. Weak: 'in people's heads', unmapped → can't codify, key-person risk."}, {'q': "Are experts' procedures/judgment being codified into skills, or only documented?", 'looking_for': 'Distinguishes executable skills from passive docs. Strong: know-how turned into runnable skills. Weak: wikis/SOPs only → not usable by agents.'}, {'q': 'How do you codify know-how without flattening its nuance?', 'looking_for': "Probes whether judgment, edge cases and the 'why' survive — not just happy-path steps. Strong: experts review; edge cases + rationale captured; tested on hard cases; feedback loop. Weak: thin checklists → confidently wrong output."}, {'q': "What stops a senior expert's knowledge from leaving with them?", 'looking_for': 'Tests resilience to attrition (key-person risk). Strong: critical expertise codified and shared. Weak: knowledge walks out the door when they leave.'}]

## Relationships (incoming)

- [Dimension 2: Knowledge Building & Capability Reuse](./dim__2.md) → has_criterion
- [Knowledge Moat](./concept__knowledge_moat.md) → references_criterion
- [Skill](./concept__skill.md) → references_criterion
- [Skills-as-Documentation](./concept__skills_as_documentation.md) → references_criterion
- [Skill Spec](./template__skill_spec.md) → references_criterion

## Sources

- dimensions.json
