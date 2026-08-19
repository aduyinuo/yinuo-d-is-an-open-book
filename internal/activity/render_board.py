#!/usr/bin/env python3
"""
Turn activity.json into the heatmaps and the page that carries them.

    python internal/activity/render_board.py

Writes  content/.gitbook/assets/activity-heatmap.png
        content/.gitbook/assets/heat-<project>.png
        content/personal/what-is-she-up-to.md
"""
import os, re, json, time, datetime

from config import HERE, ROOT, load
import heatmap

DATA = os.path.join(HERE, "activity.json")
ASSETS = os.path.join(ROOT, "content", ".gitbook", "assets")
BIG = os.path.join(ASSETS, "activity-heatmap.png")
PAGE = os.path.join(ROOT, "content", "personal", "what-is-she-up-to.md")

STATE_WORD = {"active": "at the desk", "recent": "warm", "idle": "resting",
              "missing": "folder missing"}


def ago(ts):
    if not ts:
        return "—"
    d = time.time() - ts
    if d < 3600:
        return "%d minutes ago" % max(1, d // 60)
    if d < 86400:
        return "%d hours ago" % (d // 3600)
    if d < 7 * 86400:
        return "%d days ago" % (d // 86400)
    return datetime.datetime.fromtimestamp(ts).strftime("%b %d")


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:48]


def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main():
    if not os.path.exists(DATA):
        raise SystemExit("No activity.json yet. Run collect_activity.py first.")
    doc = json.load(open(DATA, encoding="utf-8"))
    cfg = load()
    rng = doc.get("range", "6m")
    custom = cfg.get("heatmap_custom")
    projects = doc["projects"]

    ticked = [p for p in projects if p.get("heatmap", True)]
    total = heatmap.draw(ticked, BIG, rng, custom, title=None)

    lines = ["---", "description: What I am working on, and what changed.", "---", "",
             "# What is she up to?", ""]
    here = doc.get("here")
    lines.append("At the desk on **%s**." % esc(here) if here
                 else "Away from the desk right now.")
    lines += ["", '<figure><img src="../.gitbook/assets/activity-heatmap.png" '
              'alt="Daily activity across projects"><figcaption><p>%s</p></figcaption>'
              '</figure>' % heatmap.legend_line(total, rng, custom), ""]

    group_of = {}
    for p in projects:
        group_of.setdefault(p.get("group") or "Other", []).append(p)
    order = sorted(group_of, key=lambda g: -max(
        (q["at"] or 0) for q in group_of[g]))

    for g in order:
        rows = sorted(group_of[g], key=lambda q: q["at"] or 0, reverse=True)
        thread = rows[0].get("thread") or g
        lines += ["## %s" % esc(thread), ""]
        for p in rows:
            lines += _project(p, rng, custom)
        lines.append("")

    site = doc.get("site") or []
    if site:
        lines += ["## What changed on this site", ""]
        for s in site[:8]:
            lines.append("* **%s** — %s" % (ago(s["at"]), esc(s["what"])))
        lines.append("")

    lines.append("_Last looked at %s_" % datetime.datetime.fromtimestamp(
        doc.get("generated", time.time())).strftime("%b %d, %H:%M"))
    lines.append("")
    open(PAGE, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
    print("heatmaps and page written")


def _project(p, rng, custom):
    state = p.get("state", "idle")
    head = p.get("update") or ("nothing recorded yet" if state != "missing"
                               else "the folder is not where it was")
    bits = [STATE_WORD.get(state, state), ago(p.get("at"))]
    if p.get("hours_week"):
        bits.append("%sh this week" % p["hours_week"])
    summary = "%s — %s" % (esc(p["name"]), esc(head))

    out = ["<details>", "", "<summary>%s</summary>" % summary, ""]
    out.append("_%s_" % " · ".join(bits))
    out.append("")

    if (p.get("days") or p.get("hours")) and state != "missing":
        mini = os.path.join(ASSETS, "heat-%s.png" % slug(p["name"]))
        heatmap.draw([p], mini, rng, custom, cell=7, gap=2, labels=False)
        out += ['<figure><img src="../.gitbook/assets/heat-%s.png" alt="Daily work on %s">'
                '<figcaption></figcaption></figure>' % (slug(p["name"]), esc(p["name"])), ""]

    for d in p.get("details", [])[:6]:
        out.append("* **%s** — %s" % (ago(d["at"]), esc(d["what"])))
    if p.get("hours_total"):
        out.append("* %s hours logged in this window" % p["hours_total"])
    if p.get("page"):
        out += ["", "[%s](../%s)" % (esc(p.get("thread") or "the project page"), p["page"])]
    out += ["", "</details>", ""]
    return out


if __name__ == "__main__":
    main()
