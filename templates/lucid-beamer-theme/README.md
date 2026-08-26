# The Lucid Beamer Theme

A clean beamer theme for research talks. Large type, sparse slides, one accent
colour, and no author or institution anywhere unless you ask for it.

**Start with `main.tex`** — a working deck, already set up. Change the title,
replace the slides, done.

**`demo.pdf` is the manual** — every component shown next to the code that
made it.

## What's in here

```
main.tex               START HERE -- a working deck to edit
beamerthemelucid.sty   the theme itself
demo.tex / demo.pdf    the manual: each component with its code
snippets/*.tex         every code block as its own file, ready to copy
refs.bib               sample bibliography
tools/to-pptx.py       convert a compiled PDF to PowerPoint
```

Compile with **pdfLaTeX**, twice. A third pass if you use citations.

## Quick start

```latex
\documentclass[11pt,aspectratio=43]{beamer}   % 169 for widescreen
\usetheme{lucid}

\title{Your Title}
\date{}

\begin{document}

\begin{frame}[plain]
  \titlepage
\end{frame}

\section{First section}

\begin{frame}{A slide}
  \begin{itemize}
    \item A point worth making
  \end{itemize}
\end{frame}

\end{document}
```

## Components

Each row has a matching file in `snippets/` you can copy from.

| You write | You get | Snippet |
|---|---|---|
| `\begin{frame}{Title}` | a slide | `new-slide` |
| `\section{Name}` | an outline slide, current section marked | `sections` |
| `\term{x}` | primary term — accent, bold | `color` |
| `\altterm{x}` | secondary term — teal, italic | `color` |
| `\hl{x}` | amber highlight, the emphasis device | `color` |
| `\ul{x}` | underline | `color` |
| `\tint{gold}{x}` | any palette colour by name | `color` |
| `\slidefigure[w]{f}` | centred, uncaptioned figure | `figure` |
| `\figcaption{x}` | a caption, when one is needed | `figure` |
| `figuretext[0.55]` … `\nextpane` | two panes | `figure-text` |
| `lucidtable` + `\thead{}` | horizontal-rule table | `table` |
| `\citeline{x}` | small source line at the slide foot | `references` |
| `\cite{key}` + `\bibliography` | real citations from a `.bib` | `references` |
| `\takeaway{x}` | one sentence across the slide | `closing` |
| `\speakernote{x}` | a speaker note | `notes` |
| `\begin{hidden}` … | a parked slide | `hide-slide` |
| `\backupframes` | backup slides, outside the page count | `backup` |
| `steps`, `\stepafter`, `\showfrom` … | animation | `animation` |
| `align*`, `cases`, `theorem` … | maths and statements | `math` |
| `lstlisting` | code on a slide | `code` |

## Animation

An overlay is **not motion**. Each step prints as another **page** of the PDF,
showing a little more. A frame with three steps becomes three pages — which is
why an animated deck has more pages than slides.

```latex
\begin{steps}          % bullets appear one at a time
  \item First
  \item Second
\end{steps}

\stepafter             % break here; the rest lands on the next page
\showfrom{2}{x}        % from page 2 on, space reserved before
\showonly{2}{x}        % only on page 2, no space reserved
\emphat{2}{x}          % highlighted on page 2, plain otherwise
\swap{2}{a}{b}         % a until page 2, then b in its place
```

Beamer's own `<1->`, `\pause`, `\only` and `\alt` still work.

To **print** an animated deck, add `handout` to `\documentclass` — every step
collapses back to one page per slide. See `snippets/handout.tex`.

## Two things with an on/off mode

**Speaker notes.** `notes=off` is the default: notes stay in your source and
are *not compiled*. That is the file you hand out.

```latex
\usetheme{lucid}                % off  -- notes not compiled (default)
\usetheme[notes=pages]{lucid}   % a typeset notes page after each slide
\usetheme[notes=only]{lucid}    % notes without slides -- a script
\usetheme[notes=second]{lucid}  % presenter view, notes on screen two
```

**Hidden slides.** Wrap anything in `hidden` to park it. `hidden=off` is the
default: the block is *not compiled*, so it is not in the PDF or the page
count.

```latex
\begin{hidden}
\begin{frame}{Cut for time}
  ...
\end{frame}
\end{hidden}
```

```latex
\usetheme[hidden=show]{lucid}   % compile them, to see what you parked
```

