---
description: Sixteen senses of transfer in my own files, and the two a security room reaches for first.
icon: almost-equal-to
---

# Transfer Learning Terms

My publication list already carries this word in two senses. _Accounting for transfer of learning using human behavior models_ is about a person carrying a skill from one task to the next. _Crossing the Cyber Divide: Sim-to-Sim and Sim-to-Real Transfer for RL Agents_ is about a policy being executed in a simulator it was never trained in. Neither title tells a reader which one is meant, and the two do not share a single technical commitment.

So I counted the word across my own writing before defining it. Fifty-nine files, two hundred and sixty-seven occurrences, from the website and the FOE-Dreamer manuscript and the RAISE sections and the Learn Structure notes and the mind maps. Sixteen senses. Two of the sixteen are what a security audience hears first, and neither of them occurs in my files even once.

## What moves is a policy or a model

_**Policy transfer across environments.**_ Executing a policy trained in one environment inside a second whose state space, action space or dynamics differ, with the source policy left unchanged. The test is whether a wrapper has to be written before the policy can emit a legal action. This is the whole of the RAISE work, and a hundred and twelve of the two hundred and sixty-seven occurrences sit in its nine section files.

_**Sim-to-sim and sim-to-real.**_ The same thing, where the target is the place the policy is meant to run rather than another simulator of equal standing. My position is that these are one problem with one difference: sim-to-real is sim-to-sim with a target that is only partially known. Supplying the missing ground truth collapses the second into the first, which is still hard, because finding an abstraction that relates two fully specified environments is itself computationally difficult. Two of my projects use this sense against each other. FOE-Dreamer removes the simulator stage so that no such step is needed. The RAISE work studies the step directly.

_**Transfer to unseen opponents.**_ A defender trained against one set of attacker classes holding up against a class it never saw, with the environment held fixed. What changes is the adversary, not the network. This is the sense a security reader supplies by default when nobody names one, and it is a different claim from the two above: variation inside the trained attacker classes, transfer to unseen classes, and an adversary that adapts against the deployed defender are three questions travelling under one word.

_**Transfer learning, in the survey sense.**_ Pan and Yang's definition. Improving the learning of a target predictive function using knowledge from a source domain and task, where the domains or the tasks differ. This page is named for that sense and almost nothing in my corpus is that sense. What the RAISE method does is closer to unsupervised domain adaptation, since the encoder sees unlabeled observations from the target and no reward from it, while the policy takes no gradient step there at all.

_**Reuse inside one training run.**_ A shared network or representation carrying across iterations, epochs, or members of a population inside a single procedure. Whether a later PSRO epoch is a different task is a real question and not a settled one, which is why this one keeps coming back ambiguous.

_**Generalization to unseen configurations.**_ One policy performing on instances of the same environment family it was never trained on, with no gradient step at test time. No wrapper is written and none is needed, and that is the whole difference from the first sense.

## What moves is a claim, a method, or a person

_**Method transfer between literatures.**_ A measure, a construction or a proof carried out of the field that produced it and into mine, with its presuppositions rechecked in the new setting. This is not a citation. A citation moves a sentence. This moves an operation together with the conditions under which it is licensed, and the conditions are what fails first: one row of the Learn Structure adaptation table records a measure whose transfer is stopped by a presupposition stated in its own source.

_**Whether a result survives the move.**_ Whether a finding obtained in one environment remains true in another. The subject of the verb is a claim, not an agent, and it can fail while the engineering succeeds. A transferred policy that scores well has either learned the task or learned the benchmark, and the score alone will not say which.

_**Transfer of learning, in a person.**_ A person applying what was learned in one setting to another, with Barnett and Ceci's near-far taxonomy as the standard placement. It is not retention. Someone who can recite an operation has retained it, and whether they deploy it on a problem that does not announce which operation it wants is the other thing entirely. The finding in my own corpus is that the two come apart, because general heuristics conceal many sub-strategies that must themselves be learned. If the thing that moves is inside a person, no amount of architecture talk applies and the evidence standard is behavioral.

## Homonyms, and why they matter

Bytes moving between hosts. Transfer entropy, which is conditional mutual information between a source process's past and a target's present. Transferable utility, which is what licenses the Shapley construction. State transfer in the control sense, priced by input energy. And the institutional kind, a technology transfer grant or a transfer student.

These share the spelling and nothing else, and three of them sit in the same folders as the senses above. Two files sitting next to each other in Learn Structure carry four senses between them, of which one is the word this page is about. A search over that folder for the term returns mostly noise, which is worth knowing before running one.

## The two senses I never use

This is the part worth carrying into a room.

_**Attack transferability.**_ An adversarial input crafted against one model succeeding against a second model the attacker never had access to, which is what makes black-box attacks practical. Every sense above treats moving as the goal and failure to move as the problem. Here the moving is the failure, and a defense works by making transfer harder, which is the exact opposite of what my transfer paper optimizes. A reader arriving from adversarial machine learning will read that paper's title against this sense first and expect a threat model.

_**Risk transfer.**_ A risk treatment option in which the financial consequence of a risk is moved to a third party by insurance or by contract. Nothing technical moves and the risk itself is unchanged. This is the sense a governance audience hears first, and it is why the phrase transfer assumptions checklist on my own project page wants renaming before that page reaches one.

## The boundary my own corpus keeps failing to mark

I assigned every occurrence, then assigned them all again with the sense labels shuffled and the first pass hidden. Ninety-two percent came back the same. Every one of the disagreements sits on one boundary: whether the target is a new configuration of one environment or a new environment. That is the distinction that decides whether a wrapper has to be written, and it is the one my sentences leave out.

## What to say instead

Say policy transfer, not transfer learning, for the RAISE work, because no learning happens in the target. Say cross-environment or cross-opponent, whichever is meant, before the word transfer, since that single qualifier separates the two senses my two papers use. Say unseen configuration when no wrapper had to be written. Say the result holds, not the result transfers, so a claim about evidence does not get read as a claim about engineering. Never say transferability with nothing attached to it.

One term is missing from my vocabulary altogether. Pan and Yang name the case where source and target are unrelated and moving knowledge between them makes the target worse: negative transfer. Nothing in two hundred and sixty-seven occurrences names it, and my own strongest result about matching observation shape without matching distribution is exactly that case.

[**Download the full entry (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/cross-domain-dictionary/dict_transfer_learning.pdf)

_Last updated: 2026-08_
