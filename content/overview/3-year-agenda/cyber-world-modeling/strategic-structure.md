---
icon: diagram-project
---

# Learn Structure

Not every part of a game is strategic. Most of it isn't.

<figure><img src="../../../.gitbook/assets/strategic-dependence.gif" alt="A map of strategic dependence across a state-action space, shifting as the opponent changes"><figcaption><p>Left: how much the best action depends on the opponent, across the space. Right: probing one region against four opponent behaviours.</p></figcaption></figure>

## The intuition

**Strategic dependence** is how much a player's best action, in a given region of states and actions, turns on what the other player does.

Sometimes a choice hinges on the opponent and often it does not. Where dependence is strong the region needs game-theoretic reasoning; where it is weak or absent the region collapses into an ordinary single-agent decision.

The dependence is not uniform. It concentrates in pockets, and those pockets move during a single interaction as the opponent shifts.

## Why it forces a choice

A defender in a game too large to solve whole has to decide where game-theoretic reasoning is necessary and where the opponent can be treated as part of the environment. The cost of the analysis is what forces that choice: in empirical game-theoretic analysis every payoff entry is estimated by simulation, already prohibitive beyond two players, so which strategies enter the empirical game governs what the analysis can deliver. A fourteen-day engagement decided inside a twenty-nine-minute window turns the budget question from a tuning decision into the problem itself.

## Why existing notions of structure do not capture it

The dependency graph of a factored MDP, the relations of an object-oriented state, the causal graph, and empirical payoff dependence are all properties of the game **as written**. Strategic dependence is a property of **how the game is played**. Hold a green security game fixed and vary only the poacher's behaviour: all four are unchanged, and the reasoning the defender requires is not.

## The classification

Strategic dependence is classified by the mechanism that carries one player's behaviour into another's best action.

<table><thead><tr><th width="150">Mechanism</th><th>Carries behaviour through</th></tr></thead><tbody><tr><td><strong>Time</strong></td><td>when a move lands relative to another</td></tr><tr><td><strong>Space</strong></td><td>where in the state space the two players meet</td></tr><tr><td><strong>Control</strong></td><td>what one player's actions make available or deny to the other</td></tr><tr><td><strong>Cause</strong></td><td>what one player's actions change that the other depends on</td></tr><tr><td><strong>Information</strong></td><td>what one player can observe of the other</td></tr></tbody></table>

Each mechanism carries an ordered scale, with a test separating adjacent levels.

A structure is strategically relevant to a player when four conditions all fail to excuse ignoring it:

1. it varies over its admissible values
2. its variation changes the player's best response
3. it lies within reach of play
4. the party that would exploit it can observe it

## Where the existing measures sit

The classification positions measures built for other purposes: graphical games, influence-based abstraction, information-theoretic influence, and attention weights. Value-based abstraction is excluded as a contrast case, since it measures abstraction quality within one agent rather than dependence between players. Attention is left unplaced, because no result ties its score to a quantity of the game.

Two gaps in the measure set remain. Nothing measures agent-to-component causal strength by edge-cutting, and nothing measures regret per ordered pair of players.

## The vocabulary of record

The submission fixes the house vocabulary in a drafting-conventions block, and it governs everything else: **type** rather than kind, **degree** rather than amount, **dependence**. Type and degree are axes, not adjectives, so the classification is type by degree and not a single scale.

The earlier working file names the two axes the other way round and uses the third rejected word throughout, so both pairs are live in the corpus and only one of them is current. That matters more than it sounds, because the superseded wording is what a reader meets first: that file is the largest in the project at three hundred and eighty-eight kilobytes.

The four-level progression from pure independence through state-transition dependence to immediate-reward and future-reward dependence is retired with it. Before the revision the graded axis ran along one progression, from one-shot play to repeated play to the stochastic game, so it graded a single type, the sequential one. That restriction is gone. Anything that carries the four levels without marking them as retired sends a reader to the wrong axis.

