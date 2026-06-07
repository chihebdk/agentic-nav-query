---
id: criterion.8_8
type: Criterion
label: "8.8 Developer Endpoint & AI Coding-Tool Security"
aliases: ["8.8", "Developer Endpoint & AI Coding-Tool Security"]
tags: ["criterion", "dim-8"]
sources: ["dimensions.json"]
---

# 8.8 Developer Endpoint & AI Coding-Tool Security

**Type:** Criterion  ·  **ID:** `criterion.8_8`

**Also known as:** 8.8, Developer Endpoint & AI Coding-Tool Security

AI coding tools 'crushed the endpoint security fortress'; ungoverned local MCP/skills can exfiltrate code/secrets and execute code, with no easy block.

## Attributes

- **dimension:** 8
- **criterion_id:** 8.8
- **anchors:** {'L1': 'AI coding tools unmanaged on laptops; anyone installs MCP/skills; no awareness', 'L2': 'Risk acknowledged; informal guidance', 'L3': 'Sanctioned tools recommended; basic dev security training; some endpoint visibility', 'L4': 'Sanctioned/enterprise tools mandated & enforced; endpoint governance enforces sandboxing/least-privilege + controls MCP/skill installs; mandatory training', 'L5': 'Fully governed AI-assisted dev: sanctioned tools, enforced sandboxing/access, vetted MCP/skill allow-list, continuous endpoint discovery + runtime protection, embedded training'}
- **probing_questions:** [{'q': 'Has the security team recognized the developer-endpoint plane (AI coding assistants + locally installed MCP servers/skills) as a distinct, governed attack surface — or is it unmanaged?', 'looking_for': 'Tests recognition of the new plane. Strong: treated as a governed attack surface. Weak: unmanaged dev laptops install anything.'}, {'q': 'Do you mandate sanctioned/enterprise AI coding tools (e.g., governed Claude Code) over unmanaged consumer tools, and enforce it?', 'looking_for': 'Tests sanctioned-tool control. Strong: sanctioned/enterprise tools mandated and enforced. Weak: developers use any consumer tool freely.'}, {'q': 'Is there endpoint governance (discovery + runtime protection) that enforces sandboxing and least-privilege for AI coding tools and controls which MCP servers/skills can be installed (vetted/allow-listed)?', 'looking_for': 'Tests enforcement on the endpoint. Strong: discovery + sandboxing/least-privilege + vetted MCP/skill allow-list. Weak: no endpoint controls → shadow MCP/skills, code/secret exfiltration.'}, {'q': 'Is there mandatory security-awareness / responsible-use training for developers using assistant/coding tools?', 'looking_for': 'Tests dev awareness. Strong: mandatory responsible-use training. Weak: none → careless installs/usage.'}, {'q': 'Do you have visibility/inventory of coding agents, MCP servers, and skills running on developer machines?', 'looking_for': 'Tests visibility. Strong: endpoint inventory of agents/MCP/skills. Weak: blind to what runs on dev laptops.'}]

## Relationships (incoming)

- [Dimension 8: Security & Risk](./dim__8.md) → has_criterion

## Sources

- dimensions.json
