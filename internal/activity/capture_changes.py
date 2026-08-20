#!/usr/bin/env python3
"""
Capture what actually changed, with enough of the content that a sentence can
be written about it.

Keeps a snapshot of every tracked file's text. On each run it diffs the current
state against that snapshot and writes changes.json: per project, the files that
changed and the lines that were added or removed.

changes.json is raw material. It is not shown to anyone. summarize_changes.py
reads it and writes the sentences.

    python internal/activity/capture_changes.py

First run only records the snapshot and reports nothing changed, which is
correct: there is no before.
"""
import os, re, json, time, hashlib, difflib, subprocess

from config import HERE, ROOT, load, path_of, watched, excluded

SNAP = os.path.join(HERE, "snapshot.json")
OUT = os.path.join(HERE, "changes.json")

# files whose text we can read and diff
TEXT = {".tex", ".md", ".txt", ".py", ".bib", ".r", ".jl", ".ipynb",
        ".yaml", ".yml", ".json", ".csv", ".sh", ".bat", ".html", ".css", ".js"}
# files we note as changed but cannot read
OPAQUE = {".docx", ".pptx", ".xlsx", ".pdf", ".png", ".jpg", ".jpeg", ".gif",
          ".webp", ".mp4", ".zip", ".pkl", ".pt", ".ckpt", ".npz"}

SKIP_DIR = re.compile(
    r"(^|[\\/])(\.git|__pycache__|node_modules|build|dist|\.ipynb_checkpoints"
    r"|venv|\.venv|checkpoints|wandb|outputs?|logs?|_minted.*)([\\/]|$)", re.I)
SKIP_FILE = re.compile(
    r"(\.aux|\.log|\.out|\.toc|\.synctex\.gz|\.fls|\.fdb_latexmk|\.bbl|\.blg"
    r"|\.nav|\.snm|\.vrb|\.DS_Store|Thumbs\.db)$", re.I)
NOISE_PATH = re.compile(
    r"(LaTeX2e\+|Proceedings\+Templates|AuthorKit|[\\/]CFP[\\/]|sample-|"
    r"splncs|llncs|acmart)", re.I)

MAX_BYTES = 400_000


def readable(path):
    ext = os.path.splitext(path)[1].lower()
    if ext in TEXT:
        try:
            if os.path.getsize(path) > MAX_BYTES:
                return None
            with open(path, encoding="utf-8", errors="replace") as f:
                return f.read()
        except OSError:
            return None
    return None


def walk(folder):
    for dirpath, dirnames, filenames in os.walk(folder):
        if SKIP_DIR.search(dirpath):
            dirnames[:] = []
            continue
        dirnames[:] = [d for d in dirnames if not SKIP_DIR.search(d)]
        for name in filenames:
            if SKIP_FILE.search(name) or name.startswith("~$"):
                continue
            ext = os.path.splitext(name)[1].lower()
            if ext not in TEXT and ext not in OPAQUE:
                continue
            p = os.path.join(dirpath, name)
            if NOISE_PATH.search(p):
                continue
            yield p


def state_of(path):
    """(hash, text-or-None, mtime) for one file."""
    try:
        mtime = os.path.getmtime(path)
    except OSError:
        return None
    text = readable(path)
    if text is not None:
        h = hashlib.sha1(text.encode("utf-8", "replace")).hexdigest()
    else:
        try:
            with open(path, "rb") as f:
                h = hashlib.sha1(f.read(MAX_BYTES)).hexdigest()
        except OSError:
            return None
    return {"hash": h, "text": text, "mtime": mtime}


def diff_lines(before, after, limit=60):
    """The lines that were added and removed, trimmed."""
    if before is None or after is None:
        return {"added": [], "removed": [], "opaque": True}
    added, removed = [], []
    for line in difflib.unified_diff(before.splitlines(), after.splitlines(),
                                     n=0, lineterm=""):
        if line.startswith("+") and not line.startswith("+++"):
            s = line[1:].strip()
            if s:
                added.append(s)
        elif line.startswith("-") and not line.startswith("---"):
            s = line[1:].strip()
            if s:
                removed.append(s)
    return {"added": added[:limit], "removed": removed[:limit], "opaque": False}


def site_commits(since_ts):
    """Commit subjects from this repo since the last run."""
    if not since_ts:
        return []
    try:
        out = subprocess.run(
            ["git", "log", "--since=@%d" % int(since_ts), "--no-merges",
             "--pretty=format:%s%x1f%ct"],
            cwd=ROOT, capture_output=True, text=True, timeout=30).stdout
    except Exception:
        return []
    rows = []
    for line in out.splitlines():
        if "\x1f" not in line:
            continue
        subj, ct = line.rsplit("\x1f", 1)
        if subj.startswith("GITBOOK-"):
            continue
        rows.append({"what": subj.strip(), "at": int(ct)})
    return rows


def main():
    doc = load()
    prev, prev_run = {}, 0
    if os.path.exists(SNAP):
        try:
            blob = json.load(open(SNAP, encoding="utf-8"))
            prev, prev_run = blob.get("files", {}), blob.get("at", 0)
        except Exception:
            pass

    now = time.time()
    snapshot, changes = {}, []

    for p in watched(doc):
        root = path_of(doc, p)
        if not os.path.isdir(root):
            continue
        touched, seen = [], set()
        # A project added to the board since the last run has no before. Record
        # it and say nothing, rather than announcing every file as created.
        first_time = not any(k.startswith(p["folder"] + "|") for k in prev)
        for path in walk(root):
            st = state_of(path)
            if st is None:
                continue
            rel = os.path.relpath(path, root)
            if excluded(p, rel):
                continue
            key = p["folder"] + "|" + rel
            seen.add(key)
            snapshot[key] = st
            was = prev.get(key)
            if was is None:
                if prev_run and not first_time:  # only new against a real before
                    touched.append({"file": rel,
                                    "how": "created", "at": st["mtime"],
                                    **diff_lines("", st["text"] or "", limit=40)})
            elif was["hash"] != st["hash"]:
                touched.append({"file": rel,
                                "how": "edited", "at": st["mtime"],
                                **diff_lines(was.get("text"), st["text"])})
        for key in prev:
            if key.startswith(p["folder"] + "|") and key not in seen:
                touched.append({"file": key.split("|", 1)[1], "how": "deleted",
                                "at": now, "added": [], "removed": [], "opaque": True})
        if touched:
            touched.sort(key=lambda t: t["at"], reverse=True)
            changes.append({"folder": p["folder"], "name": p["name"],
                            "files": touched[:40]})

    payload = {"captured": int(now), "since": int(prev_run),
               "first_run": prev_run == 0, "projects": changes,
               "site_commits": site_commits(prev_run)}
    json.dump(payload, open(OUT, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    json.dump({"at": int(now), "files": snapshot},
              open(SNAP, "w", encoding="utf-8"), ensure_ascii=False)

    if payload["first_run"]:
        print("snapshot recorded: %d files. Nothing to report on a first run."
              % len(snapshot))
    else:
        n = sum(len(p["files"]) for p in changes)
        print("%d changed file(s) across %d project(s)" % (n, len(changes)))


if __name__ == "__main__":
    main()
