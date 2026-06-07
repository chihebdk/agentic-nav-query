---
id: criterion.5_7
type: Criterion
label: "5.7 Interoperability, Integration & Build-vs-Buy / Topology"
aliases: ["5.7", "Interoperability, Integration & Build-vs-Buy / Topology"]
tags: ["criterion", "dim-5"]
keywords: ["build-vs-buy", "criterion", "dim-5", "integration", "interoperability", "topology"]
status: current
sources: ["dimensions.json"]
entity_page: ../../knowledge-base/entities/criterion__5_7.md
---

# 5.7 Interoperability, Integration & Build-vs-Buy / Topology  ·  _Criterion_

Standardized integration and deliberate build/buy prevent fragmentation and accidental multi-platform sprawl.

**Key facts:** dimension=5; criterion_id=5.7; anchors={'L1': 'Bespoke integration per agent; accidental platforms', 'L2': 'Some shared connectors', 'L3': 'Standardized integration patterns; build/buy considered', 'L4': 'Deliberate build/buy rule; intentional deployment topology', 'L5': 'Consistent, reusable integration across the estate; intentional, optimized topology'}; probing_questions=[{'q': 'Does the platform provide standardized patterns for integrating with enterprise systems (events, APIs, message bus), or does each team wire its own?', 'looking_for': 'Tests reusable enterprise integration. Strong: standardized, reusable patterns. Weak: bespoke per agent.'}, {'q': 'How do you decide build vs buy for platform primitives (harness, gateways, registry, orchestration, eval tooling)?', 'looking_for': 'Tests sourcing discipline. Strong: a deliberate build/buy rule. Weak: accidental/duplicated builds.'}, {'q': 'What is your deployment topology — managed harness, cloud agent platform, home-built, or a mix — and is the mix intentional?', 'looking_for': 'Tests topology intent. Strong: an intentional topology with rationale. Weak: accidental multi-platform sprawl.'}, {'q': 'Are integration and platform patterns consistent across deployment types and teams?', 'looking_for': 'Tests consistency. Strong: consistent across the estate. Weak: fragmented → rework, brittle integration.'}].

**Connected to:** Dimension 5: Agentic Platform & Control Plane (Operating Model) → has_criterion; Production Readiness → references_criterion.

**Sourced from:** dimensions.json.
