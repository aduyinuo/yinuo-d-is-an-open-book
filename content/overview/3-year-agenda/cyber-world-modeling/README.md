---
icon: connectdevelop
---

# Cyber World Modeling

## **Challenges**

<mark style="color:$primary;">**I — multiple sources of change, one stream of observation.**</mark> Everything a world model has to explain between one step and the next comes from more than one processes that behave nothing alike. The network's own dynamics are close to stationary and roughly causal: reachability, topology, load. The adversary's contribution is strategic and non-stationary — it adapts to the defender, it hides, and it shifts precisely when the defender starts to model it well. Fold both into a single latent and they contaminate each other: an error in the opponent model bleeds into the estimate of the network, and an ordinary change in the network gets read as the adversary doing something deliberate.&#x20;

<mark style="color:$primary;">**II — the observations are adversarial and the compute is small.**</mark> Operationally, the stream a model learns from is degraded, intermittent, and partial: sensors are noisy or poisoned, the adversary spends genuine effort staying unobserved, and the gaps are not random but chosen by someone who profits from the defender's blind spots. More than often, the model also has to run where the decision is taken, on edge hardware with a fraction of the compute a latent world model would prefer. A luxury reconstruction of the whole state space is off the table on both counts. The representation has to be learnable from sparse, actively-hidden observation and cheap enough to query inside the control loop — which is what turns factoring from a tidy idea into a requirement. You cannot model, or defend, everywhere at once.

## Where We Are at Year-1

[**FOE-Dreamer**](environment.md) is a Dreamer-style latent world model that keeps the opponent in a latent of its own. Instead of one monolithic state it separates the environment's dynamics from the adversary's, so the opponent model stays separable and inspectable and an error there is contained rather than smeared across the whole representation. The factorization is learned rather than hand-specified.

[**Learn Structure**](strategic-structure.md) takes a step further and exploits the structure of factorized components. Given that most of a long interaction is not strategic, where does the strategic part live? We attempt to make strategic dependence a measurable quantity — how much value a defender forfeits by ignoring the opponent, as a function of the game's structure — generates games that contain a known amount of it, then learns that structure back and checks the recovery. Find where dependence is high and expensive game-theoretic reasoning can be spent there and nowhere else.

## Ongoing & Future Work

1. A learned world model is always wrong somewhere, and a factored model that is confidently wrong about the opponent's latent may be worse than an honest monolith. How can we decide if a world model is "reasonably accurate"? What types of "errors" are more or less acceptable for a defense agent in operational networks?
2. Once a "reasonably accurate" model exists, can we use to expedite the search for strategic responses rather than only to roll the world forward?

Those are the questions the thread turns on [next](next.md).

_Last updated: 2026-08_
