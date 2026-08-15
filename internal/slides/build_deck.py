#!/usr/bin/env python3
"""
Build a talk from a JSON spec.  python internal/slides/build_deck.py <spec.json>

Spec: {"slug","title","subtitle","opening", "slides":[ {...}, ... ]}
Slide kinds: section | points | statement | figure | two_col | placeholder
Every slide carries "note" — the narration, which is also the annotation shown
under the slide on the site. Use "---" on its own line to split reveal steps.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deckbuilder import Deck

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "slides-source")


def build(spec_path):
    spec = json.load(open(spec_path, encoding="utf-8"))
    d = Deck(spec["title"], spec.get("subtitle", ""), spec.get("opening", ""))
    for s in spec["slides"]:
        k = s.get("kind", "points")
        note = s.get("note", "")
        if k == "section":
            d.section(s["title"], note)
        elif k == "statement":
            d.statement(s["title"], s.get("line", ""), note)
        elif k == "figure":
            d.figure(s["title"], s.get("caption", ""), note,
                     label=s.get("label", "figure"))
        elif k == "two_col":
            d.two_col(s["title"], s["left_head"], s["left"],
                      s["right_head"], s["right"], note)
        elif k == "placeholder":
            d.placeholder(s["title"], s["what"], note)
        else:
            d.points(s["title"], s.get("bullets", []), note,
                     size=s.get("size", 30))
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, spec["slug"] + ".pptx")
    d.save(p)
    words = sum(len((sl.get("note") or "").split()) for sl in spec["slides"])
    words += len((spec.get("opening") or "").split())
    print("%-22s %2d slides  %4d words  ~%.1f min"
          % (spec["slug"], len(spec["slides"]) + 1, words, words / 140.0))
    return p


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        specs = sorted(os.path.join(os.path.dirname(__file__), "decks", f)
                       for f in os.listdir(os.path.join(os.path.dirname(__file__), "decks"))
                       if f.endswith(".json"))
        args = specs
    for a in args:
        build(a)
