---
id: criterion.8_2
type: Criterion
label: "8.2 Agent Identity & Least-Privilege Access"
aliases: ["8.2", "Agent Identity & Least-Privilege Access"]
tags: ["criterion", "dim-8"]
sources: ["dimensions.json"]
---

# 8.2 Agent Identity & Least-Privilege Access

**Type:** Criterion  ·  **ID:** `criterion.8_2`

**Also known as:** 8.2, Agent Identity & Least-Privilege Access

Without identity & least-privilege, agents are 'anonymous employees'; sub-tasks inherit/escalate permissions.

## Attributes

- **dimension:** 8
- **criterion_id:** 8.2
- **anchors:** {'L1': 'Shared/blanket credentials', 'L2': 'Some per-agent identity, ad-hoc', 'L3': 'Per-agent least-privilege identity for priority agents', 'L4': 'Zero-trust for AI workloads; JIT; sub-agent permissions controlled; identity inventory', 'L5': 'Full zero-trust agent identity, platform-governed, provable and least-privilege by default'}
- **probing_questions:** [{'q': 'Does every agent have a distinct identity with least-privilege and on-behalf-of/context-aware access, as a standard — not blanket service accounts?', 'looking_for': "Tests the identity primitive's security. Strong: per-agent least-privilege identity. Weak: shared/blanket credentials → 'anonymous employees'."}, {'q': 'Have you inventoried all agent/machine identities, with lifecycle and credential controls?', 'looking_for': 'Tests identity governance. Strong: a maintained identity inventory + lifecycle. Weak: unknown machine identities.'}, {'q': 'Is zero-trust extended to AI workloads with just-in-time access, and are inherited/sub-agent permissions controlled?', 'looking_for': 'Tests zero-trust for agents. Strong: JIT + sub-agent permission control. Weak: standing broad access; sub-tasks inherit/escalate.'}, {'q': 'Is agent identity governed consistently via the platform/control plane (Dim 5.5)?', 'looking_for': 'Tests consistency. Strong: platform-governed identity. Weak: per-team ad-hoc.'}]

## Relationships (outgoing)

- cross_references → [5.5 Control-Plane Primitives: Registry, Identity, Gateways & Observability](./criterion__5_5.md)

## Relationships (incoming)

- [Dimension 8: Security & Risk](./dim__8.md) → has_criterion

## Sources

- dimensions.json
