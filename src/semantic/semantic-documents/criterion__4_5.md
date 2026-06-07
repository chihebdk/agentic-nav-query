---
id: criterion.4_5
type: Criterion
label: "4.5 Evaluation & Quality (Evals)"
aliases: ["4.5", "Evaluation & Quality (Evals)"]
tags: ["criterion", "dim-4"]
keywords: ["criterion", "dim-4", "evals", "evaluation", "quality"]
status: current
sources: ["dimensions.json"]
entity_page: ../../knowledge-base/entities/criterion__4_5.md
---

# 4.5 Evaluation & Quality (Evals)  ·  _Criterion_

If judging needs a human on every instance, no autonomous version could know it had gone wrong.

**Key facts:** dimension=4; criterion_id=4.5; anchors={'L1': 'Ship on demos/vibes', 'L2': 'Manual spot-checks', 'L3': 'Eval suite + regression for priority agents', 'L4': 'Tiered evals gate releases; distribution tested; failures feed back', 'L5': "Evals + trajectory feedback drive continuous improvement; the gate's 'evaluable' condition is met by design"}; probing_questions=[{'q': 'How do you evaluate agents — eval suites, scored traces, regression tests?', 'looking_for': "Evals are quality AND the gate's 'evaluable' condition. Strong: real eval suites + regression. Weak: demos/spot-checks → nothing can credibly graduate."}, {'q': 'Can you objectively tell if the work was done correctly across ordinary, edge, and worst cases?', 'looking_for': 'The evaluable condition. Strong: objective judging incl. edges/worst cases. Weak: needs a human on every instance → no safe autonomy possible.'}, {'q': 'Do you tier evals by cost/speed (commit / PR / pre-deploy / production)?', 'looking_for': 'Tests practical eval discipline. Strong: tiered evals. Weak: all-or-nothing → evals skipped under pressure.'}, {'q': 'Do production failures become regression tests, and do you test the distribution, not the happy path?', 'looking_for': 'Tests the closed quality loop + non-determinism. Strong: failures -> regressions; distribution tested. Weak: happy-path only → silent tail failures.'}].

**Connected to:** Dimension 4: Agent Platform, Harness Engineering & Operations (incl. Autonomy) → has_criterion; 5.8 Cross-Team Alignment (Governance, Data, Quality) → cross_references; Evals & Guardrails → supports_craft; Agent → references_criterion; Retrieval Craft → references_criterion; Eval Suite → references_criterion; Guardrail Stack → references_criterion.

**Sourced from:** dimensions.json.
