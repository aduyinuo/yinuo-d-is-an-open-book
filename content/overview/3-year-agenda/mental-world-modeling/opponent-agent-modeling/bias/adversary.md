---
icon: face-shaking-horizontal
---

# Challenging Attacker

<figure><img src="../../../../../.gitbook/assets/adversary-beeline-meander.gif" alt="B-line and Meander attackers moving through the same network, side by side"><figcaption><p>Both are heading for the operational server. They get there very differently.</p></figcaption></figure>

## B-line

A fixed route. The agent carries a prepared sequence of actions — discover, exploit, escalate, repeat — aimed straight at the operational server, with a jump table telling it where to fall back to when a step fails. It touches almost nothing it doesn't need.

Cheap to detect if you know the route. Almost impossible to detect from volume, because there isn't any.

## Meander

Breadth first. It scans every subnet it can see, discovers services on every address it has learned, exploits what it can, escalates where it can, and only then arrives at the same server. It leaves marks across the whole network on its way.

Loud, slow, and much harder to predict, because what it does next depends on what it happened to find.

##

## What challenging means here

Knowing the enemy is the expensive half. Red teams are scarce, hand-built attack scripts are slow to write and subjective to evaluate, and the automated adversaries that replace them are optimal, deterministic, and therefore learnable. A defender who has only ever trained against a learnable attacker is a defender who has trained against the wrong thing.

So challenging is not a feeling here. An attacker is more challenging than another when a defender who has repeated experience against both ends up worse off against the first one. Three properties have to hold before the word is allowed.

1. **It is a claim about the defender, not the attacker.** Raw attacker strength is not the quantity. An attacker that wins on the first episode and is shut out by the two-thousandth is easy, whatever its opening score.
2. **It is measured after learning, not before.** The comparison is between the first five hundred episodes and the last five hundred. Every ranking here reverses somewhere in that interval, and reporting either end alone gets the ordering backwards.
3. **It has to survive the substitution of a human for the model.** A simulated defender that finds an attacker hard is a prediction. It becomes a finding when human participants, facing the same three attackers in the same task, reproduce the ordering.

## Two more attackers, which this page does not draw

_**The cognitive attacker.**_ An attacker whose action selection is a cognitive model of experiential choice rather than a script or an optimizer. It stores each state, action and outcome as an instance, retrieves past instances by activation, blends their outcomes into an expected value for each option, and takes the option with the highest blended value. The neighbour it gets confused with is a reinforcement learning attacker. Both learn from interaction, and the difference is what each is built for: a reinforcement learning algorithm is built to solve the problem optimally, a cognitive model is built to reproduce how a person solves it, which means it carries decay, retrieval noise and recency as constraints rather than as defects. The two can reach the same policy and are not the same object. Remove the memory decay and the activation noise. If the agent still behaves the same, nothing cognitive was doing work and you have a value-based learner with extra vocabulary.

Trained against a passive defender for two thousand episodes it reaches a mean reward of 104.64 against B-line's 112.8, and by the end of training fifty-five percent of the runs score above B-line. It learns that policy with no strategy encoded anywhere in it.

_**The strategic attacker.**_ An attacker whose policy is fixed in advance, whether deterministic like B-line or stochastic like Meander. Fixed means it does not condition on the defender's behaviour and does not change across episodes. Stochastic is not adaptive, which is the point of the term: it groups the two attackers this page describes and separates them from the one it does not. Freeze the defender's policy halfway through training. If the attacker's behaviour distribution is unchanged by that, it was never conditioning on the defender.

_**Deterministic in 2023, strategic in 2025.**_ The earlier version of this work is titled human-like attackers are more challenging for defenders than deterministic attackers. The journal version says cognitive attackers are more challenging for defenders than strategic attackers. Same finding, two vocabularies, and the substitution is not cosmetic. The earlier paper ran two attackers and the comparison class had one member, B-line, which really is deterministic. The later paper adds Meander, which is not, so the comparison class had to be renamed to something that covers both. Strategic is the wider word and the wider claim is the one worth having, because the easy reply to the earlier paper is that stochasticity alone would have closed the gap. Meander is the control that says it does not. The same pass renamed the attacker, and human-like became cognitive.

_**Hard to predict is not hard to defend against.**_ This page says Meander is much harder to predict. Both papers say Meander is the easiest of the three to shut down. Neither statement is wrong, and the pair is the whole point of the branch, but they sit under a heading that says Challenging Attacker, so a reader arrives at the wrong conclusion. Unpredictability is a property of the action sequence. Difficulty is a property of the defender's loss. Meander is high on the first and lowest on the second, because randomness without adaptation is noise, and a defender learns to ignore noise faster than it learns to counter a plan. The attacker that is hard to defend against is the one that changes in response to what the defender did, and that is neither of the two attackers drawn above.

