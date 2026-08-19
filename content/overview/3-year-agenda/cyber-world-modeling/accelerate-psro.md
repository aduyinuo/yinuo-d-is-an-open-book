---
icon: gauge-high
---

# AcceleratePSRO

A world model is useful for more than prediction.

## The intuition

Once a world model exists, the interesting use is not only prediction but acceleration: imagined rollouts can stand in for expensive environment interaction when computing a best response inside PSRO.

Co-learning a world model with the empirical game is not itself new — Dyna-PSRO does exactly this. The open question is what a _faulty, adversarially-stressed_ model does to that loop. Does model-based imagination still reduce the regret PSRO leaves on the table, or does a wrong model inject a bias that the game-solving step then amplifies? When does imagination help, and when is it worse than honest, slower interaction?

This is where "what if the world model is faulty" and "use the world model to expedite PSRO" turn out to be the same question asked twice.

## Where acceleration can be introduced

The working question is where a PSRO-like loop can be sped up without losing solution quality — which of its steps tolerate approximation, and which do not. Three outputs carry the track:

1. a catalogue of the acceleration levers available in the loop
2. a risk register for the approximation shortcuts each lever takes
3. a validation protocol that says whether an accelerated run reached the same place a slower one would have

## Environment

The work runs against **CyGym**, a simulation-based game-theoretic analysis framework for cybersecurity, which supplies the empirical game the loop is solved over.

**Related:** [FOE-Dreamer](environment.md) supplies the factored world model, [Learn Structure](strategic-structure.md) says where in the game strategic reasoning is worth spending, and [Next](next.md) carries the open questions this track sits inside.

_Last updated: 2026-08_
