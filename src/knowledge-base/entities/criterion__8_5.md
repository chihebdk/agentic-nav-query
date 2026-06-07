---
id: criterion.8_5
type: Criterion
label: "8.5 Risk Triage & Right-to-Deploy"
aliases: ["8.5", "Risk Triage & Right-to-Deploy"]
tags: ["criterion", "dim-8"]
sources: ["dimensions.json"]
---

# 8.5 Risk Triage & Right-to-Deploy

**Type:** Criterion  ·  **ID:** `criterion.8_5`

**Also known as:** 8.5, Risk Triage & Right-to-Deploy

Risk triaging is continuous, not one-off; you must earn the right to deploy.

## Attributes

- **dimension:** 8
- **criterion_id:** 8.5
- **anchors:** {'L1': 'No risk triage; agents ship ungated', 'L2': 'Ad-hoc/one-time risk review', 'L3': 'Standard triage rubric; right-to-deploy gate for priority agents', 'L4': 'Continuous triage + risk-tiered controls; reversibility/recovery-cost included', 'L5': 'Continuous, fleet-wide triage; deploy earned and re-gated on signals'}
- **probing_questions:** [{'q': 'Does the team triage agent risks on a standard rubric (severity, probability, detectability, business value), continuously — not once?', 'looking_for': 'Tests risk discipline. Strong: continuous triage on a rubric. Weak: ad-hoc/one-time or none.'}, {'q': 'Is there a digital-trust / right-to-deploy gate before scaling, with risk-tiered controls (sandbox -> team -> enterprise)?', 'looking_for': 'Tests the deploy gate. Strong: a trust gate + risk tiers. Weak: agents ship ungated.'}, {'q': 'Does triage incorporate error reversibility/recovery cost (Dim 6.2 / 4.4)?', 'looking_for': 'Tests integration with reversibility. Strong: reversibility/recovery cost in triage. Weak: ignored → irreversible high-cost agents shipped.'}, {'q': 'Are high-risk agents pulled back or re-gated when risk signals change?', 'looking_for': 'Tests reversibility of deploy. Strong: re-gated/pulled back on signals. Weak: one-way deploy.'}]

## Relationships (outgoing)

- cross_references → [6.2 Error Reversibility & Recovery-Cost Assessment](./criterion__6_2.md)

## Relationships (incoming)

- [Dimension 8: Security & Risk](./dim__8.md) → has_criterion

## Sources

- dimensions.json
