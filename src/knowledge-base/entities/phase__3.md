---
id: phase.3
type: EngagementPhase
label: "Phase 3: Capture & Analyze"
aliases: ["Phase 3", "Capture & Analyze"]
tags: ["engagement-phase", "phase-3"]
sources: ["engagement-workflow.md"]
---

# Phase 3: Capture & Analyze

**Type:** EngagementPhase  ·  **ID:** `phase.3`

**Also known as:** Phase 3, Capture & Analyze

Log each interview; map each response to the criteria it informs; score 1-5 with rationale and confidence flag; note gaps and contradictions; generate targeted follow-ups.

## Attributes

- **number:** 3
- **artifact:** Interview logs + running scoresheet.
- **exit_check:** Coverage check passes: each priority criterion has ≥1 corroborated data point; contradictions resolved.
- **templates_used:** ['template.interview_log']

## Relationships (outgoing)

- depends_on → [Phase 2: Frame Interviews](./phase__2.md)
- produces_artifact → [Interview Log](./template__interview_log.md)
- precedes → [Phase 4: Synthesize the As-Is](./phase__4.md)

## Relationships (incoming)

- [Phase 2: Frame Interviews](./phase__2.md) → precedes
- [Phase 4: Synthesize the As-Is](./phase__4.md) → depends_on
- [Interview Method](./method__interview_method.md) → applies_to_phase
- [Analysis Method](./method__analysis_method.md) → applies_to_phase

## Sources

- engagement-workflow.md
