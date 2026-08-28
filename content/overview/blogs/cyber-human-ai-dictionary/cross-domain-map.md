---
description: The dictionary table, extended, and the words that carry two objects at once.
icon: almost-equal-to
---

# Cross-Domain Map

This is the question I set myself, and it is still the shortest statement of what this page is for.

> Try to match terminologies about opponent modeling, transfer learning, cyber environments across cybersecurity, AI, and human factors community.

Three rows of it already sit on the [overview page](./): opponent modeling, threat modeling, adversary emulation, against five columns. The columns stay. What follows adds the rest of the rows, in five families.

A row is one word as one community uses it, and the four things saying it commits me to. Words that name the same object from three sides sit next to each other, so what a family shows is the difference that survives when I cross from one community into the next.

If you are short of time, skip to the collisions. The rows are the easy half. The words that carry two objects at once are the ones that stop a conversation, and I have been on the wrong side of every one of them.

## Reading the other agent

The three original rows are on the overview page. These are the five that were missing.

| Concept | What is represented? | Why represent it? | Relationship to reality | Output |
| --- | --- | --- | --- | --- |
| **Agent modeling** | another agent's kind, cooperative or adversarial | coordinate with it or compete with it | recover a hidden type from behavior while the other party adapts | a type estimate carried into the next round |
| **Attacker profile** | a stipulated attacker, a script or a parameter set | hold the opponent fixed so a defender result is attributable | set by the experimenter and varied on a known schedule | a runnable opponent |
| **Cognitive model** | how an attacker values gains, losses and risk | face the defender with a realistic opponent rather than an idealized one | put the deviation in the reward and let the trajectory follow | a generative attacker whose paths can be run |
| **Opponent embedding** | attacker type and recent attacker behavior | keep the adversary's contribution separable from the network's | inferred only from defender-observable signals | a latent the reward predictor reads |
| **Categorization** | a small set of partner kinds, relative to the group | carry many relationships on little computation | compress observed partners against the group mean, not a fixed threshold | a classification that moves when the room moves |

The family turns on epistemic operation. Threat modeling describes, opponent modeling and agent modeling infer, adversary emulation and the cognitive model enact. Specificity does the second cut: threat modeling is at its most useful over an adversary class, adversary emulation over a particular actor. The [full census of this word](opponent-modeling-terms.md) is nine senses long.

## Moving a policy

| Concept | What is represented? | Why represent it? | Relationship to reality | Output |
| --- | --- | --- | --- | --- |
| **Transfer learning** | competence held in a policy or a representation | spend it where it was not trained | relate two environments that describe the world differently | a policy executable in the target |
| **Sim2sim** | the gap between two fully specified simulators | measure the gap without an operational network to measure against | both sides are known, so the abstraction between them can be checked | a drop that can be attributed |
| **Sim2real** | the gap between a simulator and a deployment | put the policy where the network is | the target is known only in part | a policy that survives live services, or does not |
| **Zero-shot transfer** | competence carried with no retraining in the target | test whether the representation did the work | source and target share an interface and nothing else | the same policy, run unchanged |
| **Domain adaptation** | the distributional gap left after the schema matches | make one feature carry one number in both | learned from observations of a random policy in each | an encoder a discriminator cannot read the source off |
| **Action translation** | what an action does, apart from how it is written | separate the intent from the target's syntax | a shared vocabulary that wrapper logic resolves | one action name per simulator |
| **State alignment** | each observation as kill-chain stage per host | give two environments one schema | computed deterministically, nothing learned | a fixed-size vector in both |

This family turns on object, because every row moves something different. Transfer learning moves a policy, domain adaptation moves the numbers on an observation, action translation moves an action, state alignment moves the schema underneath both. Naming the family by what it moves is what keeps the four from being read as four names for one procedure, which is how they get read. The bare word carries sixteen senses across my own files, and [the census of it](transfer-learning-terms.md) is where they are separated.

## Where the agent runs

