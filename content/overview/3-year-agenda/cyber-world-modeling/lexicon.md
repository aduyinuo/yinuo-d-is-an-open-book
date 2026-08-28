---
description: The words all three tracks share, and the five places they disagree.
icon: spell-check
---

# Lexicon

Three tracks sit under this heading and they share a vocabulary nobody negotiated. [FOE-Dreamer](environment.md) built the factored model. [Learn Structure](strategic-structure.md) asks where in a game the strategic part actually lives. [AcceleratePSRO](accelerate-psro.md) asks what a wrong model does to a game solver. Each page was written at its own time, and each took its words from a different literature, so the same word arrives three times carrying three histories.

A term belongs on this page when more than one track uses it. Where two tracks use one word for two things, both uses stay, and the entry says how the other track uses it. That difference is a finding. I am not tidying it away.

## Who owns which words

One sentence of mine already divides the labour, and it is the scoping line for the whole page: FOE-Dreamer supplies the factored world model, Learn Structure says where in the game strategic reasoning is worth spending, and [Next](next.md) carries the open questions the third track sits inside.

Read that as a statement about vocabulary rather than as a table of contents. FOE-Dreamer owns the representation words. Learn Structure owns the allocation words. AcceleratePSRO owns the budget words. Nearly every disagreement further down is a word that crossed one of those two boundaries and kept its old sense on arrival.

The two challenges on the [cluster page](README.md) are why the vocabulary has the shape it does. The first, that more than one process drives a single observation stream, is why _factoring_ carries weight here and why contamination is the failure it names. The second, that the stream is degraded and the compute is small, is why _operational_ is stipulated narrowly instead of used as praise, and why every acceleration word is a word about a budget.

## The representation words

_**World model.**_ A learned model of the transition dynamics and the reward, queried by rolling it forward instead of acting in the environment. No page of mine gives it a one-sentence definition, which is itself worth recording, since it is the term the cluster is named for. It is not a simulator. A simulator is written by a person and is correct by construction where it is correct at all; a world model is fitted, so it is wrong somewhere, and where it is wrong is a property of the data it saw. Ask what produced it. If a person specified the transition rules, it is a simulator. If a loss was descended on interaction data, it is a world model, and the next question is where it was fitted. The three tracks put three demands on the same object: be accurate, be readable, be cheap.

_**Factoring, factorization.**_ The split of a latent state into components by the source of the variation each carries, so that an error in one component is contained inside it. Not a factored MDP, where the factoring is a property of the game as written and the parts are state variables. Here the parts are sources of variation, the split is learned, and the argument for it is error containment rather than compactness. Perturb one component and ask what else moves. If everything moves, the split is nominal. FOE-Dreamer factors by driver: defender-driven, environment-driven, opponent-inferred. Learn Structure factors per device and keeps two attention graphs so that environmental correlation is not read as strategic dependence. AcceleratePSRO inherits whichever factoring the model it accelerates happens to carry.

_**Latent.**_ A learned state variable that is not observed, carried forward by a recurrent model and read by the decoders. Used as a count noun throughout the cluster, which is the usage that matters. It is not a belief: a belief is a distribution over a state space that already exists and is named, while a latent has no referent fixed in advance and what it holds is settled by the loss and by whatever separation the architecture enforces. Ask whether the quantity has a name outside the model. A compromise flag has one. A latent does not, and calling it the opponent is a claim about identifiability rather than a description.

_**Opponent latent.**_ The component of the representation that carries the adversary's contribution, inferred from defender-side observation and read by whatever consumes it. Not opponent modeling in the game-theoretic sense, which returns a strategy or a type for a player, and not threat modeling, which returns a catalogue of what an adversary could do. This one returns a vector, and its warrant is that the decoders improve when it is present. Remove the component and retrain. If the reconstruction and the reward prediction do not degrade, nothing about the opponent was in it. AcceleratePSRO does not carry one at all, because in a solver the opponent is a member of the strategy population rather than a latent.

## The failure words

