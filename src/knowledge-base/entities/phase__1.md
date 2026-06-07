---
id: phase.1
type: EngagementPhase
label: "Phase 1: Scope & Plan"
aliases: ["Phase 1", "Scope & Plan"]
tags: ["engagement-phase", "phase-1"]
sources: ["engagement-workflow.md"]
---

# Phase 1: Scope & Plan

**Type:** EngagementPhase  ·  **ID:** `phase.1`

**Also known as:** Phase 1, Scope & Plan

Clarify objectives and the business question (SCQA); map stakeholders to the nine dimensions; set initial hypotheses; draft a workplan with timeboxes; define success criteria.

## Attributes

- **number:** 1
- **artifact:** Engagement plan + stakeholder map.
- **exit_check:** Sponsor + scope agreed; interview list drawn.
- **templates_used:** ['template.engagement_plan', 'template.stakeholder_map']

## Relationships (outgoing)

- produces_artifact → [Engagement Plan](./template__engagement_plan.md)
- produces_artifact → [Stakeholder Map](./template__stakeholder_map.md)
- precedes → [Phase 2: Frame Interviews](./phase__2.md)

## Relationships (incoming)

- [Phase 2: Frame Interviews](./phase__2.md) → depends_on
- [State Management](./method__state_management.md) → applies_to_phase

## Sources

- engagement-workflow.md
