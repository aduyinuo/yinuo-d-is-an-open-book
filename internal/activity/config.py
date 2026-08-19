#!/usr/bin/env python3
"""
The project list, and where it comes from.

Projects are the numbered SUBFOLDERS inside each research folder, not the
research folders themselves. `[1] 2025-2026 sample_efficient_FOEDreamer` is a
project; `2025-2026 LucidWorld` is the thread it sits under.

Everything is stored in projects.json so the list can be changed from the
control window without touching code.
"""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CONFIG = os.path.join(HERE, "projects.json")
SECRETS = os.path.join(HERE, "secrets.json")     # gitignored

DEFAULT_RESEARCH = r"G:\Other computers\My Mac\[2025-2026][postdoc][utep]\[2] Research Projects"

# research folder -> the thread it is on the site, and the page it links to
THREADS = {
    "2025-2026 LucidWorld":     ("Cyber World Modeling",
                                 "overview/3-year-agenda/cyber-world-modeling/"),
    "2025-2026 PickYourBattles": ("Cyber World Modeling",
                                 "overview/3-year-agenda/cyber-world-modeling/next.md"),
    "2025-2026 DesignTheGame":  ("Mental World Modeling",
                                 "overview/3-year-agenda/mental-world-modeling/problem-solving/"),
    "2022-2026 ReadTheRoom":    ("Mental World Modeling",
                                 "overview/3-year-agenda/mental-world-modeling/opponent-agent-modeling/"),
    "2025-2026 UnitedForces":   ("Human-AI Complementarity",
                                 "overview/3-year-agenda/human-ai-complementarity/"),
    "2026 BeRealistic":         ("Toward Deployment",
                                 "overview/3-year-agenda/toward-deployment/"),
    "IRB Applications":         ("Across threads", "overview/3-year-agenda/"),
    "RESEARCH STATEMENT":       ("Across threads", "research/overview.md"),
    "READING NOTES":            ("Across threads", "personal/overview.md"),
}

# subfolders that hold supporting material rather than a project of their own
SUPPORTING = re.compile(
    r"^(code|literature|notes?|data|figures?|archive|old|scratch|shared|"
    r"latex(_.*)?)$", re.I)


def _pretty(folder):
    """A first guess at a display name, from the folder name."""
    s = re.sub(r"\.lnk$", "", folder, flags=re.I)
    s = re.sub(r"\s*-\s*Shortcut$", "", s, flags=re.I)
    s = re.sub(r"^\[\d+\]\s*", "", s)                   # drop [1]
    s = re.sub(r"^\d{4}([_-]\d{4})?[_ ]+", "", s)       # drop 2025-2026 / 2025_2026
    s = re.sub(r"^\[\d+\]\s*", "", s)
    s = s.replace("_", " ").strip(" -")
    return s[:1].upper() + s[1:] if s else folder


def _entry(thread_folder, sub, thread, page, alias=False):
    return {
        "folder": os.path.join(thread_folder, sub) if sub else thread_folder,
        "name": _pretty(sub or thread_folder),
        "thread": thread,
        "group": thread_folder,
        "page": page,
        "clockify": "",
        "watch": not alias,
        "heatmap": not alias,
        "alias": alias,
    }


def discover(research_root):
    """Every project subfolder under every known research folder.

    A research folder whose subfolders are all supporting material is itself
    the project. Mac alias files are listed but cannot be followed from
    Windows, so they come through unwatched for you to repoint.
    """
    found = []
    if not os.path.isdir(research_root):
        return found
    for thread_folder in sorted(os.listdir(research_root)):
        tpath = os.path.join(research_root, thread_folder)
        if not os.path.isdir(tpath) or thread_folder.startswith("."):
            continue
        thread, page = THREADS.get(thread_folder, (thread_folder, ""))
        here = []
        for sub in sorted(os.listdir(tpath)):
            if sub.startswith("."):
                continue
            spath = os.path.join(tpath, sub)
            if os.path.isdir(spath):
                if SUPPORTING.match(sub):
                    continue
                here.append(_entry(thread_folder, sub, thread, page))
            elif _is_alias(spath) and not SUPPORTING.match(_pretty(sub)):
                here.append(_entry(thread_folder, sub, thread, page, alias=True))
        if not here:
            here = [_entry(thread_folder, "", thread, page)]
        found.extend(here)
    return found


def _is_alias(path):
    """Mac alias / Windows shortcut standing in for a folder somewhere else."""
    if path.lower().endswith(".lnk"):
        return True
    try:
        if os.path.getsize(path) > 8192:
            return False
        with open(path, "rb") as fh:
            head = fh.read(8)
        return head.startswith(b"book\x00\x00\x00\x00") or head.startswith(b"\x00\x00\x00\x00mark")
    except OSError:
        return False


def load():
    """The saved config, seeded from disk on first run."""
    if os.path.exists(CONFIG):
        with open(CONFIG, encoding="utf-8") as fh:
            doc = json.load(fh)
        doc.setdefault("research_root", DEFAULT_RESEARCH)
        doc.setdefault("heatmap_range", "6m")
        doc.setdefault("projects", [])
        for p in doc["projects"]:
            p.setdefault("clockify", "")
            p.setdefault("watch", True)
            p.setdefault("heatmap", True)
            p.setdefault("group", os.path.dirname(p.get("folder", "")))
        return doc
    doc = {"research_root": DEFAULT_RESEARCH, "heatmap_range": "6m",
           "projects": discover(DEFAULT_RESEARCH)}
    save(doc)
    return doc


def save(doc):
    with open(CONFIG, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=2)


def path_of(doc, project):
    """Absolute path of a project folder. Absolute `folder` values pass through."""
    f = project.get("folder", "")
    return f if os.path.isabs(f) else os.path.join(doc["research_root"], f)


def watched(doc):
    return [p for p in doc["projects"] if p.get("watch", True)]


def load_secrets():
    if os.path.exists(SECRETS):
        with open(SECRETS, encoding="utf-8") as fh:
            return json.load(fh)
    return {}


def save_secrets(d):
    with open(SECRETS, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(d, fh, indent=2)
