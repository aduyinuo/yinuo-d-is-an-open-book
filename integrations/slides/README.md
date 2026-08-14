# Annotated Slides integration

Embeds a deck from `docs/slides/` inside a GitBook page using a ContentKit `webframe`,
which is GitBook's supported way to run an external page inline (raw iframes are blocked by
their CSP).

## One-time setup

1. Enable GitHub Pages on this repo: Settings -> Pages -> Source: `main`, folder `/docs`.
   Decks are then served at `https://aduyinuo.github.io/yinuo-d-is-an-open-book/slides/<slug>.html`.
2. Install the GitBook CLI and publish this integration:
   ```
   npm install -g @gitbook/cli
   gitbook auth
   cd integrations/slides && gitbook publish .
   ```
3. Install the integration on the space from the GitBook integrations page.

## Use

In a page, insert the **Annotated slides** block and set `deck` to the slug, e.g.
`cyber-world-modeling--environment`.

Until the integration is installed, each project page carries a plain link to the same deck,
so nothing is broken in the meantime.
