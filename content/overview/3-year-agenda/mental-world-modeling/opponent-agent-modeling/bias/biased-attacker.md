---
icon: honey-pot
---

# Biased Attacker

Real attackers are not expected-utility maximisers. Most models of them are.

<figure><img src="../../../../../.gitbook/assets/biased-attacker.gif" alt="A prospect-theory value function changing shape, and the attack trajectory it produces changing with it"><figcaption><p>Three parameter settings. The curve on the left decides the path on the right.</p></figcaption></figure>

## Bias as a reward, not a rule

The usual options are both unsatisfying: assume game-theoretic rationality, or hand-write behavioural rules until the agent looks human. The first is wrong about people; the second doesn't generalise past the cases you wrote down.

The move here is to put the bias in the reward function. Prospect theory's value function goes directly into the POMDP:

$$v(x) = x^{\alpha} \text{ for } x \ge 0, \qquad v(x) = -\lambda(-x)^{\beta} \text{ for } x < 0$$

Three parameters, three levers. $$\alpha$$ and $$\beta$$ set the curvature on gains and losses, which is risk sensitivity. $$\lambda$$ is the loss-aversion multiplier — how much more a loss weighs than an equivalent gain.

| Profile     | $$\alpha$$ | $$\beta$$ | $$\lambda$$ |
| ----------- | ---------- | --------- | ----------- |
| Rational    | 1.0        | 1.0       | 1.0         |
| Loss averse | 1.0        | 1.0       | 2.25        |
| Risk averse | 0.5        | 1.0       | 1.0         |

Risk aversion also needs the environment to cooperate: targets are presented with different success probabilities, and risky attacks are penalised, so uncertainty becomes psychologically expensive rather than merely uncertain.

## The setting

CAGE Challenge 2, built on CybORG. Thirteen hosts across three subnets, with the operational subnet reachable only through the enterprise layer. The attacker starts with a permanent foothold on User0. Holding a user host pays 0.1 per step, an enterprise or operational server pays 1.0, and Impact on Op\_Server0 pays 10.0.

Two defenders: one that removes attacker sessions, one that restores hosts to a clean state. The restoring defender makes the environment non-stationary from the attacker's side — lose the server, lose the reward, re-exploit or fall behind.

## Why it matters

Change the curve and the trajectory changes with it. Nothing about the network, the action space, or the objective moved — only how outcomes are valued.

If those deviations are systematic and separable, they are behavioural fingerprints: you could tell one kind of adversary from another by how they move, and train defenders against a population rather than a single idealised opponent.

_The trajectories shown are illustrative of the mechanism. Measured results are still being written up._

## What one sentence settles

Putting the bias in the reward settles three things at once. Bias becomes a continuous parameter rather than a rule, so intensity is expressible. It sits in the objective rather than the policy, so a single training procedure produces every profile and none of them are hand-written. And because the agent still has to learn its policy under that objective, what comes out is a trajectory through a network rather than a preference over two lotteries.

That last one is the part I care about. Prospect theory is usually tested by asking a person to pick between fixed options once. Nobody was watching what a biased decision maker does on step fourteen of a break-in, and that is where the differences worth having are.

The transform is not reward shaping. Shaping adds a term to steer learning toward a policy you already want and is supposed to leave the optimal policy alone. This changes the optimum. The behaviour it produces is worse by the environment's own reward, and that is the intended result. Set all three parameters to one and the function collapses to the identity; any profile that does not reduce to the baseline there is not this transform.

It also needs a reference point, and the reference point here is the per-step reward, so eviction by the defender is what puts the agent in the loss domain. That is why the defender's choice between removing and restoring changes the biased agent's behaviour and not the baseline's. Shift every payoff in the environment by a constant. If the agent's behaviour changes, the model is reference dependent.

## What the three parameters do separately

$$\alpha$$ is the exponent on gains. Below one the value function is concave, so each additional unit of reward is worth less than the last and a payoff of ten is not twice a payoff of five. It is the risk aversion lever, trained at 0.8, 0.5 and 0.2 with the other two held at one.

$$\beta$$ is the exponent on losses. Below one the loss branch is compressed, so a large loss is felt as less than its size and failures stop mattering. It is the risk seeking lever, trained at the same three values.

