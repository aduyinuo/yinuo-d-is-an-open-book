---
icon: family-pants
---

# Small Groups

<figure><img src="../../../../.gitbook/assets/ps-winter-survival.gif" alt="Winter survival task: individual rankings converging on a group ranking, against the expert ranking"><figcaption><p>Four people rank twelve items. The group then has to agree on one ranking.</p></figcaption></figure>

The winter survival task. A plane goes down in a frozen forest and twelve salvaged items have to be ranked by how much they matter to staying alive — a lighter, newspaper, a compass, gauze, a knife, an air map, canvas, a shirt, whisky, chocolate, rope, an ax.

There is an expert ranking, so error is measurable. Each person ranks alone first. Then the group has to produce one ranking together.

## What the discussion does

The animation shows the talk and the ranking side by side. Three error figures track along with it: how wrong the average member was alone, how wrong the simple pool of their four rankings is, and how wrong the ranking is after they argue.

Pooling already helps before anyone says a word — four noisy rankings average out. The question is whether talking adds anything on top of that, and if so, which exchanges did the work.

## Groups of language models, on the same task

We ran the same kind of task with groups of LLM agents talking freely, and compared them against human groups on an open dataset.

The agent groups **outperformed the human groups**, and gained more from discussion — their scores improved further after free conversation than the humans' did.

The way they talked was different too. Agent groups produced **more disagreements**, **more complex statements**, and a marked **preference for positive statements** compared with people. So the advantage doesn't come from being agreeable and converging quickly. It comes with more argument, not less.

That cuts against the intuition that synthetic groups would collapse into consensus. It also raises the obvious question for anyone thinking about mixed teams: whether an agent's willingness to disagree survives contact with a human who outranks it.

## The score, and the scale it sits on

This is the one project in the cluster whose unit is not a mental operation. The unit is an utterance, the object is a group rather than a solver, and the ranking is scored against an expert answer, so error is a number rather than a construct anyone has to code. That makes it the cheapest project here to measure and the one furthest from the cluster's own definition problem. It belongs anyway, because it is the only one that already has both a human corpus and a synthetic one over the same task.

The absolute individual score is $$\mathrm{AIS} = 100 - \sum_i \lvert \mathrm{Rank}_{\text{individual}}(i) - \mathrm{Rank}_{\text{expert}}(i) \rvert$$, and the absolute group score is the same expression with the group's ranking in place of the individual's. The exercise reads the result in survival bands: at 50 and above the group survives, between 40 and 49 a member might get frostbite, from 30 to 39 at most three members survive, and at 30 and below the group is in serious danger.

It is a sum of absolute differences and not a rank correlation, which is deliberate. A single item moved far is penalised much more heavily under this score than under a correlation, and that is the intended behaviour when the items are survival goods and one of them is the lighter. It also carries no positional weighting: two adjacent items swapped at the bottom of the list cost the same two points as a swap at the top. Random performance was fitted as a Gaussian with mean $$15.34$$ and standard deviation $$12.71$$, $$R^2 = 0.95$$, and that is the baseline any group score is read against.

_**Fix the item count before quoting any of those numbers.**_ The version above uses twelve items. The paradigm also circulates in a fifteen-item form, and the paper describes it that way, so neither number is a mistake. The consequence is arithmetic and it is not optional. The largest the sum of absolute rank differences can be is $$\lfloor n^2/2 \rfloor$$: 72 at twelve items and 112 at fifteen. So the floor of the scale is 28 in one version and $$-12$$ in the other, and the survival bands sit at different points on the two scales. A score quoted from one version cannot be read against the other without saying which.

## What the talk has to beat

Pooling is the ranking obtained by averaging the members' independent rankings, with no conversation at all. It is the statistical benefit of several noisy estimates of one quantity, and it is free. The group ranking after discussion is a different number, and the interesting quantity is the difference between the two rather than either one on its own. The test is blunt: could the improvement have been obtained by a clerk with the four sheets of paper and no room? If yes, the talk did nothing that averaging would not have done. That is why the animation carries three error figures side by side instead of two.