Better than commenting out, which is tedious to undo and invisible to a
search. Better than deleting, which loses the slide.

## Options

```latex
\usetheme[palette=maroon,notes=pages]{lucid}
```

| Option | Values (default first) |
|---|---|
| `palette` | `green`, `maroon`, `slate` |
| `font` | `cabin`, `helvet`, `none` |
| `footer` | `full`, `page`, `none` |
| `pagenumber` | `plain`, `total` |
| `outline` | `auto`, `manual` |
| `align` | `top`, `center` |
| `notes` | `off`, `pages`, `only`, `second` |
| `hidden` | `off`, `show` |
| `blind` | `false`, `true` |

### Anonymous submission

Nothing identifying is emitted unless you set `\author`, `\institute` or
`\lucidlogo`. `blind` suppresses all three even when set, so a deck flips to
anonymous without editing its front matter:

```latex
\usetheme[blind]{lucid}
```

## Converting to PowerPoint

```bash
pip install pymupdf python-pptx
python tools/to-pptx.py main.pdf --notes-from main.tex
```

Each PDF page becomes one slide, placed as a full-bleed image at the right
aspect ratio. Speaker notes are carried across and attached to the correct
slide by matching the frame title. A text layer goes into the notes too, so
the deck stays searchable.

**The text is not editable in PowerPoint,** and cannot be: these slides are
set by LaTeX, with its maths, fonts, spacing and TikZ drawings, none of which
has a faithful PowerPoint equivalent. This gives you a deck to *present* from,
or to hand to someone who requires `.pptx` — not one to rewrite there.

Convert a `handout` build if the deck is animated, or every overlay step
becomes its own near-identical slide.

```
--dpi 300     sharper, larger file      --dpi 150   smaller
-o talk.pptx  choose the output name
```

---

## Setup: Overleaf

1. **New Project → Upload Project**, and upload the zip. Overleaf keeps the
   folder structure, so `snippets/` still resolves.
2. Open `main.tex` and press **Recompile**. Press it again — the outline
   slides need a second pass.
3. If the compiler is not already pdfLaTeX: **Menu → Compiler → pdfLaTeX**.
4. To switch which file builds: **Menu → Main document**.

To add the theme to a project you already have, upload just
`beamerthemelucid.sty` and add `\usetheme{lucid}`.

Everything used here is on Overleaf. Nothing needs installing.

## Setup: VS Code + LaTeX Workshop

1. Install **TeX Live** (or MiKTeX) so `pdflatex` is on your `PATH` — check
   with `pdflatex --version`.
2. Install the **LaTeX Workshop** extension (James Yu).
3. Open **this folder** (not a parent — `snippets/` paths are relative to the
   `.tex`). Open `main.tex` and save. It builds on save and opens the PDF
   beside it.

The default `latexmk` recipe runs enough passes. If you switched to a plain
`pdflatex` recipe, make it run twice — `Ctrl+Shift+P` → *Preferences: Open
User Settings (JSON)*:

```json
{
  "latex-workshop.latex.recipes": [
    { "name": "pdflatex x2", "tools": ["pdflatex", "pdflatex"] }
  ],
  "latex-workshop.latex.tools": [
    {
      "name": "pdflatex",
      "command": "pdflatex",
      "args": ["-synctex=1", "-interaction=nonstopmode",
               "-file-line-error", "%DOC%"]
    }
  ],
  "latex-workshop.latex.outDir": "%DIR%/build"
}
```

---

## Requirements

pdfLaTeX, with `beamer`, `tikz`, `booktabs`, `appendixnumberbeamer`, `comment`,
`ulem`, `cabin` and `newtxsf`. All are in a full TeX Live or MiKTeX install and
all are on Overleaf. Nothing is downloaded at compile time.

If `cabin` is missing the theme falls back to Helvetica and says so. You can
ask for that explicitly with `font=helvet`.

## Notes on the design

Colours are chosen so any two that carry different meaning stay apart in
greyscale, because handouts and posters get printed that way. The frame title
is told apart from body text by the band and its position rather than by
colour — which is why removing the band breaks more than it looks like it
should.

Text is deliberately large and slides deliberately sparse: about two
top-level bullets and 25–30 words. The third list level is styled to be
unappealing on purpose. Emphasis is a highlight, not bold — bold runs at about
3% of characters in decks that read well.
