#!/usr/bin/env python3
"""Render the Mermaid map in README.md as assets/roadmap.png (roadmap poster).

The Mermaid block stays the source of truth; this only draws it. Needs Google Chrome
or Chromium for layout + rasterizing (ImageMagick shrinks the PNG if present).
Run from anywhere after changing the map:  python3 scripts/render_map.py
"""
import json, pathlib, re, shutil, subprocess, sys, tempfile, time

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "roadmap.png"
WIDTH, SCALE = 1440, 2

CHROME = next((c for c in [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    shutil.which("google-chrome"), shutil.which("chromium"), shutil.which("chromium-browser"),
] if c and pathlib.Path(c).exists()), None)
if not CHROME:
    sys.exit("render_map.py: Google Chrome / Chromium not found")

# --- parse the map -------------------------------------------------------------------
readme = (ROOT / "README.md").read_text()
mm = re.search(r"```mermaid\n(.*?)```", readme, re.S)
if not mm:
    sys.exit("README.md: no mermaid block")
areas, node_area, cur = [], {}, None
for line in mm.group(1).splitlines():
    m = re.match(r'\s*subgraph \w+\["(\d\d) · (.+?)"\]', line)
    if m:
        cur = {"num": m.group(1), "title": m.group(2), "ids": [], "topics": [], "subs": [], "subids": {}, "detour": False}
        areas.append(cur); continue
    if line.strip() == "end":
        cur = None; continue
    if cur:  # same convention as check.py: a line `<id> -.-> ...` lists that node's sub-topics;
        # subs[i] is a list of [label, [child labels...]] pairs (a sub-topic may have one more level)
        nodes = re.findall(r'(\w+)\["(.+?)"\]', line)
        for nid, _ in nodes:
            node_area[nid] = cur["num"]
        if sub := re.match(r'\s*(\w+) -\.->', line):
            pid = sub.group(1)
            if pid in cur["ids"]:
                i = cur["ids"].index(pid)
                cur["subs"][i] = [[label, []] for _, label in nodes]
                for k, (nid, _) in enumerate(nodes):
                    cur["subids"][nid] = (i, k)
            elif pid in cur["subids"]:
                i, k = cur["subids"][pid]
                cur["subs"][i][k][1] = [[label, []] for _, label in nodes]
            else:
                sys.exit(f"render_map.py: '{pid}' is not a topic or sub-topic of area {cur['num']} (run scripts/check.py)")
        else:
            for nid, label in nodes:
                cur["ids"].append(nid); cur["topics"].append(label); cur["subs"].append([])
# areas entered only from a "%% side branches" edge are detours off the spine
section, targets = None, {"spine": set(), "side": set()}
for line in mm.group(1).splitlines():
    s = line.strip()
    if s.startswith("%% spine"):
        section = "spine"
    elif s.startswith("%% side"):
        section = "side"
    elif section and (m := re.match(r'(\w+) --> (\w+)', s)):
        targets[section].add(node_area[m.group(2)])
for a in areas:
    a["detour"] = a["num"] in targets["side"] - targets["spine"]

