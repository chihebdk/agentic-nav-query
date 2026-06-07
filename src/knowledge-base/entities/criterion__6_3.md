---
id: criterion.6_3
type: Criterion
label: "6.3 Deterministic <-> Agentic Composition"
aliases: ["6.3", "Deterministic <-> Agentic Composition"]
tags: ["criterion", "dim-6"]
sources: ["dimensions.json"]
---

# 6.3 Deterministic <-> Agentic Composition

**Type:** Criterion  ·  **ID:** `criterion.6_3`

**Also known as:** 6.3, Deterministic <-> Agentic Composition

Composition keeps the agentic workflow evaluable and auditable; over-agentifying or blind automation both fail.

## Attributes

- **dimension:** 6
- **criterion_id:** 6.3
- **anchors:** {'L1': 'Monolithic agent swallows deterministic steps', 'L2': 'Some separation, ad-hoc', 'L3': 'Agent scoped to judgment; deterministic shell around it', 'L4': 'Anti-patterns avoided (no re-agentifying BPA; augmentation-first where right)', 'L5': 'Clean deterministic<->agentic composition; workflow orchestrates, agent judges'}
- **probing_questions:** [{'q': 'As a standard, how does the team compose deterministic steps (sequencing/validation/routing) with the agentic judgment step — a shared pattern, or does each build differ?', 'looking_for': 'Tests for a reusable composition pattern. Strong: a shared, reused pattern. Weak: every build improvises the boundary.'}, {'q': 'How consistently does the team recognize and avoid over-agentifying work already handled by deterministic automation — is there an explicit reliability-vs-intelligence check?', 'looking_for': 'Tests maturity against anti-pattern 1. Strong: an explicit check; deterministic work stays deterministic. Weak: routinely re-agentifies working BPA/RPA.'}, {'q': "For work that doesn't need agent intelligence, is 'augment people first, earn trust through use' an established team practice, or is blind automation the default?", 'looking_for': 'Tests maturity against anti-pattern 2. Strong: augmentation-first is the norm. Weak: defaults to blind automation.'}, {'q': "How clearly and consistently does the team separate orchestration (workflow/durable execution) from the agent's judgment role across its builds?", 'looking_for': 'Tests architectural maturity. Strong: consistent separation. Weak: agents routinely try to run the whole flow.'}]

## Relationships (incoming)

- [Dimension 6: Agentic Workflow Redesign & Human-AI Pairing](./dim__6.md) → has_criterion
- [Pairing Mode Playbook](./template__pairing_mode_playbook.md) → references_criterion

## Sources

- dimensions.json
