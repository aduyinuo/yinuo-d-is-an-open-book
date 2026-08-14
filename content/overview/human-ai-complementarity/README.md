---
icon: hand-holding-hand
---

# Human-AI Complementarity

## Challenges

**I — complementarity depends on knowledge neither side can fully state.** The reason a human-AI pair can beat either alone is that each holds knowledge it cannot completely externalize: the analyst's trained sense that something is off, the model's latent state. But if the useful knowledge cannot be put into words, two hard problems follow. You cannot build a clean interface across it — there is nothing to hand over — and you cannot easily tell whether complementarity actually happened or whether one party simply deferred to the other. The fundamental challenge is to make teaming a structure you can specify — who authorizes what, who sees what, who learns from whom — so that "complementarity" becomes a measurable variable, and to find protocols that move tacit knowledge across the human-AI boundary without demanding it be fully articulated first.

**II — in cyber defense the authority structure is a safety necessity.** An agent can act faster than a human can review; some defensive actions are irreversible; the human is accountable for what the agent does; and trust — the analyst deciding whether the recommendation on the screen is worth acting on — is the real bottleneck. So the structure of who may do what, and who has to see what before it happens, is load-bearing. And when such a team fails, the trace has to be detailed enough to say the failure was in the structure — an approval that routed wrong, an explanation that never arrived — rather than merely that the team lost.

## Where We Are

Three instruments, each turning a piece of the structure into something you can set and observe.

[**Team Defense Game**](team-defense-game.md) — one human, one agent, one network, coupled by approval, a shared pool, and an agent that learns from moves the human made and it did not. The team structure is the manipulation, not the backdrop.

[**CyberAgentFlow**](cyberagenttrace.md) instruments agent workflows so their behaviour can be examined rather than inferred — the traces you need before you can attribute a failure to anything at all.

[**CHART**](chart.md) makes team structure a directed graph: approvals route along control edges, explanations reach a panel, messages route by mention. Change the graph and you have changed the team, on purpose and on the record.

## Future Work

CHART is only a first step to capture the syntax of human-agent teamwork. Its completeness and succinctness remain to be tested. Can it express the teamwork in a SOC center or a incident response team? Can we prescribe, monitor, and diagnose human-agent teamwork represented with CHART? These questions are taken up [next](next.md).

_Last updated: 2026-08_

