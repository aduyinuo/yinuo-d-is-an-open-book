---
icon: high-definition
---

# Toward Deployment

## Sim2Real Challenges in Cybersecurity

Sim2real refers to the long standing challenge encountered by embodied agents — between where a policy is trained and where it would run. Dynamics and sensing differ between the training world and the real one. A policy drifts as the deployment ages away from the data it was built on. And any safety we claim has to hold while the model is wrong, because out of distribution it will be.

In the cyber setting ...

## Where We Are at Year-1 (There's Much Work To Do...)

To find a solution we must first understand the problem. [**When We Say "A Realistic Cyber Environment"**](when-we-say-a-realistic-cyber-environment.md)**,** what exactly does it entail? In this project we take on the ambitious mission to define an actionable taxonomy of realism based on consensus from all the relevant parties.

How about we bypass the problem altogether? If transferring from sim to real is a dead end, can we [**Train in "Realistic" Environments Directly**](training-in-realistic-environments.md)? How much will we pay for the high fidelity training environment? Will it be worth it?

But then again...before the dreams come true and we get unlimited amount of access to operational environments for training purposes, how do we evaluate and improve our methods for sim2real? One key insight we had is that the sim2real challenge can be transformed to a sim2sim without loss of its complexity. So perhaps we can tackle [**sim2sim before sim2real**](transfer-to-realistic-environments.md)?

[**Cyber Environments & Benchmarks**](../../blogs/cyber-environments-and-benchmarks/) is a collection of cyber environments that I used, adapted, built in my various projects.

_Last updated: 2026-08_
