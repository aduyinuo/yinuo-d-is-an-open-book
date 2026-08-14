---
icon: connectdevelop
---

# Cyber World Modeling

Before an agent can defend a network it has to hold a model of one — and of whoever is moving through it. The trouble is that those are two different kinds of thing arriving on the same wire, and a model that cannot tell them apart will be confidently wrong in exactly the place an adversary is working.

## The puzzle

**Fundamental — two sources of change, one stream of observation.** Everything a world model has to explain between one step and the next comes from two processes that behave nothing alike. The network's own dynamics are close to stationary and roughly causal: reachability, topology, load. The adversary's contribution is strategic and non-stationary — it adapts to the defender, it hides, and it shifts precisely when the defender starts to model it well. Fold both into a single latent and they contaminate each other: an error in the opponent model bleeds into the estimate of the network, and an ordinary change in the network gets read as the adversary doing something deliberate. The question the thread keeps returning to is what a defender actually has to represent, and how that representation should be factored, so that being wrong about the adversary does not force it to be wrong about the world.

**Domain — the observations are adversarial and the compute is small.** Operationally, the stream a model learns from is degraded, intermittent, and partial: sensors are noisy or poisoned, the adversary spends genuine effort staying unobserved, and the gaps are not random but chosen by someone who profits from the defender's blind spots. The model also has to run where the decision is taken, on edge hardware with a fraction of the compute a latent world model would prefer. A luxury reconstruction of the whole state space is off the table on both counts. The representation has to be learnable from sparse, actively-hidden observation and cheap enough to query inside the control loop — which is what turns factoring from a tidy idea into a requirement. You cannot model, or defend, everywhere at once.

## Work so far

Two moves, each aimed at one face of the puzzle.

[**FOE-Dreamer**](environment.md) is a Dreamer-style latent world model that keeps the opponent in a latent of its own. Instead of one monolithic state it separates the environment's dynamics from the adversary's, so the opponent model stays separable and inspectable and an error there is contained rather than smeared across the whole representation — the factoring the fundamental challenge asks for, learned rather than hand-specified.

[**Learn Structure**](strategic-structure.md) takes on the second half. Given that most of a long interaction is not strategic, where does the strategic part live? The work makes strategic dependence a measurable quantity — how much value a defender forfeits by ignoring the opponent, as a function of the game's structure — generates games that contain a known amount of it, then learns that structure back and checks the recovery. Find where dependence is high and expensive game-theoretic reasoning can be spent there and nowhere else.

## What's still open

Neither move closes the thread, and this page is not meant to read as if it did. A learned world model is always wrong somewhere, and an adversary is exactly the process that searches for the region where it is wrong — a factored model that is confidently wrong about the opponent's latent may be worse than an honest monolith. And once a usable model exists, the sharper question is what to spend it on: whether an imperfect model can be used to expedite the search for strategic responses rather than only to roll the world forward. Those are the questions the thread turns on [next](next.md).

_Last updated: 2026-08_
