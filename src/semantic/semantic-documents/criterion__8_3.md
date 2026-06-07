---
id: criterion.8_3
type: Criterion
label: "8.3 Runtime Threat Protection & Guardrails (security)"
aliases: ["8.3", "Runtime Threat Protection & Guardrails (security)"]
tags: ["criterion", "dim-8"]
keywords: ["criterion", "dim-8", "guardrails", "protection", "runtime", "security", "threat"]
status: current
sources: ["dimensions.json"]
entity_page: ../../knowledge-base/entities/criterion__8_3.md
---

# 8.3 Runtime Threat Protection & Guardrails (security)  ·  _Criterion_

Prompt-layer guardrails fail under attack; enforce what the agent CANNOT reach; secure the tool/supply-chain layer.

**Key facts:** dimension=8; criterion_id=8.3; anchors={'L1': 'Prompt-only or no guardrails; open egress', 'L2': 'Basic input/output filtering', 'L3': 'Runtime guardrails + tool allow-listing for priority agents', 'L4': 'Enclave/least-privilege enforcement; MCP-gateway + vetted supply chain; sandboxing/secrets standard', 'L5': 'Defense-in-depth runtime protection; security & governance guardrails both engineered in'}; probing_questions=[{'q': 'Are security guardrails enforced at runtime INCLUDING enforcement of what the agent CANNOT REACH (enclave/least-privilege at the connector level), not just prompt-layer instructions?', 'looking_for': 'Tests real enforcement. Strong: enclave/least-privilege enforcement. Weak: prompt-only guardrails → talked out of them under attack.'}, {'q': 'Is tool/MCP traffic secured (allow-listing, egress control, MCP-gateway), and are third-party skills/tools vetted (supply chain)?', 'looking_for': 'Tests tool-layer security. Strong: governed tool/MCP traffic + vetted supply chain. Weak: open egress; unvetted skills.'}, {'q': 'Are sandboxing and secrets handling standard for agent execution?', 'looking_for': 'Tests execution security. Strong: sandboxed; secrets managed. Weak: agents run with exposed secrets/no isolation.'}, {'q': 'Are security guardrails distinguished from governance guardrails, with BOTH implemented?', 'looking_for': 'Tests the layered model. Strong: separate security + governance guardrails. Weak: conflated or only one.'}].

**Connected to:** Dimension 8: Security & Risk → has_criterion; Tool Design & Permissioning → supports_craft; Evals & Guardrails → references_criterion; Retrieval Craft → references_criterion; Agentic Threat Model → references_criterion; Guardrail Stack → references_criterion.

**Sourced from:** dimensions.json.
