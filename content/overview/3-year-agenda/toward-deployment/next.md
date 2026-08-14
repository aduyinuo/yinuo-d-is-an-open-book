---
icon: crystal-ball
---

# Next

## Winning for the right reasons

A transferred policy that scores well has either learned the task or learned the benchmark, and the score alone will not say which. The open question is a test that separates them: causal probes that perturb the parts of the environment a genuine policy should depend on and a benchmark-reader should not, held-out kinds of realism the policy never trained against, counterfactual episodes built to fail a policy that has memorised surface structure. Transfer is only evidence of deployment-readiness if it survives being actively doubted.

## Drift after deployment

A policy is built on a snapshot; the network it defends keeps moving. Knowing when a deployed policy has aged out of usefulness — before it fails rather than after — is an open detection problem: watching for the distribution shift that matters to _this_ policy rather than shift in general, and deciding when to retrain, roll back, or hand control to a human.

## Behavior while the model is wrong

Out of distribution the model is wrong, and safety has to mean something anyway. Bounding worst-case behavior under model error — so that being wrong degrades the defender gracefully instead of catastrophically — is the last open piece, and the one that ties this thread back to the faulty-model question in [Cyber World Modeling](../cyber-world-modeling/next.md): a deployed defender and a defender with a wrong world model are facing the same danger from two sides.

_Last updated: 2026-08_
