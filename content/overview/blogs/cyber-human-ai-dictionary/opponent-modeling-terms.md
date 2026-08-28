---
description: Nine senses of one word, and the nine places where two passes disagreed.
icon: almost-equal-to
---

# Opponent Modeling Terms

My Headspace page asks the question this page exists to make answerable.

> How exactly can opponent modeling benefit network defense? What network security (or specifically, adversary emulation, threat modeling, etc) constrains and demands pose interesting challenges on opponent modeling?

The [dictionary overview](./) puts opponent modeling, threat modeling and adversary emulation side by side, three siblings placed on five dimensions. The Headspace question puts two of them underneath the third, as the source of its constraints. Both placements are mine, they are days apart, and they are not the same claim.

So I counted. Forty occurrences of the word in my own files, nine more anchored in the three fields that use it, nine senses. Forty of the forty-nine hold one sense through a second pass made with the file names taken away. Nine do not, and those nine are the ones worth having.

## Nine senses

Four fields each, in the order I use them. Definition. Distinguishes it from. Operational test. In my project.

_**Learned opponent representation.**_ A vector inferred from the modeling agent's own observation stream, trained to predict something about the other agent, and consumed by a policy. It differs from type inference because no set of opponents is named anywhere: the representation is whatever the loss makes it, and it carries no promise of being interpretable as a type. The test is whether there is a decoder or a classifier head used in training and thrown away before deployment. This is FOE-Dreamer's opponent latent, the per-device opponent state in PickYourBattles, and the opponent latent on the Cyber World Modeling pages.

_**Type inference.**_ A posterior over a set of opponent types fixed before play began, updated from observed behavior. The set exists first and the inference returns a distribution over it, which is what separates it from a learned representation. It is also absolute, and does not shift when the population around the opponent changes. The test is whether you can write down the types before the first episode and get back a number per type. It is the word "type" in the approach section of the FOE-Dreamer paper, and the recovery of a hidden type from behavior on the Mental World Modeling pages.

_**Best response to a fixed strategy.**_ The opponent is a strategy already sitting in a population, and modeling it means computing a best response and putting the answer back in the population. Nothing is inferred. The opponent is handed to you and the operation is optimization rather than estimation. The test is whether the output of the modeling step goes into a strategy pool rather than into a policy's input. This is AcceleratePSRO, the whole loop, and it is what Learn Structure's opponent-blindness test decides can be skipped for a region.

_**Behavioral adversary model.**_ A parameterized departure from expected-utility maximization, fitted to or imposed on the choices of a human adversary. A type is a label, a behavioral model is a curve, and its parameters have psychological names and vary continuously. The test is whether the model has a parameter you could report to a psychologist, a loss-aversion multiplier or a response precision. This is the Biased Attacker work in full, prospect theory's value function sitting inside the POMDP.

_**Categorization by a bounded observer.**_ A small number of categories assigned by an agent that will not carry one model per partner, made relative to the group rather than against a fixed threshold. Hold a partner's behavior fixed and change the room around them: if the category changes, this is the sense, and if it does not, you were looking at type inference. Cooperative, conditional and exploitative, assigned against the group mean, on the Iterated Prisoner's Dilemma page.

_**Theory of mind.**_ Attribution of unobservable mental states to the other agent, including that agent's beliefs about you, to a stated depth. The model contains a model of the modeler, and depth is a property of the representation that has to be declared. I do not use it. It is the sense the cognitive science literature reaches for first, and naming it here is what keeps it from being read into the other eight.

_**Threat modeling.**_ A prospective structured record of protected assets, system boundaries, adversary goals, knowledge and capabilities, reachable attack surface, adverse events, likelihood assumptions, and controls. It is written before the exercise and it says what is out of scope. It is a document, not a run, and the test is whether it contains a list of things it declines to consider. Section 4 of the FOE-Dreamer paper is one, and it is doing the bounding job rather than the characterizing job: the two scripted profiles are fixed-class, and adaptive learning adversaries that retrain against the deployed defender are declared outside the claim.

_**Adversary emulation.**_ Reproduction of a documented actor's tactics, techniques and procedures so that a red team can test detection and response against that actor's behavior. It differs from threat modeling, which characterizes a space rather than enacting one, and from red teaming, which searches for any way to defeat the system. Emulation is the narrower case that fixes one adversary's known behavior. The test is whether you can name the real actor being reproduced and cite the report it came from. I do not use it as a method. It appears twice, as a sibling concept on the overview page and as a source of constraints in the Headspace question.

_**Attacker construction.**_ Writing the opponent you will train or evaluate against, with its behavior specified by you and its ground truth available to you by construction. The fidelity target is a behavioral property, sophistication or bias or patience, rather than a named actor, and there is no report to cite because the actor does not exist. The test is whether you wrote the attacker and can read its internal state out of the simulator. B-line and Meander. Avoidant and Enticed. The three prospect-theory profiles. This is the sense my table has no row for, and it is the one that appears most often in my own files.

## Three fields, three outputs

The same object goes by three names, and the output is the reliable tell. Multi-agent RL returns a vector, and calls it an opponent embedding or a latent. Game theory returns a distribution or a strategy, and calls it a type or a belief over types. Network security returns a document, and calls it a threat actor profile or a threat model. When a conversation stalls, ask what the other person expects to hold in their hand at the end of the modeling, and the sense falls out.

One row of that translation is not a translation, and it is worth saying plainly. Opponent model and threat model are not each other's words. They are the same slot filled by different objects, one learned and one written, one consumed by a policy and one read by a person. My own table already says so in its Output column. The Headspace question is asking what the second can demand of the first, and that is a real question with no answer yet in any of the three fields.

## What the five dimensions cannot hold

Two things the table misses, both visible once the senses sit next to each other.

_**Fidelity rises with specificity, in every sense but one.**_ Abstract representations describe generic adversaries and executable reproductions reproduce particular actors. The exception is attacker construction, which is maximally executable and deliberately generic, a class rather than an actor. That single off-diagonal cell is why it needs a row of its own instead of being read as a weak form of adversary emulation.

_**The epistemic operation axis has no position for optimize.**_ It runs describe, infer, predict, simulate and enact. Best response does none of those. It takes an opponent as given and returns a policy. Either the axis gains a fifth position or best response is declared outside the dictionary's scope, and the second option costs me AcceleratePSRO.

[**Download the full entry (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/cross-domain-dictionary/dict_opponent_modeling.pdf)

_Last updated: 2026-08_
