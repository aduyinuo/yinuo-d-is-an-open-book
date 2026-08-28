# Sim2Sim before Sim2Real

An agent that learns to attack or defend a network learns it _somewhere_. That somewhere is a simulator, because letting a learning agent explore production infrastructure by trial and error is not an option. The question this line of work asks is what happens next.

<figure><img src="../../../.gitbook/assets/transfer-loop.gif" alt="Zero-shot policy transfer from a source environment through representation alignment to target environments"><figcaption><p>A policy trained in one environment, moved to others without retraining.</p></figcaption></figure>

## The problem

A policy trained in simulator A cannot simply be run in simulator B. The two describe the world differently: different state spaces, different action vocabularies, different assumptions about what the agent can see. Formally, given environments with state and action spaces that do not coincide, can a policy trained to competence in one be executed in the other without retraining?

This shows up in two places that look separate but are not:

* An organization trains a red-teaming agent in simulation and wants to run it against its own network.
* An organization wants to compare its agent against one trained in a different simulator.

Both reduce to the same thing — aligning policies across environments that speak different representations. Sim-to-real is the same problem as sim-to-sim, with one extra difficulty: the target is only partially known. Supplying the missing ground truth would collapse it back to sim-to-sim, which is still hard; finding the abstraction that relates two fully specified environments is itself computationally difficult.

## The approach

Split transfer into two mappings and build each without touching the underlying simulators.

**Action translation.** A shared, deterministic action vocabulary in which each action advances a chosen host along the kill chain. Wrapper logic resolves the choice into whatever the target simulator natively expects. The policy's intent — which host to move on next — is decoupled from the mechanics of expressing it.

**State alignment.** Each raw observation is projected into a fixed-size vector organized by kill-chain stage per host: phase, reachability, attacker presence, target designation, plus a small block of episode-level context. This is computed deterministically per environment, with nothing learned.

That handles structural mismatch but leaves a distributional gap — the same feature carries different numbers across simulators, because networks differ in size, discovery rates, and reward scales. A lightweight encoder closes it, trained with adversarial domain confusion so a discriminator cannot tell which simulator an observation came from, with reconstruction to stop the encoder collapsing everything to one point, and a mean-alignment term to steady early training.

One detail that turned out to matter: features that mean the same thing in both environments — the flags identifying the goal — bypass the encoder entirely. Routing them through adversarial alignment suppresses the goal signal and the agent stops behaving goal-directedly.

Encoder pretraining needs only observations from a random policy in each environment. No trajectories, no rewards from the target.

## Questions being asked

1. Can offensive cyber policies transfer zero-shot across environments, with no retraining?
2. Which parts of a policy actually transfer — the state understanding, the action selection, or neither?
3. Does transfer survive when the target is only partially observable, as in emulation or a live deployment?

## Where it runs

Evaluated across [CyberWheel](../../blogs/cyber-environments-and-benchmarks/cyber-wheel.md) as the source, with NetSecGame and [CyberBattleSim](../../blogs/cyber-environments-and-benchmarks/cyber-battle-field.md) as targets at different distances from it, and NASim's emulation mode — Docker containers, live services, real exploit execution — as a proxy for deployment.

**Related:** [Toward Deployment](./) | [Training in Realistic Environments](training-in-realistic-environments.md) | [Cyber Environments & Benchmarks](../../blogs/cyber-environments-and-benchmarks/)

## What the encoder is for, and what it is not

The two wrappers deliver vectors of the same width with the same field in the same position. That is structural mismatch closed, and it is not enough. The field is in the same place in both vectors and its values are drawn from different distributions, because the two environments differ in network size, in how fast discovery happens, and in how reward is scaled. Hold the field position fixed and compare the two value distributions. Same position, different distribution, is the gap the encoder exists for.

Three losses train it and each does a separate job. **Adversarial domain confusion** trains a discriminator to name the source environment from the latent and trains the encoder against it, in both directions symmetrically. The label it needs is which simulator produced the observation, which is free, and that is why no target rewards are required at all. **Reconstruction** is the guard on the first: under adversarial pressure alone the cheapest way to confuse a discriminator is to output the same vector for everything, which aligns the domains and destroys the observation. Nothing here wants a good reconstruction; it wants the latent to remain able to distinguish observations, and reconstruction is the cheapest way to require that. **Mean alignment** pulls the two latent centroids together directly, which supplies a gradient in the epochs before the discriminator has converged and has anything useful to say. It is a training aid and the smallest claim of the three.

The check that the alignment did what it says is measured on the latents rather than on the win rate: the distance between the two domain centroids falls by roughly three fifths after encoding. That is reported before any transfer result, so a reader can see the encoder worked as an encoder before seeing whether it helped as a policy input.

## Two regimes, and opposite rankings

