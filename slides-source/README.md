# Slides

Put a PowerPoint deck here, push, and it appears on the site.

## How to add a deck

1. Save your deck as `.pptx` in this folder, e.g. `foe-dreamer.pptx`.
   The file name becomes the web address, so keep it lowercase with dashes.
2. Type your narration in PowerPoint's **Notes** pane under each slide.
   That text appears beneath the slide on the website. Leave it empty if you
   don't want narration on a slide.
   * A blank line starts a new paragraph.
   * A line containing only `---` splits the notes, so the slide stays up and
     the narration advances one piece at a time when the reader clicks.
   * `**bold**` and `_italic_` work.
3. Push. GitHub Actions converts the deck and publishes it.

## How to put it on a page

Add this where you want it, replacing the file name:

    {% embed url="https://aduyinuo.github.io/yinuo-d-is-an-open-book/slides/foe-dreamer.html" %}

Before the GitBook integration is installed this shows as a link; after, it plays
inline. Either way the deck itself works, and any slide is linkable with `#s3`.

## Decks built from LaTeX

A deck whose diagrams PowerPoint drew from its own shapes — boxes, arrows,
connectors, groups — cannot be published this way. Those shapes carry no
image, so the converter drops them and the layout collapses into the gap.
That is what happened to the ASU brown bag deck.

For those, keep a LaTeX build beside the `.pptx`:

    slides-source/asu-brown-bag.pptx            the original, for narration
    slides-source/asu-brown-bag-latex/*.pdf     the compiled deck

The workflow renders that PDF, one image per page, so nothing can be lost.
Narration still comes from the `.pptx` notes, matched to pages by counting
frame starts. A folder ending `-latex` is picked up automatically.

To create one from an existing deck:

    python templates/lucid-beamer-theme/tools/from-pptx.py slides-source/talk.pptx \
        -o slides-source/talk-latex

## Converting locally (optional)

    pip install python-pptx pillow pymupdf
    python internal/slides/pptx_to_deck.py          # every .pptx

    # a deck that has a LaTeX build
    python internal/slides/pdf_to_deck.py slides-source/asu-brown-bag-latex/asu-brown-bag.pdf \
        --slug asu-brown-bag --notes slides-source/asu-brown-bag.pptx

Output lands in `docs/slides/`.
