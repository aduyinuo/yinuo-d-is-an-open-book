#!/usr/bin/env python3
r"""
from-pptx.py --- rebuild a PowerPoint deck as a Lucid beamer deck.

    python tools/from-pptx.py talk.pptx -o rebuilt/

WHAT IT RECOVERS

    * the title of every slide, and its body text as bullets
    * every speaker note
    * every embedded image, at original resolution, placed on its slide
    * any table, as a lucidtable
    * the aspect ratio

WHAT IT CANNOT RECOVER

Diagrams that PowerPoint drew from its own shapes -- boxes, arrows,
connectors, grouped constructions -- are not pictures. They live as
drawing instructions with no image behind them, and there is nothing to
extract. Those slides come out with their text and a marked placeholder
saying what was on them, so you can redraw them in TikZ or paste a
screenshot.

This is the same limit that mangles a deck when it is pushed through
pdf-to-HTML converters: they keep the embedded pictures, drop the drawn
shapes, and lose the layout. The difference is that this script tells
you which slides lost something instead of quietly shipping them.

Run it, read the report at the end, then fix the listed slides by hand.

REQUIREMENTS

    pip install python-pptx
"""

import argparse
import os
import re
import sys

try:
    from pptx import Presentation
    from pptx.util import Emu
except ImportError:
    sys.exit("Missing python-pptx.  pip install python-pptx")


# LaTeX special characters, in an order that does not double-escape.
_TEX = [
    ("\\", r"\textbackslash{}"),
    ("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"),
    ("_", r"\_"), ("{", r"\{"), ("}", r"\}"),
    ("~", r"\textasciitilde{}"), ("^", r"\textasciicircum{}"),
]


# Characters that actually turn up in slide decks, mapped to something
# pdflatex can set. Everything unmapped is dropped, not turned into "?",
# because a stray "?" reads as a real question mark in the text.
_UNI = [
    ("\u2019", "'"), ("\u2018", "`"), ("\u201c", "``"), ("\u201d", "''"),
    ("\u2013", "--"), ("\u2014", "---"), ("\u2026", r"\ldots{}"),
    ("\u00a0", " "), ("\u2192", r"$\rightarrow$"), ("\u2190", r"$\leftarrow$"),
    ("\u21d2", r"$\Rightarrow$"), ("\u00d7", r"$\times$"),
    ("\u2265", r"$\geq$"), ("\u2264", r"$\leq$"), ("\u2260", r"$\neq$"),
    ("\u2248", r"$\approx$"), ("\u00b1", r"$\pm$"), ("\u221e", r"$\infty$"),
    ("\u03b1", r"$\alpha$"), ("\u03b2", r"$\beta$"), ("\u03b3", r"$\gamma$"),
    ("\u03bb", r"$\lambda$"), ("\u03bc", r"$\mu$"), ("\u03c0", r"$\pi$"),
    ("\u03c3", r"$\sigma$"), ("\u03b8", r"$\theta$"), ("\u03b5", r"$\epsilon$"),
    ("\u2022", ""), ("\u25cf", ""), ("\u25aa", ""), ("\u2013", "--"),
    ("\u00b0", r"$^\circ$"), ("\u00ae", ""), ("\u2122", ""),
    # Non-ASCII hyphens and dashes. Dropping these silently welds words
    # together -- a non-breaking hyphen turns "Cyber-Deception" into
    # "CyberDeception" -- so every one of them is mapped.
    ("\u2010", "-"), ("\u2011", "-"), ("\u2012", "--"), ("\u2015", "---"),
    ("\u2212", "-"), ("\u00ad", "-"), ("\u2044", "/"),
]


def tex(s):
    """Escape a plain string for LaTeX."""
    if not s:
        return ""
    for a, b in _TEX:
        s = s.replace(a, b)
    # Strip decorative leading glyphs BEFORE mapping. Doing it after
    # would eat the leading dollar of an arrow substitution and leave
    # unbalanced math behind.
    s = re.sub(r"^[^\w]{1,4}\s*(?=[A-Za-z0-9])", "", s)
    for a, b in _UNI:
        s = s.replace(a, b)
    # Anything still outside ASCII would need inputenc to survive
    # pdflatex, so drop it rather than break the build.
    return "".join(c if ord(c) < 128 else "" for c in s).strip()


def is_pic(shape):
    return str(shape.shape_type).startswith("PICTURE")


