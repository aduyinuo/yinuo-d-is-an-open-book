# Use

A study session, start to finish. Setup is about fifteen minutes; a session runs as long as the task does.

## Start it

Python 3.9+ is all you need; dependencies install into a local virtual environment on first run.

```bash
cd astrolabe
bash run.sh          # serves at http://127.0.0.1:8000
```

The first run snapshots the source document, parses it, and creates the database. Later runs reuse both. Model calls are optional — export an `ANTHROPIC_API_KEY` to unlock the "refine with LLM" button, or leave it unset and the rule-based suggestions work offline.

## Define the operations taxonomy

What operations will a participant use in solving your problem? Register them once as a candidate set — the vocabulary the coders will annotate against.

```bash
curl -X POST http://localhost:8000/pipeline/candidate-sets \
  -H "Content-Type: application/json" \
  -d '{"category":"operations",
       "items":["understand_spec","design_structure","implement_module",
                "test_component","debug_issue","refactor","optimize"]}'
```

## Run the session

The participant thinks aloud and the subquestions get annotated as they emerge — add a card, type the subquestion, start its timer. Only one timer runs at a time; stopping it rolls the elapsed time up the parent chain so each node carries its accumulated total. Let the structure emerge rather than imposing it.

The tells worth catching while they work: *"first, let me break this into…"* is a decomposition; *"this is like the problem where…"* is pattern recognition; *"wait, let me check that"* is verification; a long pause is deep thinking, not a cue to interrupt.

## Code it, and check agreement

If you recorded audio, upload and transcribe it, then have two coders annotate the same segments independently:

```bash
curl -X POST http://localhost:8000/transcript/t123/annotation \
  -H "Content-Type: application/json" \
  -d '{"annotator":"alice","item_id":"seg_001","label":"decompose_problem",
       "start_char":450,"end_char":650}'
```

Then ask the app where they disagreed:

```bash
curl "http://localhost:8000/transcript/t123/agreement"        # percent + kappa
curl "http://localhost:8000/transcript/t123/agreement.csv"    # the report
```

The segments where coders split are the segments where the operation is genuinely ambiguous — which is the part worth studying, not smoothing away.

## Export

```bash
curl http://localhost:8000/graph  > graph.json     # structure
curl http://localhost:8000/scores > scores.json    # the 11 dimensions
curl http://localhost:8000/timer  > timers.json    # time per card
```

CSV exports of the graph, scores, timeline and agreement matrix drop straight into Gephi, NetworkX, R or Python for the write-up.

## Scaling to many participants

Either reset the database for a clean start per participant, or keep one database and scope each participant to a different `project_id` — the API handles the isolation, so a multi-study instance needs no extra setup.

_Last updated: 2026-08_
