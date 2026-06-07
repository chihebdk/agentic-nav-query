# -*- coding: utf-8 -*-
"""Tiny dependency-free search over the Optimus knowledge system.

Usage:
    python search.py "chapter lead responsibilities"
    python search.py --entity "pod owner"
    python search.py "ABR funding" -n 5

It ranks documents with TF-IDF (from search-index.json) and also resolves the
query against entity labels/aliases (entity-index.json) so you get both the
best passages and the matching knowledge-graph entities.
"""
import os, re, json, sys, math
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
IDX = json.load(open(os.path.join(HERE, "search-index.json"), encoding="utf-8"))
ENT = json.load(open(os.path.join(HERE, "entity-index.json"), encoding="utf-8"))

STOP = set("a an the of to in on for and or with by as at is are be this that those it its from "
           "into within across each per via not no only etc vs they their our we you".split())

def tok(text):
    return [t for t in re.findall(r"[a-z][a-z0-9&/+\-]{1,}", text.lower())
            if t not in STOP and len(t) > 1]

def search_docs(query, n=8):
    q = tok(query)
    scores = Counter()
    for t in q:
        idf = IDX["idf"].get(t)
        if not idf:
            continue
        for docid, tf in IDX["postings"].get(t, []):
            dl = IDX["docs"][docid]["len"] or 1
            scores[docid] += (tf / dl) * idf
    out = []
    for docid, sc in scores.most_common(n):
        d = IDX["docs"][docid]
        out.append((round(sc, 4), d["path"], d["title"]))
    return out

def search_entities(query, n=8):
    ql = query.lower(); qtok = set(tok(query))
    res = []
    for eid, e in ENT.items():
        hay = " ".join([e["label"]] + e.get("aliases", []) + e.get("tags", [])).lower()
        score = 0
        if ql in e["label"].lower() or any(ql in a.lower() for a in e.get("aliases", [])):
            score += 5
        score += len(qtok & set(tok(hay)))
        if score:
            res.append((score, e["degree"], eid, e["type"], e["label"]))
    res.sort(key=lambda x: (-x[0], -x[1]))
    return res[:n]

def main():
    args = [a for a in sys.argv[1:]]
    n = 8; ent_only = False
    if "--entity" in args:
        ent_only = True; args.remove("--entity")
    if "-n" in args:
        i = args.index("-n"); n = int(args[i+1]); del args[i:i+2]
    query = " ".join(args).strip()
    if not query:
        print(__doc__); return
    print(f"\n== Query: {query} ==\n")
    ents = search_entities(query, n)
    if ents:
        print("Matching entities (knowledge graph):")
        for score, deg, eid, typ, label in ents:
            print(f"  [{typ:<14}] {label:<48} ({eid}, links={deg})")
        print()
    if not ent_only:
        docs = search_docs(query, n)
        print("Top passages (TF-IDF):")
        for sc, path, title in docs:
            print(f"  {sc:>7}  {title[:60]:<60}  {path}")
    print()

if __name__ == "__main__":
    main()