One smaller inconsistency is open. The experiments section calls the first domain network defense while the motivating-domains and object-oriented-specification sections call it attack-defense, and both names are in the current draft.

## Where the dependence is zero

Every scale has a bottom, and the bottom is characterized once rather than stipulated per scale: a structure sits at the zero point of a scale exactly when, for that type, every reason a defender could have to attend to it fails. Four of the five zeros conform outright. The causal zero conforms with two recorded qualifications.

The four excuses are what the zero point is checked against, and each has a runnable form.

* **No variation** reads the generating process's support over the modelled lifetime, not the snapshot.
* **Out of reach** has a spatial clause, structural d-separation from the player's reward and observation variables, and a temporal clause, a discounted tail below a declared tolerance.
* **Opponent-blindness** treats the opponent's whole observation process as an experiment and asks whether it is null for the structure.
* **Invariant best play** asks whether, for every admissible opponent behaviour, one way of playing in the player's actual strategy set is a best response at every admissible value.

Every test returns excused or not excused, and no test returns important. Importance is what remains when none of the four excuses. The logical content is two independent conditions, since a structure is excused exactly when invariant best play holds or opponent-blindness holds. The four survive as a testing order from cheap to expensive: no variation needs only a marginal support, the two reach tests need graph computations and no solving, and invariant best play needs value computation and runs last.

The filter runs on a declared triple of the game, the structure under examination, and the structure's admissible value set, with three further parameters declared: the admissible opponent behaviours, the retained conditioning set, and a temporal tolerance. Leave any of them implicit and verdicts stop being comparable across runs.

One caution binds the whole list. Single-structure verdicts do not compose. A common best play can exist across the admissible values of one structure alone, and across those of another alone, and fail to exist across the product of the two sets. A filter pass is not a licence to drop everything it excused.

## Seven senses of structure

My own glossary opens by conceding the problem rather than solving it. The word carries a different precise meaning in each literature the project draws on, and the definitions follow the original sources.

<table><thead><tr><th width="200">Sense</th><th>What structure means there</th></tr></thead><tbody><tr><td><strong>Factored</strong></td><td>the sparse dependency graph among state variables across one time step</td></tr><tr><td><strong>State abstraction</strong></td><td>an equivalence or similarity relation on the state space that lets a decision maker ignore distinctions that do not matter for behaviour or value</td></tr><tr><td><strong>Bisimulation</strong></td><td>the exact version of that relation, two states equivalent when they have matching reward and matching transition behaviour into corresponding classes</td></tr><tr><td><strong>Object</strong></td><td>the decomposition of the state into typed objects and their relations</td></tr><tr><td><strong>Causal</strong></td><td>the directed graph of cause-and-effect relations among variables, actions and rewards, as opposed to merely correlational dependence</td></tr><tr><td><strong>Empirical game</strong></td><td>the pattern of how each player's payoff depends on the other players' strategies inside the estimated game</td></tr><tr><td><strong>Strategic (in)dependence</strong></td><td>the degree to which one player's best choice depends on the other player's behaviour, in a given region of states and actions</td></tr></tbody></table>

The seven fall into three families. Factored, object and causal structure are statements about the environment. State abstraction and bisimulation are statements about equivalence. Empirical game structure and strategic dependence are statements about the game. Or in one line: how the world factors, which distinctions to keep, and who must reason about whom. No claim is made that any one sense reduces to another.

A structure itself is a set together with a relation. The dependence is the relation the structure carries, and keeping the set in the definition is what lets a structure be named as a thing to test: a state variable, a payoff term, an edge of the interaction graph, a signal channel, a mechanism parameter.

## The game the account has to cover

Three domains motivate the work and they share five features: sequential play, compositional or graph-structured state, adversarial objectives, heterogeneous players, and endogenous environment dynamics. This is not a list of desirable properties. Each feature imposes one entrance condition on any account of strategic dependence, under one warrant written once: a feature enlarges what can happen in play, and an account blind to the enlargement returns one verdict where the games separate into many. For each feature, name the pair of plays it makes possible and ask whether the account separates them.

