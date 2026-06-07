---
id: criterion.1_8
type: Criterion
label: "1.8 Adaptability & Pattern Resilience (build-to-delete)"
aliases: ["1.8", "Adaptability & Pattern Resilience (build-to-delete)"]
tags: ["criterion", "dim-1"]
sources: ["dimensions.json"]
---

# 1.8 Adaptability & Pattern Resilience (build-to-delete)

**Type:** Criterion  ·  **ID:** `criterion.1_8`

**Also known as:** 1.8, Adaptability & Pattern Resilience (build-to-delete)

AI patterns churn yearly (chatbot->agentic->harness/skills); over-committing to a pattern/vendor creates write-offs.

## Attributes

- **dimension:** 1
- **criterion_id:** 1.8
- **anchors:** {'L1': 'Big bets on one pattern/vendor; unaware of churn', 'L2': 'Aware patterns change, no deliberate response', 'L3': 'Some durable-asset focus; lock-in acknowledged', 'L4': 'Build-to-delete posture; durable assets prioritized; model/harness swappable', 'L5': 'Strategy assumes churn; advantage parked in durable assets (skills/data); re-platforms cheaply'}
- **probing_questions:** [{'q': 'If the dominant agent pattern shifts again in 12 months, what would you have to throw away?', 'looking_for': 'Tests exposure to pattern churn. Strong: little is wasted — durable assets survive. Weak: large bespoke builds would be written off → fragile strategy.'}, {'q': 'Are you investing in durable assets (skills, data, knowledge) or in brittle orchestration / bespoke loops?', 'looking_for': 'Probes where the bet is parked. Strong: durable assets that outlast patterns. Weak: heavy investment in brittle plumbing that the next model release breaks.'}, {'q': 'How locked-in are you to a specific vendor or pattern, and can you swap models/harnesses cheaply?', 'looking_for': "Tests lock-in and build-to-delete posture. Strong: swappable, vendor-agnostic. Weak: deeply coupled → can't adapt when the field moves."}, {'q': 'Does leadership treat fast pattern change as a planning assumption?', 'looking_for': "Tests strategic realism. Strong: churn is assumed and planned for. Weak: treats today's pattern as permanent → over-commits."}]

## Relationships (incoming)

- [Dimension 1: Strategy, Leadership & Value Realization](./dim__1.md) → has_criterion
- [Build-to-Delete](./concept__build_to_delete.md) → references_criterion
- [The Two Moats](./concept__the_two_moats.md) → references_criterion
- [Model Selection](./template__model_selection.md) → references_criterion

## Sources

- dimensions.json
