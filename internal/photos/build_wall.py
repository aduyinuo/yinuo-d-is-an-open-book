#!/usr/bin/env python3
"""
Step 3: publish the shortlist as photo walls.

    python internal/photos/build_wall.py

Writes web-sized copies into content/.gitbook/assets/photos/ with EXIF and GPS
stripped, then writes one page per collection under
content/personal/photo-collections/ as a grid of thumbnails, each linking to the
larger copy. Subject tags (food, plant, cat, ...) become their own walls.

Only blocks GitBook renders natively — a table of images — so there is nothing to
install and nothing to sanitize away.
"""
import os, json, shutil, datetime, collections, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SHORT = os.path.join(HERE, "shortlist.json")
ASSETS = os.path.join(ROOT, "content", ".gitbook", "assets", "photos")
PAGES = os.path.join(ROOT, "content", "personal", "photo-collections")
REL = "../../.gitbook/assets/photos"

THUMB, FULL, COLS = 520, 1800, 3


def slug(s):
    s = re.sub(r"[^a-zA-Z0-9]+", "-", (s or "").lower()).strip("-")
    return s or "untitled"


def publish(p, idx):
    """Write thumb + full copies, stripped of metadata. Returns file names."""
    from PIL import Image
    try:
        import pillow_heif; pillow_heif.register_heif_opener()
    except Exception:
        pass
    base = "ph-%s-%03d" % (slug(p.get("collection") or p.get("place") or "misc"), idx)
    os.makedirs(ASSETS, exist_ok=True)
    with Image.open(p["path"]) as im:
        im = im.convert("RGB")            # convert() drops the EXIF block, GPS with it
        big = im.copy(); big.thumbnail((FULL, FULL), Image.LANCZOS)
        big.save(os.path.join(ASSETS, base + ".jpg"), "JPEG",
                 quality=84, optimize=True, progressive=True)
        th = im.copy(); th.thumbnail((THUMB, THUMB), Image.LANCZOS)
        th.save(os.path.join(ASSETS, base + "-t.jpg"), "JPEG",
                quality=78, optimize=True, progressive=True)
    return base + ".jpg", base + "-t.jpg"


def wall(photos, cols=COLS):
    """A grid of thumbnails; clicking one opens the larger copy."""
    rows = [photos[i:i+cols] for i in range(0, len(photos), cols)]
    head = "".join('<th></th>' for _ in range(cols))
    body = ""
    for r in rows:
        tds = ""
        for p in r:
            cap = p.get("caption") or ""
            tds += ('<td><a href="%s/%s"><img src="%s/%s" alt="%s"></a>%s</td>'
                    % (REL, p["full"], REL, p["thumb"],
                       (cap or "photo").replace('"', "'"),
                       ("<br>" + cap) if cap else ""))
        tds += "<td></td>" * (cols - len(r))
        body += "<tr>%s</tr>" % tds
    return ("<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (head, body))


def page(title, intro, sections):
    out = ["# %s" % title, ""]
    if intro:
        out += [intro, ""]
    for name, photos in sections:
        if not photos:
            continue
        if name:
            out += ["## %s" % name, ""]
        out += [wall(photos), ""]
    out += ["_Last updated: %s_" % datetime.date.today().strftime("%Y-%m"), ""]
    return "\n".join(out)


def main():
    doc = json.load(open(SHORT, encoding="utf-8"))
    photos = doc["photos"]
    if not photos:
        raise SystemExit("shortlist is empty — run ingest.py then curate.py first")

    for i, p in enumerate(photos, 1):
        p["full"], p["thumb"] = publish(p, i)

    os.makedirs(PAGES, exist_ok=True)
    by_coll = collections.defaultdict(list)
    for p in photos:
        by_coll[p.get("collection") or "Elsewhere"].append(p)

    written = []
    for coll, items in sorted(by_coll.items()):
        items.sort(key=lambda p: p.get("taken") or "")
        by_ev = collections.defaultdict(list)
        for p in items:
            by_ev[p.get("event", "")].append(p)
        secs = [(ev if ev != "undated" else "", ps) for ev, ps in sorted(by_ev.items())]
        path = os.path.join(PAGES, slug(coll) + ".md")
        open(path, "w", encoding="utf-8", newline="\n").write(
            page(coll, "", secs))
        written.append((coll, len(items), path))

    # subject walls: food, plant, cat and whatever else got tagged
    by_tag = collections.defaultdict(list)
    for p in photos:
        for t in p.get("tags", []):
            by_tag[t].append(p)
    if by_tag:
        secs = [(t.title(), sorted(ps, key=lambda p: p.get("taken") or ""))
                for t, ps in sorted(by_tag.items())]
        open(os.path.join(PAGES, "by-subject.md"), "w",
             encoding="utf-8", newline="\n").write(
            page("By subject", "The same photos, sorted by what is in them.", secs))
        written.append(("By subject", sum(len(v) for v in by_tag.values()), "by-subject.md"))

    index = ["# Photo Collections", "",
             "Where the camera has been.", ""]
    for coll, n, _ in written:
        index.append("* [%s](%s.md) — %d photos" % (coll, slug(coll), n))
    index += ["", "_Last updated: %s_" % datetime.date.today().strftime("%Y-%m"), ""]
    open(os.path.join(PAGES, "README.md"), "w", encoding="utf-8", newline="\n").write(
        "\n".join(index))

    for coll, n, _ in written:
        print("  %-22s %d photos" % (coll, n))
    print("published %d photos into %d pages" % (len(photos), len(written)))


if __name__ == "__main__":
    main()