The benign party belongs to the fourth feature and is not decoration. It is always present in the real domain, users, civilians, bystanders, and prior two-party formulations omit it, which is a modelling limitation rather than an absence from the games. That is why the setting is named **three-party** with **heterogeneous players** rather than multiagent. Three-party places the work in the literature; heterogeneous players names the structural property, players asymmetric in objective and observation. The caveat travels with the term, since the naming comes from the cyber and Stackelberg literature, and pursuit-evasion and green security games may name the third party differently or lack one.

_**Compositional carries two senses and both are live.**_ In the state sense a single game's state divides into parts, a network of devices or a grid of locations, which is a property of the state. In the game sense a large game splits into smaller games, which is what compositional means in game theory. The ambiguity is not between factored and object representations. It is between a property of the state and a property of the game. Ask what is being divided. The project uses the state sense in its feature list and inherits the game sense from the literature it cites, which is exactly the kind of place a reader substitutes one for the other without noticing.

The representation is the multi-agent object-oriented Markov decision process rather than a factored MDP, and the reasons are all matching reasons. A factored MDP fixes a variable count; the object-oriented form gives per-host entities that recur across states, supports a varying number of objects, and shares one class-level transition function per class, which gives transfer across states and across object instances. In the multi-agent form the transition depends on the joint action and each agent carries a private reward. Ask whether the state has a fixed number of slots. If adding a host adds a variable rather than an instance of an existing class, the representation is factored rather than object-oriented.

## What the five candidates actually take in

The candidate set is seeded from game abstraction, because that is the body of work that built smaller games by exploiting non-uniform dependence.

<table><thead><tr><th width="230">Candidate</th><th>What it does</th></tr></thead><tbody><tr><td><strong>Graphical games</strong></td><td>Drops links between players. Keeps no edge between two players whose payoffs do not affect each other. The graph is fixed by the modeler</td></tr><tr><td><strong>Influence-based abstraction</strong></td><td>Drops outside state variables, keeps only what crosses into the local region. The kept set is chosen by a graph test</td></tr><tr><td><strong>Value-similarity abstraction</strong></td><td>Merges states whose future-strength trajectories are similar</td></tr><tr><td><strong>Information-theoretic influence</strong></td><td>Marks the state and action pairs where one agent changes the other's transition or reward. Zero means independent there</td></tr><tr><td><strong>Attention in multi-agent RL</strong></td><td>Drops links between agents, then weights the survivors. The cut is learned end to end by a gate</td></tr></tbody></table>

These are not five competing definitions of one thing. They are objects of three kinds: a map of where interaction exists, a ruler inside one player's view, and three meters that output amounts. Ask what each takes in and what it puts out and the difference is immediate: a game alone; a game plus fixed outside policies plus a region; a game plus a joint policy; one training run.

Organized by property rather than by candidate, the sharpest finding comes out of the opponent property. **None of the four is defined for an adapting adversary.** The graphical representation presupposes no behaviour at all. The influence construction requires the other players' policies fixed and known. The information-theoretic pair presupposes teammates with a shared reward. Attention presupposes co-trained agents inside one run. Against the three motivating domains, where the intruder, the evader and the poacher all adapt, every candidate needs the adversarial adaptation.

Two counts are live in the corpus. The status file says five and lists value-similarity among them; the taxonomy section says four and excludes value-similarity as the contrast case, since it measures the quality of an abstraction, which is a within-agent question and not dependence between players. The exclusion argument is the better one and it is the one on this page. The decision is mine and it is not made.

The same care applies to the unplaced candidate. Expressing a type at degree zero and not reading the type at all are different facts, and assigning attention a zero would assert the first when only the second is known.

## The generator

Every structure the generator reports falls in exactly one of two cases, and there is no third.

_**Set by construction.**_ Written directly as a generator parameter. True because it was set.

