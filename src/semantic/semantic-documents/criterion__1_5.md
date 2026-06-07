---
id: criterion.1_5
type: Criterion
label: "1.5 Investment & Funding Model"
aliases: ["1.5", "Investment & Funding Model"]
tags: ["criterion", "dim-1"]
keywords: ["criterion", "dim-1", "funding", "investment", "model"]
status: current
sources: ["dimensions.json"]
entity_page: ../../knowledge-base/entities/criterion__1_5.md
---

# 1.5 Investment & Funding Model  ·  _Criterion_

At scale, poor unit economics can erase the margin AI was meant to defend; error-recovery cost is part of true TCO (ties to Dim 6.2).

**Key facts:** dimension=1; criterion_id=1.5; anchors={'L1': 'No dedicated funding / one-off; recovery cost ignored', 'L2': 'Pilots funded ad-hoc, no business case', 'L3': 'Funding gated by business case for priority work', 'L4': 'Funding intent + run-cost/unit economics modelled, incl. error-recovery cost', 'L5': 'Capital allocated dynamically by proven return; full TCO (build+run+recovery) feeds go/no-go'}; probing_questions=[{'q': 'How are AI initiatives funded (innovation pot, BU budgets, central)?', 'looking_for': 'Reveals whether funding is intentional and sustainable. Strong: a clear, fit-for-purpose model. Weak: ad-hoc scraps → pilots starve.'}, {'q': 'Is a business case required to fund — and to continue funding?', 'looking_for': 'Tests funding discipline and stage-gating. Strong: business case to start and to continue. Weak: fund-and-forget → zombie projects.'}, {'q': 'Do you model run-cost / unit (inference) economics before scaling?', 'looking_for': 'Probes scale-economics awareness (margin risk). Strong: unit economics modeled pre-scale. Weak: unaware → cost blowouts at scale.'}, {'q': 'Who owns the inference / token bill?', 'looking_for': 'Reveals cost accountability. Strong: a clear owner watching spend. Weak: nobody → runaway cost.'}, {'q': 'Does the TCO include the cost of ERROR RECOVERY — the expected cost of detecting, correcting, and reversing agent mistakes (rework, remediation, downstream impact), not just inference and build?', 'looking_for': '2026 honesty check, ties to Dim 6.2 reversibility. Strong: recovery cost is modeled in TCO and feeds the go/no-go gate. Weak: only build+inference counted → TCO understated, autonomy looks cheaper than it is.'}].

**Connected to:** cross_references → 6.2 Error Reversibility & Recovery-Cost Assessment; Dimension 1: Strategy, Leadership & Value Realization → has_criterion; 6.2 Error Reversibility & Recovery-Cost Assessment → cross_references.

**Sourced from:** dimensions.json.
