---
icon: high-definition
---

# Toward Deployment

## Sim2Real Challenges in Cybersecurity

Sim2real refers to the long standing challenge encountered by embodied agents — between where a policy is trained and where it would run. Dynamics and sensing differ between the training world and the real one. A policy drifts as the deployment ages away from the data it was built on. And any safety we claim has to hold while the model is wrong, because out of distribution it will be.

In the cyber setting each of those sentences changes meaning, and each change costs a project.

There is no physics to converge to. A robot's real world is governed by laws that hold whether or not anyone wrote them down, so a simulator can be wrong about them and can be made less wrong. A network is an artifact. It is whatever some organization built, configured, patched unevenly and then partly forgot, and two enterprises differ from each other more than two laboratory floors do. There is no single target to approach.

The real world has an occupant who wants to be missed. Friction does not adapt. An adversary does, and the parts of an environment that make adaptation possible, benign activity to blend into and telemetry to evade, are the parts current environments most often leave out.

There is no cheap real to transfer into. You do not get to try the policy on the production network and see what happens. Either you make training in a real enough environment affordable, or you learn to measure the gap without an operational network to measure against.

And the target is only partially known, and not by anyone. The defender's own inventory is incomplete, the segmentation is not what the diagram says, and the organization will not hand over its topology because it cannot. That is what makes sim2real strictly harder than sim2sim rather than a different problem.

## Where We Are at Year-1 (There's Much Work To Do...)

To find a solution we must first understand the problem. [**When We Say "A Realistic Cyber Environment"**](when-we-say-a-realistic-cyber-environment.md)**,** what exactly does it entail? In this project we take on the ambitious mission to define an actionable taxonomy of realism based on consensus from all the relevant parties.

How about we bypass the problem altogether? If transferring from sim to real is a dead end, can we [**Train in "Realistic" Environments Directly**](training-in-realistic-environments.md)? How much will we pay for the high fidelity training environment? Will it be worth it?

But then again...before the dreams come true and we get unlimited amount of access to operational environments for training purposes, how do we evaluate and improve our methods for sim2real? One key insight we had is that the sim2real challenge can be transformed to a sim2sim without loss of its complexity. So perhaps we can tackle [**sim2sim before sim2real**](transfer-to-realistic-environments.md)?

[**Cyber Environments & Benchmarks**](../../blogs/cyber-environments-and-benchmarks/) is a collection of cyber environments that I used, adapted, built in my various projects.

The words all three projects use, and the two places one word carries two objects, are on the [Lexicon](lexicon.md) page.

_Last updated: 2026-08_
