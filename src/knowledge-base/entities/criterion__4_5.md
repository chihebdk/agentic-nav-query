---
id: criterion.4_5
type: Criterion
label: "4.5 Evaluation & Quality (Evals)"
aliases: ["4.5", "Evaluation & Quality (Evals)"]
tags: ["criterion", "dim-4"]
sources: ["dimensions.json"]
---

# 4.5 Evaluation & Quality (Evals)

**Type:** Criterion  ·  **ID:** `criterion.4_5`

**Also known as:** 4.5, Evaluation & Quality (Evals)

If judging needs a human on every instance, no autonomous version could know it had gone wrong.

## Attributes

- **dimension:** 4
- **criterion_id:** 4.5
- **anchors:** {'L1': 'Ship on demos/vibes', 'L2': 'Manual spot-checks', 'L3': 'Eval suite + regression for priority agents', 'L4': 'Tiered evals gate releases; distribution tested; failures feed back', 'L5': "Evals + trajectory feedback drive continuous improvement; the gate's 'evaluable' condition is met by design"}
- **probing_questions:** [{'q': 'How do you evaluate agents — eval suites, scored traces, regression tests?', 'looking_for': "Evals are quality AND the gate's 'evaluable' condition. Strong: real eval suites + regression. Weak: demos/spot-checks → nothing can credibly graduate."}, {'q': 'Can you objectively tell if the work was done correctly across ordinary, edge, and worst cases?', 'looking_for': 'The evaluable condition. Strong: objective judging incl. edges/worst cases. Weak: needs a human on every instance → no safe autonomy possible.'}, {'q': 'Do you tier evals by cost/speed (commit / PR / pre-deploy / production)?', 'looking_for': 'Tests practical eval discipline. Strong: tiered evals. Weak: all-or-nothing → evals skipped under pressure.'}, {'q': 'Do production failures become regression tests, and do you test the distribution, not the happy path?', 'looking_for': 'Tests the closed quality loop + non-determinism. Strong: failures -> regressions; distribution tested. Weak: happy-path only → silent tail failures.'}]

## Relationships (incoming)

- [Dimension 4: Agent Platform, Harness Engineering & Operations (incl. Autonomy)](./dim__4.md) → has_criterion
- [5.8 Cross-Team Alignment (Governance, Data, Quality)](./criterion__5_8.md) → cross_references
- [Evals & Guardrails](./craft__evals_guardrails.md) → supports_craft
- [Agent](./concept__agent.md) → references_criterion
- [Retrieval Craft](./craft__retrieval_craft.md) → references_criterion
- [Eval Suite](./template__eval_suite.md) → references_criterion
- [Guardrail Stack](./template__guardrail_stack.md) → references_criterion

## Sources

- dimensions.json
