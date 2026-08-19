#!/usr/bin/env python3
"""
The settings window: which projects are on the board, what they are called,
which Clockify project each maps to, and what the heatmap covers.

    python internal/activity/control_window.py

Writes projects.json and secrets.json. No code is edited to change the board.
"""
import os, json, datetime
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

import config
import clockify

RANGE_LABELS = [("1 month", "1m"), ("3 months", "3m"), ("6 months", "6m"),
                ("1 year", "1y"), ("All time", "all"), ("Custom…", "custom")]


class Window:
    def __init__(self):
        self.doc = config.load()
        self.secrets = config.load_secrets()
        self.clock_names = [""]

        self.root = tk.Tk()
        self.root.title("Projects on the board")
        self.root.geometry("980x640")
        outer = ttk.Frame(self.root, padding=12)
        outer.pack(fill="both", expand=True)

        self._root_row(outer)
        self._table(outer)
        self._range_row(outer)
        self._key_row(outer)
        self._buttons(outer)
        self.reload_table()

    # ---------- research root ----------
    def _root_row(self, parent):
        row = ttk.Frame(parent)
        row.pack(fill="x", pady=(0, 10))
        ttk.Label(row, text="Research folder").pack(side="left")
        self.root_var = tk.StringVar(value=self.doc["research_root"])
        ttk.Entry(row, textvariable=self.root_var).pack(
            side="left", fill="x", expand=True, padx=8)
        ttk.Button(row, text="Browse", command=self.browse_root).pack(side="left")
        ttk.Button(row, text="Find projects", command=self.rediscover).pack(
            side="left", padx=(6, 0))

    def browse_root(self):
        d = filedialog.askdirectory(initialdir=self.root_var.get())
        if d:
            self.root_var.set(os.path.normpath(d))

    def rediscover(self):
        root = self.root_var.get()
        found = config.discover(root)
        if not found:
            messagebox.showwarning("Nothing found",
                                   "No project subfolders under that folder.")
            return
        have = {p["folder"] for p in self.doc["projects"]}
        added = [f for f in found if f["folder"] not in have]
        self.doc["projects"] += added
        self.doc["research_root"] = root
        self.reload_table()
        messagebox.showinfo("Done", "Added %d new project(s)." % len(added))

    # ---------- table ----------
    def _table(self, parent):
        wrap = ttk.Frame(parent)
        wrap.pack(fill="both", expand=True)
        cols = ("on", "heat", "name", "folder", "clockify", "status")
        self.tree = ttk.Treeview(wrap, columns=cols, show="headings",
                                 selectmode="browse", height=15)
        for c, t, w in (("on", "Watch", 55), ("heat", "Heatmap", 66),
                        ("name", "Shown as", 210), ("folder", "Folder", 280),
                        ("clockify", "Clockify", 175), ("status", "", 90)):
            self.tree.heading(c, text=t)
            self.tree.column(c, width=w, anchor="w",
                             stretch=(c in ("name", "folder", "clockify")))
        sb = ttk.Scrollbar(wrap, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        self.tree.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        self.tree.tag_configure("missing", foreground="#b3261e")
        self.tree.tag_configure("off", foreground="#9a9a9a")
        self.tree.bind("<Double-1>", self.on_double)

    def reload_table(self):
        self.tree.delete(*self.tree.get_children())
        for i, p in enumerate(self.doc["projects"]):
            full = config.path_of(self.doc, p)
            ok = os.path.isdir(full)
            status = "found" if ok else ("alias" if p.get("alias") else "missing")
            tags = () if ok and p.get("watch", True) else (
                "missing" if not ok else "off",)
            self.tree.insert("", "end", iid=str(i), tags=tags, values=(
                "yes" if p.get("watch", True) else "",
                "yes" if p.get("heatmap", True) else "",
                p["name"], p["folder"], p.get("clockify", ""), status))

    def selected(self):
        s = self.tree.selection()
        return int(s[0]) if s else None

    def on_double(self, event):
        i = self.selected()
        if i is None:
            return
        col = self.tree.identify_column(event.x)
        p = self.doc["projects"][i]
        if col == "#1":
            p["watch"] = not p.get("watch", True)
        elif col == "#2":
            p["heatmap"] = not p.get("heatmap", True)
        elif col == "#3":
            self.edit_name(p)
        elif col == "#4":
            self.edit_folder(p)
        elif col == "#5":
            self.edit_clockify(p)
        else:
            self.edit_name(p)
        self.reload_table()
        self.tree.selection_set(str(i))

    def edit_name(self, p):
        v = _prompt(self.root, "Shown as", "Name for the board:", p["name"])
        if v:
            p["name"] = v

    def edit_folder(self, p):
        base = self.root_var.get()
        start = config.path_of(self.doc, p)
        d = filedialog.askdirectory(
            initialdir=start if os.path.isdir(start) else base)
        if not d:
            return
        d = os.path.normpath(d)
        try:
            rel = os.path.relpath(d, base)
            p["folder"] = d if rel.startswith("..") else rel
        except ValueError:
            p["folder"] = d
        p["alias"] = False
        p["group"] = os.path.dirname(p["folder"]) or p.get("group", "")

    def edit_clockify(self, p):
        v = _choose(self.root, "Clockify project",
                    "Which Clockify project is this?",
                    self.clock_names, p.get("clockify", ""))
        if v is not None:
            p["clockify"] = v

    # ---------- heatmap range ----------
    def _range_row(self, parent):
        row = ttk.Frame(parent)
        row.pack(fill="x", pady=(12, 0))
        ttk.Label(row, text="Heatmap covers").pack(side="left")
        cur = self.doc.get("heatmap_range", "6m")
        self.range_var = tk.StringVar(value=cur)
        for label, key in RANGE_LABELS:
            ttk.Radiobutton(row, text=label, value=key, variable=self.range_var,
                            command=self.on_range).pack(side="left", padx=(8, 0))
        c = self.doc.get("heatmap_custom") or {}
        self.custom_var = tk.StringVar(
            value="%s to %s" % (c.get("from", ""), c.get("to", "")) if c else "")
        ttk.Label(row, textvariable=self.custom_var,
                  foreground="#777").pack(side="left", padx=(10, 0))
        ttk.Label(parent, text="Double-click a row to change it. "
                  "Watch = scanned at all. Heatmap = counted in the big one.",
                  foreground="#777").pack(anchor="w", pady=(6, 0))

    def on_range(self):
        if self.range_var.get() != "custom":
            return
        a = _prompt(self.root, "From", "First day (YYYY-MM-DD):",
                    (self.doc.get("heatmap_custom") or {}).get("from", ""))
        b = _prompt(self.root, "To", "Last day (YYYY-MM-DD):",
                    (self.doc.get("heatmap_custom") or {}).get(
                        "to", datetime.date.today().isoformat()))
        try:
            datetime.date.fromisoformat(a); datetime.date.fromisoformat(b)
        except (ValueError, TypeError):
            messagebox.showerror("Dates", "Use YYYY-MM-DD for both.")
            self.range_var.set(self.doc.get("heatmap_range", "6m"))
            return
        self.doc["heatmap_custom"] = {"from": a, "to": b}
        self.custom_var.set("%s to %s" % (a, b))

    # ---------- clockify key ----------
    def _key_row(self, parent):
        row = ttk.Frame(parent)
        row.pack(fill="x", pady=(12, 0))
        ttk.Label(row, text="Clockify key").pack(side="left")
        self.key_var = tk.StringVar(value=self.secrets.get("clockify_key", ""))
        ttk.Entry(row, textvariable=self.key_var, show="•").pack(
            side="left", fill="x", expand=True, padx=8)
        ttk.Button(row, text="Test", command=self.test_key).pack(side="left")
        self.key_msg = tk.StringVar(value="")
        ttk.Label(parent, textvariable=self.key_msg,
                  foreground="#777").pack(anchor="w", pady=(4, 0))

    def test_key(self):
        key = self.key_var.get().strip()
        ok, msg = clockify.check(key)
        self.key_msg.set(msg)
        if ok:
            self.clock_names = [""] + [n for _i, n in clockify.projects(key)]
            self.key_msg.set(msg + " %d projects available."
                             % (len(self.clock_names) - 1))

    # ---------- save ----------
    def _buttons(self, parent):
        row = ttk.Frame(parent)
        row.pack(fill="x", pady=(14, 0))
        ttk.Button(row, text="Remove", command=self.remove).pack(side="left")
        ttk.Button(row, text="Add…", command=self.add).pack(side="left", padx=6)
        ttk.Button(row, text="Save", command=self.save).pack(side="right")
        ttk.Button(row, text="Cancel", command=self.root.destroy).pack(
            side="right", padx=6)

    def add(self):
        base = self.root_var.get()
        d = filedialog.askdirectory(initialdir=base)
        if not d:
            return
        d = os.path.normpath(d)
        rel = os.path.relpath(d, base)
        folder = d if rel.startswith("..") else rel
        self.doc["projects"].append({
            "folder": folder, "name": config._pretty(os.path.basename(d)),
            "thread": os.path.basename(os.path.dirname(d)),
            "group": os.path.dirname(folder), "page": "", "clockify": "",
            "watch": True, "heatmap": True, "alias": False})
        self.reload_table()

    def remove(self):
        i = self.selected()
        if i is None:
            return
        if messagebox.askyesno("Remove",
                               "Take %s off the board?"
                               % self.doc["projects"][i]["name"]):
            del self.doc["projects"][i]
            self.reload_table()

    def save(self):
        self.doc["research_root"] = self.root_var.get()
        self.doc["heatmap_range"] = self.range_var.get()
        config.save(self.doc)
        key = self.key_var.get().strip()
        if key:
            self.secrets["clockify_key"] = key
            config.save_secrets(self.secrets)
        messagebox.showinfo("Saved", "Run the refresh to rebuild the board.")
        self.root.destroy()

    def run(self):
        if self.key_var.get().strip():
            self.test_key()
        self.root.mainloop()


def _prompt(parent, title, label, initial=""):
    from tkinter import simpledialog
    return simpledialog.askstring(title, label, initialvalue=initial, parent=parent)


def _choose(parent, title, label, options, current=""):
    win = tk.Toplevel(parent)
    win.title(title)
    win.transient(parent)
    win.grab_set()
    ttk.Label(win, text=label, padding=10).pack()
    var = tk.StringVar(value=current)
    box = ttk.Combobox(win, textvariable=var, values=options, width=44)
    box.pack(padx=12, pady=(0, 8))
    if len(options) <= 1:
        ttk.Label(win, text="Test the Clockify key first to load the list.",
                  foreground="#777", padding=(12, 0)).pack()
    out = {}

    def ok():
        out["v"] = var.get().strip()
        win.destroy()
    ttk.Button(win, text="OK", command=ok).pack(pady=10)
    parent.wait_window(win)
    return out.get("v")


if __name__ == "__main__":
    Window().run()
