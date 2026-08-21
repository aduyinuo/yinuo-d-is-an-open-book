#!/usr/bin/env python3
"""
Draw the collaborator map for the Research page.

    python internal/collaborators/build_map.py

Reads  people.json   — everyone the site names, and where they are
       places.json   — the institutions and their coordinates
       world.json    — land outlines, Natural Earth 110m (public domain)
Writes content/.gitbook/assets/collaborator-map.png
       and the map block on content/research/overview.md

Equirectangular projection, cropped to the places that actually have someone in
them, so the map is of Max's collaborations rather than of the whole planet.
"""
import os, io, json, re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
ASSETS = os.path.join(ROOT, "content", ".gitbook", "assets")
OUT = os.path.join(ASSETS, "collaborator-map.png")
PAGE = os.path.join(ROOT, "content", "research", "overview.md")

LAND = "#e8ece8"
EDGE = "#d3d9d3"
PIN = "#22452f"
PIN_SOFT = "#4a7c59"
INK = "#1f2430"
MUTE = "#8a9199"

BEGIN = "<!-- collaborator-map -->"
END = "<!-- /collaborator-map -->"


def load(name):
    with io.open(os.path.join(HERE, name), encoding="utf-8") as fh:
        return json.load(fh)


def draw(places, pad=13.0):
    import math
    lons = [p["lon"] for p in places]
    lats = [p["lat"] for p in places]
    x0, x1 = min(lons) - pad * 1.3, max(lons) + pad * 1.3
    y0, y1 = min(lats) - pad * 1.7, max(lats) + pad * 1.2
    y0, y1 = max(y0, -58), min(y1, 82)

    # Plate carrée squashes longitude by cos(latitude). Stretching the vertical
    # by 1/cos(mean lat) puts the shapes back to roughly the right proportions,
    # and keeps the pins round rather than oval.
    mean_lat = math.radians((y0 + y1) / 2.0)
    aspect = 1.0 / max(0.35, math.cos(mean_lat))

    width = 10.0
    fig, ax = plt.subplots(
        figsize=(width, width * (y1 - y0) * aspect / (x1 - x0)), dpi=170)
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)
    ax.axis("off")
    ax.set_aspect(aspect)

    for ring in load("world.json"):
        xs = [c[0] for c in ring]
        ys = [c[1] for c in ring]
        if max(xs) < x0 or min(xs) > x1 or max(ys) < y0 or min(ys) > y1:
            continue
        ax.fill(xs, ys, facecolor=LAND, edgecolor=EDGE, linewidth=0.5, zorder=1)

    biggest = max(len(p["people"]) for p in places) or 1
    for p in places:
        n = len(p["people"])
        p["_size"] = 120 + 520 * (n / biggest)
        ax.scatter([p["lon"]], [p["lat"]], s=p["_size"], zorder=4,
                   c=PIN if n > 1 else PIN_SOFT, edgecolors="white", linewidths=1.2)
        if n > 1:
            ax.text(p["lon"], p["lat"], str(n), color="white", fontsize=8.5,
                    fontweight="bold", ha="center", va="center", zorder=5)

    for p, (lx, ly, ha) in zip(places, _place_labels(places, x0, x1, y0, y1, aspect)):
        drop = 0.0 if (lx, ly) != (p["lon"], p["lat"]) else 0.0
        ax.text(lx, ly, p["short"], color=INK, fontsize=9.5, ha=ha, va="top",
                zorder=5)
        ax.text(lx, ly - 2.9, p["city"], color=MUTE, fontsize=7.8, ha=ha,
                va="top", zorder=5)
        edge = lx + (0.6 if ha == "left" else -0.6 if ha == "right" else 0)
        if abs(lx - p["lon"]) > 1.5 or abs(ly - p["lat"]) > 4.5:
            ax.plot([p["lon"], edge], [p["lat"], ly - 0.9], color=MUTE,
                    linewidth=0.6, zorder=3)

    plt.subplots_adjust(0, 0, 1, 1)
    os.makedirs(ASSETS, exist_ok=True)
    fig.savefig(OUT, transparent=True, bbox_inches="tight", pad_inches=0.1)
    plt.close(fig)


ROLE_ORDER = {"collaborator": 0, "co-author": 1, "mentee": 2}