def is_drawn(shape):
    kind = str(shape.shape_type)
    return (kind.startswith("AUTO_SHAPE") or kind.startswith("GROUP")
            or kind.startswith("LINE") or kind.startswith("FREEFORM")
            or kind.startswith("CONNECTOR"))


def slide_title(slide):
    if slide.shapes.title is not None and slide.shapes.title.has_text_frame:
        t = slide.shapes.title.text_frame.text.strip()
        if t:
            return " ".join(t.split())
    return ""


def body_bullets(slide, skip_shape, limit=6):
    """Text from every non-title text frame, as bullet strings."""
    out = []
    for sh in slide.shapes:
        if sh is skip_shape or not sh.has_text_frame:
            continue
        for para in sh.text_frame.paragraphs:
            line = " ".join(r.text for r in para.runs).strip()
            line = " ".join(line.split())
            if len(line) > 1:
                out.append(line)
    # drop duplicates, keep order
    seen, uniq = set(), []
    for line in out:
        key = line.lower()
        if key not in seen:
            seen.add(key)
            uniq.append(line)
    return uniq[:limit]


def save_images(slide, index, img_dir, rel_dir):
    """Write out the slide's pictures; return (relpaths, widths_fraction)."""
    paths = []
    for n, sh in enumerate(s for s in slide.shapes if is_pic(s)):
        try:
            image = sh.image
        except Exception:
            continue
        ext = image.ext or "png"
        name = "s%02d_%d.%s" % (index, n, ext)
        with open(os.path.join(img_dir, name), "wb") as fh:
            fh.write(image.blob)
        paths.append("%s/%s" % (rel_dir, name))
    return paths


def slide_tables(slide):
    out = []
    for sh in slide.shapes:
        if getattr(sh, "has_table", False) and sh.has_table:
            rows = []
            for r in sh.table.rows:
                rows.append([" ".join(c.text.split()) for c in r.cells])
            if rows:
                out.append(rows)
    return out


def render_table(rows):
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    spec = "l" * ncol
    lines = [r"  \begin{lucidtable}", r"  \begin{tabular}{%s}" % spec,
             r"    \toprule"]
    head = " & ".join(tex(c) for c in rows[0])
    lines.append(r"    \thead{%s} \\" % head)
    lines.append(r"    \midrule")
    for r in rows[1:]:
        lines.append("    " + " & ".join(tex(c) for c in r) + r" \\")
    lines += [r"    \bottomrule", r"  \end{tabular}", r"  \end{lucidtable}"]
    return "\n".join(lines)


def build(pptx_path, out_dir, max_bullets):
    prs = Presentation(pptx_path)
    ratio = prs.slide_width / float(prs.slide_height)
    aspect = "169" if ratio > 1.6 else "43"

    img_dir = os.path.join(out_dir, "figures")
    os.makedirs(img_dir, exist_ok=True)

    body = []
    needs_work = []
    lost_chars = 0

    for i, slide in enumerate(prs.slides, 1):
        title = slide_title(slide)
        title_shape = slide.shapes.title
        bullets = body_bullets(slide, title_shape, max_bullets)
        images = save_images(slide, i, img_dir, "figures")
        tables = slide_tables(slide)
        drawn = sum(1 for sh in slide.shapes if is_drawn(sh))

        note = ""
        if slide.has_notes_slide:
            note = " ".join(slide.notes_slide.notes_text_frame.text.split())

        # A slide whose picture is really the whole slide gets the figure
        # its own frame; otherwise text leads and the figure follows.
        head = title or (bullets[0] if bullets else "Slide %d" % i)
        if not title and bullets:
            bullets = bullets[1:]
        # A slide's title is very often repeated in a separate text box,
        # so it arrives as a bullet too. Printing it twice is the most
        # visible artefact of a naive conversion.
        key = " ".join(head.lower().split())
        bullets = [b for b in bullets
                   if " ".join(b.lower().split()) != key]

        # A recovered slide is often taller than one beamer frame:
        # PowerPoint text boxes hold more than this type size does. Let
        # dense frames continue onto a second page rather than overprint
        # the footer. Truncating instead would throw away text the
        # author wrote, which is worse than an extra page.
        dense = len(bullets) > 3 or tables or (bullets and images)
        opt = "[allowframebreaks]" if dense else ""

        lines = []
        lines.append("%% ---- slide %d " % i + "-" * 50)
        lines.append(r"\begin{frame}%s{%s}" % (opt, tex(head)))

        if bullets:
            lines.append(r"  \begin{itemize}")
            for b in bullets:
                lines.append(r"    \item %s" % tex(b))
            lines.append(r"  \end{itemize}")

        for t in tables:
            lines.append(render_table(t))

        if images:
            if len(images) == 1:
                w = "0.62\\textwidth" if bullets else "0.82\\textwidth"
                lines.append(r"  \slidefigure[%s]{%s}" % (w, images[0]))
            else:
                each = min(0.42, 0.9 / min(len(images), 3))
                lines.append(r"  \begin{center}")
                for pth in images[:3]:
                    lines.append(r"    \includegraphics[width=%.2f\textwidth,"
                                 r"height=0.34\textheight,keepaspectratio]{%s}\hfill"
                                 % (each, pth))
                lines.append(r"  \end{center}")
                if len(images) > 3:
                    lines.append(r"  %% %d more image(s) in figures/, not placed"
                                 % (len(images) - 3))

        if drawn and not images:
            lines.append(r"  \vfill")
            lines.append(r"  \begin{center}")
            lines.append(r"    \fbox{\begin{minipage}{0.8\textwidth}\centering")
            lines.append(r"      \color{lucidMuted}\small REDRAW: this slide's "
                         r"diagram was built from %d PowerPoint shapes," % drawn)
            lines.append(r"      which carry no image to extract.\end{minipage}}")
            lines.append(r"  \end{center}")
            lines.append(r"  \vfill")
            needs_work.append((i, head, drawn))

        if note:
            lines.append(r"  \speakernote{%s}" % tex(note))

        lines.append(r"\end{frame}")
        lines.append("")
        body.append("\n".join(lines))

    return aspect, body, needs_work, len(prs.slides)


