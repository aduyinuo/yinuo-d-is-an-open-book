#!/usr/bin/env python3
"""
Capture what actually changed, with enough of the content that a sentence can
be written about it.

Keeps a snapshot of every tracked file's text. On each run it diffs the current
state against that snapshot and writes changes.json: per project, the files that
changed and the lines that were added or removed.

changes.json is raw material. It is not shown to anyone. A separate step reads
it and writes the sentences into activity.json.

    python internal/activity/capture_changes.py

First run only records the snapshot and reports nothing changed, which is
correct: there is no before.
"""
import os, re, json, time, hashlib, difflib, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SNAP = os.path.join(HERE, "snapshot.json")
OUT = os.path.join(HERE, "changes.json")

RESEARCH = os.environ.get(
    "RESEARCH_ROOT",
    r"G:\Other computers\My Mac\[2025-2026][postdoc][utep]\[2] Research Projects")

# folder on disk -> project name on the site
from collect_activity import PROJECTS  # reuse the one mapping

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
            if SKIP_FILE.search(name):
                continue
            ext = os.path.splitext(name)[1].lower()
            if ext not in TEXT and ext not in OPAQUE:
                continue
            yield os.path.join(dirpath, name)


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
    a = before.splitlines()
    b = after.splitlines()
    added, removed = [], []
    for line in difflib.unified_diff(a, b, n=0, lineterm=""):
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
    """Commit subjects and diffstat from this repo since the last run."""
    try:
        out = subprocess.run(
            ["git", "log", f"--since=@{int(since_ts)}", "--no-merges",
             "--pretty=format:%H%x1f%s%x1f%ct", "--name-status"],
            cwd=ROOT, capture_output=True, text=True, timeout=30).stdout
    except Exception:
        return []
    commits, cur = [], None
    for line in out.splitlines():
        if "\x1f" in line:
            h, subj, ct = line.split("\x1f")
            cur = {"sha": h[:8], "subject": subj, "at": int(ct), "files": []}
            commits.append(cur)
        elif line.strip() and cur is not None:
            parts = line.split("\t")
            if len(parts) >= 2:
                cur["files"].append({"status": parts[0], "path": parts[-1]})
    return commits


def main():
    prev = {}
    prev_run = 0
    if os.path.exists(SNAP):
        with open(SNAP, encoding="utf-8") as f:
            blob = json.load(f)
        prev = blob.get("files", {})
        prev_run = blob.get("at", 0)

    now = time.time()
    snapshot = {}
    changes = []

    for folder, name, thread, page in PROJECTS:
        root = os.path.join(RESEARCH, folder)
        if not os.path.isdir(root):
            continue
        touched = []
        for path in walk(root):
            st = state_of(path)
            if st is None:
                continue
            key = os.path.relpath(path, RESEARCH)
            snapshot[key] = {"hash": st["hash"], "text": st["text"],
                             "mtime": st["mtime"]}
            was = prev.get(key)
            if was is None:
                touched.append({
                    "file": os.path.relpath(path, root),
                    "how": "created",
                    "at": st["mtime"],
                    **diff_lines("", st["text"] or "", limit=40),
                })
            elif was["hash"] != st["hash"]:
                touched.append({
                    "file": os.path.relpath(path, root),
                    "how": "edited",
                    "at": st["mtime"],
                    **diff_lines(was.get("text"), st["text"]),
                })
        # files that vanished
        for key, was in prev.items():
            if key.startswith(folder + os.sep) and key not in snapshot:
                touched.append({"file": os.path.relpath(key, folder),
                                "how": "deleted", "at": now,
                                "added": [], "removed": [], "opaque": True})
        if touched:
            touched.sort(key=lambda t: t["at"], reverse=True)
            changes.append({"project": name, "thread": thread, "page": page,
                            "files": touched})

    payload = {
        "captured": int(now),
        "since": int(prev_run),
        "first_run": prev_run == 0,
        "projects": changes,
        "site_commits": site_commits(prev_run) if prev_run else [],
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    with open(SNAP, "w", encoding="utf-8") as f:
        json.dump({"at": int(now), "files": snapshot}, f, ensure_ascii=False)

    if payload["first_run"]:
        print(f"snapshot recorded: {len(snapshot)} files. "
              f"Nothing to report on a first run.")
    else:
        n = sum(len(p['files']) for p in changes)
        print(f"{n} changed file(s) across {len(changes)} project(s) "
              f"-> {os.path.relpath(OUT, ROOT)}")


if __name__ == "__main__":
    main()
