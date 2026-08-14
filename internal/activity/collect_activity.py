#!/usr/bin/env python3
"""
Collect what is actually being worked on, and write it to activity.json.

Runs on the machine that can see the research folders (Windows, G: drive).
It records, per project, the most recent piece of real work: the file that
changed, what kind of work that file represents, and when. No event counts,
no byte totals.

    python internal/activity/collect_activity.py

Writes internal/activity/activity.json, which render_board.py turns into the
board and the page.
"""
import os, re, json, time, datetime, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "activity.json")

RESEARCH = os.environ.get(
    "RESEARCH_ROOT",
    r"G:\Other computers\My Mac\[2025-2026][postdoc][utep]\[2] Research Projects")

# folder on disk -> the project as it is named on the site, and its page
PROJECTS = [
    ("2025-2026 LucidWorld",   "LucidWorld",     "Cyber World Modeling",
     "overview/3-year-agenda/cyber-world-modeling/"),
    ("2025-2026 PickYourBattles", "PickYourBattles", "Cyber World Modeling",
     "overview/3-year-agenda/cyber-world-modeling/next.md"),
    ("2025-2026 DesignTheGame", "DesignTheGame", "Mental World Modeling",
     "overview/3-year-agenda/mental-world-modeling/problem-solving/"),
    ("2022-2026 ReadTheRoom",  "ReadTheRoom",    "Mental World Modeling",
     "overview/3-year-agenda/mental-world-modeling/opponent-agent-modeling/"),
    ("2025-2026 UnitedForces", "UnitedForces",   "Human-AI Complementarity",
     "overview/3-year-agenda/human-ai-complementarity/"),
    ("2026 BeRealistic",       "BeRealistic",    "Toward Deployment",
     "overview/3-year-agenda/toward-deployment/"),
    ("IRB Applications",       "IRB",            "Across threads",
     "overview/3-year-agenda/"),
    ("RESEARCH STATEMENT",     "Research statement", "Across threads",
     "research/overview.md"),
]

# what a file says about the kind of work, in plain language
KIND = [
    (r"\.(tex|rmd|md|docx?|txt)$",      "writing"),
    (r"\.(py|ipynb|r|jl|sh|yaml|yml)$", "code"),
    (r"\.(csv|tsv|json|parquet|sav)$",  "data"),
    (r"\.(pptx?|key)$",                 "slides"),
    (r"\.(pdf)$",                       "reading"),
    (r"\.(png|jpe?g|svg|gif)$",         "figures"),
    (r"\.(bib)$",                       "references"),
]

SKIP_DIR = {".git", ".ipynb_checkpoints", "__pycache__", "node_modules",
            ".Rproj.user", "venv", ".venv", "CFP", "Package", "AuthorKit27",
            "samples", "Overleaf", "results", "models", "images", "checkpoints",
            "wandb", "runs", "site-packages", "Templates"}

# Paths that are somebody else's material rather than your writing: conference
# templates, downloaded papers, model checkpoints.
NOISE_PATH = re.compile(
    r"(LaTeX2e\+|Proceedings\+Templates|AuthorKit|/CFP/|\\CFP\\|"
    r"Literature|Templates?|sample-|splncs|llncs|acmart)", re.I)
SKIP_FILE = re.compile(
    r"(^~\$|^\.|desktop\.ini$|\.lnk$|\.Rhistory$|\.DS_Store$|"
    r"\.(aux|log|out|toc|synctex\.gz|bbl|blg|fls|fdb_latexmk|tmp|bak|"
    r"pth|ckpt|pt|h5|npz|zip|cls|bst|sty)$)", re.I)


def kind_of(name):
    for pat, k in KIND:
        if re.search(pat, name, re.I):
            return k
    return "files"


def newest_in(folder, limit_seconds=None):
    """Most recently modified real working file under folder."""
    best = None
    for dirpath, dirnames, files in os.walk(folder):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIR]
        for f in files:
            if SKIP_FILE.search(f):
                continue
            p = os.path.join(dirpath, f)
            if NOISE_PATH.search(p):
                continue
            try:
                m = os.path.getmtime(p)
            except OSError:
                continue
            if best is None or m > best[0]:
                best = (m, p)
    return best


def git_recent(root, days=14):
    """Recent commit subjects in the site repo, as human-readable work."""
    try:
        out = subprocess.run(
            ["git", "log", "--since=%d days ago" % days, "--no-merges",
             "--pretty=%at|%s"], cwd=root, capture_output=True, text=True,
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


def describe(path, folder):
    rel = os.path.relpath(path, folder)
    parts = [p for p in rel.split(os.sep) if p]
    name = parts[-1]
    where = parts[0] if len(parts) > 1 else ""
    k = kind_of(name)
    stem = os.path.splitext(name)[0].replace("_", " ").replace("-", " ").strip()
    if where:
        where = re.sub(r"^\[\d+\]\s*", "", where)
        where = re.sub(r"^\d{4}(-\d{4})?\s+", "", where)
        return "%s in %s — %s" % (k, where, stem)
    return "%s — %s" % (k, stem)


def main():
    now = time.time()
    entries = []
    for folder, name, thread, page in PROJECTS:
        full = os.path.join(RESEARCH, folder)
        if not os.path.isdir(full):
            entries.append({"project": name, "thread": thread, "page": page,
                            "state": "unknown", "what": "", "at": None})
            continue
        b = newest_in(full)
        if not b:
            entries.append({"project": name, "thread": thread, "page": page,
                            "state": "idle", "what": "", "at": None})
            continue
        m, p = b
        entries.append({
            "project": name, "thread": thread, "page": page,
            "at": int(m),
            "what": describe(p, full),
            "file": os.path.basename(p),
            "state": "active" if (now - m) < 6 * 3600 else
                     ("recent" if (now - m) < 7 * 86400 else "idle"),
        })
    entries.sort(key=lambda e: e["at"] or 0, reverse=True)
    live = [e for e in entries if e["state"] == "active"]
    doc = {
        "generated": int(now),
        "here": live[0]["project"] if live else None,
        "projects": entries,
        "site": git_recent(ROOT),
    }
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=2)
    print("wrote", OUT)
    for e in entries:
        when = (datetime.datetime.fromtimestamp(e["at"]).strftime("%Y-%m-%d %H:%M")
                if e["at"] else "—")
        print("  %-20s %-8s %s  %s" % (e["project"], e["state"], when, e["what"]))


if __name__ == "__main__":
    main()
