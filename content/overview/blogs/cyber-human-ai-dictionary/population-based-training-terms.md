---
description: Six senses of one phrase, and what happens to the population when training stops.
icon: almost-equal-to
---

# Population-based Training Terms

The phrase reaches my reading already attached to something else. The PSRO survey closes its framework section by saying PSRO can be classified as a variant of population-based training, and the label sticks, so every PSRO paper I read inherits a name coined for a different algorithm solving a different problem.

The two are not the same thing and the difference is not cosmetic. In one of them the population is scaffolding that gets thrown away. In the other the population is the answer.

## Six senses

_**The hyperparameter population.**_ Jaderberg et al. 2017, the paper the phrase was coined in: a fixed computational budget spent jointly on a population of models and their hyperparameters, discovering a schedule of settings rather than a single fixed set for the whole run. Members are ranked, the worst are overwritten by mutated copies of the best, and the run ends with one model and one schedule. The population exists so that a schedule can be found. It does not survive the run and no result is ever stated over it.

_**The strategy population.**_ The set of strategies in a restricted game, expanded each iteration by strategies that respond to a mixture over the existing set. Every member is kept, because dropping one changes the restricted game and therefore changes the equilibrium and the regret computed over it. The cost of building the set is the research problem, which is what the strategy exploration problem names. The population is what the answer is stated about.

_**Co-evolving species.**_ Multiple populations evolved in parallel, one per species, with no explicit fitness function, so that a member's fitness depends only on how well it interacts with members of the other populations. This is where the diversity measures descend from, and why behavioral diversity and response diversity are two measures rather than one.

_**The opponent set.**_ One learner is trained, and the population is the distribution it trains against. Czempin and Gleave use the phrase this way and report that how hard the victim is to exploit tracks the size of the opponent set. No hyperparameters are searched and no restricted game is solved.

_**The league.**_ The strategy population with an organizational chart imposed on it. Main agents, main exploiters trained only against the current main agent, and league exploiters trained against the league, with matchmaking by a performance score and members added and reset on schedule. This is the version most cyber papers reach for when they cite population training.

_**The sampled population.**_ In epidemiology and in human-subjects work, population-based names a sample drawn to stand for a defined population rather than for whoever arrived at the clinic. The property claimed is representativeness, the failure mode is selection bias, and nothing is trained at all. This is the sense a collaborator from the behavioral side hears first, and it is the one my own testbed sentence is closest to.

## The operational test

Ask what survives training.

1. If the members are discarded and one model ships, the population was a search device and the phrase is Jaderberg's.
2. If every member is kept because the result is stated over the set, the phrase is the PSRO one.
3. If the members were never trained at all, the word is describing the environment, and the word training does not apply to them.

One question settles all three. Name the object the paper's headline number is computed over. A score for one model gives case one. A regret or an exploitability gives case two. A description of the setting gives case three.

## Where my own uses land

Seven occurrences across three projects, and none of them is the hyperparameter sense. I have never run a hyperparameter population and will not in this line of work. The phrase enters my vocabulary only as a label a survey hands to something else.

[AcceleratePSRO](../../3-year-agenda/cyber-world-modeling/accelerate-psro.md) takes the strategy sense as its subject, assembling a set that represents the full game under a computational budget. [Learn Structure](../../3-year-agenda/cyber-world-modeling/strategic-structure.md) supplies the admission question, which strategies enter the empirical game, and the finding that goes with it: restricting the strategy space is standard rather than cheating, and the restriction error, the chosen subset against the full policy space, is not bounded. [FOE-Dreamer](../../3-year-agenda/cyber-world-modeling/environment.md) uses the word in the sampled sense, for the scripted user and attacker populations of Daedalus, which have nothing to do with a training scheme.

Two of the seven will not sit still. The user and attacker populations are scripted and fixed and stand in for real users and real attackers, which is the sampled sense, and two attacker profiles are also a strategy set of size two that never expands, which is the strategy sense frozen at initialization. And PSRO as a variant of population-based training describes one sense under the name of another, which is the whole reason this page exists.

## Three collisions

_**The label is borrowed from a loop that is not being run.**_ Jaderberg's population is discarded and the members were a search device. The PSRO population is retained in full and the equilibrium is defined over it. The same three words name two opposite fates, so any sentence claiming a method inherits guarantees or intuitions from population-based training has to say which one, because nothing carries across.

_**Two populations in one testbed, sharing nothing but plurality.**_ Daedalus has an attacker population of two scripted profiles, fixed for the life of the experiment, part of the environment, untouched by any gradient. AcceleratePSRO has a strategy population that expands every iteration and is the output of the algorithm. Whichever page a reader arrives from, the other sentence will mislead them.

_**Diversity is measured against two different things.**_ In the hyperparameter sense, diversity is spread in hyperparameter space and its value is that the search does not collapse early. In the strategy sense it splits in two: behavioral diversity is the difference between action-state coverages, and response diversity is the distance between the payoff vector a new strategy induces and the payoff vectors already in the restricted game. A population can score high on the first and add nothing to the restricted game, which is the failure the second exists to catch. Importing a diversity mechanism from the hyperparameter sense gives no reason to expect the second kind.

## The entry

A training scheme that holds more than one learner at once and operates on the set rather than on any single member, so that what is selected, measured, or reported is a property of the set.

It differs from self-play, where a strategy trains against its own current copy, so the set has size one at every moment and there is no diversity to select over. It differs from ensembling, where several models are trained independently and combined only at inference, never competing for training resources against each other.

When the three tracks are written about together, the word needs qualifying every single time it appears.

[**Download the full entry (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/cross-domain-dictionary/dict_population_based_training.pdf)

_Last updated: 2026-08_
