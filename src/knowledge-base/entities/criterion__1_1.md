---
id: criterion.1_1
type: Criterion
label: "1.1 AI & Agentic Vision / Ambition (fit autonomy, augmentation-first)"
aliases: ["1.1", "AI & Agentic Vision / Ambition (fit autonomy, augmentation-first)"]
tags: ["criterion", "dim-1"]
sources: ["dimensions.json"]
---

# 1.1 AI & Agentic Vision / Ambition (fit autonomy, augmentation-first)

**Type:** Criterion  ·  **ID:** `criterion.1_1`

**Also known as:** 1.1, AI & Agentic Vision / Ambition (fit autonomy, augmentation-first)

Sets the altitude. In 2026, maturity = matching autonomy to value/risk and maximizing augmentation, NOT maximizing autonomy.

## Attributes

- **dimension:** 1
- **criterion_id:** 1.1
- **anchors:** {'L1': 'No vision; AI talked about, not directed', 'L2': "Vision = 'become autonomous'; autonomy treated as the goal", 'L3': 'Written end-state; autonomy considered per use case', 'L4': 'Augmentation-first operating model; autonomy matched to value/risk; socialized', 'L5': 'Deliberate human-AI operating model; augmentation maximized, autonomy only where value>cost; adapts as tech shifts'}
- **probing_questions:** [{'q': 'What does the enterprise look like in 3 years if AI/agents succeed?', 'looking_for': "Tests whether a concrete end-state exists. Strong: a vivid, specific picture of what's different and how people work with AI. Weak: vague 'more efficient' or silence → vision absent."}, {'q': 'Is more autonomy the goal, or do you match autonomy to the value and the cost-of-being-wrong of each use case?', 'looking_for': "The core 2026 test. Strong: autonomy is fitted per use case by value/risk; not an end in itself. Weak: 'become a fully autonomous enterprise' as the goal → chasing the low-yield pattern that mostly fails."}, {'q': 'Where is your value coming from — augmenting people via reusable skills, or autonomous end-to-end agents?', 'looking_for': 'Augmentation is the higher-value zone today. Strong: augmentation-first, autonomy applied selectively where justified. Weak: the program is bet on autonomous agents → high failure risk, lower realized value.'}, {'q': 'Has leadership written down and socialized an AI/agent vision?', 'looking_for': "Separates a shared vision from hallway talk. Strong: documented, communicated, referenced in decisions. Weak: lives in a few heads → won't align the org."}]

## Relationships (incoming)

- [Dimension 1: Strategy, Leadership & Value Realization](./dim__1.md) → has_criterion
- [Augmentation-First](./concept__augmentation_first.md) → references_criterion
- [Autonomy Ladder](./concept__autonomy_ladder.md) → references_criterion
- [Problem-First Scoping](./craft__problem_first_scoping.md) → references_criterion

## Sources

- dimensions.json
