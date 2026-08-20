#!/usr/bin/env python3
"""
The popup. Asks what you were doing on work Clockify has no entry for, and
logs it there for you.

Rules it keeps to:
  * at most once an hour, and it says when it may next ask
  * only projects where you have not already logged the time yourself
  * never the same change twice — answers are keyed by the files involved
  * nothing reaches Clockify unless you typed a description and pressed Save
  * closing it is fine; nothing is posted and the generated sentence stands

    python internal/activity/ask_max.py            normal, respects the hour
    python internal/activity/ask_max.py --now      ask anyway
"""
import os, sys, json, time, datetime

from config import HERE
import clockify

UPDATES = os.path.join(HERE, "updates.json")
ANSWERS = os.path.join(HERE, "answers.json")
LAST = os.path.join(HERE, "last_asked.json")

HOUR = 3600
MIN_BLOCK = 900          # never suggest less than 15 minutes
MAX_BLOCK = 4 * 3600     # never guess more than 4 hours


def _load(path, default):
    if os.path.exists(path):
        try:
            return json.load(open(path, encoding="utf-8"))
        except Exception:
            pass
    return default


def _save(path, obj):
    json.dump(obj, open(path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)


def due(force=False):
    if force:
        return True, 0
    last = _load(LAST, {}).get("at", 0)
    waited = time.time() - last
    return waited >= HOUR, int(HOUR - waited)


def suggested_hours(window):
    """How long the work looks like it took, from the file timestamps."""
    if not window:
        return 0.5
    span = int(window["to"]) - int(window["from"])
    span = max(MIN_BLOCK, min(span, MAX_BLOCK))
    return round(span / 3600.0, 2)


def pending():
    """Projects that did work you have not logged."""
    blob = _load(UPDATES, {}).get("projects", {})
    answers = _load(ANSWERS, {})
    out = []
    for folder, v in blob.items():
        if not v.get("needs_asking"):
            continue
        sig = "|".join(sorted(v.get("unnamed", [])))
        if answers.get(folder, {}).get("sig") == sig:
            continue                              # already asked about exactly this
        out.append({"folder": folder, "sig": sig,
                    "name": v.get("name") or os.path.basename(folder),
                    "files": v.get("unnamed", []),
                    "guess": v.get("guess", ""),
                    "clockify": v.get("clockify", ""),
                    "window": v.get("window")})
    return out


def ask(items):
    import tkinter as tk
    from tkinter import ttk

    answers = _load(ANSWERS, {})
    root = tk.Tk()
    root.title("What did you do?")
    frame = ttk.Frame(root, padding=14)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Work with no time logged against it. "
              "Fill a line in and it goes to Clockify.",
              foreground="#666").pack(anchor="w", pady=(0, 12))

    rows = []
    for it in items:
        block = ttk.Frame(frame)
        block.pack(fill="x", pady=(0, 12))
        head = ttk.Frame(block)
        head.pack(fill="x")
        ttk.Label(head, text=it["name"],
                  font=("Segoe UI", 10, "bold")).pack(side="left")
        ttk.Label(head, text="  " + ", ".join(it["files"][:3]), foreground="#999",
                  font=("Consolas", 8)).pack(side="left")

        e = ttk.Entry(block, width=76)
        e.insert(0, it["guess"] or answers.get(it["folder"], {}).get("text", ""))
        e.pack(fill="x", pady=(3, 3))

        foot = ttk.Frame(block)
        foot.pack(fill="x")
        hv = tk.StringVar(value="%.2f" % suggested_hours(it["window"]))
        ttk.Label(foot, text="hours").pack(side="left")
        ttk.Entry(foot, textvariable=hv, width=7).pack(side="left", padx=(4, 12))
        send = tk.BooleanVar(value=bool(it["clockify"]))
        cb = ttk.Checkbutton(foot, variable=send,
                             text="log to %s" % (it["clockify"] or "not mapped"))
        cb.pack(side="left")
        if not it["clockify"]:
            cb.state(["disabled"])
        rows.append((it, e, hv, send))

    rows[0][1].focus_set()

    nxt = (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%H:%M")
    ttk.Label(frame, text="Won't ask again before %s." % nxt,
              foreground="#888").pack(anchor="w")

    state = {"saved": False, "notes": []}

    def finish(save_it):
        if save_it:
            for it, e, hv, send in rows:
                text = e.get().strip()
                answers[it["folder"]] = {"text": text, "sig": it["sig"],
                                         "at": int(time.time())}
                if not (text and send.get() and it["clockify"]):
                    continue
                try:
                    hours = max(0.05, min(float(hv.get()), 12.0))
                except ValueError:
                    state["notes"].append("%s: hours not a number, nothing logged"
                                          % it["name"])
                    continue
                end = int((it["window"] or {}).get("to") or time.time())
                ok, msg = clockify.post_entry(it["clockify"], text,
                                              end - int(hours * 3600), end)
                state["notes"].append("%s: %s" % (it["name"], msg))
            state["saved"] = True
        else:
            for it, _e, _h, _s in rows:
                answers.setdefault(it["folder"], {})
                answers[it["folder"]]["sig"] = it["sig"]   # asked; don't ask again
                answers[it["folder"]].setdefault("text", "")
        root.destroy()

    bar = ttk.Frame(frame)
    bar.pack(fill="x", pady=(10, 0))
    ttk.Button(bar, text="Save", command=lambda: finish(True)).pack(side="right")
    ttk.Button(bar, text="Skip", command=lambda: finish(False)).pack(side="right", padx=6)
    root.protocol("WM_DELETE_WINDOW", lambda: finish(False))
    root.bind("<Return>", lambda _e: finish(True))
    root.mainloop()

    _save(ANSWERS, answers)
    _save(LAST, {"at": int(time.time())})
    for n in state["notes"]:
        print("  " + n)
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
        _save(LAST, {"at": int(time.time())})
        return
    try:
        saved = ask(items)
    except Exception as e:
        print("could not open the window (%s) — carrying on without it" % e)
        return
    print("saved your words" if saved else "skipped")


if __name__ == "__main__":
    main()
