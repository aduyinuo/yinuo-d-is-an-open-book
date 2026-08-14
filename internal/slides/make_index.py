#!/usr/bin/env python3
"""Write docs/index.html listing every deck in docs/slides/."""
import os, html
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
D = os.path.join(ROOT, "docs", "slides")
os.makedirs(D, exist_ok=True)
decks = sorted(f[:-5] for f in os.listdir(D) if f.endswith(".html"))
items = "\n".join(
    '<li><a href="slides/%s.html">%s</a></li>' % (d, html.escape(d.replace("-", " ")))
    for d in decks) or "<li><em>No decks yet.</em></li>"
open(os.path.join(ROOT, "docs", "index.html"), "w", encoding="utf-8", newline="\n").write(
"""<!doctype html><meta charset="utf-8"><title>Slides</title>
<style>body{font-family:-apple-system,"Segoe UI",sans-serif;max-width:700px;margin:44px auto;
padding:0 20px;color:#1f2430}h1{color:#22452f;font-size:20px}a{color:#4a7c59}li{margin:.45em 0}</style>
<h1>Slide decks</h1><ul>
%s
</ul>""" % items)
print("index:", len(decks), "decks")
