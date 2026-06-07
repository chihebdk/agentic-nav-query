# -*- coding: utf-8 -*-
"""Warm, dependency-free MCP server over the Optimus knowledge graph (semantic/optimus.db).

Loads the indexed store ONCE at startup, then answers many queries from a long-lived process —
eliminating the ~80 ms-per-call Python cold-start that dominates the CLI tools. Auto-refreshes:
before each query it stat()s the db and transparently reopens if it changed on disk (atomic
swap / sync) or appeared since startup, so a freshly-built/synced db is served on the next call
with NO server (or Cowork) restart. Stdlib only (sqlite3 + a hand-rolled stdio JSON-RPC 2.0
loop); no `mcp` package required.

Transport: newline-delimited JSON-RPC 2.0 over stdin/stdout (MCP stdio). All diagnostics go to
stderr so stdout stays a clean protocol channel.

Tools exposed (all temporality-aware, current-only by default):
  kg_entity(term, history?, as_of?)   kg_neighbors(term, rel?)   kg_search(query, n?)
  kg_by_type(type, state?, limit?)    kg_open_questions(limit?)  kg_stale()

Register in the project MCP config (.mcp.json):
  {"mcpServers": {"optimus-kg": {"command": "python",
     "args": ["src/semantic/mcp_server.py"]}}}
"""
import os, sys, json, sqlite3, re

# MCP requires UTF-8; Windows consoles default to cp1252 which breaks chars like "→".
try:
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8", newline="\n")
except Exception:
    pass

# ---- project identity (server name / db / cache / env vars) from project.config.json ----
# Looked up next to the server (plugin layout) or in ../pipeline (repo layout); else Optimus defaults.
def _load_project_cfg():
    here = os.path.dirname(os.path.abspath(__file__))
    for p in (os.environ.get("KOS_PROJECT_CONFIG"),
              os.path.join(here, "project.config.json"),
              os.path.join(here, "..", "pipeline", "project.config.json")):
        if p and os.path.exists(p):
            try:
                return json.load(open(p, encoding="utf-8"))
            except Exception:
                pass
    return {}

_pcfg = _load_project_cfg()
SLUG = _pcfg.get("slug", "optimus")
NAME = _pcfg.get("name", "Optimus")
SERVER_NAME = _pcfg.get("server_name", "optimus-kg")
DB_NAME = _pcfg.get("db_name", "optimus.db")
CACHE_DIR = os.path.expanduser(_pcfg.get("cache_dir", "~/.optimus-kg"))
ENV_DB = f"{SLUG.upper()}_DB"                 # e.g. OPTIMUS_DB (slug=optimus) — backward-compatible
ENV_QUERY_REPO = f"{SLUG.upper()}_QUERY_REPO"

def _resolve_db():
    """<SLUG>_DB env wins; else the db next to this script (repo in-place); else the
    plugin/consumer cache (kept fresh by the sync hook)."""
    env = os.environ.get(ENV_DB)
    if env:
        return env
    local = os.path.join(os.path.dirname(os.path.abspath(__file__)), DB_NAME)
    if os.path.exists(local):
        return local
    return os.path.join(CACHE_DIR, "src", "semantic", DB_NAME)

DB = _resolve_db()
SERVER_INFO = {"name": SERVER_NAME, "version": "1.1.0"}   # 1.1.0: in-memory load + db auto-refresh
DEFAULT_PROTOCOL = "2024-11-05"


def log(*a):
    print(f"[{SERVER_NAME}]", *a, file=sys.stderr, flush=True)


# ---- warm store with AUTO-REFRESH ----
# Load the indexed db into an IN-MEMORY copy at startup and release the file handle immediately,
# then re-check the file before each query and transparently reload if it changed on disk (atomic
# rebuild swap / git-pull sync) or appeared since startup — so a freshly-built/synced db is served
# on the next call with NO server (or Cowork) restart. Loading into memory (not holding the file
# open) is essential on Windows: a process that holds the db open LOCKS it, so the build/sync can't
# replace it (that's why build_sqlite used to leave a .db.new). Releasing the handle lets the swap
# happen; queries then run from RAM (warm-fast). The freshness check is a single stat() (negligible);
# a reload happens only when the file actually changes.
con = None
_db_sig = None        # (path, mtime_ns, size) of the currently-loaded db

def _sig(path):
    try:
        st = os.stat(path)
        return (path, st.st_mtime_ns, st.st_size)
    except OSError:
        return None