# --- page ---------------------------------------------------------------------------
HTML = r"""<!doctype html><meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; }
html, body { width: __W__px; background: #fbfbfd; }
body { color: #111827; font-family: -apple-system, "SF Pro Display", "SF Pro Text", Inter, "Helvetica Neue", Arial, sans-serif;
  background-image: radial-gradient(#dfe2ea 1px, transparent 1px); background-size: 28px 28px; }
.mono { font-family: "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace; }
#page { position: relative; width: __W__px; overflow: hidden; }
#halo { position: absolute; left: 50%; top: -340px; width: 1300px; height: 800px; transform: translateX(-50%); z-index: 0;
  background: radial-gradient(closest-side, rgba(14,165,233,.16), rgba(124,58,237,.08) 55%, transparent); }
header { position: relative; z-index: 1; text-align: center; padding-top: 92px; }
.kicker { font-size: 12px; letter-spacing: .24em; color: #4f46e5; }
h1 { margin-top: 16px; font-size: 56px; font-weight: 700; letter-spacing: -0.03em; color: #0f172a; }
h1 b { background: linear-gradient(90deg, #0ea5e9, #7c3aed); -webkit-background-clip: text; background-clip: text;
  -webkit-text-fill-color: transparent; color: transparent; }
.lede { font-size: 18px; color: #4b5563; max-width: 720px; margin: 16px auto 0; line-height: 1.5; }
.legend { display: flex; justify-content: center; gap: 26px; margin-top: 36px; font-size: 13px; color: #4b5563; }
.legend span { display: inline-flex; align-items: center; gap: 8px; }
.sw { width: 24px; height: 15px; border-radius: 4px; border: 1.5px solid #d1d5db; background: #fff; }
.sw.area { border-color: #6366f1; box-shadow: 0 0 0 2px rgba(99,102,241,.2); }
.sw.detour { border-style: dashed; border-color: #7c3aed; background: transparent; }
.sw.topic { border-left: 3px solid #6366f1; }
.sw.sub { background: #f8fafc; border-left: 3px solid rgba(99,102,241,.45); }
.sw.aside { border-style: dashed; background: transparent; }
.sw.spine { width: 28px; height: 3px; border: 0; border-radius: 2px; background: linear-gradient(90deg, #0ea5e9, #7c3aed); }
.node { position: absolute; border: 1.5px solid #e2e5ec; border-left: 3px solid var(--c); border-radius: 7px; padding: 10px 14px;
  font-size: 15px; font-weight: 500; line-height: 1.3; background: #fff; color: #111827;
  box-shadow: 0 1px 2px rgba(15,23,42,.05); }
.area { background: #fff; border: 1.5px solid var(--c); border-radius: 10px; padding: 13px 16px;
  font-size: 17px; font-weight: 600; line-height: 1.25; display: flex; gap: 12px; align-items: baseline; color: #0f172a;
  box-shadow: 0 0 0 3px color-mix(in srgb, var(--c) 18%, transparent), 0 12px 28px -12px color-mix(in srgb, var(--c) 55%, transparent); }
.area .num { font-size: 12px; font-weight: 600; letter-spacing: .1em; color: var(--c); flex: none; }
.detour { background: #fbfbfd; border-style: dashed; box-shadow: none; }
.tag { position: absolute; top: -8px; right: 12px; background: #fbfbfd; padding: 0 6px;
  font-size: 10px; letter-spacing: .14em; color: var(--c); line-height: 14px; }
.sub { font-size: 13px; font-weight: 400; padding: 7px 12px; background: #f8fafc; border-color: #e5e7eb;
  border-left: 3px solid color-mix(in srgb, var(--c) 45%, transparent); color: #374151; box-shadow: none; }
.sub2 { font-size: 12px; padding: 6px 10px; color: #4b5563; }
.aside { background: transparent; border-style: dashed; color: #4b5563; box-shadow: none; }
.start { background: linear-gradient(90deg, #0ea5e9, #7c3aed); color: #fff; border: 0; border-radius: 999px;
  font-size: 11px; font-weight: 700; letter-spacing: .16em; padding: 7px 14px; box-shadow: 0 8px 24px -8px rgba(124,58,237,.6); }
#wires { position: absolute; left: 0; top: 0; }
footer { position: absolute; left: 0; right: 0; text-align: center; font-size: 13px; color: #6b7280; }
</style>
<div id="page">
<div id="halo"></div>
<svg id="wires"><defs>
  <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5"/></filter>
</defs></svg>
<header>
  <p class="kicker mono"></p>
  <h1>Identity Engineering <b>Roadmap</b></h1>
  <p class="lede">The concepts an identity engineer needs in the AI era, in learning order, from first
  primitives to AI agents. Every node is backed by the RFC, spec, or paper that defines it.</p>
  <div class="legend">
    <span><i class="sw spine"></i>Learning path</span>
    <span><i class="sw area"></i>Area on the path</span>
    <span><i class="sw detour"></i>Detour: take it when your job needs it</span>
    <span><i class="sw topic"></i>Topic</span>
    <span><i class="sw sub"></i>Sub-topic</span>
    <span><i class="sw aside"></i>Aside</span>
  </div>
</header>
<footer class="mono"></footer>
</div>
<script>
const D = __DATA__;
const PAL = ['#f59e0b', '#f43f5e', '#ec4899', '#a855f7', '#6366f1', '#3b82f6', '#0891b2',
             '#14b8a6', '#10b981', '#65a30d', '#ca8a04', '#f97316', '#d946ef'];  // one accent per area number
const W = __W__, SPINE = W / 2, MARGIN = 40, COL_W = 450, TITLE_W = 340;
const BUS_GAP = 30, TOPIC_GAP = 10, GROUP_GAP = 44, SPINE_GAP = 52;
const SUB_INSET = 36, SUB_GAP = 6;
const page = document.getElementById('page'), svg = document.getElementById('wires');
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
let C = PAL[6];  // accent of the area being drawn
function node(cls, html, x, w) {
  const el = document.createElement('div');
  el.className = 'node ' + cls; el.innerHTML = html; el.style.setProperty('--c', C);
  el.style.left = x + 'px'; el.style.width = w + 'px';
  page.appendChild(el); return el;
}
const put = (el, y) => { el.style.top = y + 'px'; return y + el.offsetHeight; };
function shape(tag, attrs, parent = svg) {
  const e = document.createElementNS('http://www.w3.org/2000/svg', tag);
  for (const k in attrs) e.setAttribute(k, attrs[k]);
  parent.appendChild(e); return e;
}
function wire(d, cls) {  // connectors take the current area's accent
  const a = { d, fill: 'none', stroke: C, 'stroke-width': 1.5, 'stroke-linecap': 'round' };
  if (cls === 'sub') { a['stroke-width'] = 1; a['stroke-opacity'] = .55; }
  if (cls === 'branch') { a['stroke-width'] = 2; a['stroke-dasharray'] = '6 6'; }
  return shape('path', a);
}
const geo = s => s === 'L'
  ? { col: MARGIN, near: MARGIN + COL_W, bus: MARGIN + COL_W + BUS_GAP, edge: SPINE - TITLE_W / 2 }
  : { col: W - MARGIN - COL_W, near: W - MARGIN - COL_W, bus: W - MARGIN - COL_W - BUS_GAP, edge: SPINE + TITLE_W / 2 };
// sub-topics at level n (1 or 2): boxes inset n steps from the topic column, flush with the outer margin,
// a mini-bus in the inset gap next to them
const lv = (s, n) => { const w = COL_W - n * SUB_INSET; return s === 'L'
  ? { x: MARGIN, w, near: MARGIN + w, mbus: MARGIN + w + SUB_INSET / 2 }
  : { x: W - MARGIN - w, w, near: W - MARGIN - w, mbus: W - MARGIN - w - SUB_INSET / 2 }; };
const count = l => l.reduce((n, [, kids]) => n + 1 + count(kids), 0);
const nTopics = D.areas.reduce((n, a) => n + a.topics.length, 0);
const nSubs = D.areas.reduce((n, a) => n + a.subs.reduce((m, l) => m + count(l), 0), 0);
document.querySelector('.kicker').textContent = `${D.areas.length} AREAS · ${nTopics} TOPICS · ${nSubs} SUB-TOPICS`;

let y = document.querySelector('header').getBoundingClientRect().height + 64;
const start = node('start mono', 'START HERE', 0, 0);
start.style.width = 'auto'; start.style.left = (SPINE - start.offsetWidth / 2) + 'px';
let spineEnd = put(start, y);
const segs = [];  // spine segments [y0, y1, arrow], drawn last so their colour can follow the page depth
let branchY = 0;
const sideEnd = { L: spineEnd, R: spineEnd };
let side = 'L';
D.areas.forEach(a => {
  C = PAL[(+a.num - 1) % PAL.length];
  const g = geo(side), other = side === 'L' ? 'R' : 'L';
  const n0 = page.children.length, s0 = svg.children.length;  // everything this area adds comes after these
  const title = `<span class="num mono">${a.num}</span><span>${esc(a.title)}</span>`;
  const topics = a.topics.map(t => node(/^Aside:/.test(t) ? 'aside' : '', esc(t), g.col, COL_W));
  let path = '', last;
  const column = ty => {  // place each topic, then its sub-topics beneath it; returns the bottom of the last box
    const place = (items, n, top) => {  // items: [label, children][] at level n, hanging off a box that ends at `top`
      const q = lv(side, n); let sp = '', sl;
      items.forEach(([s, kids]) => {
        const se = node('sub' + (n > 1 ? ' sub2' : ''), esc(s), q.x, q.w), sb = put(se, ty + SUB_GAP);
        sl = sb - se.offsetHeight / 2; sp += `M${q.near},${sl} H${q.mbus}`; ty = sb;
        if (kids.length) place(kids, n + 1, sb);
      });
      if (sp) wire(sp + `M${q.mbus},${top} V${sl}`, 'sub');
    };
    topics.forEach((el, i) => {
      const b = put(el, ty); last = b - el.offsetHeight / 2; path += `M${g.bus},${last} H${g.near}`; ty = b;
      place(a.subs[i], 1, b);
      ty += TOPIC_GAP;
    });
    return ty - TOPIC_GAP;
  };
  if (!a.detour) {
    const t = node('area', title, SPINE - TITLE_W / 2, TITLE_W);
    const th = t.offsetHeight, h1 = topics[0].offsetHeight;
    y = Math.max(spineEnd + SPINE_GAP, sideEnd[side] + GROUP_GAP, branchY + SPINE_GAP);
    const tb = put(t, y + Math.max(0, (h1 - th) / 2)), cy = tb - th / 2;
    segs.push([spineEnd, tb - th, true]);
    spineEnd = tb;
    sideEnd[side] = column(y + Math.max(0, (th - h1) / 2));
    wire(path + `M${g.edge},${cy} H${g.bus} V${last}`, 'wire');
  } else {
    // a detour hangs off the area before it (its side edge leaves that area's last topic): lay it out in
    // the free column, then slide it down so it ends level with the parent's column and branches from
    // the spine where the parent's topics end
    const h = node('area detour', title + '<span class="tag mono">DETOUR</span>', g.col, COL_W);
    const ty = put(h, Math.max(sideEnd[side] + GROUP_GAP, spineEnd + 24)), cy = ty - h.offsetHeight / 2;
    const end = column(ty + TOPIC_GAP);
    wire(path + `M${g.bus},${cy} H${g.near} M${g.bus},${cy} V${last}`, 'wire');
    wire(`M${SPINE},${cy} H${g.bus}`, 'branch');
    shape('circle', { cx: SPINE, cy, r: 5, fill: C });
    const dy = Math.max(0, sideEnd[other] - end);
    [...page.children].slice(n0).forEach(el => el.style.top = (parseFloat(el.style.top) + dy) + 'px');
    [...svg.children].slice(s0).forEach(el => el.setAttribute('transform', `translate(0 ${dy})`));
    branchY = cy + dy; sideEnd[side] = end + dy;
  }
  side = other;
});
if (branchY > spineEnd) segs.push([spineEnd, branchY, false]);  // a trailing detour: run the rail down to it
const bottom = Math.max(spineEnd, sideEnd.L, sideEnd.R, branchY);
const f = document.querySelector('footer');
f.textContent = `${D.repo}   ·   ${D.areas.length} areas · ${nTopics} topics · ${nSubs} sub-topics`;
f.style.top = (bottom + 64) + 'px';
const H = Math.ceil(bottom + 64 + f.offsetHeight + 72);
// the spine: one rail shading from sky at the top to violet at the bottom, soft glow, an arrowhead into each area
const rgb = h => [1, 3, 5].map(i => parseInt(h.slice(i, i + 2), 16));
const tint = t => 'rgb(' + rgb('#0ea5e9').map((v, i) => Math.round(v + (rgb('#7c3aed')[i] - v) * t)).join(',') + ')';
const glow = shape('g', { filter: 'url(#blur)', opacity: .3 });
segs.forEach(([y0, y1, arrow]) => {
  const c = tint(y1 / H), end = arrow ? y1 - 10 : y1;
  shape('path', { d: `M${SPINE},${y0} V${end}`, stroke: c, 'stroke-width': 9, fill: 'none' }, glow);
  shape('path', { d: `M${SPINE},${y0} V${end}`, stroke: c, 'stroke-width': 3, fill: 'none', 'stroke-linecap': 'round' });
  if (arrow) shape('path', { d: `M${SPINE - 6},${y1 - 11} L${SPINE + 6},${y1 - 11} L${SPINE},${y1} Z`, fill: c });
  else shape('circle', { cx: SPINE, cy: y1, r: 5, fill: c });
});
svg.insertBefore(glow, svg.firstChild.nextSibling);  // glow under the wires, above the defs
page.style.height = H + 'px'; svg.setAttribute('width', W); svg.setAttribute('height', H);
svg.style.zIndex = 0; [...page.querySelectorAll('.node')].forEach(n => n.style.zIndex = 1);
document.body.dataset.height = H;
</script>
"""

