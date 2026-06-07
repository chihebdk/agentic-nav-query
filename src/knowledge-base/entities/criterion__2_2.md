---
id: criterion.2_2
type: Criterion
label: "2.2 Skill / Capability Packaging (Assetization)"
aliases: ["2.2", "Skill / Capability Packaging (Assetization)"]
tags: ["criterion", "dim-2"]
sources: ["dimensions.json"]
---

# 2.2 Skill / Capability Packaging (Assetization)

**Type:** Criterion  ·  **ID:** `criterion.2_2`

**Also known as:** 2.2, Skill / Capability Packaging (Assetization)

Build once, reuse anywhere (any function); else the 2nd time you do similar work costs as much as the 1st.

## Attributes

- **dimension:** 2
- **criterion_id:** 2.2
- **anchors:** {'L1': 'Repeatable work redone ad-hoc each time', 'L2': 'Copy-paste reuse; no standard', 'L3': 'Skills packaged as versioned modular assets with a spec', 'L4': 'Composable library; new work assembled largely from existing skills', 'L5': 'Assetization is the default; cross-harness, cross-function portable skills'}
- **probing_questions:** [{'q': 'Are repeatable workflows (any function) captured as versioned, executable skills — or ad-hoc prompts/docs/tribal knowledge?', 'looking_for': 'Tests assetization across the org. Strong: versioned, executable skills. Weak: scattered prompts/tribal practice → no leverage.'}, {'q': 'Are capabilities built as modular, reusable components?', 'looking_for': 'Probes composability. Strong: modular building blocks that recombine. Weak: monolithic one-offs.'}, {'q': 'When you do similar work a second time (another QBR, vendor review, postmortem, service, or agent), how much is an existing reusable skill vs. redone by hand?', 'looking_for': 'The reuse-vs-rebuild test; reveals whether cost compounds or stays linear. Strong: most is reused, only the genuinely new part is built. Weak: rebuilt each time → no compounding, work costs full price every time.'}, {'q': "Is there a standard format/spec for a 'skill' that any function can publish to?", 'looking_for': 'Tests for a common contract enabling org-wide reuse. Strong: a shared spec/format. Weak: none → incompatible, un-shareable assets.'}]

## Relationships (incoming)

- [Dimension 2: Knowledge Building & Capability Reuse](./dim__2.md) → has_criterion
- [Knowledge Moat](./concept__knowledge_moat.md) → references_criterion
- [Skill](./concept__skill.md) → references_criterion
- [Skills-as-Documentation](./concept__skills_as_documentation.md) → references_criterion
- [Skill Spec](./template__skill_spec.md) → references_criterion

## Sources

- dimensions.json