def _open_db(path):
    global con, _db_sig
    try:
        sig = _sig(path)                                          # stamp before the brief read
        src = sqlite3.connect(f"file:{path}?mode=ro&immutable=1", uri=True)
        mem = sqlite3.connect(":memory:", check_same_thread=False)
        src.backup(mem)                                           # copy all pages (incl. FTS) into RAM
        src.close()                                               # <-- release the lock on the on-disk file
        mem.row_factory = sqlite3.Row
        old, con, _db_sig = con, mem, sig
        if old is not None:
            try:
                old.close()
            except Exception:
                pass
        log("loaded into memory:", path)
    except Exception as e:
        log("failed to open DB", path, repr(e))

def ensure_fresh():
    """Reopen the db if it changed/appeared on disk; a cheap no-op when unchanged. Re-resolves the
    path each time so a higher-priority db (env / local) that shows up later is picked up too."""
    global DB
    path = _resolve_db()
    cur = _sig(path)
    if cur is None:
        return            # not present right now (e.g. mid-swap) — keep serving what we have
    if con is None or cur != _db_sig:
        DB = path
        _open_db(path)

ensure_fresh()            # initial load
if con is None:
    log("DB not found:", DB, f"- waiting for sync. Set {ENV_QUERY_REPO}; it will load on the next query (no restart).")

NO_DATA_MSG = (
    f"{NAME} knowledge data is not available yet. The server could not find a database at:\n"
    f"  {DB}\n"
    f"Fix: ensure the SessionStart sync ran (set {ENV_QUERY_REPO}), or clone the "
    f"query repo into {CACHE_DIR}, or set the {ENV_DB} env var to a valid {DB_NAME}. "
    "The server will load it automatically on the next query — no restart needed."
)


# ============================ query helpers (return text) ============================
def fts(term):
    toks = re.findall(r"[A-Za-z0-9]+", term)
    return " OR ".join(f'"{t}"' for t in toks) if toks else '""'


def node(nid):
    return con.execute("SELECT * FROM nodes WHERE id=?", (nid,)).fetchone()


def label(nid):
    r = con.execute("SELECT label FROM nodes WHERE id=?", (nid,)).fetchone()
    return r["label"] if r else nid


def resolve(term, prefer_current=True):
    if node(term):
        return term, []
    rows = con.execute(
        "SELECT id FROM nodes WHERE label=? COLLATE NOCASE "
        "UNION SELECT node_id FROM aliases WHERE alias=? COLLATE NOCASE", (term, term)).fetchall()
    if rows:
        ids = [r[0] for r in rows]
        return ids[0], ids[1:6]
    try:
        rows = con.execute(
            "SELECT f.id FROM node_fts f JOIN nodes n ON n.id=f.id WHERE node_fts MATCH ? "
            "ORDER BY (CASE WHEN n.status='current' THEN 0 ELSE 1 END), bm25(node_fts) LIMIT 6",
            (fts(term),)).fetchall()
    except sqlite3.OperationalError:
        rows = []
    return (rows[0]["id"], [r["id"] for r in rows[1:]]) if rows else (None, [])


def valid_on(n, date):
    if n["valid_from"] and date < n["valid_from"]:
        return False
    if n["valid_to"] and date >= n["valid_to"]:
        return False
    return True


def entity_text(term, history=False, as_of=None):
    nid, alts = resolve(term, prefer_current=(as_of is None))
    if not nid:
        return f"No entity matched '{term}'. Try kg_search for passages, or kg_stale."
    return _card(nid, history, None, as_of) + (
        ("\n\nOther matches: " + ", ".join(f"{label(a)} ({a})" for a in alts)) if alts else "")


def neighbors_text(term, rel=None):
    nid, _ = resolve(term)
    if not nid:
        return f"No entity matched '{term}'."
    return _card(nid, False, rel, None)


