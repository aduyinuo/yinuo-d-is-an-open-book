#!/usr/bin/env python3
"""
Draw the collaborator map for the Research page.

    python internal/collaborators/build_map.py

Reads  places.json   — where people are, hand-editable
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
        size = 120 + 520 * (n / biggest)
        ax.scatter([p["lon"]], [p["lat"]], s=size, zorder=4,
                   c=PIN if n > 1 else PIN_SOFT, edgecolors="white", linewidths=1.2)
        if n > 1:
            ax.text(p["lon"], p["lat"], str(n), color="white", fontsize=8.5,
                    fontweight="bold", ha="center", va="center", zorder=5)

        # Labels are nudged by hand where pins sit close together.
        dx = p.get("label_dx", 0.0)
        dy = p.get("label_dy", 0.0)
        ha = p.get("label_ha", "center")
        drop = (size ** 0.5) / 9.0 + 1.6
        ax.text(p["lon"] + dx, p["lat"] - drop + dy, p["short"], color=INK,
                fontsize=9.5, ha=ha, va="top", zorder=5)
        ax.text(p["lon"] + dx, p["lat"] - drop - 2.9 + dy, p["city"], color=MUTE,
                fontsize=7.8, ha=ha, va="top", zorder=5)
        if dx or dy:
            ax.plot([p["lon"], p["lon"] + dx * 0.82],
                    [p["lat"], p["lat"] - drop * 0.35 + dy * 0.82],
                    color=MUTE, linewidth=0.6, zorder=3)

    plt.subplots_adjust(0, 0, 1, 1)
    os.makedirs(ASSETS, exist_ok=True)
    fig.savefig(OUT, transparent=True, bbox_inches="tight", pad_inches=0.1)
    plt.close(fig)


def block(places):
    total = sum(len(p["people"]) for p in places)
    rows = ["<table><thead><tr><th width=\"230\">Where</th><th>Who</th>"
            "</tr></thead><tbody>"]
    for p in sorted(places, key=lambda q: (-len(q["people"]), q["short"])):
        rows.append("<tr><td><strong>%s</strong><br><em>%s</em></td><td>%s</td></tr>"
                    % (p["institution"], p["city"], ", ".join(p["people"])))
    rows.append("</tbody></table>")
    return "\n".join([
        BEGIN, "",
        '<figure><img src="../.gitbook/assets/collaborator-map.png" '
        'alt="Where the collaborators are: %s people across %d institutions">'
        '<figcaption><p>%d people, %d institutions, four countries.</p></figcaption>'
        '</figure>' % (total, len(places), total, len(places)),
        "", "\n".join(rows), "", END])


def main():
    places = [p for p in load("places.json")["places"] if p["people"]]
    draw(places)

    text = io.open(PAGE, encoding="utf-8").read()
    new = block(places)
    if BEGIN in text and END in text:
        text = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), new, text,
                      flags=re.S)
    else:
        text = text.replace("* [ ] a map of collaborators", new, 1)
    io.open(PAGE, "w", encoding="utf-8", newline="\n").write(text)
    print("map and page written:", os.path.relpath(OUT, ROOT))


if __name__ == "__main__":
    main()
