---
id: criterion.5_1
type: Criterion
label: "5.1 Platform Ownership & Platform-as-Product"
aliases: ["5.1", "Platform Ownership & Platform-as-Product"]
tags: ["criterion", "dim-5"]
sources: ["dimensions.json"]
---

# 5.1 Platform Ownership & Platform-as-Product

**Type:** Criterion  ·  **ID:** `criterion.5_1`

**Also known as:** 5.1, Platform Ownership & Platform-as-Product

An unowned, project-run platform decays; product management sustains adoption. (Score outcome, not org chart.)

## Attributes

- **dimension:** 5
- **criterion_id:** 5.1
- **anchors:** {'L1': 'No clear owner; conflated with data/AI', 'L2': 'Owner emerging; run as a side project', 'L3': 'Clear agentic-platform ownership; basic roadmap/support', 'L4': 'Run as a product: roadmap, SLAs, users, funded', 'L5': 'Funded product driving adoption; primitives fully owned'}
- **probing_questions:** [{'q': 'Who owns the agentic platform today, and is it distinct from your data/AI platforms?', 'looking_for': 'Tests clear ownership of an AGENTIC platform. Strong: a clear owner, distinct from (but aligned to) data/AI platforms. Weak: no owner, or conflated with a generic AI/data platform.'}, {'q': 'Is the platform run as a product (roadmap, SLAs, named internal users, support), or as a side project?', 'looking_for': "Tests platform-as-product maturity. Strong: product-managed with users and support. Weak: ad-hoc/project. (Score on a spectrum; early-stage orgs legitimately aren't here yet.)"}, {'q': 'Does the owning team understand and own the platform primitives (harness, runtime, registry, gateways, tools)?', 'looking_for': 'Tests depth of ownership. Strong: primitives clearly owned and understood. Weak: primitives scattered/unowned.'}, {'q': 'How is platform investment funded and prioritized against demand?', 'looking_for': 'Tests sustainability. Strong: funded, demand-driven roadmap. Weak: unfunded/reactive → platform decays.'}]

## Relationships (incoming)

- [Dimension 5: Agentic Platform & Control Plane (Operating Model)](./dim__5.md) → has_criterion

## Sources

- dimensions.json
