# Design

_This is the intended design of a tool still on the waitlist. What's below is the MVP scope, not a shipped system._

## The MVP

Four pieces:

1. **An event schema** for human–agent research interactions — one typed record per interaction, so heterogeneous sources become comparable.
2. **Multi-provider ingestion adapters** — so interaction that happened across different agent platforms lands in one store.
3. **A provenance graph** with team, task, and cognition annotations — the interactions linked into a structure you can trace and query.
4. **Weekly diagnostics** for data quality and drift — because a collection substrate that silently degrades is worse than none.

## Five dimensions

The provenance graph annotates each interaction along five axes, so a single record can be read more than one way:

**Teamwork** — the coordination structure of the interaction. **Cognition** — the reasoning and problem-solving steps inside it. **Science quality** — whether the work meets the standards it claims. **Wellbeing** — the human's state through the interaction. **Organizational dynamics** — how the interaction sits inside larger structures of authority and process.

The point of annotating all five on the same record is that they are not separable in practice: a coordination breakdown is often a wellbeing signal, and a cognitive shortcut is often an organizational pressure.

## Consent as a gate, not a checkbox

The design commitment that shapes the rest: responses are captured only under an explicit, versioned protocol, and the protocol version is stored with the data. That means the exact instrument used for any given session can always be reconstructed, even after the protocol has moved on — the same discipline that makes a longitudinal study defensible rather than a moving target.

## Where it connects

This is the layer beneath the specific studies. [CHART](../chart/) generates one kind of interaction trace; [Astrolabe](../astrolabe/) codes another; Agentic Lab is the general substrate those specific instruments would feed into, with the consent and provenance guarantees carried through rather than reinvented per study.

_Last updated: 2026-08_
