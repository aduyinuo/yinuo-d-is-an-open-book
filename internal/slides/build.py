import os, re, json, sys, html
sys.path.insert(0, "/tmp/slides")
from viewer import VIEWER

ROOT = "/sessions/festive-hopeful-edison/mnt/GitHub"
CONTENT = os.path.join(ROOT, "content")
OUT = os.path.join(ROOT, "docs/slides")
os.makedirs(OUT, exist_ok=True)

SKIP_SECTIONS = {"publications", "collaborators"}

def strip_md(t):
    t = re.sub(r"<figure>.*?</figure>", "", t, flags=re.S)
    t = re.sub(r"<table>.*?</table>", "", t, flags=re.S)
    t = re.sub(r"\$\$(.+?)\$\$", r"\1", t, flags=re.S)
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = t.replace("&#x20;", " ").replace("&#x26;", "&")
    return t.strip()

def esc(t):
    return html.escape(t, quote=False)

def sentences(p):
    return [s.strip() for s in re.split(r"(?<=[.?!])\s+", p) if s.strip()]

def parse_page(path):
    raw = open(path, encoding="utf-8").read()
    body = re.sub(r"^---.*?---\s*", "", raw, flags=re.S)
    m = re.search(r"^#\s+(.+)$", body, flags=re.M)
    title = m.group(1).strip() if m else os.path.basename(path)
    body = body[m.end():] if m else body
    body = re.sub(r"_Last updated:.*$", "", body, flags=re.M)

    parts = re.split(r"^##\s+(.+)$", body, flags=re.M)
    intro = strip_md(parts[0])
    secs = []
    for i in range(1, len(parts), 2):
        h = strip_md(parts[i]).strip()
        if h.lower().strip() in SKIP_SECTIONS: continue
        txt = strip_md(parts[i+1] if i+1 < len(parts) else "")
        if txt: secs.append((h, txt))
    return title, intro, secs

def slide_title(title, sub):
    return (f'<div class="slide title"><h2>{esc(title)}</h2>'
            f'<div class="meta">{esc(sub)}</div></div>')

def slide_lead(kicker, head, paras):
    frags = "".join(f'<p class="lead frag">{esc(p)}</p>' for p in paras[1:])
    return (f'<div class="slide"><div class="kicker">{esc(kicker)}</div>'
            f'<div class="rule"></div><h2>{esc(head)}</h2>'
            f'<p class="lead">{esc(paras[0])}</p>{frags}</div>')

def slide_points(kicker, head, points):
    lis = "".join(f'<li class="frag">{esc(p)}</li>' for p in points)
    return (f'<div class="slide"><div class="kicker">{esc(kicker)}</div>'
            f'<div class="rule"></div><h2>{esc(head)}</h2><ul>{lis}</ul></div>')

def build(path, rel_slug, thread):
    title, intro, secs = parse_page(path)
    frags, narr, n = {}, {}, 1
    frags[n] = slide_title(title, thread); narr[n] = intro or title; n += 1

    if intro:
        ip = [p for p in intro.split("\n") if p.strip()]
        head = sentences(ip[0])[0] if ip else title
        rest = sentences(" ".join(ip))[1:4]
        if rest:
            frags[n] = slide_points("The idea", head, rest)
            narr[n] = intro; n += 1

    for h, txt in secs:
        paras = [p.strip() for p in txt.split("\n") if p.strip()]
        if not paras: continue
        bullets = [p.lstrip("*-• ").strip() for p in paras if re.match(r"^\s*[*-]\s", p)]
        if len(bullets) >= 2:
            frags[n] = slide_points(thread, h, bullets[:6])
        else:
            sents = sentences(" ".join(paras))
            frags[n] = slide_lead(thread, h, sents[:3] or [paras[0]])
        narr[n] = "\n\n".join(paras); n += 1

    doc = (VIEWER.replace("__TITLE__", esc(title))
                 .replace("__SUB__", esc(thread))
                 .replace("__FRAGS__", json.dumps(frags, ensure_ascii=False))
                 .replace("__NARR__", json.dumps(narr, ensure_ascii=False)))
    out = os.path.join(OUT, rel_slug + ".html")
    open(out, "w", encoding="utf-8", newline="\n").write(doc)
    return rel_slug, len(frags)

THREADS = {
    "cyber-world-modeling": "Cyber World Modeling",
    "mental-world-modeling": "Mental World Modeling",
    "human-ai-complementarity": "Human-AI Complementarity",
    "toward-deployment": "Toward Deployment",
}

built = []
base = os.path.join(CONTENT, "overview/3-year-agenda")
for dirpath, _, files in os.walk(base):
    for f in files:
        if not f.endswith(".md"): continue
        if f in ("README.md", "next.md"): continue
        p = os.path.join(dirpath, f)
        rel = os.path.relpath(p, base)
        thread = THREADS.get(rel.split(os.sep)[0], "Research")
        slug = rel[:-3].replace(os.sep, "--")
        wc = len(strip_md(open(p, encoding="utf-8").read()).split())
        if wc < 120: continue
        built.append(build(p, slug, thread))

for s, k in sorted(built): print(f"{k:2d} slides  {s}")
print("total decks:", len(built))
