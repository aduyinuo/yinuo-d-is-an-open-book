# Opportunity scout

Fills the four pages under `content/overview-4/` from eleven sources, daily.

## It runs itself

`.github/workflows/opportunities.yml` fetches, scores and rebuilds the pages
every morning at 05:00 El Paso time, and commits whatever changed. Nothing on
your machine has to be running — the sources are all public and need no key.

To run it by hand, double-click **`SCOUT.bat`** at the repo root. It does the
same three steps and asks whether to publish.

## The three steps

| Step | Does |
|---|---|
| `fetch.py` | reads every source in `sources.json`, normalises the results, drops duplicates keeping whichever copy knows a deadline → `raw.json` |
| `score.py` | scores each against `profile.json`, drops what has already closed → `scored.json` |
| `build_pages.py` | writes the four pages plus the index |

## Sources

| Stream | Where from |
|---|---|
| Conferences | CCF deadlines, sec-deadlines, ai-deadlines, WikiCFP (security, AI, HCI) |
| Funding | NSF upcoming-funding feed, Grants.gov search API |
| Postdoc and faculty | AcademicJobsOnline CS and postdoc listings; LinkedIn's public job search |
| Micro | Grants.gov, filtered to travel awards, seed and planning grants, workshops, early career |

Add a source by adding an entry to `sources.json`. `stream` decides which page it
lands on; `kind` picks the reader. A source that fails is reported and skipped,
and the rest still run.

## Scoring

`profile.json` holds the terms and their weights. A listing's score is the sum of
the terms that appear in its title, description or location, minus any penalty
terms. Every term that fired is printed on the page beside the score, so a
ranking can be argued with rather than trusted.

Edit the weights freely. Nothing in that file is inferred from anything — it is a
statement of what you want to see, and changing a number changes the ranking on
the next run.

## What it will not do

**Nothing is deleted, but not everything is shown at the top.** Anything scoring
below `threshold` is folded into an "Everything else found" block at the foot of
its page. Without that, the first screen of the funding page was ornithology
posts and marine policy fellowships. The only things dropped outright are
listings whose deadline has already passed and listings beyond the horizon.

**Relevance comes from the source as well as the words.** A security conference
is relevant because of the feed it was found in, not because its name contains a
keyword, so each source carries a `base` score added to every item from it. That
is what keeps USENIX Security on the page.

**It does not invent a deadline.** A listing with no date says so, and is ranked
by fit alone in its own section. Where a date was read out of prose rather than
given as a field, the page says that too.

**LinkedIn is opt-in and shallow.** LinkedIn's terms prohibit scraping, so the
only thing read is the guest endpoint LinkedIn serves to logged-out visitors —
one page per search, spaced out. There is no public way to harvest *posts*
without an account, so posts are not a source; positions are. Set
`"enabled": false` on that entry in `sources.json` to turn it off entirely.

**It does not follow links.** A row is built from what the source returned. The
link is there so a promising row can be read at its origin.
