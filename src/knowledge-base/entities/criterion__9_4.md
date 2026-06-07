---
id: criterion.9_4
type: Criterion
label: "9.4 Explainability, Transparency & Auditability"
aliases: ["9.4", "Explainability, Transparency & Auditability"]
tags: ["criterion", "dim-9"]
sources: ["dimensions.json"]
---

# 9.4 Explainability, Transparency & Auditability

**Type:** Criterion  ·  **ID:** `criterion.9_4`

**Also known as:** 9.4, Explainability, Transparency & Auditability

Governance without evidence is not governance; transparency and oversight are convergent regulatory requirements.

## Attributes

- **dimension:** 9
- **criterion_id:** 9.4
- **anchors:** {'L1': 'Black-box; no audit trail', 'L2': 'Basic logging; limited explainability', 'L3': 'Immutable audit trails + disclosure for priority agents', 'L4': 'Decisions reconstructable/defensible; transparency standard (e.g., Agent Identity Cards)', 'L5': 'Provable, audit-ready, transparent by design across the fleet'}
- **probing_questions:** [{'q': "Can agent decisions be explained, and is agent use transparently disclosed (e.g., users know they're dealing with an agent; Agent Identity Cards)?", 'looking_for': 'Tests explainability + transparency. Strong: explainable + disclosed. Weak: black-box, undisclosed.'}, {'q': 'Are there immutable audit trails of decisions, context evaluated, rules applied, and human reviews?', 'looking_for': "Tests evidence. Strong: immutable, complete audit trails. Weak: 'governance without evidence'."}, {'q': 'Can you reconstruct and defend a decision to a regulator or customer?', 'looking_for': "Tests defensibility. Strong: decisions reconstructable/defensible. Weak: can't explain what happened."}, {'q': 'Is explainability/transparency a standard requirement, or case-by-case?', 'looking_for': 'Tests standardization. Strong: standard requirement. Weak: ad-hoc.'}]

## Relationships (incoming)

- [Dimension 9: Governance & Responsible AI](./dim__9.md) → has_criterion

## Sources

- dimensions.json