_**Drift.**_ Movement of the opponent latent away from the region the model was fitted on. The cluster carries two senses of the word, both mine, in neighbouring paragraphs of one page. The borrowed sense is distributional shift of the policy, where the learner does the moving. Mine is the one where the adversary does. Ask who moved, and the sense follows. Learn Structure has the same phenomenon under a different name, the manipulation schedule, because there the experimenter moves the opponent deliberately and on a known schedule. Same movement, opposite epistemic position.

_**Objective mismatch.**_ The gap between the loss the model descends and the accuracy the policy needs, since the first is averaged over the data and the second is local to where the policy will act. It is not underfitting. Underfitting is failure on the same distribution the loss is averaged over; objective mismatch is compatible with a low training loss and is caused by it. Compare the model's error on the data distribution against its error on the states the policy visits. AcceleratePSRO inherits it in the sharpest possible form, because the states a best response visits are the states the previous iteration did not.

_**Model exploitation.**_ A policy improving its modelled return by moving into states where the model is wrong. Objective mismatch is a property of the loss; model exploitation is a property of the optimizer's answer to it. Score the policy in the model and in the environment, and a gap that widens with the number of policy improvement steps is exploitation.

_**The twist.**_ Both of those failures are borrowed from single-agent model-based reinforcement learning, where the drift is an artefact of the training loop. Here it is an opponent's objective, so uniform predictive loss is selected against. The test is whether the process producing the shift has an incentive. If it does, no amount of care inside the training loop closes the gap, because no update rule bounds a second party. That one sentence is what makes the first track and the third track two views of a single problem.

_**Fails honestly, fails silently.**_ Two failure shapes. Honest failure is wide predictive uncertainty in the region the model is wrong about. Silent failure is a sharp prediction that is wrong. This is not calibration in the ordinary sense, which is averaged over a whole test set; the distinction here is local, and only the region an adversary would choose is being asked about. Find a region the model is wrong about and read its predictive spread there. The FOE-Dreamer page states the same idea as a question. The Next page states it as the coinage, and the coinage is better, because it says what the two failures look like rather than which one is preferred.

_**Identifiability.**_ Whether the adversary's contribution is recoverable from the data one side actually holds, separately from everything else in the latent. It is not accuracy. A model can predict well and still hold no separable adversary component, since fitting the joint law does not constrain its factorization. Vary the opponent while holding the environment fixed; if the component that is supposed to carry the opponent does not move, it is not carrying it. FOE-Dreamer states the assumption and the fallback in one breath, and the fallback surrenders attribution and keeps the alarm.

## The allocation words

_**Strategic dependence.**_ The degree to which one player's best choice depends on another player's behaviour, in a given region of states and actions. Four neighbouring notions of structure are all properties of the game as written: the dependency graph of a factored MDP, the relations of an object-oriented state, the causal graph, and empirical payoff dependence. This one is a property of how the game is played, and it moves while the game does not. Fix a game completely and change only one player's behaviour. If the other player's best action changes, dependence is present there and none of the four neighbours can express it.

_**Non-stationary.**_ A transition law that changes over the interaction because a party outside the model is changing its own behaviour. Not endogenous environment change, where the world moves on its own for reasons of its own, a device wearing out or a service churning. Both violate stationarity and only one of them is answering the defender. The discriminating clause is on the cluster page already: it shifts when the defender starts to model it well. Learn Structure buys stationarity back by fixing the other two parties within a batch, and states the price openly.

_**Operational.**_ A claim about a specific list of things being real, given together with the complementary list of things that are emulated. Not real-world, production, or deployed, none of which carry a list and all of which a reader will hear as a stronger claim than the one being made. Ask for the two lists. A use of the word that cannot produce them is doing rhetorical work rather than descriptive work. Six items real and three emulated, on the FOE-Dreamer page.

## The budget words

_**Interaction budget.**_ The number of environment steps a method is allowed before its result is read. Not the compute budget, which counts gradient steps and wall clock. The two come apart exactly where a world model is used, since imagined rollouts cost compute and no interaction. Ask what the horizontal axis of the plot counts. FOE-Dreamer reports both, a three-day budget on one GPU and matched compute against the baselines, because the deployment argument is about interaction and the fairness argument is about compute.

