---
icon: high-definition
---

# Toward Deployment

Almost everything in autonomous cyber defense is trained somewhere other than where it would be used. This thread takes that seriously instead of treating it as a footnote — and it is the one place in the program where the discipline is subtraction rather than construction: not believing a result until it has survived the move out of the environment that produced it.

## The puzzle

The gap between where a policy is trained and where it would run is the same gap embodied agents hit as sim-to-real, and it has the same three teeth. Dynamics and sensing differ between the training world and the real one. A policy drifts as the deployment ages away from the data it was built on. And any safety you claim has to hold while the model is wrong, because out of distribution it will be. In the cyber setting those teeth show up as three specific ways a good-looking result fails to mean what it says.

_Realism is asserted, not checked._ Two environments can agree on every feature and still describe the world completely differently, so "we evaluated in a realistic environment" is a claim almost no one puts to the test.

_A heavier environment costs more, and win rate hides whether it paid._ Training in a richer world is expensive, and the headline number can improve for reasons that have nothing to do with the added realism.

_A policy that transfers may be winning for the wrong reasons._ Move it to a new environment and a high score can mean it learned the task — or that it learned the benchmark.

## Work so far

[**When We Say "A Realistic Cyber Environment"**](when-we-say-a-realistic-cyber-environment.md) pins down what a realism claim could even mean, so that it can be checked rather than asserted.

[**Training in "Realistic" Environments**](training-in-realistic-environments.md) asks what the extra fidelity costs and why win rate can hide whether it worked.

[**Transfer to "Realistic" Environments**](transfer-to-realistic-environments.md) moves a policy across the gap without retraining it, and treats the crossing itself as the object of study.

[**Cyber Environments & Benchmarks**](cyber-environments-and-benchmarks/) is the ground the rest runs on — the environments, and what each one does and does not represent.

## What's still open

The thread's own next step is the hardest of its claims to secure: a way to show a transferred policy is winning for the right reasons and not reading the benchmark, plus detecting drift once deployed and bounding behaviour while the model is off-distribution. Those are taken up [next](next.md).

_Last updated: 2026-08_
