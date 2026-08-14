# Annotated Slides — GitBook integration

Renders a deck inline in a GitBook page using a ContentKit `webframe`, which is
GitBook's supported way to run an external page inside content. Raw `<iframe>`
tags are blocked by GitBook's content security policy, so this is the route that
is documented to work.

## Publish and install

Node 18+ required.

```bash
npm install -g @gitbook/cli
gitbook auth                      # paste a personal access token from
                                  # gitbook.com -> Settings -> Developer
cd integrations/slides
gitbook publish .
```

`gitbook publish` prints the integration's page. Open it, click **Install**, and
choose the space for this site.

## Use

Either paste a deck URL onto a page —

    https://aduyinuo.github.io/yinuo-d-is-an-open-book/slides/asu-brown-bag.html

which the block claims through `urlUnfurl` and turns into the deck — or insert
the **Annotated Slides** block and set `deck` to the file name without `.html`.

## Notes

* The deck posts `@webframe.ready` and `@webframe.resize` so the frame sizes
  itself to the current slide plus its narration.
* Decks are built from `slides-source/*.pptx` by
  `internal/slides/pptx_to_deck.py` and published to the `gh-pages` branch under
  `/slides/`.
* If you move the site, change `BASE` in `src/index.tsx`, the `urlUnfurl` entry
  in `gitbook-manifest.yaml`, and `SLIDES_BASE_URL` for the converter.
