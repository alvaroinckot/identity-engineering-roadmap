#!/usr/bin/env python3
"""Consistency check for the roadmap: map <-> area folders <-> topic files <-> links.

Exits 1 with a list of errors. Run from anywhere: python3 scripts/check.py
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors = []
err = errors.append

readme = (ROOT / "README.md").read_text()
mm = re.search(r"```mermaid\n(.*?)```", readme, re.S)
if not mm:
    sys.exit("README.md: no mermaid block")
# Inside an area subgraph, labeled nodes are topics, except on a line that starts
# `<id> -.->`: those are that node's sub-topics, in order (the parent may itself be a
# sub-topic: one more level, no deeper). Files for all of them are flat.
areas = {}  # "01" -> (title, [(id, label)] topics, {parent id: [(id, label)] sub-topics})
ids, cur = set(), None
for line in mm.group(1).splitlines():
    m = re.match(r'\s*subgraph \w+\["(\d\d) · (.+?)"\]', line)
    if m:
        cur = m.group(1); areas[cur] = (m.group(2), [], {}); continue
    if line.strip() == "end":
        cur = None; continue
    if not cur:
        continue
    nodes = re.findall(r'(\w+)\["(.+?)"\]', line)
    for nid, _ in nodes:
        if nid in ids:
            err(f"map: duplicate node id '{nid}' (Mermaid silently merges them)")
        ids.add(nid)
    sub = re.match(r'\s*(\w+) -\.->', line)
    if line.count("-.->") > (1 if sub else 0):
        err(f"map: '-.->' only starts a sub-topic line ('<topic id> -.-> ...'): {line.strip()[:60]}")
    if sub:
        areas[cur][2][sub.group(1)] = nodes
    else:
        areas[cur][1].extend(nodes)

TAGS = {"official", "article", "video", "paper", "opensource", "course", "book"}
RES_RE = re.compile(r'^- \[@(\w+)@[^\]]+\]\(https?://[^)\s]+\)')
NOSRC = "_No dedicated source yet._"

seen = set()
for d in sorted(p for p in (ROOT / "roadmap").iterdir() if p.is_dir()):
    num = d.name[:2]; seen.add(num)
    if num not in areas:
        err(f"{d.name}: folder has no area on the map"); continue
    title, tnodes, subs = areas[num]
    known = {i for i, _ in tnodes} | {i for kids in subs.values() for i, _ in kids}
    for parent in subs:
        if parent not in known:
            err(f"map area {num}: sub-topics hang off '{parent}', which is not a topic or sub-topic of that area")
    expected = []  # (depth, label) in README order: 0 topic, 1 sub-topic, 2 sub-sub-topic
    def walk(nid, label, depth):
        if depth > 2:
            err(f"map area {num}: '{label}' is nested deeper than two levels below its topic"); return
        expected.append((depth, label))
        for cid, cl in subs.get(nid, []):
            walk(cid, cl, depth + 1)
    for tid, l in tnodes:
        walk(tid, l, 0)
    labels = [l for _, l in expected]
    if len(set(labels)) != len(labels):
        err(f"map area {num}: duplicate labels {sorted({l for l in labels if labels.count(l) > 1})}")
    rd = d / "README.md"
    if not rd.exists():
        err(f"{d.name}: missing README.md"); continue
    rtxt = rd.read_text()
    h1 = re.match(r'# (\d\d) · (.+)', rtxt)
    if not h1 or h1.group(2).strip() != title:
        err(f"{rd.relative_to(ROOT)}: H1 must be '# {num} · {title}'")
    topics = {}  # H1 -> file, topics and sub-topics alike
    for f in sorted(d.glob("*.md")):
        if f.name == "README.md":
            continue
        t = f.read_text()
        m = re.match(r'# (.+)\n', t)
        if not m:
            err(f"{f.relative_to(ROOT)}: no H1"); continue
        if m.group(1).strip() in topics:
            err(f"{f.relative_to(ROOT)}: same H1 as {topics[m.group(1).strip()].name}")
        topics[m.group(1).strip()] = f
        res = re.search(r'^## Resources\n(.*?)(?:\n---|\Z)', t, re.S | re.M)
        if not res:
            err(f"{f.relative_to(ROOT)}: no '## Resources' section"); continue
        body = res.group(1).strip()
        if body == NOSRC:
            continue
        for l in body.splitlines():
            if not l.strip():
                continue
            m2 = RES_RE.match(l)
            if not m2:
                err(f"{f.relative_to(ROOT)}: resource line must be '- [@tag@Title](url)': {l[:70]}")
            elif m2.group(1) not in TAGS:
                err(f"{f.relative_to(ROOT)}: unknown tag @{m2.group(1)}@ (use {sorted(TAGS)})")
    for l in labels:
        if l not in topics:
            err(f"{d.name}: map node '{l}' has no topic file with that H1")
    for t, f in topics.items():
        if t not in labels:
            err(f"{f.relative_to(ROOT)}: topic '{t}' is not a node on the map")
    section = rtxt.split("\n## Topics\n", 1)[-1].split("\n## ", 1)[0]
    listed = re.findall(r'^( *)\d+\. \[(.+?)\]\((.+?)\)', section, re.M)
    if [(len(ind) // 3, t) for ind, t, _ in listed] != expected:  # 3 spaces of indent per level
        want = ", ".join("↳ " * d + l for d, l in expected)
        err(f"{rd.relative_to(ROOT)}: '## Topics' list must match the map, in order, sub-topics nested under their topic (3 spaces per level): {want}")
    for _, t, f in listed:
        if t in topics and topics[t].name != f:
            err(f"{rd.relative_to(ROOT)}: '{t}' links to {f}, expected {topics[t].name}")
for num in areas:
    if num not in seen:
        err(f"map area {num} has no roadmap/{num}-* folder")

def anchors(txt):
    return {re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in re.findall(r'^#+ (.+)$', txt, re.M)}

for f in ROOT.rglob("*.md"):
    if ".git" in f.parts or ".github" in f.parts:
        continue
    txt = f.read_text()
    for target in re.findall(r'\]\(([^)\s]+)\)', txt):
        if re.match(r'https?://|mailto:', target):
            continue
        path, _, anchor = target.partition('#')
        dest = (f.parent / path).resolve() if path else f
        if not dest.exists():
            err(f"{f.relative_to(ROOT)}: broken link {target}"); continue
        if anchor and dest.suffix == ".md" and anchor not in anchors(dest.read_text()):
            err(f"{f.relative_to(ROOT)}: missing anchor {target}")

if errors:
    print("\n".join(errors)); print(f"\n{len(errors)} error(s)"); sys.exit(1)
n_sub = sum(len(s) for v in areas.values() for s in v[2].values())
print(f"OK: {len(areas)} areas, {sum(len(v[1]) for v in areas.values())} topics, {n_sub} sub-topics, all links resolve")
