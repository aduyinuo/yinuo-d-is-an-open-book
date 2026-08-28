---
icon: gauge-high
---

# AcceleratePSRO

A world model is useful for more than prediction.

## The intuition

Once a world model exists, the interesting use is not only prediction but acceleration: imagined rollouts can stand in for expensive environment interaction when computing a best response inside PSRO.

Co-learning a world model with the empirical game is not itself new — Dyna-PSRO does exactly this. The open question is what a _faulty, adversarially-stressed_ model does to that loop. Does model-based imagination still reduce the regret PSRO leaves on the table, or does a wrong model inject a bias that the game-solving step then amplifies? When does imagination help, and when is it worse than honest, slower interaction?

This is where "what if the world model is faulty" and "use the world model to expedite PSRO" turn out to be the same question asked twice.

## Where acceleration can be introduced

The working question is where a PSRO-like loop can be sped up without losing solution quality — which of its steps tolerate approximation, and which do not. Three outputs carry the track:

1. a catalogue of the acceleration levers available in the loop
2. a risk register for the approximation shortcuts each lever takes
3. a validation protocol that says whether an accelerated run reached the same place a slower one would have

## The experiment

The risk is that the acceleration runs negative: model bias becomes bias in the best-response target, which the game-solving step then amplifies, and slower honest interaction wins.

The experiment settles it by degrading model quality along a controlled axis and measuring regret against interaction budget, relative to model-free PSRO. The deliverable is the crossover point below which imagination stops paying.

This is also the strategy exploration problem — assembling a strategy population that represents the full game under a computational budget.

## Environment

The work runs against **CyGym**, a simulation-based game-theoretic analysis framework for cybersecurity, which supplies the empirical game the loop is solved over.

## Whose words these are

This track has a vocabulary problem the other two do not. Almost every word in it belongs to somebody else already. PSRO, the restricted game, the response oracle, the strategy exploration problem and regret all arrive with fixed definitions from empirical game-theoretic analysis. Dyna-PSRO already co-learns a world model with an empirical game, so the obvious sentence is taken. CyGym is somebody else's simulator with somebody else's game model attached.

What is mine here is small and it is worth stating exactly: three outputs, one experiment, and one number. Everything below separates the borrowed part from those, so that a sentence about this track cannot be read as a claim on the borrowed part.

## The loop, in four objects

_**PSRO.**_ An iterative scheme that alternates two steps: solve the restricted game over the strategies collected so far, then compute a new strategy that responds to that solution and add it to the set. It is not self-play, which trains against the current copy and keeps a set of size one at every moment, and it is not fictitious play, which responds to the empirical average of history rather than to a solution of a restricted game. It generalizes both, and it generalizes the double oracle method by replacing the exact best-response oracle with a learner. Ask what the new strategy responds to.

_**The empirical game.**_ The payoff model over a restricted set of strategies, with every entry estimated by simulation. Count the entries. If the payoff of every joint strategy had to be estimated by running the game, the object is an empirical game and its size is the budget. This is the term the three tracks meet on, and [Learn Structure](strategic-structure.md) states the cost argument in one sentence.

_**The meta-strategy solver.**_ The routine that computes a mixed profile from the current restricted game, which is the target the next response is computed against. It is a slot rather than a solution concept, and Nash is one filler among several.

_**The response oracle.**_ The routine that computes or learns a best response against the target the solver designated. Not an exact best-response oracle, which is what double oracle assumes and what almost no interesting game supplies. In PSRO the oracle is a reinforcement learner and its output is approximate, so every guarantee downstream of it inherits the approximation.

The two per-iteration costs are the response solve and the meta-game solve, and those are the two things any acceleration catalogue has to address. Sitting above both is the **strategy exploration problem**: choosing which strategies enter the restricted game so that it represents the full game well at the smallest number of members. Not exploration in the single-agent sense, which chooses actions inside one episode. This chooses members of a population, and each member costs a full response computation.

## What Dyna-PSRO settles, and what it leaves

Dyna-PSRO is PSRO with two alterations: a world model trained in parallel with the loop's own routines on the data those routines already produce, and a Dyna-style learner used as the response oracle, so planning in the model substitutes for part of the environment interaction a response would have cost. The model persists across iterations and is fed by every episode the loop runs, which is what makes it a co-learning claim rather than a per-iteration speedup claim. Ask where the model's training data comes from. If it comes from the payoff-estimation and response-learning episodes the loop was going to run anyway, the model is co-learned at no extra collection cost.

