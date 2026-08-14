---
icon: crystal-ball
---

# Next

The two pieces in this thread — a factored world model, and a way of finding where strategic dependence lives — are each a partial answer to a standing question, not a closed one. Three follow-ups are what the thread is actually pointed at.

## When the model is wrong in the place that matters

Every learned model is wrong somewhere. In an adversarial setting that is not a rounding error, because the adversary is the process that looks for the region where the model is confidently wrong and operates there. The question is whether a defender can be made robust to its own model's blind spots — detecting when the opponent latent has drifted, bounding how badly a wrong model can hurt, preferring a model that fails honestly (wide and uncertain) over one that fails silently (sharp and wrong). Factoring helps frame this, because the error can be localized to the opponent latent rather than the whole state, but it does not by itself answer it.

## Using an imperfect model to expedite strategic search

Once a world model exists, the interesting use is not only prediction but acceleration: imagined rollouts can stand in for expensive environment interaction when computing a best response inside PSRO. Co-learning a world model with the empirical game is not itself new — Dyna-PSRO does exactly this. The open question is what a _faulty, adversarially-stressed_ model does to that loop. Does model-based imagination still reduce the regret PSRO leaves on the table, or does a wrong model inject a bias that the game-solving step then amplifies? When does imagination help, and when is it worse than honest, slower interaction? This is where "what if the world model is faulty" and "use the world model to expedite PSRO" turn out to be the same question asked twice.

## The triple, under real constraints

The setting that motivates the whole thread — a defender that adapts fast, learns from little, and stays strategically robust, all on edge compute — asks for three things usually studied apart. Meta-learning gives fast adaptation; a factored world model gives sample efficiency; PSRO gives robustness to a changing adversary. Each pairing has been done on its own: meta-learned responses inside PSRO, a world model co-learned with the empirical game, MAML on a model-based learner. Putting all three together, and doing it inside a degraded-comms, edge-compute budget, is the bet this thread is working toward — not a result it can report yet.

_Last updated: 2026-08_
