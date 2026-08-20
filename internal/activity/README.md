# Activity board

Answers "what is she up to?" from real work, not counters.

## The two things you double-click

* **`refresh-activity-board.bat`** (repo root) — rebuilds everything.
* **`board-settings.bat`** (repo root) — the settings window.

Then commit and push in GitHub Desktop to publish.

## What a project is

A project is a **subfolder** inside a research folder:
`[2] Research Projects\2025-2026 LucidWorld\[1] 2025-2026 sample_efficient_FOEDreamer`.
`LucidWorld` is the thread it sits under, not a project. `Code`, `Literature`,
`Notes` and `Latex_…` are supporting folders and are skipped. A research folder
with no real project subfolders counts as one project itself.

Mac alias files (the ones under `IRB Applications`) cannot be followed from
Windows. They are listed in the settings window marked `alias` and unwatched —
double-click the folder cell and point them at the real place.

## The settings window

Everything the board does is set in `projects.json`, and the window edits it.
Double-click any cell:

| Column | Double-click does |
|---|---|
| Watch | on/off — off means not scanned at all |
| Heatmap | on/off — whether it counts in the big heatmap |
| Shown as | rename it; the display name is independent of the folder |
| Folder | folder picker; repoints the project, fixes an alias |
| Clockify | pick the matching Clockify project |

Below the table: the heatmap range (1 month, 3, 6, 1 year, all time, or a custom
pair of dates), and the Clockify key with a Test button.

**Find projects** re-scans the research folder and adds anything new without
touching what is already there.

## Clockify

The free plan allows 30 requests per hour per workspace; a refresh uses about
three, and results are cached for half an hour. The key is stored in
`secrets.json`, which is gitignored.

What it buys:

* Your typed description becomes the update sentence for that project.
* Your logged hours shade the heatmap and give the "this week" figure.
* Anything you logged never triggers the popup.

Without a key everything else still works; the hours are simply absent.

## The popup

`ask_max.py` opens at most **once an hour**, and only for a project that did
work Clockify has no entry covering. Each row carries the description (prefilled
from the diff), an editable hours figure guessed from the file timestamps, and a
tick naming the Clockify project.

**Save posts the entry to Clockify.** Nothing is ever posted without a
description you typed and Save pressed — Skip and closing the window post
nothing. It never asks twice about the same set of files.

`python ask_max.py --now` ignores the hour.

## Excludes

A project can carry an `exclude` list in `projects.json`, of paths relative to
its folder. The website project uses it so the board does not report on its own
generated output:

    "exclude": ["internal/activity", "content/.gitbook/assets", "docs"]

A project added to the board after the last run is baselined quietly on its
first pass, rather than announcing every file it contains as new.

## The pipeline

| Step | Does |
|---|---|
| `capture_changes.py` | snapshots every tracked file and diffs against the last snapshot |
| `summarize_changes.py` | turns those diffs into sentences; merges Clockify descriptions |
| `ask_max.py` | asks you about what is left, at most hourly |
| `collect_activity.py` | states, timestamps, hours, daily tallies → `activity.json` |
| `render_board.py` | heatmap PNGs + `content/personal/what-is-she-up-to.md` |

Sentences come from what the diff actually contains — new `\section{}` and `##`
headings, new `\cite` keys, new `def`/`class` names, new `\includegraphics`, new
bib entries, results files appearing. Never event counts, file counts or byte
totals. Word, PowerPoint and PDF files are named as changed but not read.

## Safety rails

* If the research folder is missing, `collect_activity.py` **refuses to write**
  and leaves the last good board alone. It used to overwrite it with blanks.
* `snapshot.json` holds the full text of unpublished work and is gitignored,
  along with `changes.json`, `updates.json`, `answers.json`, `clockify.json`,
  `last_asked.json` and `secrets.json`.

## Keeping it current

`.github/workflows/activity.yml` re-renders the heatmaps and the page from
`activity.json` on every push, so the published page always matches the last
collection. Collection itself has to run on the machine that can see `G:`. Use
Windows Task Scheduler on the `.bat` if you want it automatic.

## GitHub Projects

Not wired in. It needs a personal access token, which should not sit in this
repository. If you want it, add the token as a repository secret and extend
`collect_activity.py` with a function that reads item status changes the same
way `git_recent()` reads commits.
