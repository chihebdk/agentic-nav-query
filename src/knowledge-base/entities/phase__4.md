---
id: phase.4
type: EngagementPhase
label: "Phase 4: Synthesize the As-Is"
aliases: ["Phase 4", "Synthesize the As-Is"]
tags: ["engagement-phase", "phase-4"]
sources: ["engagement-workflow.md"]
---

# Phase 4: Synthesize the As-Is

**Type:** EngagementPhase  ·  **ID:** `phase.4`

**Also known as:** Phase 4, Synthesize the As-Is

Finalize current scores per criterion/dimension; build the radar and Strategy×Execution 2×2; distill findings (answer-first, MECE) and patterns; identify the binding constraint.

## Attributes

- **number:** 4
- **artifact:** As-is findings (storyline + scores + visuals).
- **exit_check:** A defensible current-state the sponsor recognizes.
- **templates_used:** ['template.as_is_findings']

## Relationships (outgoing)

- depends_on → [Phase 3: Capture & Analyze](./phase__3.md)
- produces_artifact → [As-Is Findings](./template__as_is_findings.md)
- precedes → [Phase 5: Gap & Target](./phase__5.md)

## Relationships (incoming)

- [Phase 3: Capture & Analyze](./phase__3.md) → precedes
- [Phase 5: Gap & Target](./phase__5.md) → depends_on
- [McKinsey Method](./method__mckinsey_method.md) → applies_to_phase
- [Analysis Method](./method__analysis_method.md) → applies_to_phase
- [Diagram Toolkit](./method__diagram_toolkit.md) → applies_to_phase

## Sources

- engagement-workflow.md