def block(places):
    total = sum(len(p["people"]) for p in places)
    countries = {p["city"].rsplit(",", 1)[-1].strip() for p in places}
    rows = ["<table><thead><tr><th width=\"230\">Where</th><th>Who</th>"
            "</tr></thead><tbody>"]
    for p in sorted(places, key=lambda q: (-len(q["people"]), q["short"])):
        who = sorted(p["people"],
                     key=lambda x: (ROLE_ORDER.get(x.get("role"), 9), x["name"]))
        rows.append("<tr><td><strong>%s</strong><br><em>%s</em></td><td>%s</td></tr>"
                    % (p["institution"], p["city"],
                       ", ".join(x["name"] for x in who)))
    rows.append("</tbody></table>")
    return "\n".join([
        BEGIN, "",
        '<figure><img src="../.gitbook/assets/collaborator-map.png" '
        'alt="Where the collaborators are: %s people across %d institutions">'
        '<figcaption><p>%d people, %d institutions, %d countries.</p></figcaption>'
        '</figure>' % (total, len(places), total, len(places), len(countries)),
        "", "\n".join(rows), "", END])


def gather():
    """Attach people to places. Anyone unplaced is reported, never dropped."""
    places = {p["institution"]: dict(p, people=[])
              for p in load("places.json")["places"]}
    unplaced, unknown = [], set()
    for person in load("people.json")["people"]:
        inst = person.get("institution") or ""
        if inst in places:
            places[inst]["people"].append(person)
        else:
            unplaced.append(person)
            if inst:
                unknown.add(inst)
    return ([p for p in places.values() if p["people"]], unplaced, sorted(unknown))


def main():
    places, unplaced, unknown = gather()
    draw(places)

    text = io.open(PAGE, encoding="utf-8").read()
    new = block(places)
    for inst in unknown:
        print("  no place for institution: %s" % inst)
    for person in unplaced:
        print("  no affiliation: %s (%s)" % (person["name"], person.get("role", "")))
    if BEGIN in text and END in text:
        text = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), new, text,
                      flags=re.S)
    else:
        text = text.replace("* [ ] a map of collaborators", new, 1)
    io.open(PAGE, "w", encoding="utf-8", newline="\n").write(text)
    print("map and page written:", os.path.relpath(OUT, ROOT))



def _place_labels(places, x0, x1, y0, y1, aspect):
    """Put each label somewhere it does not sit on another label or pin.

    Hand-nudging every label stops working as soon as a cluster like the
    northeast corridor appears. Each place gets tried against a ring of
    candidate offsets; the first that collides with nothing already placed
    wins. An explicit label_dx / label_dy in places.json overrides all of it.
    """
    span = x1 - x0
    char = span * 0.0062                     # rough width of one character
    line = span * 0.011 / aspect             # rough height of one text line

    def box_at(p, dx, dy, ha):
        w = max(len(p["short"]), len(p["city"])) * char
        left = dx - (0 if ha == "left" else w if ha == "right" else w / 2)
        return (p["lon"] + left, p["lat"] + dy - line * 2.6,
                p["lon"] + left + w, p["lat"] + dy)

    def hits(b, taken):
        return any(not (b[2] < o[0] or b[0] > o[2] or b[3] < o[1] or b[1] > o[3])
                   for o in taken)

    order = sorted(range(len(places)), key=lambda i: -len(places[i]["people"]))
    out = [None] * len(places)
    taken = [(p["lon"] - 1.6, p["lat"] - 1.6, p["lon"] + 1.6, p["lat"] + 1.6)
             for p in places]                # the pins themselves

    for i in order:
        p = places[i]
        drop = (p.get("_size", 300) ** 0.5) / 9.0 + 1.6
        if "label_dx" in p or "label_dy" in p:
            cands = [(p.get("label_dx", 0.0), -drop + p.get("label_dy", 0.0),
                      p.get("label_ha", "center"))]
        else:
            cands = [(0, -drop, "center"), (2.6, -drop + 1.2, "left"),
                     (-2.6, -drop + 1.2, "right"), (0, drop + line * 2.6, "center"),
                     (7.0, -drop + 2.0, "left"), (-7.0, -drop + 2.0, "right"),
                     (12.0, 2.0, "left"), (-12.0, 2.0, "right"),
                     (12.0, -8.0, "left"), (-12.0, -8.0, "right"),
                     (0, -drop - 9.0, "center"), (0, drop + 12.0, "center")]
        for dx, dy, ha in cands:
            b = box_at(p, dx, dy, ha)
            if not hits(b, taken):
                break
        taken.append(b)
        out[i] = (p["lon"] + dx, p["lat"] + dy, ha)
    return out

if __name__ == "__main__":
    main()
