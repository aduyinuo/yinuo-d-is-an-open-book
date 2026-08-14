#!/usr/bin/env python3
"""
Turn activity.json into the activity board image and the page that carries it.

    python internal/activity/render_board.py

Writes  content/.gitbook/assets/activity-board.png
        content/personal/what-is-she-up-to.md
"""
import os, json, time, datetime
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DATA = os.path.join(HERE, "activity.json")
ASSETS = os.path.join(ROOT, "content", ".gitbook", "assets")
BOARD = os.path.join(ASSETS, "activity-board.png")
PAGE = os.path.join(ROOT, "content", "personal", "what-is-she-up-to.md")
AVATAR = os.path.join(ASSETS, "yinuo-du.png")

D="#22452f"; M="#4a7c59"; L="#93b294"; VL="#e6efe4"; OFF="#e7ece7"
INK="#1f2430"; MUTE="#8a9199"; OCH="#a8843c"

STATE_COLOR = {"active": D, "recent": M, "idle": OFF, "unknown": OFF}
STATE_WORD  = {"active": "at the desk", "recent": "warm",
               "idle": "resting", "unknown": "not scanned"}


def ago(ts):
    if not ts:
        return "—"
    d = time.time() - ts
    if d < 3600:   return "%d minutes ago" % max(1, d // 60)
    if d < 86400:  return "%d hours ago" % (d // 3600)
    if d < 7*86400: return "%d days ago" % (d // 86400)
    return datetime.datetime.fromtimestamp(ts).strftime("%b %d")


def round_avatar(path, px=150):
    im = Image.open(path).convert("RGB")
    s = min(im.size)
    im = im.crop(((im.width-s)//2, (im.height-s)//2,
                  (im.width-s)//2+s, (im.height-s)//2+s)).resize((px, px), Image.LANCZOS)
    mask = Image.new("L", (px*4, px*4), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, px*4-1, px*4-1), fill=255)
    out = Image.new("RGBA", (px, px), (0, 0, 0, 0))
    out.paste(im, (0, 0), mask.resize((px, px), Image.LANCZOS))
    return out


def render(doc):
    items = doc["projects"]
    n = len(items)
    fig, ax = plt.subplots(figsize=(9.6, 0.86*n + 2.2), dpi=170)
    ax.set_xlim(0, 10); ax.set_ylim(-1.5, n + 0.9); ax.axis("off")

    here = doc.get("here")
    ax.text(0, n + 0.55, "What is she up to?", fontsize=16, fontweight="bold", color=D)
    sub = ("At the desk on %s" % here) if here else "Away from the desk"
    ax.text(0, n + 0.16, sub, fontsize=10.5, color=MUTE, style="italic")

    av = None
    if os.path.exists(AVATAR):
        try: av = round_avatar(AVATAR, 150)
        except Exception: av = None

    for i, it in enumerate(items):
        y = n - 1 - i
        st = it.get("state", "idle")
        ax.add_patch(FancyBboxPatch((0.9, y + 0.12), 8.9, 0.72,
                     boxstyle="round,pad=0,rounding_size=0.16",
                     fc=VL if st == "active" else "#f6f8f6", ec="none"))
        ax.add_patch(Circle((0.62, y + 0.48), 0.16, fc=STATE_COLOR.get(st, OFF),
                            ec="none", zorder=3))
        ax.text(1.15, y + 0.62, it["project"], fontsize=11,
                fontweight="bold" if st == "active" else "normal", color=D, va="center")
        ax.text(1.15, y + 0.30, it["thread"], fontsize=8.4, color=MUTE, va="center")
        what = it.get("what") or "nothing recorded yet"
        ax.text(4.15, y + 0.62, what[:74], fontsize=9.2, color=INK, va="center")
        ax.text(4.15, y + 0.30, "%s · %s" % (STATE_WORD.get(st, st), ago(it.get("at"))),
                fontsize=8.4, color=OCH if st == "active" else MUTE, va="center")
        if st == "active" and av is not None:
            ax.add_artist(AnnotationBbox(OffsetImage(av, zoom=0.20),
                          (0.30, y + 0.48), frameon=False, zorder=4))

    stamp = datetime.datetime.fromtimestamp(doc.get("generated", time.time()))
    ax.text(0, -1.0, "last looked at %s · each row is the most recent piece of real work, "
            "not a count of events" % stamp.strftime("%b %d, %H:%M"),
            fontsize=8.2, color=MUTE)
    plt.tight_layout()
    os.makedirs(ASSETS, exist_ok=True)
    fig.savefig(BOARD, transparent=True, bbox_inches="tight", pad_inches=0.16)
    plt.close(fig)


def write_page(doc):
    here = doc.get("here")
    lines = ["---", "description: An Activity Board...", "---", "",
             "# What is she up to?", ""]
    lines.append("At the desk on **%s**." % here if here
                 else "Away from the desk right now.")
    lines.append("")
    lines.append('<figure><img src="../.gitbook/assets/activity-board.png" '
                 'alt="Activity board: each project with the last piece of work on it">'
                 '<figcaption><p>Where the work actually is.</p></figcaption></figure>')
    lines.append("")
    lines.append("<table><thead><tr><th width=\"170\">Project</th>"
                 "<th width=\"120\">State</th><th>Last piece of work</th></tr></thead><tbody>")
    for it in doc["projects"]:
        st = it.get("state", "idle")
        link = '<a href="../%s">%s</a>' % (it["page"], it["project"]) if it.get("page") else it["project"]
        mark = {"active": "at the desk", "recent": "warm",
                "idle": "resting", "unknown": "not scanned"}.get(st, st)
        what = it.get("what") or "—"
        lines.append("<tr><td>%s<br><em>%s</em></td><td>%s</td><td>%s<br><em>%s</em></td></tr>"
                     % (link, it["thread"], mark, what, ago(it.get("at"))))
    lines.append("</tbody></table>")
    lines.append("")
    site = doc.get("site") or []
    if site:
        lines.append("## What changed on this site")
        lines.append("")
        for s in site[:8]:
            lines.append("* **%s** — %s" % (ago(s["at"]), s["what"]))
        lines.append("")
    lines.append("_Last updated: %s_" %
                 datetime.datetime.fromtimestamp(doc.get("generated", time.time())).strftime("%Y-%m"))
    lines.append("")
    open(PAGE, "w", encoding="utf-8", newline="\n").write("\n".join(lines))


def main():
    if not os.path.exists(DATA):
        raise SystemExit("No activity.json yet. Run collect_activity.py first.")
    doc = json.load(open(DATA, encoding="utf-8"))
    render(doc)
    write_page(doc)
    print("board and page written")


if __name__ == "__main__":
    main()
