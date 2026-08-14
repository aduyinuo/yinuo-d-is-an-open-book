import os, re, glob, hashlib, unicodedata
from PIL import Image, ImageDraw, ImageFont

ROOT = "/sessions/festive-hopeful-edison/mnt/GitHub/content"
ASSETS = os.path.join(ROOT, ".gitbook/assets")
SIZE = 96                       # stored resolution
DISPLAY = 48                    # rendered width

# green palette
TINTS = [("#22452f", "#ffffff"), ("#4a7c59", "#ffffff"),
         ("#3a6347", "#ffffff"), ("#5c8f6b", "#ffffff")]

# real photos already in the repo, keyed by collaborator name
PHOTO_DIR = "/tmp/heads"
REAL = {"Palvi Aggarwal": "/sessions/festive-hopeful-edison/mnt/GitHub/content/.gitbook/assets/palvi-aggarwal.jpg"}
for _n, _f in {
    "Christopher Kiekintveld": "christopher-kiekintveld",
    "Cleotilde Gonzalez": "cleotilde-gonzalez",
    "Fei Fang": "fei-fang",
    "Baptiste Prebot": "baptiste-prebot",
    "Maria Jose Ferreira": "maria-jose-ferreira",
    "Tyler Malloy": "tyler-malloy",
    "Stephanie Milani": "stephanie-milani",
    "Prashanth Rajivan": "prashanth-rajivan",
    "Antti Oulasvirta": "antti-oulasvirta",
    "Maria Rigaki": "maria-rigaki",
    "Carlos A. Catania": "carlos-a-catania",
    "Volodymyr (Vlad) Miloserdov": "volodymyr-vlad-miloserdov",
    "Aritran Piplai": "aritran-piplai",
    "Jaime Acosta": "jaime-acosta",
    "Anantaa Kotal": "anantaa-kotal",
    "Kuldeep Singh": "kuldeep-singh",
}.items():
    REAL[_n] = os.path.join(PHOTO_DIR, _f + ".bin")

def slug(name):
    s = unicodedata.normalize("NFKD", name)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = s.replace("(", "").replace(")", "").replace(".", "")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s

def initials(name):
    parts = [p for p in re.split(r"[\s\-]+", name) if p and p[0].isalpha()]
    if not parts: return "?"
    if len(parts) == 1: return parts[0][:2].upper()
    return (parts[0][0] + parts[-1][0]).upper()

def circle_mask(size):
    m = Image.new("L", (size*4, size*4), 0)
    ImageDraw.Draw(m).ellipse((0, 0, size*4-1, size*4-1), fill=255)
    return m.resize((size, size), Image.LANCZOS)

def font(px):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"]:
        if os.path.exists(p):
            return ImageFont.truetype(p, px)
    return ImageFont.load_default()

def make_avatar(name):
    out = os.path.join(ASSETS, f"collab-{slug(name)}.png")
    mask = circle_mask(SIZE)
    key = unicodedata.normalize("NFKD", name)
    key = "".join(c for c in key if not unicodedata.combining(c))
    src = REAL.get(key) or REAL.get(name)
    if src and os.path.exists(src):
        im = Image.open(src).convert("RGB")
        w, h = im.size
        side = min(w, h)
        left = (w - side) // 2
        top = int((h - side) * 0.28) if h > w else (h - side) // 2   # bias toward the face
        im = im.crop((left, top, left + side, top + side))
        im = im.resize((SIZE, SIZE), Image.LANCZOS)
    else:
        bg, fg = TINTS[int(hashlib.md5(name.encode()).hexdigest(), 16) % len(TINTS)]
        im = Image.new("RGB", (SIZE, SIZE), bg)
        d = ImageDraw.Draw(im)
        txt = initials(name)
        f = font(int(SIZE*0.40))
        bb = d.textbbox((0, 0), txt, font=f)
        d.text(((SIZE-(bb[2]-bb[0]))/2 - bb[0], (SIZE-(bb[3]-bb[1]))/2 - bb[1]),
               txt, font=f, fill=fg)
    av = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    av.paste(im, (0, 0), mask)
    av.save(out)
    return f"collab-{slug(name)}.png"

BULLET = re.compile(r"^\*\s+(?:\[(?P<n1>[^\]]+)\]\((?P<url>[^)]+)\)|(?P<n2>[^—\n]+?))\s*(?:—\s*(?P<aff>.*?))?\s*$")

def parse(line):
    m = BULLET.match(line.rstrip())
    if not m: return None
    name = (m.group("n1") or m.group("n2") or "").strip()
    if not name: return None
    url = m.group("url")
    aff = (m.group("aff") or "").strip()
    note = ""
    nm = re.search(r"_\((.*?)\)_", aff)
    if nm:
        note = nm.group(1)
        aff = aff.replace(nm.group(0), "").strip()
    return {"name": name, "url": url, "aff": aff, "note": note}

def cell(p, rel):
    img = f'<img src="{rel}/{p["asset"]}" alt="{p["name"]}" width="{DISPLAY}">'
    nm = f'<a href="{p["url"]}"><strong>{p["name"]}</strong></a>' if p["url"] else f'<strong>{p["name"]}</strong>'
    lines = [img, nm]
    if p["aff"]: lines.append(p["aff"])
    if p["note"]: lines.append(f'<em>({p["note"]})</em>')
    return "<td>" + "<br>".join(lines) + "</td>"

def table(people, rel, per_row=5):
    chunks = [people[i:i+per_row] for i in range(0, len(people), per_row)]
    width = max(len(c) for c in chunks)
    head = "".join('<th></th>' for _ in range(width))
    rows = ""
    for ch in chunks:
        tds = "".join(cell(p, rel) for p in ch)
        tds += "<td></td>" * (width - len(ch))
        rows += f"<tr>{tds}</tr>"
    return (f'<table data-header-hidden><thead><tr>{head}</tr></thead>'
            f'<tbody>{rows}</tbody></table>')

changed = []
for path in sorted(glob.glob(os.path.join(ROOT, "overview/3-year-agenda/**/*.md"), recursive=True)):
    txt = open(path, encoding="utf-8").read()
    if "## Collaborators" not in txt: continue
    lines = txt.split("\n")
    try: start = next(i for i, l in enumerate(lines) if l.strip() == "## Collaborators")
    except StopIteration: continue
    i = start + 1
    people = []
    last = i
    while i < len(lines):
        l = lines[i]
        if l.strip().startswith("##"): break
        if l.strip().startswith("*"):
            p = parse(l)
            if p: people.append(p); last = i
            else: last = i
        elif l.strip() == "":
            pass
        else:
            break
        i += 1
    if not people: continue
    for p in people: p["asset"] = make_avatar(p["name"])
    depth = os.path.relpath(path, ROOT).count("/")
    rel = "/".join([".."] * depth) + "/.gitbook/assets"
    new = lines[:start+1] + ["", table(people, rel), ""] + lines[last+1:]
    out = "\n".join(new)
    out = re.sub(r"\n{3,}", "\n\n", out)
    open(path, "w", encoding="utf-8", newline="\n").write(out)
    changed.append((os.path.relpath(path, ROOT), len(people)))

for c, n in changed: print(f"{n} collaborators  {c}")
print("avatars:", len(glob.glob(os.path.join(ASSETS, "collab-*.png"))))
