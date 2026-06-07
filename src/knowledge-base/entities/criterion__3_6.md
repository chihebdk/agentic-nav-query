---
id: criterion.3_6
type: Criterion
label: "3.6 Data Governance, Privacy & Rights for AI/Agent Use"
aliases: ["3.6", "Data Governance, Privacy & Rights for AI/Agent Use"]
tags: ["criterion", "dim-3"]
sources: ["dimensions.json"]
---

# 3.6 Data Governance, Privacy & Rights for AI/Agent Use

**Type:** Criterion  ·  **ID:** `criterion.3_6`

**Also known as:** 3.6, Data Governance, Privacy & Rights for AI/Agent Use

Governance hasn't scaled with data distribution; unstructured data is especially exposed.

## Attributes

- **dimension:** 3
- **criterion_id:** 3.6
- **anchors:** {'L1': 'No AI-specific data governance', 'L2': 'Basic classification; gaps in unstructured', 'L3': 'Classification + access control for priority AI data', 'L4': 'Consent/rights enforced; access traceable; unstructured covered', 'L5': "Governance scaled to AI's reach; continuous, automated, auditable"}
- **probing_questions:** [{'q': 'Is data classified and access-controlled for AI use cases (including unstructured)?', 'looking_for': 'Tests AI-specific data governance. Strong: classification + access control incl. unstructured. Weak: ungoverned → over-retrieval, leaks.'}, {'q': 'Do you enforce consent/usage rights on data fed to agents?', 'looking_for': 'Probes rights/consent. Strong: rights enforced on agent inputs. Weak: none → privacy/regulatory breach.'}, {'q': 'Can you trace what data an agent accessed and why?', 'looking_for': 'Tests data-access traceability. Strong: traceable access. Weak: invisible access → undetectable breaches.'}, {'q': "Has governance scaled to match AI's reach into your data?", 'looking_for': 'Tests whether governance kept pace with AI adoption. Strong: governance scaled with AI. Weak: governance lagging → growing exposure.'}]

## Relationships (incoming)

- [Dimension 3: Data, Knowledge Sources & Retrieval](./dim__3.md) → has_criterion
- [8.7 AI Hygiene & Shadow-AI / Human-Trust Risk](./criterion__8_7.md) → cross_references

## Sources

- dimensions.json