$$\lambda$$ scales the whole loss branch by a constant. $$\beta$$ bends it; $$\lambda$$ multiplies it, and a high $$\lambda$$ with a low $$\beta$$ pull in opposite directions and can cancel. Loss aversion is an asymmetry between two branches; risk aversion is curvature within one. An agent can be loss averse and risk neutral, which is exactly the profile in the table above. Trained at 1.5, 2.0 and 2.25, and the top value is not arbitrary: 2.25 is the estimate Tversky and Kahneman fitted in 1992, so the strong setting is the human average rather than an extreme.

## The profiles, including the two the table leaves out

_**Rational baseline.**_ All three at 1.0. Not an optimal agent. It is the best policy this learner found under the true objective, and every comparison is against it rather than against an optimum.

_**Risk averse.**_ Gain curvature below one. Not cautiousness in the ordinary sense: this agent is not slower or quieter. It takes more hosts than the baseline and takes longer to reach the objective, because intermediate gains have become relatively more valuable and the final prize relatively less. All three of its hypotheses hold.

_**Loss averse.**_ $$\lambda$$ above one. Losing a held host is felt as more than gaining an equivalent one, so eviction dominates what happens next. It is cautious about a different thing than the risk averse agent is: risk aversion shows up in target selection before anything is lost, loss aversion shows up only after the defender acts and is invisible against a passive defender. Look at the first actions after an eviction. A loss averse agent goes back for what it lost instead of moving on. Both of its hypotheses hold, and it ends with the largest compromised host count of any profile, which is the same fact twice: a policy that spends its steps on recovery accumulates held hosts.

_**Risk seeking.**_ Loss curvature below one. Failures are compressed, so setbacks stop being expensive and the agent drives forward. It is not an aggressive attacker: it is fast because setbacks are cheap to it, not because rewards are attractive to it. It reaches the objective in fewer steps than the baseline, holds the smallest and steadiest set of hosts, and after eviction continues lateral movement instead of recovering. Three of its four hypotheses hold, and the fourth is the useful one.

_**Combined.**_ $$\alpha = \beta = 0.88$$, $$\lambda = 2.25$$. Mild concavity on both branches with strong loss weighting, which is the reflection effect: a risk attitude that depends on whether the agent is currently in the gain domain or the loss domain. The three single-parameter profiles hold one attitude throughout an episode; this one is state dependent, so it can look cautious early and risk seeking after it has been evicted. Split an episode at the first eviction and measure target preference on each side. A single-parameter profile gives the same answer twice. Those three numbers are the fitted human values, which makes this the closest thing in the grid to an average human attacker.

_**Risk seeking is not the mirror of risk aversion.**_ The prediction that failed is that the risk seeking agent would prefer high-risk, high-reward targets. It shows no target preference at all, and the reason is in the parameterisation rather than in the agent. Risk aversion is implemented as gain compression, $$\alpha < 1$$. Risk seeking is implemented as loss compression, $$\beta < 1$$. Those are not opposites. Making large uncertain rewards more attractive needs gain amplification, $$\alpha > 1$$, and no run has that. So the risk seeking profile as trained is a loss-compression profile, and the name promises a target preference the configuration cannot produce. Either the name changes or the grid extends above one on $$\alpha$$. Until one of those happens, that is not a failed prediction about behaviour. It is a prediction about a condition that was never run.

_**The table above is a corner of the grid.**_ The project grid has eleven settings, three intensities per bias plus the combined profile. Two things go missing in the reduction to three rows. Risk seeking is absent, so there is no $$\beta$$ row at all and a reader concludes that $$\beta$$ is unused. And the combined profile is absent, which is the one row a person would want, since it is the only setting fitted to human data. The table shows the corners and the result that matters most is in the middle.

## The four metrics the fingerprints load on

* **Low-risk target selection.** The share of successful exploits aimed at low-risk, high-certainty targets. Risk here is the success probability of the attack and not the worth of the host, and the environment has to present those separately or the metric reads flat for every profile. It rises as $$\alpha$$ falls and it is already visible at mild compression. The clearest single result.
* **Steps to impact.** The number of steps to the first successful impact on the operational server. Not total reward, which a slow attacker can still accumulate from held hosts. Risk aversion lengthens it and risk seeking shortens it, so this is the metric on which the two named-as-opposite profiles actually behave as opposites.
* **Foothold size.** The number of hosts held, reported at first impact, as an episode average, and as an episode standard deviation. A large foothold is not deep penetration. The loss averse agent has the largest foothold and is the slowest to the objective, because it keeps going back. The standard deviation is the informative one: a low value means the agent is not losing and regaining ground.
* **Post-eviction lateral movement.** The share of actions immediately after an eviction that continue toward new targets rather than recovering the lost host. It requires the defender to act, so it is undefined against a passive defender, and any run that reports it has an active defender in it. It falls as $$\lambda$$ rises.

