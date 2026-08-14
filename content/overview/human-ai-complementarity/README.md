---
icon: hand-holding-hand
---

# Human-AI Complementarity

Assigning a person and an agent to the same task does not by itself produce a team. Their interaction has a structure, meaning who can approve an action, what information they share, and what each learns from the other, and that structure is usually left unspecified. An unspecified structure cannot be varied or measured, so its effect on the outcome cannot be studied.

Part of what makes this difficult is that the benefit of pairing a person with an agent often comes from each having information the other cannot fully state: the person's judgment, the agent's internal representation. When that information cannot be stated, it is not obvious how to build an interface that transfers it, or how to determine whether the pair produced a result that neither would have produced alone rather than one party deferring to the other.

In cyber defense the team's structure also has consequences that make it more than a design detail. An agent can act faster than a person can review; some actions cannot be undone; the person remains accountable; and whether the person trusts the agent's recommendation often decides the outcome. When such a team performs poorly, distinguishing a failure of the authority structure from a failure of a message reaching the right party, or a failure of the underlying decision, requires detailed records of what happened.

The thread builds instruments for studying this. [Team Defense Game](team-defense-game.md) pairs one person and one agent on a shared network, connected through an approval mechanism and a shared resource, with an agent that learns from the actions the person takes. [CHART](chart.md) represents a team's structure as a directed graph that the software enforces, so that changing the structure is a controlled manipulation. [CyberAgentFlow](cyberagenttrace.md) records agent workflows in enough detail to examine their behavior directly.

Two questions remain open: how to measure complementarity, and whether information that a person or an agent cannot state can still be transferred between them. They are described on the [next](next.md) page.

_Last updated: 2026-08_