_**Imagination, imagined rollout.**_ A trajectory generated by rolling the learned model forward rather than by acting, used wherever an environment trajectory would have been. The word is reserved for a learned model, and the reason the distinction is kept is that only one of the two can be wrong in a way nobody specified. Ask whether the generator of the trajectory was fitted. If it was, the trajectory carries the model's error into whatever consumes it.

_**Regret.**_ The payoff a player gives up by playing its chosen strategy rather than the best available response, read against a stated set of alternatives. Not episode loss, which is FOE-Dreamer's metric and is absolute. Regret needs a comparison class and is meaningless without one. Name the set the maximum is taken over. If nobody can name it, the number is not a regret.

## Five places the tracks disagree

_**Strategic dependence, defined twice.**_ The project page says it is how much a player's best action turns on what the other player does. The cluster page, one level up and about the same project, says it is how much value a defender forfeits by ignoring the opponent. The first is sensitivity of a best action, the second is a loss in payoff units, and they are not the same functional. The gap has a name inside Learn Structure: one of the two recorded holes in its measure set is a pairwise deviation gain in payoff units, and nothing in the candidate set delivers it. Until that hole is filled, the cluster page is naming a quantity the project page does not yet define.

_**Adversary, opponent, attacker, poacher.**_ Four words for the other side, and no page says whether the difference is intended. The reading that fits every occurrence is that adversary names the party, opponent names the model of the party, and attacker and poacher name the role in a specific domain. It fits, and it is stated nowhere, so a reader arriving from any one page will read the other two through their own use.

_**Structure, in a cluster that names a project after it.**_ Learn Structure's own glossary carries seven senses of the word and says so. FOE-Dreamer uses the word in a sense none of the seven covers, the split of a latent by the source of its variation. AcceleratePSRO uses it barely at all, and where it does the referent is the empirical game's payoff structure. The reconciliation, if one is wanted, is that FOE-Dreamer's sense is the learned counterpart of the object and causal senses, applied to a latent rather than to observed variables.

_**The environment, in three incompatible senses.**_ FOE-Dreamer's environment is Daedalus, a substrate on which things happen. Learn Structure's is a generated instance whose every dependence is recorded with the grounds on which its value is known. AcceleratePSRO's is CyGym, whose job is to supply an empirical game. The first supports a deployment claim, the second a recovery claim, the third an equilibrium claim. None supports the others, and a sentence in the cluster's voice about running in realistic environments is true of one third of the cluster at a time.

_**Model error, priced three ways.**_ FOE-Dreamer prices it as a defence failure: which errors a defender survives, and whether the drift is caught before the region is reached. Learn Structure prices it as a recovery failure and splits it in two, since a model can fit the data and not the law, and it can fit the law while mislabelling who drives whom. AcceleratePSRO prices it as a solver failure: model bias becomes bias in the best-response target, which the game-solving step then amplifies. One quantity, three consumers, three different questions asked of it. That is why the cluster cannot report a single number for how good its world model is.

## The four questions, and the terms they will need

The cluster page closes on four questions. Two of them already have vocabulary and two do not.

1. Whether a world model is reasonably accurate, and which errors a defence agent in an operational network can accept. The terms are above: honest against silent failure, drift, the failure taxonomy, the success criteria fixed in advance.
2. Whether a reasonably accurate model can expedite the search for strategic responses rather than only roll the world forward. The terms are on the [AcceleratePSRO](accelerate-psro.md) page: acceleration levers, the risk register, the crossover point.
3. How to factor a model so that it generalizes to novel scenarios with zero or few-shot training. No page in the cluster develops this. What exists is identifiability, which is the negative half of the same question.
4. How to compose a suitable model for a target operational environment, given a set of components. Also undeveloped, and the nearest thing to a vocabulary is Learn Structure's per-type record, since a component set that can be composed is a component set whose dependences are declared.

Questions three and four appear once each, on the cluster page, and nowhere else. They are the open ground.

[**Download the full lexicon (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/project-lexicons/cwm_shared.pdf)

_Last updated: 2026-08_