Systematic is settled. Every confirmed hypothesis separates its agent from the baseline at $$p < 0.001$$ under a Mann-Whitney test, with effect sizes read as Cliff's $$\delta$$, which is reported alongside every $$p$$ value because a thousand evaluation episodes will make almost anything significant. Separability holds where I have looked: risk aversion loads on target preference, loss aversion on post-eviction recovery, risk seeking on steps to objective. Recovering the bias from the profile is the step after this one.

## Every bias has an operating range

The operating range is the interval of a bias parameter within which the intended signature appears **and** the agent still functions as an attacker. It is not the range that is legal. Every value in the grid trains. Not every value produces an agent that reaches the operational server. Plot the signature metric and task performance against the parameter on the same axis, and the operating range ends where the two curves separate.

Moderate risk aversion produces the target preference; strong risk aversion makes the agent chase guaranteed intermediate gains and never arrive. Moderate loss aversion produces the recovery behaviour; strong loss aversion turns the agent into a repair crew. Moderate loss compression produces a steady forward policy, and only the strongest setting breaks it. So bias intensity is not a dial that can be turned to the end, and a simulated adversary population should be sampled from inside these intervals rather than from the parameter grid at large.

## Why this setting and not another

Three properties of the scenario above are doing work and none of them are incidental.

**The foothold is permanent.** The attacker cannot be removed from the starting host. So every episode is a recovery problem rather than an intrusion problem, and the loss domain is always reachable.

**The payoffs span two orders of magnitude.** A user host pays 0.1 and an impact pays 10.0. Gain curvature has nothing to bite on if all the payoffs are the same size, and at this spread a concave agent's preference between accumulating hosts and pressing the objective is a real preference rather than a rounding.

**The two defenders differ in exactly one respect.** One removes sessions, one restores hosts. Removing takes the session; restoring takes the reward stream with it. That is the difference between an inconvenience and a loss, and it is the reason the loss averse profile is only visible against the restoring defender.

The condition about differentiated success probabilities is a requirement on the environment rather than a description of the agent, and it is the one place this line needed the testbed changed rather than the objective. Without it the target-preference metric is undefined and risk aversion has nowhere to show up.

## Two senses of bias, on one page

The two papers listed below do not use the word for the same thing, and I should say so rather than let the shared heading imply otherwise.

In the modelling paper a bias is a parameter of the value function. It is continuous, it has an intensity, it is one of three, and it produces its signature over a whole trajectory.

In the empirical paper a bias is a named effect from the judgement and decision making literature. The **default effect** is the tendency to take the preset or first-presented option, and in the attacker data it is scanning the first or the last system in the network's first layer before anything else; those systems were not more attractive on any observable. The **sunk cost fallacy** is letting unrecoverable past expenditure drive a present decision, and in the attacker data it is continuing to attack a system that has already failed repeatedly instead of switching; it was not rational persistence, since the correlation between a participant's maximum attempts on any system and their score was effectively zero.

Neither of those is a prospect-theory parameter. The default effect is about which target is chosen first, with no reference point and no gain or loss involved. Sunk cost is about honouring past expenditure, and the value function is memoryless over past spend. So the empirical work does not validate the modelling work. Two honest ways to fix that. Either add the two observed effects to the model, which needs a state that carries invested effort and a notion of a default option, and neither exists in the current formulation. Or say plainly that the empirical paper establishes that human attackers are biased and the modelling paper picks a different family of biases to simulate. The second is true today. The first is the more interesting project.

The empirical study runs on a different testbed for a reason: it puts a person at a command line and records what they type, which is where the evidence that human attackers are biased has to come from. Forty machines, half of them honeypots allocated at random, presented as a two-layer network of twenty reachable systems, with a reconnaissance, an exploitation and an exfiltration phase.

## What it is for

The index question asks how to best exploit the weakness, and the honest answer is in two parts.

The part that is done is a population. Training a defender against one idealised opponent produces a defender that has learned one opponent. A parameterised family of biases produces a population of adversaries that differ in ways a defender can actually meet, generated from one training procedure rather than written by hand, and sampled from inside the operating ranges so that every member is still a functioning attacker.