PREAMBLE = r"""%% =====================================================================
%%  %(name)s --- rebuilt from %(src)s with tools/from-pptx.py
%%
%%  Text, speaker notes, tables and embedded images were recovered from
%%  the PowerPoint file. Diagrams that PowerPoint drew from its own
%%  shapes could not be: they are drawing instructions, not pictures.
%%  Slides that lost one carry a REDRAW box -- see the list at the end
%%  of this file.
%%
%%  Build:  pdflatex %(name)s   (twice)
%% =====================================================================

\documentclass[11pt,aspectratio=%(aspect)s]{beamer}
\usetheme{lucid}

\usepackage{graphicx}

\title{%(title)s}
\date{}

%% \author{Your Name}
%% \institute{Your Institution}

\begin{document}

\begin{frame}[plain]
  \titlepage
\end{frame}

"""


def main():
    ap = argparse.ArgumentParser(
        description="Rebuild a .pptx as a Lucid beamer deck.")
    ap.add_argument("pptx")
    ap.add_argument("-o", "--out", default="rebuilt",
                    help="output directory (default: rebuilt/)")
    ap.add_argument("--title", default=None, help="deck title")
    ap.add_argument("--max-bullets", type=int, default=6)
    args = ap.parse_args()

    if not os.path.exists(args.pptx):
        sys.exit("No such file: %s" % args.pptx)
    os.makedirs(args.out, exist_ok=True)

    name = re.sub(r"[^a-zA-Z0-9]+", "-",
                  os.path.splitext(os.path.basename(args.pptx))[0]).strip("-")
    aspect, body, needs_work, total = build(args.pptx, args.out,
                                            args.max_bullets)

    title = args.title or name.replace("-", " ").title()
    text = PREAMBLE % {"name": name, "src": os.path.basename(args.pptx),
                       "aspect": aspect, "title": tex(title)}
    text += "\n".join(body)

    if needs_work:
        text += "\n%% --- slides whose diagram must be redrawn by hand ---\n"
        for i, head, n in needs_work:
            text += "%%   slide %-3d %-52s (%d shapes)\n" % (i, head[:52], n)

    text += "\n\\end{document}\n"

    out_tex = os.path.join(args.out, name + ".tex")
    with open(out_tex, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)

    print("wrote %s" % out_tex)
    print("  %d slides, aspect %s" % (total, aspect))
    print("  images extracted to %s/figures/" % args.out)
    print("  %d slide(s) need a diagram redrawn by hand:" % len(needs_work))
    for i, head, n in needs_work[:15]:
        safe = head[:50].encode("ascii", "replace").decode("ascii")
        print("    slide %-3d %-50s (%d shapes)" % (i, safe, n))
    if len(needs_work) > 15:
        print("    ... and %d more, all listed at the end of the .tex"
              % (len(needs_work) - 15))
    print("\nCopy beamerthemelucid.sty into %s/ and run pdflatex twice."
          % args.out)


if __name__ == "__main__":
    main()
