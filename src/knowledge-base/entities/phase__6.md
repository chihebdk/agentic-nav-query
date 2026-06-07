---
id: phase.6
type: EngagementPhase
label: "Phase 6: Roadmap & Client Backlog"
aliases: ["Phase 6", "Roadmap & Client Backlog"]
tags: ["engagement-phase", "phase-6"]
sources: ["engagement-workflow.md"]
---

# Phase 6: Roadmap & Client Backlog

**Type:** EngagementPhase  ·  **ID:** `phase.6`

**Also known as:** Phase 6, Roadmap & Client Backlog

Pull matching template stories; apply brownfield constraints (legacy, contracts, org/skills, risk, regulation, budget); sequence into compressed, parallel, risk-tiered waves.

## Attributes

- **number:** 6
- **artifact:** Client backlog + roadmap.
- **exit_check:** An executable, constrained plan.
- **templates_used:** ['template.backlog_story', 'template.roadmap_waves']

## Relationships (outgoing)

- depends_on → [Phase 5: Gap & Target](./phase__5.md)
- produces_artifact → [Backlog Story](./template__backlog_story.md)
- produces_artifact → [Roadmap Waves](./template__roadmap_waves.md)
- precedes → [Phase 7: Drive the First Waves](./phase__7.md)

## Relationships (incoming)

- [Phase 5: Gap & Target](./phase__5.md) → precedes
- [Phase 7: Drive the First Waves](./phase__7.md) → depends_on

## Sources

- engagement-workflow.md
