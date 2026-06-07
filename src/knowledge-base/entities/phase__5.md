---
id: phase.5
type: EngagementPhase
label: "Phase 5: Gap & Target"
aliases: ["Phase 5", "Gap & Target"]
tags: ["engagement-phase", "phase-5"]
sources: ["engagement-workflow.md"]
---

# Phase 5: Gap & Target

**Type:** EngagementPhase  ·  **ID:** `phase.5`

**Also known as:** Phase 5, Gap & Target

Set the right target per criterion (not all 5; floors on trust dims); compute gaps; prioritize (value × feasibility + must-dos + dependencies); plot the 2×2.

## Attributes

- **number:** 5
- **artifact:** Gap analysis + prioritized gap list.
- **exit_check:** Targets and priorities agreed.
- **templates_used:** ['template.gap_analysis']

## Relationships (outgoing)

- depends_on → [Phase 4: Synthesize the As-Is](./phase__4.md)
- produces_artifact → [Gap Analysis](./template__gap_analysis.md)
- precedes → [Phase 6: Roadmap & Client Backlog](./phase__6.md)

## Relationships (incoming)

- [Phase 4: Synthesize the As-Is](./phase__4.md) → precedes
- [Phase 6: Roadmap & Client Backlog](./phase__6.md) → depends_on
- [Diagram Toolkit](./method__diagram_toolkit.md) → applies_to_phase

## Sources

- engagement-workflow.md
