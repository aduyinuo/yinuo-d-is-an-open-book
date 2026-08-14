---
icon: crystal-ball
---

# Next

Three questions follow from this thread.

The first is how to show that a transferred policy performs well for the right reasons rather than because it has learned features specific to the benchmark. A score on the new environment does not establish this. What is needed is a test that separates the two cases: perturbing the parts of the environment that a competent policy should depend on and a benchmark-specific one should not, evaluating on forms of realism the policy was not trained on, and constructing cases designed to fail a policy that has memorized surface features. Transfer supports a claim of readiness for deployment only if it survives this kind of test.

The second is how to detect that a deployed policy has become unreliable as its environment changes. A policy is trained on a fixed description of a network that continues to change after deployment. Detecting when that change is large enough to matter for a particular policy, rather than change in general, and deciding whether to retrain, revert, or transfer control to a person, is unresolved.

The third is how a policy should behave while its model is inaccurate. Outside its training distribution the model is wrong, and a claim of safety has to hold even then. Bounding the worst-case behavior of a policy under model error, so that being wrong reduces performance gradually rather than sharply, is the remaining question. It connects to the question of the inaccurate world model in [Cyber World Modeling](../cyber-world-modeling/next.md): a deployed defender and a defender with an inaccurate world model face the same problem from two directions.

_Last updated: 2026-08_
