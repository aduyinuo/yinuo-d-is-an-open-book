---
icon: high-definition
---

# Toward Deployment

Most methods in autonomous cyber defense are developed and tested in an environment different from the one where they would be deployed. This thread treats that gap as its central problem.

The gap between a training environment and a deployment environment is the same problem that embodied agents encounter as sim-to-real transfer, and it has the same components. The dynamics and the available observations differ between the two. A policy degrades as the deployed environment moves away from the data it was trained on. And a claim of safety has to hold while the model is inaccurate, because outside its training distribution it will be. In cyber defense this appears as three ways a good result can fail to mean what it appears to mean.

First, a claim that an environment is realistic is rarely tested. Two environments can share every listed feature and still represent the world differently, so a statement that a method was evaluated in a realistic environment often goes unverified.

Second, a more detailed environment costs more to train in, and an improvement in a summary metric may not be due to the added detail. Whether the additional realism is worth its cost is easy to leave unexamined.

Third, a policy that transfers to a new environment and scores well may have learned the task, or may have learned features specific to the benchmark. Its score does not distinguish these.

The thread's lines address these points. [When We Say "A Realistic Cyber Environment"](when-we-say-a-realistic-cyber-environment.md) examines what a claim of realism can be taken to mean. [Training in "Realistic" Environments](training-in-realistic-environments.md) examines the cost of added fidelity and why a summary metric can obscure whether it helped. [Transfer to "Realistic" Environments](transfer-to-realistic-environments.md) studies moving a policy across the gap without retraining it. [Cyber Environments & Benchmarks](cyber-environments-and-benchmarks/) describes the environments this work uses and what each does and does not represent.

Two questions remain open: how to show that a transferred policy performs well for the right reasons, and how to keep it reliable as the deployed environment changes. They are described on the [next](next.md) page.

_Last updated: 2026-08_
