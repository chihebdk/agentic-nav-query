---
id: criterion.9_6
type: Criterion
label: "9.6 Agent Registry, Intake & Lifecycle Governance"
aliases: ["9.6", "Agent Registry, Intake & Lifecycle Governance"]
tags: ["criterion", "dim-9"]
keywords: ["agent", "criterion", "dim-9", "governance", "intake", "lifecycle", "registry"]
status: current
sources: ["dimensions.json"]
entity_page: ../../knowledge-base/entities/criterion__9_6.md
---

# 9.6 Agent Registry, Intake & Lifecycle Governance  ·  _Criterion_

Lifecycle governance and a complete registry make governance real and measurable; this is the policy/coverage over Dim 5.3/5.5.

**Key facts:** dimension=9; criterion_id=9.6; anchors={'L1': 'Shadow agents; no intake/registry', 'L2': 'Partial inventory; ad-hoc intake', 'L3': 'Structured intake + registry for priority agents; risk-classified', 'L4': 'Full lifecycle governed (approve->deploy->monitor->retire); governance metrics tracked', 'L5': '100% intake/registry/doc coverage; registry is the single source of truth'}; probing_questions=[{'q': 'Does every agent pass a structured intake and get registered with metadata (owner, purpose, risk class, RAI/privacy/security docs)?', 'looking_for': 'Tests intake+registry governance. Strong: structured intake + complete metadata. Weak: agents ship unregistered.'}, {'q': 'Is the full lifecycle governed (approve -> deploy -> monitor -> retire/decommission)?', 'looking_for': 'Tests lifecycle governance. Strong: governed end-to-end incl. retirement. Weak: deploy-and-forget; nothing retired.'}, {'q': 'Do you track governance metrics (structured-intake coverage, registry adoption, RAI/compliance doc coverage — target 100%)?', 'looking_for': 'Tests measurability. Strong: governance metrics tracked toward 100%. Weak: unmeasured coverage.'}, {'q': 'Is the registry the single source of truth, with no shadow/ungoverned agents? (cross-ref Dim 5.5/8)', 'looking_for': 'Tests completeness. Strong: complete registry, no shadow agents. Weak: shadow/ungoverned agents exist.'}].

**Connected to:** cross_references → 5.3 Governed Use-Case & PoC Intake; cross_references → 5.5 Control-Plane Primitives: Registry, Identity, Gateways & Observability; Dimension 9: Governance & Responsible AI → has_criterion.

**Sourced from:** dimensions.json.
