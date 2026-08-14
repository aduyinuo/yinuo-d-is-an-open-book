---
icon: hand-holding-hand
---

# Human-AI Complementarity

Putting a person and an agent on the same task does not make them a team. What makes them a team is the structure between them — who may approve what, what they share, what each learns from the other — and that structure is usually left implicit, which means it cannot be varied, measured, or blamed when the team fails.

## The puzzle

**Fundamental — complementarity depends on knowledge neither side can fully state.** The reason a human-AI pair can beat either alone is that each holds knowledge it cannot completely externalize: the analyst's trained sense that something is off, the model's latent state. But if the useful knowledge cannot be put into words, two hard problems follow. You cannot build a clean interface across it — there is nothing to hand over — and you cannot easily tell whether complementarity actually happened or whether one party simply deferred to the other. The fundamental challenge is to make teaming a structure you can specify — who authorizes what, who sees what, who learns from whom — so that "complementarity" becomes a measurable variable, and to find protocols that move tacit knowledge across the human-AI boundary without demanding it be fully articulated first.

**Domain — in cyber defense the authority structure is a safety constraint, not a nicety.** An agent can act faster than a human can review; some defensive actions are irreversible; the human is accountable for what the agent does; and trust — the analyst deciding whether the recommendation on the screen is worth acting on — is the real bottleneck. So the structure of who may do what, and who has to see what before it happens, is load-bearing. And when such a team fails, the trace has to be detailed enough to say the failure was in the structure — an approval that routed wrong, an explanation that never arrived — rather than merely that the team lost.

## Work so far

Three instruments, each turning a piece of the structure into something you can set and observe.

[**Team Defense Game**](team-defense-game.md) — one human, one agent, one network, coupled by approval, a shared pool, and an agent that learns from moves the human made and it did not. The team structure is the manipulation, not the backdrop.

[**CHART**](chart.md) makes team structure a directed graph the software enforces: approvals route along control edges, explanations reach a panel, messages route by mention. Change the graph and you have changed the team, on purpose and on the record.

[**CyberAgentFlow**](cyberagenttrace.md) instruments agent workflows so their behaviour can be examined rather than inferred — the traces you need before you can attribute a failure to anything at all.

## What's still open

Making teaming a variable is not the same as knowing what to measure. The open question is a metric of complementarity itself — evidence that the team did something neither party would have alone, not merely that it won — together with protocols for moving tacit knowledge across the boundary in both directions. Those are taken up [next](next.md).

_Last updated: 2026-08_
