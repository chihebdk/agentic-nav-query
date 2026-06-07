# Agentic Transformation Navigator — Query layer (generated; do not hand-edit)

This repository is **published automatically** by the producer's GitHub Action. Everything
under `src/` is generated from the curated knowledge graph — **do not edit it here**; changes
would be overwritten on the next publish. To change the knowledge, edit in the **producer** repo.

## What's inside
- `src/semantic/agentic-nav.db` — indexed SQLite store (nodes/edges + FTS5), the fast query backend.
- `src/semantic/mcp_server.py` — warm, dependency-free MCP server (tools `kg_entity`,
  `kg_neighbors`, `kg_search`, `kg_by_type`, `kg_open_questions`, `kg_stale`).
- `src/semantic/query.py` / `query_sql.py` / `search.py` — CLI query paths.
- `src/knowledge-base/**`, `src/ontology/**`, `src/semantic/**` — the human-readable layers.
- `.claude/skills/query-knowledge/` — the read-side skill.
- `.mcp.json` — for the *in-place* mode (clone this repo as your workspace).

## Use it (two ways)
**Cache-dir (recommended):** install the SessionStart sync hook so this repo is
cloned/pulled into `~/.agentic-nav-kg` and the skill is refreshed globally — see the producer's
`deploy/README.md`. Then `/model sonnet` and ask in natural language.

**In-place:** clone this repo, open it in Claude Code, approve the `agentic-nav-kg` MCP server
(`/mcp`), `/model sonnet`, and ask away.

Read-only by design. Temporal correctness (current-only, dated, cited) is built into the tools.