_**Measured.**_ It emerged from what was built, and its value is estimated afterward on the generated instance, which serves as its own referent, with sample counts reported beside it.

A record entry whose truth rests on neither would be an assumption wearing the clothes of a fact, and the whole evaluation chain above it would inherit the assumption. So ask where the number came from. A parameter, or a probe. If neither, the request is refused.

The measured case is not a concession. Part of strategic dependence is a property of play rather than of the game as written, since the same game yields one realized dependence under one pair of policies and none under another. The rules set a ceiling and play decides how much of it appears, which is why the generator has a strategy stage at all and why its final stage measures rather than sets.

Generation starts from a **decoupled base**, in which each entity's transition rule reads only that entity's own attribute and its own driver's action component, so the base provably contains no cross-entity dependence and every dependence is introduced afterwards as one explicit rule edit. The alternative route, generating a richly connected instance and verifying the requested structure by testing, fails on the expensive direction: soundness requires showing not only that the requested dependences hold but that no unrequested dependence crept in, and establishing absence by testing means testing every pair at every lag. One recorded exception. The adversary's reward reads the joint state, as harvest value at the poacher positions, because a fully decoupled reward would be constant and would fail the validity screen requiring rewards to vary under play.

**Refusal** is the generator's response to a request it cannot express or realize, given with its notion of infeasibility named rather than clipped to the nearest attainable value. Five notions, and a refusal names one: not specifiable, when the request falls outside the form's vocabulary; not attainable, when the request is well formed but no instance of the declared shape realizes it; not orderable, when the requested degree does not sit on the type's ordered scale; not verifiable, when the achieved degree could not be checked by any probe within a declared budget; and not knowable in a real domain, when the request's referent is a quantity no real counterpart could supply. Silent approximation is the thing being avoided, because it puts a value in the record that nobody requested and nothing guarantees, and then grades the learner against a truth that is itself an approximation of unknown quality.

One approximation is licensed and only one. Requests about played dependence name a target for a quantity the generator does not set, so the pools are grown toward the target, the realized map is measured, and the miss is published as a number rather than absorbed.

Six **perturbation operators** give the vocabulary of ways a handed structure can be wrong: declaring a present dependence absent, declaring an absent dependence present at a sampled level, reversing direction on a directed type, relabelling the type with the degree mapped to the same relative position, shifting the degree without crossing the bottom, and carrying a stale record across an instance change. Each maps a record to a record the edit forms could have produced on a neighbouring instance, so the learner is handed a possible truth rather than a malformed object. The degree shift is deliberately barred from crossing the bottom, so that strength errors never look like absence errors. A seventh exists in the vocabulary without being run, entity mis-individuation, which is the one error the given entity decomposition makes invisible.

## The learner

_**One learner, two manipulated parties.**_ The defender is the sole learner. The attacker and the benign party have their policies set by the experimenter, fixed within an episode batch, and varied across batches on a known schedule. They do not learn. The transition law the learner faces is therefore stationary within a batch, because the other two policies fold into the environment.

The price is stated openly: every learned quantity is relative to the manipulated policies in force when the data was collected, which makes it a property of that configuration rather than of the game. The compensation is that the manipulation schedule is the experiment's intervention channel on the opponent side. The defender's own actions are interventions and the attacker's are not, so a quantity defined interventionally over attacker variables becomes estimable only through the schedule.

Two checks on the learned model answer two different failures.

_**Fidelity**_ rolls model and environment from the same starts for a given number of steps and measures the divergence of the resulting state distributions, reported as a curve in the number of steps rather than as one number. A fidelity number without its horizon is not readable, since small per-step divergence still permits value error growing with the square of the effective horizon. Total variation, because that is what the model-based control bound consumes.

_**Readback**_ compares a recovered structure against the planted parameter of the generated game, one error measure per target quantity. A model can minimize its training objective and fail fidelity, having fit the data and not the law. It can pass fidelity and fail readback, its rollouts matching while its internal structure mislabels who drives whom, because fidelity constrains only the joint law and not its factorization. Only readback reads the model's insides, and it is available only where a planted parameter exists.

