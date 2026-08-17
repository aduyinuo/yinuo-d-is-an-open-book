---
icon: head-side-gear
---

# Mental World Modeling

## Challenges

<mark style="color:$primary;">**I — lack of consensus on the foundational concept — "Mental Model”**</mark>**.** A long history of work on mental operations never settled on a single canonical definition. The right grain might depend on the scale we are looking at — the same solve is a handful of steps or a thousand, depending on where you stand. General heuristics ("work backwards," "try a simpler case") transfer badly: people who can recite them still fail to deploy them, because knowing an operation and regulating when to use it are different capacities. And much of what an expert does is tacit and genuinely unavailable to introspection.&#x20;

**II — k.** In cybersecurity the other agent is frequently an adversary who is actively using deception and who departs from optimal play in structured, repeatable ways. While the human problem-solving we want to support — an analyst, a competitor in capture-the-flag — happens under time pressure, where the gold-standard elicitation method, thinking aloud as you go, is exactly what you cannot ask for. The methods have to recover strategy from sparse, sometimes adversarial traces.

## Where We Are at Year-1

[**Problem-Solving**](problem-solving/) — small groups, general computing work, and capture-the-flag — builds a deliberately coarse, reliability-first account of how people solve, and pairs it with elicitation that survives a live competition: stimulated recall anchored to submission logs, rather than think-aloud that would distort the thing it measures.

[**Opponent (Agent) Modeling**](../opponent-agent-modeling/) is the adversarial half — how agents read each other into kinds across repeated interaction, and how to model an attacker whose biases are built into the reward, so that the defender it trains faces a realistic opponent instead of an idealized one.

## Ongoing & Future Work

Existing work in both agent-based modeling and human subject studies signals the necessity to find a consensus on the definition of mental operations, and that should be _learned_ rather than fixed — mental operations treated as reusable actions an agent discovers and composes, with a separate account of the control that decides which to use and when to quit.

We attempt to tackle this problem [next](next.md).

_Last updated: 2026-08_
