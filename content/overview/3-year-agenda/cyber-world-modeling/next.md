---
icon: crystal-ball
---

# Next

## When the model is wrong in the place that matters

Every learned model is wrong somewhere. In an adversarial setting that is not a rounding error, because the adversary is the process that looks for the region where the model is confidently wrong and operates there. The question is whether a defender can be made robust to its own model's blind spots — detecting when the opponent latent has drifted, bounding how badly a wrong model can hurt, preferring a model that fails honestly (wide and uncertain) over one that fails silently (sharp and wrong). Factoring helps frame this, because the error can be localized to the opponent latent rather than the whole state, but it does not by itself answer it.

## Expedite strategic search with world models

Once a world model exists, the interesting use is not only prediction but acceleration: imagined rollouts can stand in for expensive environment interaction when computing a best response inside PSRO. Co-learning a world model with the empirical game is not itself new — Dyna-PSRO does exactly this. The open question is what a _faulty, adversarialy-stressed_ model does to that loop. Does model-based imagination still reduce the regret PSRO leaves on the table, or does a wrong model inject a bias that the game-solving step then amplifies? When does imagination help, and when is it worse than honest, slower interaction? This is where "what if the world model is faulty" and "use the world model to expedite PSRO" turn out to be the same question asked twice.

_Last updated: 2026-08_
