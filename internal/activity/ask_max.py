#!/usr/bin/env python3
"""
The popup. Asks what you did, only for work nothing else could explain.

Rules it keeps to:
  * at most once an hour, and it says when it may next ask
  * only projects where Clockify has no entry and the diff said nothing
  * never the same change twice — answers are keyed by the files involved
  * closing it is fine; the rules' sentence stands

    python internal/activity/ask_max.py            normal, respects the hour
    python internal/activity/ask_max.py --now      ask anyway
"""
import os, sys, json, time, datetime

from config import HERE

UPDATES = os.path.join(HERE, "updates.json")
ANSWERS = os.path.join(HERE, "answers.json")
LAST = os.path.join(HERE, "last_asked.json")

HOUR = 3600


def _load(path, default):
    if os.path.exists(path):
        try:
            return json.load(open(path, encoding="utf-8"))
        except Exception:
            pass
    return default


def due(force=False):
    if force:
        return True, 0
    last = _load(LAST, {}).get("at", 0)
    waited = time.time() - last
    return waited >= HOUR, int(HOUR - waited)


def pending():
    """[(folder, files)] for projects that still need a sentence from you."""
    blob = _load(UPDATES, {}).get("projects", {})
    answers = _load(ANSWERS, {})
    out = []
    for folder, v in blob.items():
        if not v.get("needs_asking"):
            continue
        sig = "|".join(sorted(v.get("unnamed", [])))
        if answers.get(folder, {}).get("sig") == sig:
            continue                              # already asked about exactly this
        out.append((folder, v.get("unnamed", []), sig))
    return out


def ask(items):
    import tkinter as tk
    from tkinter import ttk

    answers = _load(ANSWERS, {})
    root = tk.Tk()
    root.title("What did you do?")
    root.geometry("560x%d" % min(560, 150 + 96 * len(items)))
    frame = ttk.Frame(root, padding=14)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="These changed and nothing said what they were.",
              foreground="#666").pack(anchor="w", pady=(0, 10))

    boxes = []
    for folder, files, sig in items:
        ttk.Label(frame, text=os.path.basename(folder),
                  font=("Segoe UI", 10, "bold")).pack(anchor="w")
        ttk.Label(frame, text="  ".join(files[:4]), foreground="#888",
                  font=("Consolas", 8)).pack(anchor="w")
        e = ttk.Entry(frame, width=70)
        e.insert(0, answers.get(folder, {}).get("text", ""))
        e.pack(anchor="w", fill="x", pady=(2, 12))
        boxes.append((folder, sig, e))
    boxes[0][2].focus_set()

    nxt = (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%H:%M")
    ttk.Label(frame, text="Won't ask again before %s." % nxt,
              foreground="#888").pack(side="left")

    state = {"saved": False}

    def save():
        for folder, sig, e in boxes:
            answers[folder] = {"text": e.get().strip(), "sig": sig,
                               "at": int(time.time())}
        state["saved"] = True
        root.destroy()

    def skip():
        for folder, sig, e in boxes:
            answers.setdefault(folder, {})
            answers[folder]["sig"] = sig        # asked; don't ask again
            answers[folder].setdefault("text", "")
        root.destroy()

    ttk.Button(frame, text="Save", command=save).pack(side="right")
    ttk.Button(frame, text="Skip", command=skip).pack(side="right", padx=6)
    root.protocol("WM_DELETE_WINDOW", skip)
    root.bind("<Return>", lambda _e: save())
    root.mainloop()

    json.dump(answers, open(ANSWERS, "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)
    json.dump({"at": int(time.time())}, open(LAST, "w", encoding="utf-8"))
    return state["saved"]


def main():
    force = "--now" in sys.argv
    ok, wait = due(force)
    if not ok:
        print("asked recently. Next window in %d min" % max(1, wait // 60))
        return
    items = pending()
    if not items:
        print("nothing needs asking")
        json.dump({"at": int(time.time())}, open(LAST, "w", encoding="utf-8"))
        return
    try:
        saved = ask(items)
    except Exception as e:
        print("could not open the window (%s) — carrying on without it" % e)
        return
    print("saved your words" if saved else "skipped")


if __name__ == "__main__":
    main()
