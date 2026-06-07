---
id: criterion.9_5
type: Criterion
label: "9.5 Compliance & Regulatory Lifecycle"
aliases: ["9.5", "Compliance & Regulatory Lifecycle"]
tags: ["criterion", "dim-9"]
sources: ["dimensions.json"]
---

# 9.5 Compliance & Regulatory Lifecycle

**Type:** Criterion  ·  **ID:** `criterion.9_5`

**Also known as:** 9.5, Compliance & Regulatory Lifecycle

Penalties are material (to 7% of turnover); compliance is continuous; agent governance spans five frameworks.

## Attributes

- **dimension:** 9
- **criterion_id:** 9.5
- **anchors:** {'L1': 'No regulatory mapping', 'L2': 'Aware of some obligations', 'L3': 'Use cases mapped + risk-classified; documentation for priority high-risk systems', 'L4': 'Conformity-ready; continuous compliance monitoring; mandatory human oversight where required', 'L5': 'Continuous, audit-ready, framework-aligned compliance by design'}
- **probing_questions:** [{'q': 'Do you map agent use cases to applicable frameworks (EU AI Act, NIST AI RMF, ISO/IEC 42001, GDPR, SOC 2, sector rules) and risk-classify them?', 'looking_for': 'Tests regulatory mapping. Strong: mapped + risk-classified. Weak: no view of applicable rules.'}, {'q': 'Is there technical documentation / conformity readiness for high-risk systems (EU AI Act full high-risk enforcement Aug 2026)?', 'looking_for': 'Tests conformity readiness. Strong: documentation/conformity ready. Weak: unprepared for high-risk obligations.'}, {'q': 'Is compliance monitored continuously (not one-time), with audit readiness?', 'looking_for': 'Tests continuous compliance. Strong: continuous + audit-ready. Weak: one-time/never.'}, {'q': 'Is mandatory human oversight implemented where regulation requires it?', 'looking_for': 'Tests required oversight. Strong: human oversight where mandated. Weak: missing → non-compliant.'}]

## Relationships (incoming)

- [Dimension 9: Governance & Responsible AI](./dim__9.md) → has_criterion

## Sources

- dimensions.json