It establishes that the loop is sound and that it reduces both regret and experience count on partially observable general-sum games. Its own account of model error is that prediction errors compound over long rollouts while medium-term planning still helps with an imperfect model.

What it does not establish is what a faulty, adversarially stressed model does to the same loop, and that is the whole difference. Dyna-PSRO's model is imperfect because it is learned. The model this track studies is imperfect because something is stressing it, and the region it is wrong about is chosen rather than stumbled into. A result that model error is tolerable on average says nothing about a model error somebody selected.

## The catalogue of levers

An **acceleration lever** is a place in the loop where an expensive operation can be replaced by a cheaper one that the same solver can still consume. It is not an implementation optimization, which makes the same computation run faster and changes nothing about what is computed. A lever changes what is computed and therefore has an approximation to account for. Ask whether the replacement changes the object the next step consumes. If it does not, it is engineering.

The catalogue is organized by the operation each lever attacks, and the existing PSRO variants supply most of the entries.

<table><thead><tr><th width="230">Lever</th><th>What it attacks</th></tr></thead><tbody><tr><td><strong>Anytime PSRO</strong></td><td>The response solve, by keeping one approximate best response and updating it for a small number of steps per inner iteration rather than solving to convergence</td></tr><tr><td><strong>Efficient PSRO</strong></td><td>The meta-game estimation, by a minimax formulation over an unrestricted-restricted game, which removes the need for meta-game simulation</td></tr><tr><td><strong>Extensive-form double oracle</strong></td><td>The restricted game itself, by allowing population strategies to mix at every information set rather than only at the root</td></tr><tr><td><strong>Dyna-PSRO</strong></td><td>The interaction cost of the response</td></tr></tbody></table>

The **risk register** is the record, per lever, of what the shortcut assumes and what breaks when the assumption fails. It is not a limitations section, which is written after the result and is about the study. This is written with the catalogue and is about the method, and it is what makes the catalogue usable by somebody choosing a lever. For each one, name the quantity the shortcut is approximating and the direction the approximation moves it. A lever whose entry cannot name both is not understood well enough to be catalogued. The entry that matters most is the model-based one, because its shortcut is the one with no bound: a compact object is safe to substitute exactly when it preserves the property the solver needs, and the failure is borrowing a construction whose preserved property is not the one this solver needs.

The **validation protocol** decides whether an accelerated run's answer is the answer the unaccelerated run would have produced. Not a speedup measurement, which compares wall clock or interaction count and says nothing about the answer. The comparison quantity is regret against a combined strategy set: pool the strategies both methods produced and evaluate each method's solution against the pool. Without it, an accelerated run can look better simply by having explored a smaller set.

## Two words that need their axis stated

_**Acceleration, on two different axes.**_ The PSRO variants in the catalogue accelerate by reducing computation. This track accelerates by reducing environment interaction, and pays for it in computation and in model error. The word covers both and the risks are not the same. A computational lever's worst case is that it converges more slowly. An interaction lever's worst case is the negative case, a wrong answer arrived at quickly. Any catalogue that lists them in one column has to carry the axis in the row.

_**Faulty, in two senses this page merges on purpose.**_ On [Next](next.md), a faulty model is one an adversary has found the wrong region of. Here, a faulty model is one whose quality has been degraded along a controlled axis by me, in order to find a crossing. The experimental version is the instrument and the adversarial version is the phenomenon, and the instrument is a proxy for the phenomenon only if the degradation axis reaches the region an adversary would have chosen. Whether it does is a design question for that axis, and it is the question that decides whether the crossover point means anything outside the experiment.

_**Regret and interaction budget, both of which need their set named.**_ Regret is the payoff a player gives up by playing its solution rather than its best available response, taken over a stated set. Exploitability is the same idea over the full strategy space, which is not available here, which is why the set has to be named every time. Two regret numbers computed over two different sets are not comparable, and comparing them is the most common way an accelerated run flatters itself. Interaction budget counts environment steps across every routine of the loop, and the count has to include the payoff-estimation episodes, since in PSRO those are a large part of what the loop spends.

The word honest in the question above is doing work and is worth keeping. Environment interaction is honest in the sense that it cannot be wrong about the environment, only expensive. That is the trade the crossover point prices.

[**Download the full lexicon (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/project-lexicons/cwm_accelerate_psro.pdf)

**Related:** [FOE-Dreamer](environment.md) supplies the factored world model, [Learn Structure](strategic-structure.md) says where in the game strategic reasoning is worth spending, and [Next](next.md) carries the open questions this track sits inside.

_Last updated: 2026-08_