Four conditions form a ladder, and each step adds exactly one mechanism so that a failure localizes to the mechanism that was added. A random policy as the lower bound. Transfer by index-aligned padding, where the target observation is zero-padded or truncated to the source width with no attempt to put the same field in the same place. Transfer through the two wrappers, which tests whether feature alignment alone suffices. And the same plus the encoder.

The two targets return opposite rankings of the last two, and that is the finding. Where source and target already share a feature schema, the translator alone is enough and the encoder adds nothing measurable. Where the schemas diverge, the translator alone wins nothing and the encoder wins everything. Compare the two schemas first: if they already share a vocabulary, an encoder is a refinement step and should be priced as one.

The failure at the large gap is worth naming because of its shape. Given a vector of the right width whose values mean something else, the policy does not degrade. It stops acting, emits only no-ops, and owns fewer nodes than the random baseline. A degraded policy still plays and scores badly. This failure is total, not graceful, and it is diagnosable in one episode by looking at the action distribution rather than the score. It is also the reason the paper can claim that what transfers is the state distribution rather than the observation shape.

_**One design detail carried the large-gap result.**_ Features whose distribution varies across environments go through the encoder. Features that already mean the same thing in both, which here are the flags identifying the goal, go around it and are concatenated back at the output. Nothing is dropped. What is decided is which features are allowed to be aligned, and the finding is that aligning the wrong ones is worse than not aligning at all, because adversarial pressure treats the goal flag as domain evidence and erases it.

## The measures, and a verdict on one of them

_**Source-to-target gap.**_ The difference between a condition's win rate in the source and its win rate in the target, used as the measure of how much of a policy is source-specific. A target win rate alone cannot separate a policy that transfers well from a policy that was weak everywhere. On the narrow-gap target, feature engineering alone runs 99.1% at home and 47.4% away, a drop of 51.7 points, while the encoder condition runs 60.5% and 45.2%, a gap of 15.3 points. Report both numbers or neither.

_**Behavioural similarity, where win rate is unavailable.**_ Against the emulation proxy the untransferred source policy does not win at all, so its behaviour is all that can be compared. The action-type distribution over trajectories is compared against a policy evaluated natively on the emulator, and the transferred policies sit closer to it than the untransferred source does. The paper calls that result plausibility rather than transfer, and it is right to.

_**Win rate is a poor metric for the encoder.**_ When the translator alone completes the task, the encoder's contribution is invisible to a binary success measure, and the near-tie on the narrow gap is a property of the metric rather than of the encoder. The claim is not that the encoder did nothing. It is that this measurement could not have detected it. The replacements are named: step efficiency, progress rate, and performance on harder instances, meaning more nodes required, tighter budgets, branching topologies.

## What this costs, and where the assumption sits

Encoder pretraining is two thousand paired observations and fifty epochs, against two hundred thousand timesteps to train a policy from scratch. Ask what has to exist in the target before the encoder can be trained. A running environment and nothing else.

The assumption is elsewhere. The current method operates white-box: the structure of the target's state and action spaces is known, because the wrapper has to be written against it. The encoder already runs on interaction traces alone. The wrappers do not, and that is the gap between this work and a deployment where the target cannot be read. The translation is also open-loop, resolving an intent into a native action without checking whether the action succeeded, so it does not adapt to observation feedback.

The vocabulary, tier by tier, with what each term is not and how to tell: [**download the transfer lexicon (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/project-lexicons/td_sim2sim_before_sim2real.pdf)

## Publications

<table><thead><tr><th width="100"></th><th width="400">Paper</th><th>Authors</th><th></th></tr></thead><tbody><tr><td><img src="../../../.gitbook/assets/badge-raise2.png" alt="RAISE-EROCIS" data-size="original"></td><td><mark style="color:green;">Crossing the Cyber Divide: Sim-to-Sim and Sim-to-Real Transfer for RL Agents</mark><br>RAISE workshop, at ESORICS 2026</td><td>S. Saika, <strong>Y. Du</strong>, <a href="https://expertise.utep.edu/profiles/apiplai">A. Piplai</a></td><td></td></tr></tbody></table>

## Collaborators

<table><thead><tr><th width="150"></th><th width="150"></th></tr></thead><tbody><tr><td><p><img src="../../../.gitbook/assets/collab-sabrina-saika.png" alt="Sabrina Saika" data-size="original"></p><p><br><strong>Sabrina Saika</strong><br>University of Texas at El Paso</p></td><td><p><img src="../../../.gitbook/assets/collab-aritran-piplai.png" alt="Aritran Piplai" data-size="original"></p><p><br><a href="https://expertise.utep.edu/profiles/apiplai"><strong>Aritran Piplai</strong></a><br>University of Texas at El Paso</p></td></tr></tbody></table>

_Last updated: 2026-08_