| Concept | What is represented? | Why represent it? | Relationship to reality | Output |
| --- | --- | --- | --- | --- |
| **Simulator** | an abstraction of a network and of acting on it | afford the millions of steps learning wants | models the system rather than executing it | cheap steps, and an unmeasured gap |
| **Emulator** | provisioned infrastructure running real services | measure a policy against real tool execution | executes the behavior rather than modeling it | slow steps, honest ones |
| **Benchmark** | one frozen configuration and a score | make results comparable across groups | fixes both what was modeled and what was omitted | a number, and the conditions it was taken under |
| **Study platform** | a configured network with people inside it | watch what an attacker does when part of it is fake | real play, at human speed | observed human behavior, not trajectories |
| **Realism dimension** | what an environment provides, models, or emits | decide suitability per claim rather than per environment | derived from what each technique requires in ATT&CK and D3FEND | a fit score for one environment and one objective |

This is the only family that lies along a single dimension, fidelity, which is why six environments can be put on three axes and still come out unordered. The word environment does [six separate jobs](cyber-env-terms.md) inside it.

> Notice that fidelity and tractability pull against each other. The environments closest to a real system are the ones you can least afford to train in.

## Assembling a population

| Concept | What is represented? | Why represent it? | Relationship to reality | Output |
| --- | --- | --- | --- | --- |
| **Strategy population** | the strategies that enter the empirical game | represent the full game under a computational budget | every payoff entry is estimated by simulation | an empirical game, and the regret left in it |
| **Population-based training** | a set of learners and their hyperparameters | spend a fixed budget on a schedule rather than on one setting | the population is the training run, not a claim about anyone | one model, and the schedule that made it |
| **Attacker population** | a spread of stipulated adversaries | face the defender with a distribution instead of one opponent | profiles fixed within a batch, varied across batches | a defender measured against the spread |
| **Reference group** | the others a partner is judged against | fix what counts as cooperative here | the group is the standard, so identical evidence reads differently elsewhere | a relative classification |

This family turns on purpose, and object separates nothing at all. All four rows hold a set of agents, and [six senses of the phrase](population-based-training-terms.md) sit behind them. The PSRO set is what you play against, the training set is what you train with, the attacker population is what you are trained against, and the reference group is what you are judged against. One object, four jobs.

## The unseen

| Concept | What is represented? | Why represent it? | Relationship to reality | Output |
| --- | --- | --- | --- | --- |
| **Zero-day** | a vulnerability in use before its patch exists | prepare for what no signature covers | counts the days the vendor has had, not what the defender has seen | an incident with no rule waiting for it |
| **Zero-shot** | a target with no example and no retraining | test what the representation alone carries | counts what the learner was handed | a policy run unchanged |
| **Few-shot** | a target with a handful of episodes | ask what the smallest useful adaptation is | counts the same thing at a different value | an adapted policy, and its budget |
| **Out of distribution** | states outside the model's support | bound the behavior where the model is wrong | names a region rather than counting anything | a bound, or a detector |
| **Zero-day condition** | a team facing an attack with no prior signature | manipulate what the team has to work from | stipulated in the design, not encountered | a contrast between conditions |

This family turns on none of the five dimensions, and that is the finding rather than a gap in my placement. The other four families all represent something about an adversary or an environment, which is what the five were built for. This one represents the defender's own evidence. So the map takes a sixth axis, in the same spirit as the first five.

_**Evidence:**_ what is counted, and whose it is. Vendor remediation days, examples handed to a learner, the support of a fitted model, what a team knows before the episode starts.

## Two that move together

A concept here is a region per dimension plus the correlations between them, and a table of independent columns cannot hold a correlation. Two are live and both are worth writing under the table rather than leaving to the geometry.

_**Fidelity against tractability.**_ In the environments family the correlation is negative and I have never seen it broken. Cost per step rises with everything that makes a result trustworthy. Tractability is not one of the five dimensions and it should be, because an environment that scores well on fidelity and cannot be run is not a position on the trade. It is out of the family.

_**Specificity with fidelity.**_ In the reading family these two agree in all three original rows. Threat modeling is generic and abstract, adversary emulation is particular and executable, opponent modeling sits between them on both. Two columns that agree everywhere may be one column wearing two names, so the check is to find a term at an intermediate point on one and see whether the other is forced. The attacker profile is that test. A scripted B-line agent is entirely particular, one named opponent with a fixed route, and entirely abstract, since no real tool executes and no service is touched. Both columns survive, and the profile row is what proved it.

## Three names, one object