def _card(nid, history, rel, as_of):
    n = node(nid)
    L = [f"=== {n['label']}  [{n['type']}]  ({nid}) ==="]
    if n["status"] == "superseded" and not history and not as_of and n["superseded_by"] and node(n["superseded_by"]):
        L.append(f"⚠️ SUPERSEDED (valid_to={n['valid_to']}). Current → {label(n['superseded_by'])}. Showing current.")
        return "\n".join(L) + "\n\n" + _card(n["superseded_by"], history, rel, as_of)
    prov = [f"status={n['status']}"] + [f"{k}={n[k]}" for k in
            ("as_of", "valid_from", "valid_to", "source_doc") if n[k]]
    L.append("  ·  ".join(prov))
    al = [r["alias"] for r in con.execute("SELECT alias FROM aliases WHERE node_id=?", (nid,))]
    if al:
        L.append("aka: " + ", ".join(dict.fromkeys(al)))
    if n["summary"]:
        L.append("\n" + n["summary"])
    attrs = json.loads(n["attributes"] or "{}")
    if attrs:
        L.append("\nAttributes:")
        L += [f"  - {k}: {v}" for k, v in attrs.items() if v not in (None, "", [], {})]

    def keep(o):
        m = node(o)
        if not m:
            return True
        if as_of is not None:
            return valid_on(m, as_of)
        return history or m["status"] != "superseded"

    rc = " AND rel=?" if rel else ""
    a = [nid] + ([rel] if rel else [])
    out = [(e["rel"], e["dst"]) for e in con.execute(f"SELECT rel,dst,status FROM edges WHERE src=?{rc}", a)
           if (history or as_of is not None or e["status"] != "superseded") and keep(e["dst"])]
    inc = [(e["rel"], e["src"]) for e in con.execute(f"SELECT rel,src,status FROM edges WHERE dst=?{rc}", a)
           if (history or as_of is not None or e["status"] != "superseded") and keep(e["src"])]
    if out:
        L.append("\nRelationships (outgoing):")
        L += [f"  {rl} → {label(t)}" + ("" if node(t) and node(t)['status'] == 'current' else f"  [{node(t)['status']}]" if node(t) else "") for rl, t in out[:50]]
    if inc:
        L.append("\nRelationships (incoming):")
        L += [f"  {label(s)} → {rl}" for rl, s in inc[:50]]
    if history:
        preds = [r["id"] for r in con.execute("SELECT id FROM nodes WHERE superseded_by=?", (nid,))]
        if n["supersedes"]:
            sv = json.loads(n["supersedes"]); preds += sv if isinstance(sv, list) else [sv]
        preds = [p for p in dict.fromkeys(preds) if node(p)]
        if preds:
            L.append("\nHistory (superseded predecessors):")
            L += [f"  - {node(p)['label']} ({p})  valid {node(p)['valid_from']}→{node(p)['valid_to']}" for p in preds]
    src = json.loads(n["sources"] or "[]")
    if src:
        L.append("\nSources: " + ", ".join(src))
    return "\n".join(L)


def search_text(query, n=8):
    rows = con.execute("SELECT path,title,bm25(docs_fts) r FROM docs_fts WHERE docs_fts MATCH ? "
                       "ORDER BY r LIMIT ?", (fts(query), int(n))).fetchall()
    if not rows:
        return f"No passages matched '{query}'."
    return f"Passage search: {query}\n" + "\n".join(
        f"  {r['r']:.3f}  {r['title'][:58]:<58}  {r['path']}" for r in rows)


def by_type_text(type_, state=None, limit=50):
    q = "SELECT id,label,status FROM nodes WHERE type=?"
    a = [type_]
    if state:
        q += " AND json_extract(attributes,'$.state')=?"; a.append(state)
    rows = con.execute(q + " ORDER BY label LIMIT ?", a + [int(limit)]).fetchall()
    if not rows:
        return f"No nodes of type '{type_}'" + (f" with state '{state}'" if state else "") + "."
    return f"{type_} ({len(rows)}):\n" + "\n".join(
        f"  {r['label']}  ({r['id']})" + ("" if r['status'] == 'current' else f"  [{r['status']}]") for r in rows)


def open_questions_text(limit=50):
    rows = con.execute(
        "SELECT id,label,attributes FROM nodes WHERE type='Question' "
        "AND json_extract(attributes,'$.state')='open' ORDER BY id LIMIT ?", (int(limit),)).fetchall()
    if not rows:
        return "No open questions."
    out = [f"Open questions ({len(rows)}):"]
    for r in rows:
        at = json.loads(r["attributes"] or "{}")
        out.append(f"  - {r['label']}  (about: {at.get('about','?')}; "
                   f"assignee: {at.get('assigned_to_name', at.get('raised_by_name','?'))})  [{r['id']}]")
    return "\n".join(out)


def stale_text():
    sc = con.execute("SELECT status,count(*) c FROM nodes GROUP BY status").fetchall()
    out = ["status_counts: " + ", ".join(f"{r['status']}={r['c']}" for r in sc)]
    sup = con.execute("SELECT id,label,valid_to,superseded_by FROM nodes WHERE status='superseded'").fetchall()
    out.append(f"Superseded ({len(sup)}):")
    out += [f"  - {r['label']} ({r['id']})  valid_to={r['valid_to']} → {r['superseded_by'] or '?'}" for r in sup] \
        or ["  (none — every fact is current)"]
    return "\n".join(out)


