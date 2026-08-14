#!/usr/bin/env python3
"""
Convert a PowerPoint deck into an annotated-slides HTML page.

Usage:  python internal/slides/pptx_to_deck.py            # convert everything in slides-source/
        python internal/slides/pptx_to_deck.py my.pptx    # convert one file

Input   slides-source/<name>.pptx
Output  docs/slides/<name>.html   (self-contained, no build step, no dependencies)

Narration: whatever you type in the slide's Notes pane becomes the text shown
under that slide. Blank lines make paragraphs; **bold** and _italic_ work.
A line starting with '---' splits the notes so the slide reveals in steps.
"""
import os, sys, re, json, html, base64

from pptx import Presentation
from pptx.util import Emu

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SRC  = os.path.join(ROOT, "slides-source")
OUT  = os.path.join(ROOT, "docs", "slides")

# ---------------------------------------------------------------- pptx -> html
def emu_pct(v, total):
    return round(100.0 * float(v) / float(total), 3)

def pt_to_cqw(pt, slide_w_emu):
    """Font size in points -> cqw, so text scales with the slide box."""
    slide_w_pt = float(slide_w_emu) / 12700.0
    return round(100.0 * float(pt) / slide_w_pt, 3)

def color_of(run, default=None):
    try:
        c = run.font.color
        if c and c.type is not None and c.rgb is not None:
            return "#%s" % str(c.rgb)
    except Exception:
        pass
    return default

def para_html(p, slide_w, base_pt):
    bits = []
    for r in p.runs:
        t = html.escape(r.text or "", quote=False)
        if not t:
            continue
        sz = r.font.size.pt if r.font.size else base_pt
        style = ["font-size:%.2fcqw" % pt_to_cqw(sz, slide_w)]
        if r.font.bold:   style.append("font-weight:650")
        if r.font.italic: style.append("font-style:italic")
        col = color_of(r)
        if col: style.append("color:%s" % col)
        bits.append('<span style="%s">%s</span>' % (";".join(style), t))
    if not bits:
        return ""
    align = {1: "center", 2: "right", 3: "justify"}.get(
        getattr(p.alignment, "value", None), "left")
    indent = 2.2 * (p.level or 0)
    return ('<p style="margin:0 0 .45em 0;text-align:%s;margin-left:%.1fcqw">%s</p>'
            % (align, indent, "".join(bits)))

def shape_html(sh, slide_w, slide_h, media, idx):
    try:
        left, top = sh.left, sh.top
        width, height = sh.width, sh.height
        if left is None or top is None:
            return ""
    except Exception:
        return ""
    pos = ("left:%.3f%%;top:%.3f%%;width:%.3f%%;height:%.3f%%"
           % (emu_pct(left, slide_w), emu_pct(top, slide_h),
              emu_pct(width, slide_w), emu_pct(height, slide_h)))

    if sh.shape_type == 13 or sh.__class__.__name__ == "Picture":
        try:
            img = sh.image
            b64 = base64.b64encode(img.blob).decode("ascii")
            uri = "data:%s;base64,%s" % (img.content_type, b64)
            return ('<div class="shp img" style="%s">'
                    '<img src="%s" alt=""></div>' % (pos, uri))
        except Exception:
            return ""

    if not sh.has_text_frame:
        # keep simple filled shapes as blocks so layout still reads
        try:
            fill = sh.fill
            if fill.type is not None and fill.fore_color.rgb is not None:
                return ('<div class="shp box" style="%s;background:#%s"></div>'
                        % (pos, str(fill.fore_color.rgb)))
        except Exception:
            pass
        return ""

    tf = sh.text_frame
    if not (tf.text or "").strip():
        return ""
    base_pt = 18
    paras = "".join(para_html(p, slide_w, base_pt) for p in tf.paragraphs)
    if not paras:
        return ""
    anchor = {1: "center", 2: "flex-end"}.get(
        getattr(tf.vertical_anchor, "value", None), "flex-start")
    return ('<div class="shp txt" style="%s;justify-content:%s">%s</div>'
            % (pos, anchor, paras))

def notes_of(slide):
    try:
        if slide.has_notes_slide:
            return (slide.notes_slide.notes_text_frame.text or "").strip()
    except Exception:
        pass
    return ""

def convert(path):
    prs = Presentation(path)
    W, H = prs.slide_width, prs.slide_height
    frags, narr = {}, {}
    for i, slide in enumerate(prs.slides, start=1):
        shapes = [s for s in slide.shapes]
        # z-order as authored
        body = "".join(shape_html(s, W, H, None, j) for j, s in enumerate(shapes))
        frags[i] = '<div class="slide">%s</div>' % body
        n = notes_of(slide)
        # '---' in the notes marks reveal steps
        parts = [p.strip() for p in re.split(r"^\s*---\s*$", n, flags=re.M) if p.strip()]
        narr[i] = "\n\n".join(parts) if parts else n
    title = os.path.splitext(os.path.basename(path))[0].replace("-", " ").replace("_", " ")
    return title, frags, narr, (W / H if H else 16 / 9)

# ---------------------------------------------------------------- html output
def build_html(title, frags, narr, ratio):
    tpl = open(os.path.join(HERE, "viewer_template.html"), encoding="utf-8").read()
    return (tpl.replace("__TITLE__", html.escape(title, quote=False))
               .replace("__RATIO__", "%.4f" % ratio)
               .replace("__FRAGS__", json.dumps(frags, ensure_ascii=False))
               .replace("__NARR__",  json.dumps(narr,  ensure_ascii=False)))

def main(argv):
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(SRC, exist_ok=True)
    files = argv[1:] or [os.path.join(SRC, f) for f in sorted(os.listdir(SRC))
                         if f.lower().endswith((".pptx", ".potx"))]
    if not files:
        print("No .pptx found in slides-source/. Put a deck there and run again.")
        return 1
    made = []
    for f in files:
        if not os.path.isabs(f):
            f = os.path.join(SRC, f)
        title, frags, narr, ratio = convert(f)
        slug = os.path.splitext(os.path.basename(f))[0]
        out = os.path.join(OUT, slug + ".html")
        open(out, "w", encoding="utf-8", newline="\n").write(
            build_html(title, frags, narr, ratio))
        made.append((slug, len(frags), sum(1 for v in narr.values() if v)))
    for slug, n, withnotes in made:
        print("%-40s %2d slides, %d with narration" % (slug, n, withnotes))
        print("   embed: https://aduyinuo.github.io/yinuo-d-is-an-open-book/slides/%s.html" % slug)
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
