---
id: criterion.1_2
type: Criterion
label: "1.2 Business-AI Strategic Alignment"
aliases: ["1.2", "Business-AI Strategic Alignment"]
tags: ["criterion", "dim-1"]
sources: ["dimensions.json"]
---

# 1.2 Business-AI Strategic Alignment

**Type:** Criterion  ·  **ID:** `criterion.1_2`

**Also known as:** 1.2, Business-AI Strategic Alignment

Start from business needs; the build-vs-need gap drives 70-80% of scale failures.

## Attributes

- **dimension:** 1
- **criterion_id:** 1.2
- **anchors:** {'L1': 'Tech-led; no link to business goals', 'L2': 'Some initiatives loosely tied to goals', 'L3': 'Each priority initiative traces to an objective; business owns it', 'L4': 'Eng-AI & business-AI run as one operating model', 'L5': 'Alignment continuous; portfolio re-shaped by strategy'}
- **probing_questions:** [{'q': 'Which business goals does each major AI initiative serve?', 'looking_for': 'Tests outcome-orientation vs. tech-for-its-own-sake. Strong: each maps to a named business goal. Weak: tech-led experiments → scale-failure risk.'}, {'q': 'Can you trace each initiative to a specific strategic objective?', 'looking_for': "Probes portfolio traceability. Strong: explicit linkage maintained. Weak: can't trace → misalignment, wasted spend."}, {'q': "Who from the business (not IT) owns each initiative's outcome?", 'looking_for': "Reveals whether the business owns value or it's an IT science project. Strong: a named business owner accountable for results. Weak: only IT owns → adoption/value gap."}, {'q': 'Are engineering-AI and business-AI governed as one operating model?', 'looking_for': '2026 convergence test. Strong: unified governance/operating model. Weak: separate budgets/teams → duplication and fragmentation.'}]

## Relationships (incoming)

- [Dimension 1: Strategy, Leadership & Value Realization](./dim__1.md) → has_criterion
- [Problem-First Scoping](./craft__problem_first_scoping.md) → references_criterion
- [Problem-First Scoping](./template__problem_first_scoping.md) → references_criterion

## Sources

- dimensions.json