# ============================ MCP tool registry ============================
TOOLS = [
    {"name": "kg_entity",
     "description": "Look up an entity by id/label/alias and return its current state, provenance "
                    "(status/as_of/valid_from/source) and relationships. Current-only unless history/as_of given.",
     "inputSchema": {"type": "object", "properties": {
         "term": {"type": "string", "description": "Entity id, label, or alias."},
         "history": {"type": "boolean", "description": "Include superseded predecessors."},
         "as_of": {"type": "string", "description": "ISO date YYYY-MM-DD for a valid-time slice."}},
         "required": ["term"]},
     "fn": lambda a: entity_text(a["term"], a.get("history", False), a.get("as_of"))},
    {"name": "kg_neighbors",
     "description": "Show an entity's relationships, optionally filtered to one relation type.",
     "inputSchema": {"type": "object", "properties": {
         "term": {"type": "string"}, "rel": {"type": "string", "description": "e.g. led_by, raised_in, owned_by."}},
         "required": ["term"]},
     "fn": lambda a: neighbors_text(a["term"], a.get("rel"))},
    {"name": "kg_search",
     "description": "Full-text (FTS5) passage search across documents, knowledge-base notes and semantic cards.",
     "inputSchema": {"type": "object", "properties": {
         "query": {"type": "string"}, "n": {"type": "integer", "description": "max results (default 8)"}},
         "required": ["query"]},
     "fn": lambda a: search_text(a["query"], a.get("n", 8))},
    {"name": "kg_by_type",
     "description": "List nodes of a class (e.g. Session, ActionItem, Decision, Question, Person), "
                    "optionally filtered by lifecycle state (open/done/...).",
     "inputSchema": {"type": "object", "properties": {
         "type": {"type": "string"}, "state": {"type": "string"}, "limit": {"type": "integer"}},
         "required": ["type"]},
     "fn": lambda a: by_type_text(a["type"], a.get("state"), a.get("limit", 50))},
    {"name": "kg_open_questions",
     "description": "List all open questions raised in sessions, with their subject and assignee.",
     "inputSchema": {"type": "object", "properties": {"limit": {"type": "integer"}}},
     "fn": lambda a: open_questions_text(a.get("limit", 50))},
    {"name": "kg_stale",
     "description": "Audit: status counts plus every superseded fact and its successor.",
     "inputSchema": {"type": "object", "properties": {}},
     "fn": lambda a: stale_text()},
]
TOOL_BY_NAME = {t["name"]: t for t in TOOLS}


# ============================ JSON-RPC plumbing ============================
def reply(mid, result=None, error=None):
    msg = {"jsonrpc": "2.0", "id": mid}
    if error is not None:
        msg["error"] = error
    else:
        msg["result"] = result
    sys.stdout.write(json.dumps(msg, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def handle(req):
    method = req.get("method")
    mid = req.get("id")
    params = req.get("params") or {}
    if method == "initialize":
        proto = params.get("protocolVersion", DEFAULT_PROTOCOL)
        reply(mid, {"protocolVersion": proto, "capabilities": {"tools": {}},
                    "serverInfo": SERVER_INFO})
    elif method == "notifications/initialized":
        pass  # notification, no reply
    elif method == "ping":
        reply(mid, {})
    elif method == "tools/list":
        reply(mid, {"tools": [{k: t[k] for k in ("name", "description", "inputSchema")} for t in TOOLS]})
    elif method == "tools/call":
        name = params.get("name"); args = params.get("arguments") or {}
        tool = TOOL_BY_NAME.get(name)
        if not tool:
            reply(mid, error={"code": -32601, "message": f"unknown tool: {name}"}); return
        ensure_fresh()        # auto-pick-up a freshly-built/synced db (no restart needed)
        if con is None:
            reply(mid, {"content": [{"type": "text", "text": NO_DATA_MSG}], "isError": True}); return
        try:
            text = tool["fn"](args)
            reply(mid, {"content": [{"type": "text", "text": text}], "isError": False})
        except Exception as e:
            log("tool error", name, e)
            reply(mid, {"content": [{"type": "text", "text": f"error: {e}"}], "isError": True})
    elif mid is not None:
        reply(mid, error={"code": -32601, "message": f"method not found: {method}"})
    # else: unknown notification — ignore


def main():
    log("ready; tools:", ", ".join(TOOL_BY_NAME))
    for line in sys.stdin:
        line = line.lstrip("﻿").strip()  # tolerate a leading BOM
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            log("bad json:", line[:120]); continue
        try:
            handle(req)
        except Exception as e:
            log("handler error:", e)


if __name__ == "__main__":
    main()
