---
icon: user-headset
---

# Agentic Lab

A consent-aware substrate for collecting and analysing researcher–agent interaction — across teamwork, cognition, science quality, wellbeing, and organizational dynamics.

<figure><img src="../../.gitbook/assets/mock-agentic-lab.png" alt="The Agentic Lab pipeline: ingestion adapters, a typed event schema, a provenance graph, and weekly diagnostics, all behind a versioned consent gate, with the five annotated dimensions"><figcaption>Ingestion to provenance graph, gated by a versioned consent protocol.</figcaption></figure>

## The problem it addresses

As people do more of their research work *with* agents, the interaction itself becomes data — but data that is scattered across providers, uneven in quality, and ethically loaded. Agentic Lab is the collection-and-analysis layer that makes that interaction into something you can study without losing the consent context that makes studying it legitimate.

## The shape of it

**Adapters** ingest from multiple providers into one place. A typed **event schema** turns each interaction into one structured record. Those records assemble into a **provenance graph** annotated along five dimensions — teamwork, cognition, science quality, wellbeing, and organizational dynamics — so the same interaction can be read as a coordination event, a cognitive step, or a wellbeing signal. Weekly **diagnostics** watch for data-quality problems and drift.

Under all of it sits a **consent gate**: block responses are saved only under an explicit, versioned protocol, so the exact instrument used for every session is preserved even as later protocol versions appear.

## Status

On the waitlist — the design and the MVP scope are set; the build is not yet underway. What's fixed: the event schema for human–agent interactions, the multi-provider ingestion adapters, the provenance graph with team/task/cognition annotations, and the weekly data-quality-and-drift diagnostics.

## More

* [Design](design.md) — the schema, the provenance graph, and the consent model

_Last updated: 2026-08_