The representation is a three-way split of each device's dynamics by driver. The **controllable latent** is the part driven by the defender's actions. The **exogenous latent** is the part driven by background processes no agent controls, user activity, service fluctuations, routine noise. The **opponent embedding** is inferred from a history of tokens at that device. The policy operates on the controllable and opponent components only, so it does not react to uncontrollable environmental variation, while the reward decoder still conditions on the exogenous latent, so imagined rewards reflect its contribution.

The word exogenous is doing work that noise cannot do. Noise is uncorrelated with reward. This source is not, and that is the whole difficulty. Ask whether the process moves the reward. If it does and the agent cannot steer it, the word is exogenous.

Two **attention graphs** run in parallel across device slots and this is the distinguishing choice. In the controllable graph each device attends to others' controllable latents and to its own opponent embedding, and its weights carry strategic dependence conditioned on where the attacker is. In the exogenous graph each device attends to others' exogenous latents with no opponent access, and its weights carry environmental dependence from shared background processes. Every alternative found keeps one interaction graph. Keeping two is what stops environmental correlation from being read as strategic dependence. Find a device pair scoring high on the second and low on the first: that pair is environmentally linked and not strategically linked, and it can still be treated as a separate subgame.

Both sets of weights change within an episode, which gives a time-resolved picture of which pairs become strategically dependent as the attacker moves and which stay only environmentally correlated. That is the learned counterpart of the pockets at the top of this page.

## Where two of my own files disagree

<table><thead><tr><th width="330">The disagreement</th><th>Where it sits</th></tr></thead><tbody><tr><td>Best-action sensitivity or forfeited value</td><td>strategic dependence</td></tr><tr><td>One ideal measure or a family of them</td><td>strategic dependence</td></tr><tr><td>Four candidates and a contrast case, or five</td><td>the candidate set</td></tr><tr><td>Type and degree, or the superseded pair</td><td>the vocabulary of record</td></tr><tr><td>The four-level progression, current or retired</td><td>degree</td></tr><tr><td>Network defense or attack-defense</td><td>the vocabulary of record</td></tr><tr><td>Compositional in the state sense or the game sense</td><td>compositional</td></tr></tbody></table>

Four of the seven are one problem seen from four sides. The project changed its vocabulary once and the largest file in it was not rewritten. That is a housekeeping matter, and it is also the reason a reader meets the retired words first.

One of the seven is not housekeeping. Whether a candidate is an unbiased estimator of strategic dependence cannot be asked yet, because strategic dependence has not been written down as a definite functional with its arguments fixed: which game, which policies, which summary. The gap is in the target, not in the candidates. So the headword is currently a concept with a discriminating test and four partial instruments, and the choice between one ideal measure and a family is mine and is not made.

[**Download the full lexicon (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/project-lexicons/cwm_learn_structure.pdf)

## Publications

<table><thead><tr><th width="100"></th><th width="400">Paper</th><th>Authors</th><th></th></tr></thead><tbody><tr><td><img src="../../../.gitbook/assets/badge-preprint.png" alt="Preprint" data-size="original"></td><td><mark style="color:green;">Learning Strategic Structure in Sequential Adversarial Games</mark></td><td><strong>Y. Du</strong>, <a href="https://www.cs.utep.edu/kiekintveld/">C. Kiekintveld</a></td><td></td></tr></tbody></table>

## Collaborators

<table><thead><tr><th width="150"></th></tr></thead><tbody><tr><td><img src="../../../.gitbook/assets/collab-christopher-kiekintveld.png" alt="Christopher Kiekintveld" width="48"><br><a href="https://www.cs.utep.edu/kiekintveld/"><strong>Christopher Kiekintveld</strong></a><br>University of Texas at El Paso</td></tr></tbody></table>

_Last updated: 2026-08_
