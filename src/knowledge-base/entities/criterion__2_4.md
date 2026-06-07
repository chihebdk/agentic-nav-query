---
id: criterion.2_4
type: Criterion
label: "2.4 Reuse Governance, Quality & Security"
aliases: ["2.4", "Reuse Governance, Quality & Security"]
tags: ["criterion", "dim-2"]
sources: ["dimensions.json"]
---

# 2.4 Reuse Governance, Quality & Security

**Type:** Criterion  ·  **ID:** `criterion.2_4`

**Also known as:** 2.4, Reuse Governance, Quality & Security

Skills are the new packages: reuse without governance scales risk as fast as value.

## Attributes

- **dimension:** 2
- **criterion_id:** 2.4
- **anchors:** {'L1': 'No governance; anything runs', 'L2': 'Basic review by authors', 'L3': 'Ownership, versioning, certification for priority skills', 'L4': 'CoE standards; third-party skills security-vetted; deprecation process', 'L5': 'Automated quality/security gates; trusted supply chain; continuous assurance'}
- **probing_questions:** [{'q': 'Who certifies a skill as safe and fit for reuse?', 'looking_for': 'Tests the trust/quality gate that makes reuse safe. Strong: a clear certification owner/process. Weak: anything runs → no trust, reuse stalls.'}, {'q': 'Is there versioning, ownership, and a deprecation process?', 'looking_for': 'Tests lifecycle hygiene. Strong: owned, versioned, deprecated cleanly. Weak: stale/duplicated skills accumulate.'}, {'q': 'How do you vet external/third-party skills for security?', 'looking_for': 'Skills are packages → supply-chain risk (280k+ public skills, documented malicious ones). Strong: security vetting of third-party skills. Weak: unvetted → unsafe skills in production.'}, {'q': 'Are reusability and quality standards defined (e.g., by a CoE)?', 'looking_for': 'Tests whether standards exist to keep reuse safe and consistent. Strong: CoE standards. Weak: none → inconsistent quality.'}]

## Relationships (incoming)

- [Dimension 2: Knowledge Building & Capability Reuse](./dim__2.md) → has_criterion
- [Skill](./concept__skill.md) → references_criterion
- [Skill Spec](./template__skill_spec.md) → references_criterion

## Sources

- dimensions.json
