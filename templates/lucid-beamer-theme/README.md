# The Lucid Beamer Theme

A clean beamer theme for research talks. Low text density, one accent colour,
a grey title band, and no author or institution anywhere unless you ask for it.

`demo.pdf` is the manual: every slide shows a component and the code that made
it. Open it first.

## What's in here

```
beamerthemelucid.sty   the theme -- the only file you actually need
demo.tex               the manual deck
demo.pdf               the manual, already built
snippets/*.tex         each code block as its own file, ready to copy
```

## Quick start

Put `beamerthemelucid.sty` next to your `.tex` file, then:

```latex
\documentclass[11pt,aspectratio=43]{beamer}
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

Compile with **pdfLaTeX**, twice. The second pass fills in the outline slides.

Use `aspectratio=169` for widescreen.

## Components

| You write | You get |
|---|---|
| `\section{Name}` | an outline slide with the current section marked |
| `\term{x}` | primary defined term, accent + bold |
| `\altterm{x}` | secondary defined term, teal + italic |
| `\hl{x}` | amber highlight — the emphasis device, instead of bold |
| `\slidefigure[width]{file}` | a centred, uncaptioned figure |
| `\figcaption{text}` | a caption, when one is genuinely needed |
| `figuretext[0.55]` … `\nextpane` … | two panes; the number is the left pane's share |
| `lucidtable` + `\thead{...}` | horizontal-rule table with a filled header row |
| `\citeline{text}` | small source line at the foot of the slide |
| `\takeaway{text}` | one sentence set across the slide |
| `\backupframes` | start backup slides; stops them inflating the page count |

Every snippet above is also a file in `snippets/`, so you can copy from there
rather than retyping.

## Options

```latex
\usetheme[palette=maroon,pagenumber=total]{lucid}
```

| Option | Values (default first) |
|---|---|
| `palette` | `green`, `maroon`, `slate` |
| `font` | `cabin`, `helvet`, `none` |
| `footer` | `full`, `page`, `none` |
| `pagenumber` | `plain`, `total` |
| `outline` | `auto`, `manual` |
| `align` | `top`, `center` |
| `blind` | `false`, `true` |

### Anonymous submission

Nothing identifying is emitted unless you set `\author`, `\institute` or
`\lucidlogo`. Adding `blind` suppresses all three even when they are set, so a
deck flips to anonymous without editing its front matter:

```latex
\usetheme[blind]{lucid}
```

---

## Setup: Overleaf

1. In Overleaf, **New Project → Upload Project**, and upload the zip.
   Overleaf unpacks it and keeps the folder structure, so `snippets/` still
   works.
2. Open `demo.tex` and press **Recompile**. Press it a second time — the
   outline slides need two passes.
3. Set the compiler if it is not already: **Menu → Compiler → pdfLaTeX**.
4. To start your own deck, add a new `.tex` file in the same project and set it
   as the main document (**Menu → Main document**). Keep
   `beamerthemelucid.sty` at the project root.

To add the theme to a project you already have, upload just
`beamerthemelucid.sty` into it and add `\usetheme{lucid}`.

Overleaf has Cabin and all other packages used here, so nothing needs
installing.

## Setup: VS Code + LaTeX Workshop

1. Install **TeX Live** (or MiKTeX) so that `pdflatex` is on your `PATH`.
   Check with `pdflatex --version` in a terminal.
2. In VS Code, install the **LaTeX Workshop** extension (James Yu).
3. Open this folder. Open `demo.tex`. Save — LaTeX Workshop builds on save by
   default, and the PDF opens in a side tab.

Two passes matter here too. The default `latexmk` recipe already runs enough
passes; if you switched to a plain `pdflatex` recipe, run it twice.

**If your build recipe is plain `pdflatex`**, add this to `settings.json`
(`Ctrl+Shift+P` → *Preferences: Open User Settings (JSON)*) so it always runs
twice:

```json
{
  "latex-workshop.latex.recipes": [
    {
      "name": "pdflatex x2",
      "tools": ["pdflatex", "pdflatex"]
    }
  ],
  "latex-workshop.latex.tools": [
    {
      "name": "pdflatex",
      "command": "pdflatex",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "%DOC%"
      ]
    }
  ]
}
```

To keep the build files out of the way, add:

```json
{
  "latex-workshop.latex.outDir": "%DIR%/build"
}
```

**Note:** `snippets/` paths in `demo.tex` are relative to the `.tex` file, so
open the folder itself in VS Code rather than a parent directory.

---

## Requirements

pdfLaTeX, and a TeX distribution with `beamer`, `tikz`, `booktabs`,
`appendixnumberbeamer`, `cabin` and `newtxsf`. All are in a full TeX Live or
MiKTeX install, and all are on Overleaf. No downloads happen at compile time.

If `cabin` is missing, the theme falls back to Helvetica on its own and warns.
You can also ask for that explicitly with `\usetheme[font=helvet]{lucid}`.

## Notes on the design

Colours are chosen so that any two that carry different meaning stay apart in
greyscale, because handouts and posters get printed that way. The frame title
is told apart from body text by the band and its position rather than by
colour — which is why removing the band breaks more than it looks like it
should.

Text is deliberately large and slides deliberately sparse: about two top-level
bullets and 25–30 words. The third list level is styled to be unappealing on
purpose.