Four of the five families have a word in all three communities. One does not.

_**Reading the other agent.**_ Cybersecurity says threat modeling, adversary emulation, attacker profile. AI says opponent modeling, agent modeling, type inference, opponent embedding. Human factors says cognitive model, categorization, contrast. The three differ on where the model comes from: security stipulates it, AI infers it from play, human factors fits it to observed people.

_**Where the agent runs.**_ Cybersecurity says range, testbed, emulation. AI says environment, simulator, benchmark. Human factors says study platform, and puts participants in it. The three differ on what a step costs and on who takes it.

_**Assembling a population.**_ Cybersecurity says a set of attacker profiles. AI says strategy population in the game-theoretic sense and population of learners in the optimization sense, which are not each other. Human factors says reference group, and means the population that sets the standard rather than the one being trained.

_**The unseen.**_ Cybersecurity says zero-day. AI says zero-shot, few-shot, out of distribution. Human factors says the zero-day condition, an experimental manipulation in which a team has no prior signature to work from. Same prefix, three counters, and none of the three counts the same quantity.

_**Moving a policy**_ is the one with nothing in the third column. Security and AI both have the word and mean roughly compatible things by it, and nothing on my pages says what a human factors researcher would call it. The question that leaves open is worth asking on its own. When an analyst's competence in one network shows up in another, what is it that moved, and would anyone call that transfer?

## Words that collide

Recorded as collisions rather than resolved, because in every case both senses are doing real work somewhere.

_**Environment, and whether the opponent is in it.**_ In reinforcement learning the environment is everything outside the agent, which puts the adversary inside it. FOE-Dreamer takes the opposite position and gives the opponent a latent of its own, so that an error there is contained rather than smeared across the whole representation. Learn Structure then puts the boundary back where dependence is weak, since a region with no strategic content collapses into an ordinary single-agent decision. The word marks a boundary that both projects deliberately move, and where the boundary goes is the research, so the word cannot be fixed without giving up the question.

_**Model, six objects.**_ Threat model, world model, mental model, opponent model, cognitive model, model-based reinforcement learning. Two of them, threat model and mental model, are structured accounts a person writes down. Three are fitted objects a machine holds. One, the cognitive model, is a fitted object standing in for a person. In a room with all three communities, the sentence "the model was wrong" is not one claim. It is at least three, and the repair for each is different.

_**Simulation.**_ The FOE-Dreamer abstract says the defender trains without a simulator stage, and the world model generates imagined rollouts by design. Both are true. In the security sense a simulation is a modeled stand-in for a network and there is none. In the model-based reinforcement learning sense a simulation is what the world model produces. The sentence needs its qualifier every time it is written.

_**Transfer, and what is moving.**_ Sim2Sim before Sim2Real moves an offensive policy out of the environment it learned in. Training in Realistic Environments keeps a defensive policy where it is and moves nothing. Both pages are about the sim-to-real gap. One is measured by a drop after the move and the other by a training budget spent before there was ever a move to make.

_**Population, three jobs.**_ Play against, train with, be judged by. Ask which one is meant before agreeing that more population is better.

_**Zero, two counters.**_ The zero in zero-day counts the days the vendor has had. The zero in zero-shot counts the examples the learner was given. Neither counts what the defender has seen, which is what [my own question](zero-day-terms.md) was actually asking about.

_**Profile, three objects.**_ A scripted attacker profile is a route through a network, B-line taking a prepared sequence and Meander scanning breadth first. A prospect-theory profile is three numbers, the curvature on gains and on losses and the loss-aversion multiplier. MDP profiling of a cyber environment is a characterization of the environment itself, with no attacker in it at all. Route, parameters, environment. The word is doing nothing but signaling that something has been held fixed.

_**Realistic.**_ In common security usage realistic is a property of an environment, and a claim to it is a claim about the whole. My own realism work makes it a property of a pair, so GOAD is suitable for credential-based privilege escalation and not suitable for targeted data exfiltration, unchanged in between. Anyone using the first sense will hear the second as hedging, and anyone using the second will hear the first as an unsupported claim. This one is worth correcting in the room rather than letting it pass.

[**Download the full entry (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/cross-domain-dictionary/dict_cross_domain_map.pdf)

_Last updated: 2026-08_
