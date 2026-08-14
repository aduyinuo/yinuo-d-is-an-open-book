# Activity board

Answers "what is she up to?" from real work, not counters.

## What it reads

`collect_activity.py` walks each research project folder and finds the most
recent file you actually authored — writing, code, data, slides, figures —
skipping conference templates, downloaded papers, checkpoints, and build
artifacts. It records what that file was and when, then labels the project:

* **at the desk** — touched in the last 6 hours
* **warm** — touched in the last week
* **resting** — older than that

The project touched most recently and still inside the 6-hour window is where
the avatar sits on the board. If nothing is that fresh, the board says away.

It also reads this repository's commit subjects, which is what the "what changed
on this site" list is made of.

## Running it

Double-click `refresh-activity-board.bat` at the repo root, or:

    python internal/activity/collect_activity.py
    python internal/activity/render_board.py

The first writes `activity.json`; the second writes the board image and
`content/personal/what-is-she-up-to.md`. Commit and push to publish.

It has to run on the machine that can see the research folders. Set
`RESEARCH_ROOT` if that path ever changes.

## Keeping it current

`.github/workflows/activity.yml` re-renders the board and page from
`activity.json` on every push, so the published page always matches the last
collection. To collect automatically, use Windows Task Scheduler to run the
`.bat` on a schedule.

## GitHub Projects

Not wired in. The GitHub Projects API needs a personal access token, which
should not sit in this repository. If you want it, add the token as a repository
secret and extend `collect_activity.py` with a function that reads item status
changes and appends them the same way `git_recent` does.
