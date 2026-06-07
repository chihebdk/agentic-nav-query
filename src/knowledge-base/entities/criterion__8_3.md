---
id: criterion.8_3
type: Criterion
label: "8.3 Runtime Threat Protection & Guardrails (security)"
aliases: ["8.3", "Runtime Threat Protection & Guardrails (security)"]
tags: ["criterion", "dim-8"]
sources: ["dimensions.json"]
---

# 8.3 Runtime Threat Protection & Guardrails (security)

**Type:** Criterion  ·  **ID:** `criterion.8_3`

**Also known as:** 8.3, Runtime Threat Protection & Guardrails (security)

Prompt-layer guardrails fail under attack; enforce what the agent CANNOT reach; secure the tool/supply-chain layer.

## Attributes

- **dimension:** 8
- **criterion_id:** 8.3
- **anchors:** {'L1': 'Prompt-only or no guardrails; open egress', 'L2': 'Basic input/output filtering', 'L3': 'Runtime guardrails + tool allow-listing for priority agents', 'L4': 'Enclave/least-privilege enforcement; MCP-gateway + vetted supply chain; sandboxing/secrets standard', 'L5': 'Defense-in-depth runtime protection; security & governance guardrails both engineered in'}
- **probing_questions:** [{'q': 'Are security guardrails enforced at runtime INCLUDING enforcement of what the agent CANNOT REACH (enclave/least-privilege at the connector level), not just prompt-layer instructions?', 'looking_for': 'Tests real enforcement. Strong: enclave/least-privilege enforcement. Weak: prompt-only guardrails → talked out of them under attack.'}, {'q': 'Is tool/MCP traffic secured (allow-listing, egress control, MCP-gateway), and are third-party skills/tools vetted (supply chain)?', 'looking_for': 'Tests tool-layer security. Strong: governed tool/MCP traffic + vetted supply chain. Weak: open egress; unvetted skills.'}, {'q': 'Are sandboxing and secrets handling standard for agent execution?', 'looking_for': 'Tests execution security. Strong: sandboxed; secrets managed. Weak: agents run with exposed secrets/no isolation.'}, {'q': 'Are security guardrails distinguished from governance guardrails, with BOTH implemented?', 'looking_for': 'Tests the layered model. Strong: separate security + governance guardrails. Weak: conflated or only one.'}]

## Relationships (incoming)

- [Dimension 8: Security & Risk](./dim__8.md) → has_criterion
- [Tool Design & Permissioning](./craft__tool_design_permissioning.md) → supports_craft
- [Evals & Guardrails](./craft__evals_guardrails.md) → references_criterion
- [Retrieval Craft](./craft__retrieval_craft.md) → references_criterion
- [Agentic Threat Model](./template__agentic_threat_model.md) → references_criterion
- [Guardrail Stack](./template__guardrail_stack.md) → references_criterion

## Sources

- dimensions.json
