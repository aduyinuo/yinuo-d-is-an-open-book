# Refresh Button — GitBook integration

Puts a working button on a page. Pressing it starts a GitHub Actions workflow.

## Why this exists

GitBook renders markdown and runs no scripts, so nothing written into a page can
start anything — no `<button>`, no `<script>`, no link that does work. A
ContentKit block can, because the press is handled on the integration's own
runtime rather than in the reader's browser. That is the only route to a button
on the page, and it is what this is.

## What the button does

It dispatches a workflow in `aduyinuo/yinuo-d-is-an-open-book`:

| `workflow` prop | Runs | Effect |
|---|---|---|
| `board` (default) | `activity.yml` | pulls the day's logged time from Clockify, rebuilds the heatmaps and the In Action page |
| `opportunities` | `opportunities.yml` | re-fetches all eleven opportunity sources and rewrites the four queues |

The card reports back what happened — started, token missing, token refused,
workflow not found — rather than failing silently.

**It cannot scan the research folders.** Those are on a drive only Max's machine
can see, so what changed inside them is still picked up by the desktop icon.
The button covers everything else.

## Publish and install

Node 18+ is required and is not currently installed on this machine.

```bash
npm install -g @gitbook/cli
gitbook auth                      # a personal access token from
                                  # gitbook.com -> Settings -> Developer
cd integrations/refresh
npm install
gitbook publish .
```

`gitbook publish` prints the integration's page. Open it, press **Install**, and
choose the space for this site.

## Configure

In the space, open the integration's configuration and set:

* **GitHub token** — a fine-grained personal access token, scoped to this one
  repository, with **Actions: read and write**. Nothing else.
* **Repository** — defaults to `aduyinuo/yinuo-d-is-an-open-book`.
* **Branch** — defaults to `main`.

The token is held in the space installation's configuration, not in this repo.

## Use

Insert the **Refresh Button** block on a page. Leave it as it is for the board,
or set `workflow` to `opportunities` for the scout queues.
