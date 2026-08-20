#!/usr/bin/env python3
"""
Collect what is actually being worked on, and write it to activity.json.

Runs on the machine that can see the research folders (Windows, G: drive).
Per project it records the sentence about what changed, the hours logged, the
daily tally the heatmap is drawn from, and where you are sitting right now.

    python internal/activity/collect_activity.py

Refuses to write when the research root is missing, rather than publishing a
board of blanks.
"""
import os, re, json, time, datetime, subprocess, sys

from config import HERE, ROOT, load, path_of, watched, excluded
import clockify

OUT = os.path.join(HERE, "activity.json")
UPDATES = os.path.join(HERE, "updates.json")

SKIP_DIR = {".git", ".ipynb_checkpoints", "__pycache__", "node_modules",
            ".Rproj.user", "venv", ".venv", "CFP", "Package", "AuthorKit27",
            "samples", "Overleaf", "results", "models", "checkpoints",
            "wandb", "runs", "site-packages", "Templates"}
NOISE_PATH = re.compile(
    r"(LaTeX2e\+|Proceedings\+Templates|AuthorKit|[\\/]CFP[\\/]|Literature|"
    r"Templates?|sample-|splncs|llncs|acmart)", re.I)
SKIP_FILE = re.compile(
    r"(^~\$|^\.|desktop\.ini$|\.lnk$|\.Rhistory$|\.DS_Store$|"
    r"\.(aux|log|out|toc|synctex\.gz|bbl|blg|fls|fdb_latexmk|tmp|bak|"
    r"pth|ckpt|pt|h5|npz|zip|cls|bst|sty)$)", re.I)

DAY = 86400


def scan(folder, project=None, horizon_days=400):
    """(newest mtime, {day: touches}) for the real working files under folder."""
    newest, days = None, {}
    cutoff = time.time() - horizon_days * DAY
    for dirpath, dirnames, files in os.walk(folder):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIR]
        for f in files:
            if SKIP_FILE.search(f):
                continue
            p = os.path.join(dirpath, f)
            if NOISE_PATH.search(p):
                continue
            if project and excluded(project, os.path.relpath(p, folder)):
                continue
            try:
                m = os.path.getmtime(p)
            except OSError:
                continue
            if m < cutoff:
                continue
            if newest is None or m > newest:
                newest = m
            d = datetime.date.fromtimestamp(m).isoformat()
            days[d] = days.get(d, 0) + 1
    return newest, days


def git_recent(days=21):
    try:
        out = subprocess.run(
            ["git", "log", "--since=%d days ago" % days, "--no-merges",
             "--pretty=%at|%s"], cwd=ROOT, capture_output=True, text=True,
            timeout=60).stdout.strip()
    except Exception:
        return []
    items = []
    for line in out.split("\n"):
        if "|" not in line:
            continue
        ts, subj = line.split("|", 1)
        if subj.startswith("GITBOOK-"):
            continue
        items.append({"at": int(ts), "what": subj.strip()})
    return items


def main():
    doc = load()
    root = doc["research_root"]
    if not os.path.isdir(root):
        print("Cannot see the research folder:\n  %s\n"
              "Nothing written. The last good board is left alone.\n"
              "Fix the folder in the settings window and run this again." % root,
              file=sys.stderr)
        raise SystemExit(2)

    updates = {}
    if os.path.exists(UPDATES):
        try:
            updates = json.load(open(UPDATES, encoding="utf-8")).get("projects", {})
        except Exception:
            pass
    logged = clockify.entries(clockify.key())

    now = time.time()
    entries = []
    for p in watched(doc):
        folder = path_of(doc, p)
        u = updates.get(p["folder"], {})
        rows = logged.get(p.get("clockify") or "", [])

        if not os.path.isdir(folder):
            entries.append({**_base(p), "state": "missing", "at": None,
                            "update": "", "details": [], "days": {},
                            "hours_week": 0.0, "hours_total": 0.0})
            continue

        newest, days = scan(folder, p)

        hours = {}
        for e in rows:
            hours[e["day"]] = round(hours.get(e["day"], 0.0) + e["hours"], 2)
            if newest is None or e["at"] > newest:
                newest = e["at"]
        week_ago = (datetime.date.today() - datetime.timedelta(days=7)).isoformat()

        at = u.get("at") or newest
        entries.append({
            **_base(p),
            "at": int(at) if at else None,
            "state": ("active" if at and (now - at) < 6 * 3600 else
                      "recent" if at and (now - at) < 7 * DAY else "idle"),
            "update": u.get("headline", ""),
            "details": u.get("details", []),
            "days": days,
            "hours": hours,
            "hours_week": round(sum(v for d, v in hours.items() if d >= week_ago), 1),
            "hours_total": round(sum(hours.values()), 1),
        })

    entries.sort(key=lambda e: e["at"] or 0, reverse=True)
    live = [e for e in entries if e["state"] == "active"]
    out = {
        "generated": int(now),
        "here": live[0]["name"] if live else None,
        "here_folder": live[0]["folder"] if live else None,
        "range": doc.get("heatmap_range", "6m"),
        "projects": entries,
        "site": git_recent(),
    }
    json.dump(out, open(OUT, "w", encoding="utf-8", newline="\n"),
              ensure_ascii=False, indent=2)
    print("wrote", os.path.relpath(OUT, ROOT))
    for e in entries:
        when = (datetime.datetime.fromtimestamp(e["at"]).strftime("%m-%d %H:%M")
                if e["at"] else "—")
        print("  %-34s %-8s %s  %s" % (e["name"][:34], e["state"], when,
                                       (e["update"] or "")[:44]))


def _base(p):
    return {"folder": p["folder"], "name": p["name"], "thread": p.get("thread", ""),
            "group": p.get("group", ""), "page": p.get("page", ""),
            "heatmap": p.get("heatmap", True)}


if __name__ == "__main__":
    main()
