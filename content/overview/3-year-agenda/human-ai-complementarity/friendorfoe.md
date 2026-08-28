---
hidden: true
icon: users-viewfinder
---

# FriendOrFoe

The experiment [CHART](chart.md) was built for, and the first to run on it.

## The question

Whether role dependencies raise complementarity in a human-AI defense team facing zero-day attacks, and which of the leader, pool and informational dependencies carry the effect.

The design is fixed and the platform exists. Data collection is what remains.

## Why an aggregate score will not answer it

The reason a pair can beat either member alone is that each holds knowledge it cannot fully externalize: the analyst's trained sense that something is off, the model's latent state. A clean interface cannot be built across knowledge that cannot be handed over, and joint performance does not distinguish genuine complementarity from one party simply deferring to the other.

The field's working definition makes the difficulty visible without resolving it. Complementary team performance obtains when the team's loss falls strictly below both the human's and the AI's alone — a benchmark rarely reached, because the region where exactly one member is correct tends to be small. A team can therefore fail to show complementarity because the structure was wrong, or because there was none available to find. An aggregate score does not separate the two.

## What the seam carries changes the team

Where the literature has made this concrete, it has done so by fixing the combination rule and measuring it — hybridizing human and AI judgements according to which is more reliable on a given instance. That work carries a warning this experiment is built to test: displaying the AI's explanation, confidence and label induced over-reliance, whereas showing only the evidence left trust better calibrated.

What is handed across the seam changes the team, in a direction that is not obvious in advance.

## The three dependencies, as this study defines them

Three of CHART's five types are manipulated and two are left out. Synchrony and temporal are not in this design, because the task has one judgement per episode and nothing to order or to time.

_**Leader.**_ The requirement that one designated teammate's decision is the team's decision. The human holds it, and the AI teammate's judgement is available as input rather than as a vote. The alternative in the same manipulation is pool. Under leader the human's answer is the answer. Under pool the human's answer is one of two inputs to a rule that produces the answer. The difference is not how much the human is told. It is whether the human can be outvoted by the aggregation. The predicted direction is conditional rather than flat: leader helps if the human is the more accurate of the two, pooling helps if the model is.

_**Pool.**_ The rule that combines the human's and the model's separate scenario judgements into one team judgement. Each agent supplies a signed confidence, a single number carrying both which answer was given and how sure the agent was. The two are weighted by fitted reliability terms plus an intercept, and the sum goes through a logistic to give the probability that the scenario was an ongoing attack. The weights are fitted on a calibration set with known ground truth, which is what converts a stated certainty into an amount of influence.

_**Informational.**_ What the model teammate's summary contains, varied between an intuitive account of the pattern over time and a technical account naming the attack stages and the diagnostic signals. Both conditions see the same table of events. What differs is the description laid over it. The predicted direction is unusual and worth keeping in view: the expectation is that the human sees less than the two models do, and that seeing less raises complementarity by lowering the reading burden. That prediction runs against the transparency assumption most of the literature uses, and it is why the informational arm is in the design at all.

## What gets measured

_**The complementarity metric.**_ The team's accuracy divided by the accuracy of the better of its two members, computed within a team over its five episodes of scenario judgement. The strict definition is a yes or no on two inequalities; this ratio is continuous, so it can rank conditions that all fail the strict test, which is what makes it usable when complementary team performance is rarely reached. Read what is in the denominator. If it is the better member rather than the average of the two, a value of 1 means the team did no better than its best member.

_**Team alignment.**_ The proportion of decisions on which teammates gave the same answer, recorded twice: agreement of all three on event classifications, and agreement of the human and the model on scenario judgements. Not team accuracy, which compares answers to ground truth rather than to each other. Three teammates can align perfectly and all be wrong. Compute it without the answer key; if you cannot, you are computing accuracy. Alignment is the closest available reading of whether the structure did anything to the process rather than to the score.

_**Cognitive load and expertise.**_ Load is self-reported on a standard workload instrument at the end of the session, and it is predicted to be highest in the condition with no dependencies, because a teammate doing the event classifications removes twenty decisions from the human. Expertise is measured after the task and used as a covariate rather than as a screen, so it can carry an interaction: the expectation is that the more expert the participant, the more they benefit from holding the final decision and from the technical summary.

## The team is three, and the task is two decisions

A low-level model classifies single events, a high-level model summarizes and judges the sequence, and the human judges. The argument for that shape is a division of failure modes. The classifier does not invent. The language model matches patterns across sparse and disparate evidence. The human supplies the reasoning that ties a sequence of events together. Placing the language model inside a human-in-the-loop structure is what makes its opacity tolerable.

**Event classification** is the per-row decision, malicious or benign, over the sequential network events in one scenario's table. **Scenario judgement** is the single binary call at the end of an episode: whether the sequence was an ongoing attack. The two can disagree in both directions and the design keeps them as separate dependent variables throughout. Only the second is what the complementarity metric is computed on, which means the machine-learning teammate is outside the metric even though it is inside the team.

**False alarms** are in the material before anyone sees it. Each table carries a third label alongside malicious and benign, because operational detectors run false alarm rates high enough to dominate the stream, and that is the condition the task is measuring load against.

## Where the words disagree

_**Leader here, control on the platform.**_ The pre-registration lists three role dependencies CHART offers and names the first Leader, with the definition that an agent's execution depends on authorization from another agent. That is word for word the platform's definition of Control, and the earlier implementation design named the same condition Control with exactly the gloss the later document gives Leader. The new name came in with the decision-centralization literature the design is drawn from, where the contrast is between aggregated responses and a leader deciding. So the word arrived with the manipulation, not with the platform. A results section that uses both interchangeably will be read as describing two conditions.

_**Informational names a filter and a resolution.**_ On the platform, informational dependencies govern access, with redaction level and time gating and clearance as the parameters. Here the manipulation is low against high resolution summarization over the identical table. Both are honestly informational. Reporting this one as restricting information invites the reading that the human was denied data. The human was not.

_**Pool as an aggregation rule, or as a quorum trigger.**_ On the platform, nothing fires until contributions reach a threshold. Here nothing is triggered: two judgements arrive and a fixed rule reads them, and the rule still produces an answer when only one contributor acts.

Those three are one problem seen three times. This study borrowed three dependency names from [CHART](chart.md) and gave two of them different mechanisms and the third a different name. The fix is not to renormalize the study to the platform, because the study's mechanisms are the ones the data will be collected under. The fix is to say, once, in the methods, which sense is in force.

The vocabulary, tier by tier, with what each term is not and how to tell: [**download the FriendOrFoe lexicon (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/project-lexicons/hac_friendorfoe.pdf)

## Support

Supported by the UTEP University Research Institute award, with Grace Roessling, Cleotilde Gonzalez, Tyler Malloy, Baptiste Prébot and Volodymyr Miloserdov.

_Last updated: 2026-08_