data = {"areas": areas, "repo": "github.com/alvaroinckot/identity-engineering-roadmap"}
html = HTML.replace("__DATA__", json.dumps(data, ensure_ascii=False)).replace("__W__", str(WIDTH))

FLAGS = ["--headless=new", "--no-first-run", "--disable-gpu", "--hide-scrollbars",
         "--disable-background-networking", "--disable-component-update", "--disable-sync",
         "--no-service-autorun", "--use-mock-keychain", "--password-store=basic"]

def chrome(args, stdout, done, wait=60):
    """Run Chrome until done() holds, then kill it. Headless Chrome on macOS writes its
    output within a second or two and then often hangs on exit for half a minute."""
    p = subprocess.Popen([CHROME, *FLAGS, *args], stdout=stdout, stderr=subprocess.DEVNULL)
    for _ in range(wait * 10):
        if done() or p.poll() is not None:
            break
        time.sleep(0.1)
    p.kill(); p.wait()
    if not done():
        sys.exit("render_map.py: Chrome produced no output")

with tempfile.TemporaryDirectory() as tmp:
    page = pathlib.Path(tmp, "map.html"); page.write_text(html)
    dom = pathlib.Path(tmp, "dom.html")
    profile = f"--user-data-dir={tmp}/profile"
    with dom.open("w") as sink:  # pass 1: let the page lay itself out and report its height (at the
        # screenshot's scale factor: text metrics round differently per scale and the error stacks up)
        chrome([profile, f"--force-device-scale-factor={SCALE}", f"--window-size={WIDTH},1000", "--dump-dom", page.as_uri()], sink,
               lambda: dom.exists() and "</html>" in dom.read_text(errors="replace"))
    m = re.search(r'data-height="(\d+)"', dom.read_text(errors="replace"))
    if not m:
        sys.exit("render_map.py: layout script did not run")
    height = int(m.group(1))
    OUT.parent.mkdir(exist_ok=True); OUT.unlink(missing_ok=True)
    seen = []  # pass 2: screenshot at the exact height; done once the file stops growing
    def written():
        seen.append(OUT.stat().st_size if OUT.exists() else 0)
        return len(seen) > 2 and seen[-1] > 0 and seen[-1] == seen[-2] == seen[-3]
    chrome([profile, f"--force-device-scale-factor={SCALE}", f"--window-size={WIDTH},{height}",
            f"--screenshot={OUT}", page.as_uri()], subprocess.DEVNULL, written)
if magick := shutil.which("magick"):  # flat colours: a 256-colour palette is lossless to the eye, 2-3x smaller
    subprocess.run([magick, str(OUT), "-colors", "256", "-dither", "None", "-strip", str(OUT)], check=True)
print(f"wrote {OUT.relative_to(ROOT)} ({WIDTH * SCALE}x{height * SCALE}, {OUT.stat().st_size // 1024} KB)")
