#!/usr/bin/env python3
"""
Turn the captured diffs into sentences about what changed.

Order of authority, strongest first:
  1. what you typed into Clockify for that project
  2. what you typed into the popup
  3. what the diff itself says — new sections, new citations, new functions
  4. the file was touched and could not be read

Never a count of events, files or bytes.

    python internal/activity/summarize_changes.py   ->  updates.json
"""
import os, re, json, time

from config import HERE, load, watched
import clockify

CHANGES = os.path.join(HERE, "changes.json")
ANSWERS = os.path.join(HERE, "answers.json")
OUT = os.path.join(HERE, "updates.json")


def _join(bits, limit=3):
    bits = [b for b in bits if b][:limit]
    if not bits:
        return ""
    if len(bits) == 1:
        return bits[0]
    return ", ".join(bits[:-1]) + " and " + bits[-1]


def _names(lines, pattern, group=1):
    out = []
    for ln in lines:
        for m in re.finditer(pattern, ln, re.M):
            v = (m.group(group) or "").strip()
            if v and v not in out:
                out.append(v)
    return out


def clause(f):
    """One clause about one changed file, or "" when nothing can be said."""
    name = f["file"]
    ext = os.path.splitext(name)[1].lower()
    add, rem = f.get("added", []), f.get("removed", [])

    if f.get("how") == "deleted":
        return "removed %s" % os.path.basename(name)

    if f.get("how") == "created" and ext in (".tex", ".md", ".txt"):
        return "added %s" % _stem(name)          # not every heading inside it

    if ext in (".tex", ".md", ".txt"):
        bits = []
        heads = (_names(add, r"\\(?:sub)*section\*?\{([^}]{2,60})\}") +
                 _names(add, r"^#{1,4}\s+(.{2,60})$"))
        if heads:
            bits.append("opened %s" % _join(["the %s section" % h for h in heads], 2))
        cites = []
        for key in _names(add, r"\\cite[tp]?\*?\{([^}]+)\}"):
            cites += [k.strip() for k in key.split(",") if k.strip()]
        old = set()
        for key in _names(rem, r"\\cite[tp]?\*?\{([^}]+)\}"):
            old |= {k.strip() for k in key.split(",")}
        fresh = [c for c in dict.fromkeys(cites) if c not in old]
        if fresh:
            bits.append("brought in %s" % _join([_citename(c) for c in fresh], 2))
        figs = _names(add, r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")
        if figs:
            bits.append("dropped in %s" % _join([os.path.basename(g) for g in figs], 2))
        if not bits:
            prose = [l for l in add if len(l) > 40 and not l.startswith("%")]
            if prose and len(prose) > len([l for l in rem if len(l) > 40]):
                bits.append("wrote into %s" % _stem(name))
            elif add or rem:
                bits.append("reworked %s" % _stem(name))
        return _join(bits)

    if ext in (".py", ".r", ".jl", ".js", ".sh", ".ipynb"):
        pat = r"^\s*(?:def|class)\s+([A-Za-z_]\w*)|^\s*([A-Za-z_]\w*)\s*<-\s*function"
        new = [n for n in _names(add, pat) if n]
        new += [n for n in _names(add, pat, 2) if n]
        gone = [n for n in _names(rem, pat) if n]
        gone += [n for n in _names(rem, pat, 2) if n]
        new = [n for n in dict.fromkeys(new) if n not in gone]
        gone = [n for n in dict.fromkeys(gone) if n not in new]
        bits = []
        if new:
            bits.append("added %s" % _join(["%s()" % n for n in new], 2))
        if gone:
            bits.append("dropped %s" % _join(["%s()" % n for n in gone], 2))
        if not bits and (add or rem):
            bits.append("reworked %s" % _stem(name))
        return _join(bits)

    if ext == ".bib":
        keys = _names(add, r"^@\w+\{([^,]+),")
        if keys:
            return "added %s to the bibliography" % _join(keys, 2)
        return "edited the bibliography" if (add or rem) else ""

    if ext in (".csv", ".tsv", ".json", ".parquet"):
        verb = "results landed in" if f.get("how") == "created" else "refreshed"
        return "%s %s" % (verb, os.path.basename(name))

    if ext in (".pptx", ".ppt", ".key"):
        return "edited the slides %s" % os.path.basename(name)
    if ext in (".docx", ".doc"):
        return "edited the document %s" % os.path.basename(name)
    if ext == ".pdf":
        return "%s %s" % ("added" if f.get("how") == "created" else "replaced",
                          os.path.basename(name))
    if ext in (".png", ".jpg", ".jpeg", ".svg", ".gif", ".webp"):
        return "%s the figure %s" % ("added" if f.get("how") == "created" else "redrew",
                                     os.path.basename(name))
    return ""


def _stem(name):
    s = os.path.splitext(os.path.basename(name))[0]
    return s.replace("_", " ").replace("-", " ")


def _citename(key):
    m = re.match(r"([A-Za-z]+)(\d{4})", key)
    return "%s %s" % (m.group(1).capitalize(), m.group(2)) if m else key


def main():
    doc = load()
    changes = {}
    if os.path.exists(CHANGES):
        blob = json.load(open(CHANGES, encoding="utf-8"))
        changes = {p["folder"]: p for p in blob.get("projects", [])}
    answers = {}
    if os.path.exists(ANSWERS):
        try:
            answers = json.load(open(ANSWERS, encoding="utf-8"))
        except Exception:
            answers = {}
    hours = clockify.entries(clockify.key())

    out = {}
    for p in watched(doc):
        folder = p["folder"]
        ch = changes.get(folder)
        details, unnamed = [], []
        if ch:
            for f in ch["files"][:12]:
                c = clause(f)
                if c:
                    details.append({"at": int(f["at"]), "what": c})
                else:
                    unnamed.append(f["file"])

        logged = hours.get(p.get("clockify") or "", [])
        for e in logged[:6]:
            if e["what"]:
                details.append({"at": e["at"], "what": "logged %.1fh — %s"
                                % (e["hours"], e["what"])})

        details.sort(key=lambda d: d["at"], reverse=True)

        headline = ""
        if answers.get(folder, {}).get("text"):
            headline = answers[folder]["text"]
        elif any(e["what"] for e in logged):
            # the most recent entry you actually typed something into
            headline = next(e["what"] for e in logged if e["what"])
        elif details:
            headline = details[0]["what"]

        # The window of real work this run picked up, from the file timestamps.
        stamps = [int(f["at"]) for f in (ch["files"] if ch else [])]
        window = {"from": min(stamps), "to": max(stamps)} if stamps else None

        # Ask when work happened and Clockify has nothing covering it. That is
        # the case Max named: prompt when he is not actively logging.
        covered = bool(window) and any(
            e["at"] >= window["from"] - 3600 for e in logged)
        out[folder] = {
            "headline": headline,
            "details": details[:6],
            "needs_asking": bool(window) and not covered,
            "unnamed": (unnamed or [f["file"] for f in (ch["files"] if ch else [])])[:6],
            "guess": headline if not covered else "",
            "clockify": p.get("clockify", ""),
            "name": p["name"],
            "window": window,
            "at": max([d["at"] for d in details], default=None),
        }

    json.dump({"at": int(time.time()), "projects": out},
              open(OUT, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    named = sum(1 for v in out.values() if v["headline"])
    ask = sum(1 for v in out.values() if v["needs_asking"])
    print("%d project(s) with a sentence, %d needing you" % (named, ask))


if __name__ == "__main__":
    main()
