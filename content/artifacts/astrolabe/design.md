# Design

## Three layers

A static single-page frontend talks over a REST API to a FastAPI backend, which persists everything through SQLAlchemy to a single SQLite file.

The frontend draws the graph with Cytoscape.js and holds pipeline progress in client state. The backend owns the graph management, the scoring engine, the LLM integration layer, the transcript-and-annotation system, the hypergraph overlays, the timer, and the Polya-heuristic matcher. The database holds cards, edges, transcripts, annotations, timer sessions, hypergraph layers, reusable candidate sets, prompt templates, LLM configuration, and the case-review log.

That separation is deliberate: each pipeline stage is an independent endpoint, the LLM provider is an abstraction with pluggable backends, and adding a scoring dimension or an export format touches one file, not the whole system.

## The read-only guarantee

The design principle everything else is arranged around: **the source file is never written to.**

On first load the live document is copied once into a snapshot, and the app parses the snapshot. Restarting the server does *not* re-snapshot — so you can keep editing the live document while the app runs, and pull changes in only when you explicitly re-sync. Output back to the source is never an edit; it's pasteable markup you generate from the app and apply yourself.

Re-sync refreshes the source-derived fields on every card while **preserving all app-only data** — your rigor ratings, your timer history, your goal tags, your answered-state overrides. Cards that vanished from the source are kept and flagged as orphaned rather than deleted. Nothing about re-syncing loses work.

## The eleven scores

Cards are scored on a graph, in three families plus a timeline order.

**Blocking** — how much a card holds up others: child count, descendant count, and betweenness on the undirected combined graph.

**Decisiveness** — how much answering a card unblocks the rest: an AND–OR answered-propagation count, and a depth-weighted frontier-readiness measure that finds cards whose children are all answered but which are themselves open.

**Relevance** — how much a card matters to the goals: a personalized PageRank restarting from the goal set, and a distance decay from the goals.

**Combined** — relevance × decisiveness, relevance × blocking, and a live-reweightable weighted sum, all computed on min–max-normalized bases.

**Timeline** — the topological order of the origin edges, cycle-detected, with the lowest-order edge broken for layout when a cycle appears and a warning surfaced.

The scores are the answer to "which subproblem was actually the hinge" — a question that is otherwise settled by whoever argues hardest.

## Files

`parser.py` reads the source with a brace-depth macro parser; `ingest.py` snapshots, loads, and re-syncs; `graph.py` builds edges and traversals; `scores.py` computes the eleven dimensions; `polya.py` maps heuristics; `timer.py` rolls elapsed time up the parent chain; `export.py` reconstructs the source markup verbatim; `app.py` is the FastAPI server; `static/index.html` is the whole UI.

_Last updated: 2026-08_
