---
description: One borrowed word, three projects, and an adjective that is never true on its own.
icon: spell-check
---

# Lexicon

Sim2real is a borrowed word and I borrowed it on purpose. In robotics the gap between where a policy is trained and where it runs is a gap in physics: friction, latency, sensor noise, the mass of a gripper. The shape of my problem is the same. The content is not. This page says what the word carries once it arrives in a network, and it fixes the terms the three projects under this heading all use, because each of them took its vocabulary from a different place and none of us negotiated.

The word _environment_ is not defined here at all. It does six separate jobs across my files and the census of those six is in the [Cyber-Human-AI Dictionary](../../blogs/cyber-human-ai-dictionary/cyber-env-terms.md). Everything below assumes it.

## Three failures, not one

The [cluster page](./) states the problem in four sentences. Dynamics and sensing differ between the training world and the real one. A policy drifts as the deployment ages away from the data it was built on. And any safety we claim has to hold while the model is wrong, because out of distribution it will be.

Those are three failures and they are not the same failure. The first is a gap in space: the training world is not the deployment world. The second is a gap in time: the deployment world is not the world the policy was fitted to, because the network kept moving after the snapshot was taken. The third is not a gap at all. It is a requirement on behaviour in the region where both of the first two have already gone wrong. Each of the three open questions on the [Next](next.md) page answers exactly one of them, in that order.

## What the cyber setting does to the borrowed word

_**There is no physics to converge to.**_ A robot's real world is governed by laws that hold whether or not anyone wrote them down, so a simulator can be wrong about them and can be made less wrong. A network is an artifact. It is whatever some organization built, configured, patched unevenly and then partly forgot, and two enterprises differ from each other more than two laboratory floors do. There is no single target to approach, which is why the question _is this environment realistic_ has no answer and the question _realistic for what_ does.

_**The real world has an occupant who wants to be missed.**_ Friction does not adapt. An adversary does, and the parts of the environment that make adaptation possible, benign activity to blend into and telemetry to evade, are the parts current environments most often leave out. So the gap here is not just a modelling error. It is a modelling error that one of the two players is actively exploiting.

_**There is no cheap real to transfer into.**_ You do not get to try the policy on the production network and see what happens. Everything else follows from that. Either you make training in a real enough environment affordable, which is the second project, or you learn to measure the gap without an operational network to measure against, which is the third.

_**The target is only partially known, and not by anyone.**_ In robotics you can at least instrument the real system. Here the defender's own inventory is incomplete, the segmentation is not what the diagram says, and the organization will not hand over its topology because it cannot, for privacy reasons and sometimes because nobody has it. That is what makes sim2real strictly harder than sim2sim rather than a different problem: supply the missing ground truth and it collapses back to sim2sim, which is still hard.

## The three projects, as a division of vocabulary

[**Metrion**](when-we-say-a-realistic-cyber-environment.md) says what a claim needs. It owns the requirement words: dimension, scoring element, requirement profile, fit score, suitability.

[**FOE-Dreamer on Daedalus**](training-in-realistic-environments.md) buys one class of claim outright by paying the live cost. It owns the cost words: backend, fidelity gap, sample efficiency, and the scoped reading of _realistic_.

[**Sim2Sim before Sim2Real**](transfer-to-realistic-environments.md) measures the gap for everyone who cannot pay it. It owns the alignment words: action translation, state alignment, the domain gap, zero-shot.

Both of the disagreements recorded below are words that crossed one of those boundaries and kept their old sense on arrival.

## The shared terms

### The two reductions

_**Sim2real.**_ The problem of running a policy in a deployment whose dynamics, sensing and composition differ from the training environment, where the deployment cannot be enumerated in advance and cannot be used for exploratory training. Not ordinary distributional shift, which is a statement about two distributions. Sim2real names the practical situation that produces the shift and adds two constraints a shift statement does not carry: the target is only partially observable, and errors there are expensive. The test: can you enumerate the target environment? If yes, this is sim2sim. If no, and you also cannot train in it, this is sim2real.

_**Sim2sim.**_ Transfer between two fully specified environments with non-coinciding state spaces, action vocabularies and observability assumptions. Sim2real with the missing ground truth supplied. Not domain adaptation in the usual sense, where the two domains share a task specification and differ in appearance; here the action sets themselves differ, so there is no shared vocabulary to adapt within until one is constructed. The test: can you write down both environments in full? Then the remaining difficulty is finding the abstraction that relates them, which is by itself computationally hard.

### The adjective

_**Realistic.**_ A two-place predicate, never a one-place one. An environment is realistic _in a named respect_, and useful only _for a named claim_. The quotation marks in two of the three page titles are not decoration. Not fidelity, which in my files is a property of one named layer, and not validity, which is a property of an evaluation rather than of an environment. An environment can be high fidelity on every layer a claim does not depend on. The test: ask what would make this environment more realistic. If three people answer noise and a moving opponent, Active Directory and event forwarding, and task pressure with a cover story the participant believes, then the word has three senses in the room and the conversation will not converge.

_**Realism against fidelity.**_ In the realism evaluation, _fidelity_ is the score of a single named layer, as in service fidelity, OS fidelity, telemetry fidelity. _Realism_ is what the whole gets. The [blogs](../../blogs/cyber-environments-and-benchmarks/) reverse the two, where fidelity is the aggregate that pulls against tractability. There is no third sense, only two dialects with the labels swapped. The test: count the layers the sentence is about. One layer, fidelity. Eleven, realism.