## The conversation algorithm

The agent groups run under **free-form conversation**, in which no speaking order is imposed and the next speaker is self-selected. Each listening agent monitors the history and decides for itself whether to claim the floor or stay silent. Round-robin prompting is what most multi-agent setups do, and it fixes turn order in advance. Turn allocation cannot be predetermined in human conversation, so a fixed order throws away the thing being measured. Can the same agent speak twice in a row? Under free-form it can, because the speaker keeps the floor until someone claims it.

Two things are worth separating. The **floor** is possession of the right to speak, held by whoever is speaking and released voluntarily or taken by a claim. The **turn** is what a speaker produces while holding it, and one holding of the floor can span several utterances.

Each agent performs two reasoning sub-actions after every utterance it observes. The floor action decides whether to speak. The **ranking update** reconsiders the propositions made so far, integrates them, and rewrites the agent's own ranking of the items, and it runs after every observed utterance including the ones the agent does not respond to. So an agent can be persuaded without ever saying so, and a group ranking is recoverable at any point in the conversation rather than only at the end. That is why the animation can show the talk and the ranking side by side.

If more than one agent claims the floor, one is chosen at random. If no agent recognises an obligation to speak and no consensus has been reached, the conversation ceases and the group task ends in failure.

## What the two corpora are measured on

The human corpus is the Group Affect and Performance corpus: twenty-eight groups, eighty-four participants, six groups of two, sixteen of three, six of four, with speaker demographics, utterance-level transcription, timestamps, sentiment and decision annotation. The synthetic corpus is the agent groups over the same task at the same three group sizes, with the same labels applied.

* **Group action annotation.** Four labels per utterance: proposal, agreement, disagreement, confirmation. One utterance may carry more than one, which is where the complex-statement result lives. Applied by hand to the human corpus and automatically to the synthetic one, with a network fine-tuned on 60% of the annotated human corpus reaching 72.4% agreement on the remaining 40%.
* **Sentiment annotation.** Two counts per conversation, positivity and negativity. Automated with a distilled transformer fine-tuned on the same 60% and reaching 81.3% agreement on the rest. Sentiment is a label on an utterance. Satisfaction is a judgement by a person about the meeting, reported afterwards on five-point scales, and the two can move in opposite directions.
* **Airtime proportion.** Words uttered by one speaker over the total word count. Not turn count, which counts occasions rather than volume: a member who interjects often and briefly has many turns and little airtime. The distributions separate most at group size four, where more than 40% of agents occupied between 20% and 30% of the airtime against 33% of humans.
* **Meeting length**, in words rather than minutes. Elapsed time is not comparable across the two populations, since the agents are not embedded in the world and produce text as fast as the hardware allows. Back channels, coughs, nods and unclear fragments, are removed from the human transcripts so the two counts mean the same thing. Agent meetings are shorter by a wide margin, $$F(1,147) = 355.7$$, $$p < 0.0001$$, and human meeting length grows with group size while agent meeting length does not.

What is being measured across all four is human-likeness at the level of the group, not response quality at the level of an utterance. The test for whether a metric belongs in this set is whether it could be computed on a single agent talking to itself. If it could, it does not belong.

## The claims on this page, against what the paper reports

The sentence at the top is the one that would go in a talk. The numbers support its parts at different strengths, and the differences are worth carrying.

