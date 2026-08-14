---
icon: head-side-gear
---

# Mental World Modeling

## Challenges

**I — the units of a working mind are grain-relative, transfer weakly, and are partly tacit.** To model someone solving a hard problem we need units to model them in: operations, steps, moves. But a long history of work on mental operations never settled on a single canonical set, and for good reason. The right grain might depend on the scale we are looking at — the same solve is a handful of steps or a thousand, depending on where you stand. General heuristics ("work backwards," "try a simpler case") transfer badly: people who can recite them still fail to deploy them, because knowing an operation and regulating when to use it are different capacities, and the regulation is the harder one. And much of what an expert does is tacit — not withheld, but genuinely unavailable to introspection — so it has to be recovered indirectly rather than asked for. Any model of a mind at work has to be built from units that will not sit still, out of evidence the mind itself cannot fully report.

**II — the mind is often hiding, or under a clock.** In cybersecurity the other agent is frequently an adversary who is actively using deception and who departs from optimal play in structured, repeatable ways. While the human problem-solving we want to support — an analyst, a competitor in capture-the-flag — happens under time pressure, where the gold-standard elicitation method, thinking aloud as you go, is exactly what you cannot ask for. The methods have to recover strategy from sparse, sometimes adversarial traces.

## Where We Are

[**Problem-Solving**](problem-solving/) — small groups, general computing work, and capture-the-flag — builds a deliberately coarse, reliability-first account of how people solve, and pairs it with elicitation that survives a live competition: stimulated recall anchored to submission logs, rather than think-aloud that would distort the thing it measures.

[**Opponent (Agent) Modeling**](opponent-agent-modeling/) is the adversarial half — how agents read each other into kinds across repeated interaction, and how to model an attacker whose biases are built into the reward, so that the defender it trains faces a realistic opponent instead of an idealized one.

## Future Work

Existing work in both agent-based modeling and human subject studies signals the necessity to find a consensus on the definition of mental operations, and that should be _learned_ rather than fixed — mental operations treated as reusable actions an agent discovers and composes, with a separate account of the control that decides which to use and when to quit.&#x20;

We attempt to tackle this problem [next](next.md).

_Last updated: 2026-08_
