---
id: criterion.2_6
type: Criterion
label: "2.6 Measurement of Reuse & Value"
aliases: ["2.6", "Measurement of Reuse & Value"]
tags: ["criterion", "dim-2"]
sources: ["dimensions.json"]
---

# 2.6 Measurement of Reuse & Value

**Type:** Criterion  ·  **ID:** `criterion.2_6`

**Also known as:** 2.6, Measurement of Reuse & Value

What gets measured gets funded; unmeasured reuse stays incidental.

## Attributes

- **dimension:** 2
- **criterion_id:** 2.6
- **anchors:** {'L1': 'No measurement', 'L2': 'Anecdotal reuse stories', 'L3': 'Reuse rate tracked for core assets', 'L4': 'Time-to-build reduction + reuse ROI tracked, steers investment', 'L5': 'Reuse/ROI a leadership-visible metric guiding the portfolio'}
- **probing_questions:** [{'q': 'Do you measure how often core skills/components are reused?', 'looking_for': 'Tests whether reuse is tracked at all. Strong: reuse rate measured. Weak: unmeasured → reuse stays incidental.'}, {'q': 'Can you show time-to-build reduction from reuse?', 'looking_for': "Probes tangible leverage evidence. Strong: demonstrated build-time reduction. Weak: no data → can't prove value."}, {'q': 'Is reuse ROI tracked and used to steer investment?', 'looking_for': 'Tests whether measurement drives decisions. Strong: ROI steers investment. Weak: not tracked → no funding case for the platform/CoE.'}, {'q': 'What share of new work/agents is assembled mostly from existing skills?', 'looking_for': 'A maturity proxy for compounding. Strong: a high share assembled from existing skills. Weak: mostly built fresh.'}]

## Relationships (incoming)

- [Dimension 2: Knowledge Building & Capability Reuse](./dim__2.md) → has_criterion
- [Skill](./concept__skill.md) → references_criterion

## Sources

- dimensions.json