<table><thead><tr><th width="230">Claim above</th><th>What the paper reports</th></tr></thead><tbody><tr><td><strong>Outperformed the human groups</strong></td><td>One-way ANOVA on human against agent across three group sizes, $$F(1,147) = 5.121$$, $$p \lt 0.05$$</td></tr><tr><td><strong>Gained more from discussion</strong></td><td>Improvement higher than humans at group size two and group size four, both at $$p \lt 0.1$$. Group size three is not among them</td></tr><tr><td><strong>More disagreements</strong></td><td>Agents express disagreement significantly more often than humans, and make proposals more often, especially combined with agreement, disagreement or confirmation</td></tr><tr><td><strong>More complex statements</strong></td><td>Reported qualitatively, as statements that combine agreement and disagreement in one utterance. There is no separate complexity metric in the measure set</td></tr><tr><td><strong>Preference for positive statements</strong></td><td>Positivity is higher and not separated: $$M=15.218$$, $$SD=7.322$$ for agents against $$M=13.785$$, $$SD=11.767$$ for humans. Negativity is separated and lower: $$M=3.075$$, $$SD=2.046$$ against $$M=5.285$$, $$SD=6.759$$, $$F(1,147) = 9.29$$, $$p \lt 0.01$$</td></tr></tbody></table>

_**The preference for positive statements is a shortage of negatives.**_ The table separates only the negative count. Both populations produce more positive utterances than negative ones, and the agents are not distinguished by producing more positives. They are distinguished by producing fewer negatives.

The distinction matters for the mixed-team question this page ends on. An agent that says more nice things and an agent that withholds criticism behave the same way in a friendly room and differently in a hostile one. If the second reading is right, then the willingness to disagree that I am counting as an advantage is already sitting next to a reluctance to say anything negative, in the same corpus, from the same agents. The safe sentence is the abstract's: more disagreements, complex statements, and a propensity for positive statements.

Peer evaluation points the same way. Agents score lower than people on time management and on efficiency, and higher on time expectation, worked well together, and quality of work, all at $$p < 0.001$$ except worked well together at $$p < 0.05$$.

## What is still open

The missing condition is a mixed group, and neither study has run one. My own page asks whether an agent's willingness to disagree survives contact with a human who outranks it. The paper's limitation arrives at the same place from the other side: the human groups consist of different people with different background knowledge, biases and preferences, while the agent groups can be less diverse.

The efficiency half of the index question is untouched. Nothing in either corpus identifies which exchanges did the work, only that the ranking improved after them.

Two further openings, both cheap. The free-form algorithm terminates a conversation in failure when no agent recognises an obligation to speak, which is an exit condition chosen rather than derived, and the cluster's [control-layer problem](../next.md) is exactly about exit conditions. And the synthetic corpus was annotated by a network fitted to the human corpus, which means the agent conversations are described in the vocabulary of human conversations by construction. Anything the agents do that the human labels have no word for is invisible to this measure set.

[**Download the full lexicon (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/project-lexicons/mwm_small_groups.pdf)

## Publications

<table><thead><tr><th width="100"></th><th width="400">Paper</th><th>Authors</th><th></th></tr></thead><tbody><tr><td><img src="../../../../.gitbook/assets/badge-cogsci.png" alt="CogSci" data-size="original"></td><td><mark style="color:green;">Large language models for collective problem-solving: insights into group consensus decision-making</mark><br>Proceedings of the Annual Meeting of the Cognitive Science Society, 46</td><td><strong>Y. Du</strong>, <a href="https://ise.washington.edu/facultyfinder/prashanth-rajivan">P. Rajivan</a>, <a href="https://www.cmu.edu/dietrich/sds/ddmlab/cotyweb/">C. Gonzalez</a></td><td></td></tr></tbody></table>

## Collaborators

<table><thead><tr><th width="150"></th><th width="150"></th></tr></thead><tbody><tr><td><img src="../../../../.gitbook/assets/collab-prashanth-rajivan.png" alt="Prashanth Rajivan" width="48"><br><a href="https://ise.washington.edu/facultyfinder/prashanth-rajivan"><strong>Prashanth Rajivan</strong></a><br>University of Washington</td><td><img src="../../../../.gitbook/assets/collab-cleotilde-gonzalez.png" alt="Cleotilde Gonzalez" width="48"><br><a href="https://www.cmu.edu/dietrich/sds/ddmlab/cotyweb/"><strong>Cleotilde Gonzalez</strong></a><br>Carnegie Mellon University</td></tr></tbody></table>

_Last updated: 2026-08_
