#!/usr/bin/env python3
"""
Step 3: write the four opportunity pages.

    python internal/opportunities/build_pages.py

Reads scored.json and writes content/overview-4/*.md. Each row carries its
deadline, how many days are left, the fit score with the terms that produced it,
and the source it was read from.
"""
import os, io, json, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
PAGES = os.path.join(ROOT, "content", "overview-4")

STREAMS = {
    "conferences": ("conference-deadlines.md", "Conference deadlines", "calendar-days",
                    "Call-for-papers deadlines, soonest first."),
    "funding": ("funding-opportunities.md", "Funding opportunities", "sack-dollar",
                "Open and forecasted calls."),
    "jobs": ("postdoc-faculty-opportunities.md", "Postdoc/faculty opportunities",
             "user-tie", "Positions posted at institutions hiring in this area."),
    "micro": ("micro-opportunities.md", "Micro opportunities", "seedling",
              "Credits, small grants, travel awards and targeted programs."),
}

CONFIDENCE = {"stated": "", "parsed": " (read off the listing)",
              "unknown": " (no date given)"}


def esc(s):
    s = (s or "").replace("&amp;", "&")          # feeds arrive already escaped
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def urgency(days):
    if days is None:
        return "—"
    if days == 0:
        return "**today**"
    if days < 0:
        return "closed"
    if days <= 7:
        return "**%d days**" % days
    if days <= 30:
        return "%d days" % days
    return "%d days" % days


def row_html(r):
    title = esc(r["title"])[:150]
    link = '<a href="%s">%s</a>' % (r["url"], title) if r["url"] else title
    why = ", ".join(r["why"][:4]) or "no profile term matched"
    if r["against"]:
        why += " · against: " + ", ".join(r["against"][:2])
    return ("<tr><td>%s</td><td>%s%s</td><td>%s</td><td>%s</td>"
            "<td><em>%s</em></td></tr>"
            % (link,
               r["deadline"] or "—",
               CONFIDENCE.get(r.get("deadline_confidence", ""), ""),
               urgency(r["days_left"]), r["score"], esc(why)))


def page(stream, rows, doc):
    fname, title, icon, lede = STREAMS[stream]
    out = ["---", "description: Refreshed daily by the opportunity scout.",
           "icon: %s" % icon, "---", "", "# %s" % title, "", lede, ""]

    dated = [r for r in rows if r["days_left"] is not None]
    undated = [r for r in rows if r["days_left"] is None]

    if dated:
        soon = sorted([r for r in dated if r["days_left"] <= 30],
                      key=lambda r: (-r["score"], r["days_left"]))
        if soon:
            out += ["## Within a month", "",
                    "<table><thead><tr><th width=\"330\">What</th>"
                    "<th width=\"150\">Deadline</th><th width=\"90\">Left</th>"
                    "<th width=\"60\">Fit</th><th>Why it scored</th></tr></thead><tbody>"]
            out += [row_html(r) for r in soon]
            out += ["</tbody></table>", ""]
        later = sorted([r for r in dated if r["days_left"] > 30],
                       key=lambda r: (-r["score"], r["days_left"]))
        if later:
            out += ["## Later", "",
                    "<table><thead><tr><th width=\"330\">What</th>"
                    "<th width=\"150\">Deadline</th><th width=\"90\">Left</th>"
                    "<th width=\"60\">Fit</th><th>Why it scored</th></tr></thead><tbody>"]
            out += [row_html(r) for r in later]
            out += ["</tbody></table>", ""]

    if undated:
        undated = sorted(undated, key=lambda r: -r["score"])
        out += ["## No date given", "",
                "Ranked by fit alone. A missing deadline is reported as missing "
                "rather than guessed at.", "",
                "<table><thead><tr><th width=\"430\">What</th><th width=\"60\">Fit</th>"
                "<th>Why it scored</th></tr></thead><tbody>"]
        for r in undated:
            title_ = esc(r["title"])[:150]
            link = '<a href="%s">%s</a>' % (r["url"], title_) if r["url"] else title_
            why = ", ".join(r["why"][:4]) or "no profile term matched"
            out.append("<tr><td>%s</td><td>%s</td><td><em>%s</em></td></tr>"
                       % (link, r["score"], esc(why)))
        out += ["</tbody></table>", ""]

    if not rows:
        out += ["Nothing open in this stream today.", ""]

    out += ["---", "",
            "_Fit is the sum of the profile terms that appear in the listing; "
            "the terms are shown so the number can be argued with. Nothing is "
            "hidden for scoring low._", "",
            "_Last refreshed %s_" % datetime.datetime.fromtimestamp(
                doc["scored"]).strftime("%b %d, %H:%M"), ""]
    return fname, "\n".join(out)


def main():
    with io.open(os.path.join(HERE, "scored.json"), encoding="utf-8") as fh:
        doc = json.load(fh)
    os.makedirs(PAGES, exist_ok=True)
    for stream in STREAMS:
        rows = doc["streams"].get(stream, [])
        fname, text = page(stream, rows, doc)
        with io.open(os.path.join(PAGES, fname), "w", encoding="utf-8",
                     newline="\n") as fh:
            fh.write(text)
        print("  %-34s %4d rows" % (fname, len(rows)))

    index = ["---", "description: Refreshed daily by the opportunity scout.",
             "icon: arrow-pointer", "---", "", "# Opportunities", "",
             "Four queues, refreshed daily from %d sources. Ranked, not filtered: "
             "everything found is listed, with the reason it scored where it did."
             % len(set(r["source"] for rows in doc["streams"].values() for r in rows)),
             ""]
    for stream, (fname, title, _i, lede) in STREAMS.items():
        rows = doc["streams"].get(stream, [])
        soon = sum(1 for r in rows if r["days_left"] is not None and r["days_left"] <= 30)
        index.append("* [%s](%s) — %d open, %d closing within a month"
                     % (title, fname, len(rows), soon))
    index += ["", "_Last refreshed %s_" % datetime.datetime.fromtimestamp(
        doc["scored"]).strftime("%b %d, %H:%M"), ""]
    with io.open(os.path.join(PAGES, "README.md"), "w", encoding="utf-8",
                 newline="\n") as fh:
        fh.write("\n".join(index))
    print("  README.md")


if __name__ == "__main__":
    main()