_**One more spelling problem, and it is mine.**_ This page spells it B-line, with a hyphen. Both papers spell it Beeline, and the challenge that shipped it spells it Beeline as one word. The hyphenated form appears nowhere else. It is the better spelling, since the thing being named is a straight line rather than a bee, but a reader who greps the code for it finds nothing.

## The defenders

_**Passive.**_ Monitors and never acts. It models the case where a stealthy attacker is present and undetected, and it exists to give a ceiling for each attacker rather than to defend anything. It is not a defender that has learned to do nothing. This one was never able to act. Every training run and every reported ceiling is against it.

_**Cognitive.**_ The instance-based defender, built on the same theory as the cognitive attacker, whose state slots hold what a human defender would see: observed activity and known compromised status for each host, plus a step counter. The two agents share a theory and share no state representation, because they are not looking at the same thing. The attacker sees the network as an attack graph of access levels. Show the defender an observation a human defender could not have had, such as the attacker's true privilege level on an unanalyzed host, and if it consumes that it is not this model.

_**Efficient.**_ A human participant whose attacker held a reward below the mean for its condition. The split is per attacker type, so an efficient defender is efficient relative to others facing the same adversary. It is not expertise: the split is by outcome, not by background, and the sample was not selected for security experience.

## Five measurements, chosen so they can disagree

Ranking attackers needs quantities that do not all say the same thing.

<table><thead><tr><th width="190">Measurement</th><th>What it counts, and what it says</th></tr></thead><tbody><tr><td><strong>Reward</strong></td><td>Cumulative attacker reward over the twenty-five steps of an episode. Administrator access on a host pays 0.1, on a server 1.0, and a successful impact on the operational server pays 10.0 per step. Against the cognitive defender, B-line opens at 112.8 and closes at 5.15; the cognitive attacker opens at 80.34 and closes at 54.60. The crossing is the finding</td></tr><tr><td><strong>Impact duration</strong></td><td>Steps per episode on which the attacker holds and impacts the operational server, counted after the first impact lands. Reward is forgiving of a patient attacker who never arrives; this ignores everything except the objective. In the last five hundred episodes it reads 3.25 for the cognitive attacker, 0.18 for B-line, and zero for Meander</td></tr><tr><td><strong>Progress</strong></td><td>Steps to first reach the enterprise subnet and, separately, the operational subnet. A latency, and the quantity a defender actually manipulates, since a defender wins by adding steps rather than by subtracting points. By the end of training the defender adds fifteen steps to B-line's route into the enterprise subnet and ten to the operational one, while the cognitive attacker's latencies barely move</td></tr><tr><td><strong>Action frequency</strong></td><td>The distribution over commands at each step, early against late. It explains a score rather than being one. Late in training both strategic attackers are caught in a loop of exploit and escalate with the impact action gone. The cognitive attacker holds its distribution steady</td></tr><tr><td><strong>Option space</strong></td><td>The number of legal defender choices, each a command paired with a target host, at a given step. Not the action space, which is a property of the game and is constant. This is a property of the situation the attacker has created, and a defender that is winning is a defender whose option space shrinks with practice. Against both strategic attackers it shrinks. Against the cognitive attacker it does not move</td></tr></tbody></table>

If I could keep only one of the five, it would be the last.

## The finding, in three experiments

1. **Can a cognitive model attack at all?** Against a passive defender it starts near Meander and finishes near B-line, at 104.64 against 112.8, having learned the route from experience with nothing encoded. So it is a usable emulator, not a weak one.
2. **Is it harder for a learning defender?** Against the cognitive defender the ordering inverts within two thousand episodes. The defender drives both strategic attackers to near zero loss and only halves the cognitive attacker's take. Its action distribution against the strategic pair shifts toward early cheap removals; against the cognitive attacker it does not adjust at all.
3. **Do humans agree with the model?** One hundred eighty-six participants, one attacker each, seven episodes of twenty-five steps after a practice pair. The human ordering matches the simulated ordering, including the crossing: B-line ahead in the first episode, behind by the last. The cognitive attacker does its best work against the defenders who are doing everything else right.

That third result answers the second half of my index question. Prepare defenders against an adversary that adapts, because the skill that beats a fixed adversary is anticipation and it does not transfer. A cognitive attacker is cheap to run, needs no expert on call, and can be paired with a trainee's own history, which is what makes it a curriculum rather than a sparring partner.

