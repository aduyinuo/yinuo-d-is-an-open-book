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

## Converting locally (optional)

    pip install python-pptx
    python internal/slides/pptx_to_deck.py

Output lands in `docs/slides/`.