The part that is not is identification. If the fingerprints are separable, a defender watching a live trajectory could recover which bias it is facing and act on it. Loss aversion predicts an attacker that will come back for what it lost, and an attacker that will come back is an attacker you can decide where to let it come back to. The empirical side already points the same way at a coarser grain: participants converged on the first and last systems in the first layer, so a defender who knows that knows where to put the honeypots.

That empirical result also fixes how strong these effects are in people, and it is not subtle. Ninety percent of participants opened on the first or the last system. Around ninety percent kept attacking a system that had already failed them, repeatedly, in both rounds, for no gain in score. The modelling side of this line is worth doing because that is what the behaviour of real attackers looks like.

Next door, [Challenging Attacker](adversary.md) answers what a defender cannot learn to counter, and the answer is adaptivity. This line answers what a defender could plan against, and the answer is a bias with a direction. Both attackers sit on the same scenario, with the same three subnets, the same gateway, the same target, and the same three reward magnitudes. Neither has been run against the other's defender. That comparison is the open work on this branch.

[**Download the full lexicon (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/project-lexicons/mwm_biased_attacker.pdf)

## Publications

<table><thead><tr><th width="100"></th><th width="400">Paper</th><th>Authors</th><th></th></tr></thead><tbody><tr><td><img src="../../../../../.gitbook/assets/badge-preprint.png" alt="Preprint" data-size="original"></td><td><mark style="color:green;">Simulating Attackers with Cognitive Biases using Reinforcement Learning</mark></td><td><a href="https://www.linkedin.com/in/jannat-akbar/">Jannat Akbar</a>, <a href="https://users.aalto.fi/~oulasvir/">Antti Oulasvirta</a>, <a href="https://expertise.utep.edu/profiles/paggarwal">P. Aggarwal</a>, <strong>Y. Du</strong></td><td></td></tr><tr><td><img src="../../../../../.gitbook/assets/badge-hicss.png" alt="HICSS" data-size="original"></td><td><mark style="color:green;">Evidence of cognitive biases in cyber attackers from an empirical study</mark><br>Hawaii International Conference on System Sciences (HICSS)<br>Hawaii International Conference on System Sciences</td><td><a href="https://expertise.utep.edu/profiles/paggarwal">P. Aggarwal</a>, S. Rubaiyet Nowmi, <strong>Y. Du</strong>, <a href="https://www.cmu.edu/dietrich/sds/ddmlab/cotyweb/">C. Gonzalez</a></td><td></td></tr></tbody></table>

## Collaborators

<table><thead><tr><th width="150"></th><th width="150"></th><th width="150"></th><th width="150"></th><th width="150"></th></tr></thead><tbody><tr><td><p><img src="../../../../../.gitbook/assets/collab-jannat-akbar.png" alt="Jannat Akbar" data-size="original"></p><p><br><a href="https://www.linkedin.com/in/jannat-akbar/"><strong>Jannat Akbar</strong></a><br>Aalto University</p></td><td><p><img src="../../../../../.gitbook/assets/collab-antti-oulasvirta.png" alt="Antti Oulasvirta" data-size="original"></p><p><br><a href="https://users.aalto.fi/~oulasvir/"><strong>Antti Oulasvirta</strong></a><br>Aalto University</p></td><td><p><img src="../../../../../.gitbook/assets/collab-palvi-aggarwal.png" alt="Palvi Aggarwal" data-size="original"></p><p><br><a href="https://expertise.utep.edu/profiles/paggarwal"><strong>Palvi Aggarwal</strong></a><br>University of Texas at El Paso</p></td><td><p><img src="../../../../../.gitbook/assets/collab-saeefa-rubaiyet-nowmi.png" alt="Saeefa Rubaiyet Nowmi" data-size="original"></p><p><br><strong>Saeefa Rubaiyet Nowmi</strong><br>University of Texas at El Paso</p></td><td><p><img src="../../../../../.gitbook/assets/collab-cleotilde-gonzalez.png" alt="Cleotilde Gonzalez" data-size="original"></p><p><br><a href="https://www.cmu.edu/dietrich/sds/ddmlab/cotyweb/"><strong>Cleotilde Gonzalez</strong></a><br>Carnegie Mellon University</p></td></tr></tbody></table>

_Last updated: 2026-08_