The split that explains the human result is between active and passive defence actions, remove and restore against analyse and monitor. Efficient defenders facing the cognitive attacker used active actions at a higher rate than efficient defenders facing either strategic attacker, and human participants overall lean passive.

_**One scenario name, two networks.**_ This page and [Biased Attacker](biased-attacker.md) both say CAGE and both draw a three-subnet picture with an enterprise gateway and the operational server as the prize. The reward magnitudes agree exactly: 0.1 for a user host, 1.0 for a server, 10.0 for impact. The host counts do not. This line runs a seven-host reduction, because an episode has to be short enough for the defender to observe a whole attack. The biased attacker line runs the full thirteen. That changes the option space by roughly a factor of two, and the option space is one of my five measurements, so any sentence comparing a number from one page against a number from the other has to say which network it is on.

## What the code holds

The two attacker lines under Adversary live in one merge repository whose convention is to keep the two source trees separate and put comparison work in an integration folder. This line's tree holds the simulation environment and its notebook, the two cognitive agents, one file with B-line, Meander and the passive defender in it because none of the three learns, the training runs, and four pickled defenders at 500, 1000, 1500 and 2000 episodes. Those checkpoints are why every early-against-late comparison above can be rerun rather than retrained.

One more piece is worth naming to anyone who wants to reproduce this: a modified instance-based learning implementation that adds delayed feedback. The stock library assumes the outcome arrives with the action, and in a twenty-five step episode it does not. Everything else is standard.

[**Download the full lexicon (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/project-lexicons/mwm_challenging_attacker.pdf)

## Publications

<table><thead><tr><th width="100"></th><th width="400">Paper</th><th>Authors</th><th></th></tr></thead><tbody><tr><td><img src="../../../../../.gitbook/assets/badge-tsc.png" alt="ACM TSC" data-size="original"></td><td><mark style="color:green;">A cyber-war between bots: cognitive attackers are more challenging for defenders than strategic attackers</mark><br>ACM Transactions on Social Computing, 8(3–4), 1–22</td><td><strong>Y. Du</strong>, <a href="https://sites.google.com/view/baptisteprebot">B. Prébot</a>, <a href="https://scholar.google.com/citations?user=jktsx4EAAAAJ">T. Malloy</a>, <a href="https://www.cmu.edu/dietrich/sds/ddmlab/cotyweb/">C. Gonzalez</a></td><td><a href="https://doi.org/10.1145/3712672"><img src="../../../../../.gitbook/assets/badge-paper.png" alt="paper" data-size="original"></a></td></tr><tr><td><img src="../../../../../.gitbook/assets/badge-hfes.png" alt="HFES" data-size="original"></td><td><mark style="color:green;">Towards autonomous cyber defense: predictions from a cognitive model</mark><br>Human Factors and Ergonomics Society Annual Meeting, 66(1)</td><td><strong>Y. Du</strong>, <a href="https://sites.google.com/view/baptisteprebot">B. Prébot</a>, X. Xi, <a href="https://www.cmu.edu/dietrich/sds/ddmlab/cotyweb/">C. Gonzalez</a></td><td><a href="https://doi.org/10.1177/1071181322661504"><img src="../../../../../.gitbook/assets/badge-paper.png" alt="paper" data-size="original"></a></td></tr></tbody></table>

## Collaborators

<table><thead><tr><th width="150"></th><th width="150"></th><th width="150"></th></tr></thead><tbody><tr><td><p><img src="../../../../../.gitbook/assets/collab-baptiste-prebot.png" alt="Baptiste Prébot" data-size="original"></p><p><br><a href="https://sites.google.com/view/baptisteprebot"><strong>Baptiste Prébot</strong></a><br>Carnegie Mellon University</p></td><td><p><img src="../../../../../.gitbook/assets/collab-tyler-malloy.png" alt="Tyler Malloy" data-size="original"></p><p><br><a href="https://scholar.google.com/citations?user=jktsx4EAAAAJ"><strong>Tyler Malloy</strong></a><br>University of Luxembourg</p></td><td><p><img src="../../../../../.gitbook/assets/collab-cleotilde-gonzalez.png" alt="Cleotilde Gonzalez" data-size="original"></p><p><br><a href="https://www.cmu.edu/dietrich/sds/ddmlab/cotyweb/"><strong>Cleotilde Gonzalez</strong></a><br>Carnegie Mellon University</p></td></tr></tbody></table>

_Last updated: 2026-08_