### Transfer, and the gap it leaves

_**Transfer.**_ Executing a policy in an environment other than the one it was fitted in, with no gradient steps taken in the destination. Not fine-tuning, which is retraining with a warm start, and not generalization within one environment, where the interface does not change. The test: were any parameters updated after the destination was first seen?

_**Fidelity gap.**_ The difference in outcome between the same action taken in the cheap backend and in the honest one. Not an error term to be minimized but a quantity to be read off. Not model error in the world-model sense, which is a property of something fitted from data; the fidelity gap is a property of two hand-built things and is fully attributable, since you can name the action, the host, and the abstraction that caused it. The test: run the same policy on both backends and diff the outcomes per action. What differs is the gap, and it is a list rather than a number.

_**Action translation.**_ A fixed intermediate action set, indexed by kill-chain stage and host, with per-environment wrapper logic resolving each choice into whatever the destination simulator natively expects. Nothing is learned. The test: could you write the wrapper for a new simulator by reading its documentation, without collecting a single episode?

_**State alignment.**_ A deterministic per-environment projection of raw observations into one fixed schema, phase and reachability and attacker presence and target designation per host, plus a small block of episode-level context. The learned encoder that follows it is a separate thing and closes the distributional gap only. The test: does the same feature index mean the same thing in both environments? That is the projection's job. Does it carry comparable numbers? That is the encoder's.

### Cost

_**Backend.**_ One of two implementations of a single action and observation interface, differing in what a step costs and in what a step actually does. Not two environments, which is what the transfer project faces. Two backends share the interface by construction, so a policy moves between them with no alignment at all, and any difference in outcome is attributable to fidelity rather than to representation. The test: does the agent's code change between the two?

_**Sample efficiency.**_ Return achieved per unit of environment interaction, where the unit is priced in wall-clock seconds and in irreversible state changes on real machines rather than in simulator steps. Not compute efficiency, which is about the GPU, and not asymptotic performance, which assumes the interaction is free. Three days on one GPU is the headline because the GPU was never the constraint. The test: halve the step budget. If the result survives, the method was not sample-limited and this is not the axis to report.

_**Operational.**_ Stipulated narrowly, and only about how the environment is realized: services execute rather than being modelled, actions produce real state changes on real operating systems, and time passes on a wall clock. It is not a claim that the network belongs to anyone or carries production traffic. The test: if you deleted the scenario, would there still be machines running services?

### After deployment

_**Drift.**_ The widening of the gap between the data a deployed policy was fitted to and the network it now acts in, driven by the network changing rather than by the policy moving. Not the sim2real gap, which is present at time zero and is a property of two environments. Drift is a property of one environment across time. The test: freeze the policy and wait. Any degradation is drift. Anything present on day one is the transfer gap.

_**Out of distribution.**_ The region where the model's error is not small and cannot be assumed small. Treated here as the normal operating condition rather than as an edge case. Not the uncertainty a well-calibrated model reports, which is a quantity inside the model; this is the region where the calibration itself is untrustworthy. The test: would you accept the model's own confidence as evidence here?

_**Zero-shot.**_ Executed in the destination with no parameter updates and no reward signal from it. Observations from a random policy are permitted, since encoder pretraining needs only those. Not few-shot, which permits a small number of episodes in the destination, and not zero-day, which is a property of a vulnerability and not of a learning regime. The two words share a prefix and nothing else.

_**Deployment-readiness.**_ The property that a policy's score in a destination environment was produced by the task rather than by the destination's regularities. Defined by what it survives, not by a threshold. Not transfer performance, which is a number, and not suitability in the Metrion sense, which is a property of an environment and an objective rather than of a policy.

## Where the senses disagree

_**The reduction runs one way and the word does not.**_ The cluster page says the sim2real challenge _can be transformed to_ a sim2sim. The Sim2Sim page says sim-to-real _is the same problem as_ sim-to-sim with one extra difficulty. Those are different claims. A transformation into an easier problem is a research strategy and gives up nothing only if the reduction is tight. An identity plus an extra difficulty is a statement that the easier problem is a strict sub-part. Both sentences are mine, they were written for different pages, and the second is the one the experiments actually test.

_**Two dialects, reversed labels.**_ The blog corpus says fidelity and never says realism. The realism evaluation says both and splits them, with almost every fidelity token sitting inside a dimension name. Both corpora carry the same distinction between a layer and the whole, and they attach the labels the opposite way round. All three project pages in this cluster inherit the blog dialect while the framework that scores them uses the other, and the two sit one click apart on the site.

_**One word, two objects, two directions.**_ On the Sim2Sim page the thing transferred is an _offensive_ policy and it moves _across simulators_, and the obstacle is representational. On the Training page and throughout Daedalus the thing transferred is a _defensive_ policy and it moves _between two backends of one environment_, with the action and observation spaces held identical by construction, and the obstacle is not representational at all. It is fidelity. Same word, opposite sides of the engagement. The first needs an alignment. The second needs no alignment and gets a measurement instead.

The check that closes this page is the two-way one. Sim2real names sim2sim and sim2sim names sim2real. Transfer names backend and backend names transfer. Realistic names fidelity and fidelity names realistic. Drift names the transfer gap and the transfer gap has to name drift. Where a distinction runs one way only, one of the two definitions is wrong, and the transfer pair is the one to watch, because it is the pair whose two senses never appear on the same page.

[**Download the full cluster lexicon (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/project-lexicons/td_shared.pdf)

_Last updated: 2026-08_
