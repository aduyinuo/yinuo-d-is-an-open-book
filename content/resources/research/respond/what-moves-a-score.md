---
icon: chart-line
---

# What Moves a Score

## Most reviewers do not move

Across ICLR 2024 and 2025, roughly 75 to 81 percent of scores stayed where they were after the author response, 17 to 23 percent went up, and about 1 percent went down.

**Sources:** [_Insights from the ICLR Peer Review and Rebuttal Process_](https://arxiv.org/abs/2511.15462), Farhat et al., arXiv 2511.15462, 2025; [_Rebuttals Move Peer-Review Scores, but Initial-Review Structure Bounds the Movement_](https://arxiv.org/abs/2606.22166), arXiv 2606.22166, 2026.

The asymmetry is what settles the decision. The downside is the 1 percent that falls, so writing a response is close to free in expected value. The question is never whether to write one, only where its words go.

## Engagement is the largest single lever

Reviews that received no author reply rose 2.7 percent of the time. Reviews that received at least one reply rose 27.0 percent of the time. Within exchanges where authors engaged substantively the rate reached 45.6 percent, but selection inflates that figure, since authors engage more when they think they can win. The honest number to plan against is the 21 percent overall increase rate against a 1.4 percent decrease rate.

## Movement converts into acceptance

Papers whose scores rose after the response were accepted 55.7 to 57.6 percent of the time. Papers whose scores did not move were accepted 7.8 to 12.4 percent of the time. For a borderline paper the response is not decoration, and it is worth the days it takes.

## The ceiling is set before you write

Initial score position dominates every feature of the exchange, at an odds ratio of 0.141 per standard deviation. A response cannot rescue a paper the panel has already placed far from the line. It can move one that sits near it.

The practical reading is not fatalistic. It says to spend the words where the distance to the line is small, and to treat a determined outlier in either direction as fixed. It also says that one weak reject alongside two positives is exactly the configuration where a response pays, since the weak reject has the most room and the panel has the most reason to look.

On why initial position dominates, see [_Testing for Reviewer Anchoring in Peer Review: A Randomized Controlled Trial_](https://arxiv.org/abs/2307.05443), arXiv 2307.05443.

## The predictive features are mostly absences

One finding should shape how a response is drafted. The features that predict movement are mostly the _absence_ of failure rather than the presence of brilliance. What a model detects in a successful exchange is that the authors did not make the usual mistakes. Write to avoid the known failure modes first, and only then to persuade.

From the cross-validated feature set that survived Bonferroni correction:

<table><thead><tr><th width="230">Raises the score</th><th width="80">Odds ratio</th><th>What it is</th></tr></thead><tbody>
<tr><td><strong>Baseline completion</strong></td><td>1.64</td><td>Running, or accounting for, the baseline that was asked for</td></tr>
<tr><td><strong>Non-defensive tone</strong></td><td>1.51</td><td></td></tr>
<tr><td><strong>Writing fixes</strong></td><td>1.27</td><td>Committing to specific presentation changes</td></tr>
<tr><td><strong>Theoretical grounding</strong></td><td>1.18</td><td></td></tr>
</tbody></table>

<table><thead><tr><th width="230">Lowers the score</th><th width="80">Odds ratio</th><th>What it is</th></tr></thead><tbody>
<tr><td><strong>Inadequate explanation</strong></td><td>0.31</td><td>An answer pitched at the surface of an objection that goes to validity</td></tr>
<tr><td><strong>Low-effort response</strong></td><td>0.38</td><td></td></tr>
<tr><td><strong>Defensive tone</strong></td><td></td><td></td></tr>
<tr><td><strong>Weak novelty justification</strong></td><td></td><td></td></tr>
</tbody></table>

Four further behaviors are reported as negatives without odds ratios: superficial treatment of a concern, missing baselines, vague promises about future work, and pointing at a section number instead of explaining the content.

## The promise problem

That last pair deserves care. Two of the strongest positives, baseline completion and writing fixes, are things a response can only promise when the window is short. The distinction the evidence draws is between a promise that is specific and checkable and one that is not.

> We will improve the evaluation.

is a vague promise. Something closer to

> We will run the missing ablation cell and report the complete two-by-two in Table 3.

is a commitment someone can hold you to.

## Sources

* [_Insights from the ICLR Peer Review and Rebuttal Process_](https://arxiv.org/abs/2511.15462), Farhat et al., arXiv 2511.15462, 2025.
* [_Rebuttals Move Peer-Review Scores, but Initial-Review Structure Bounds the Movement_](https://arxiv.org/abs/2606.22166), arXiv 2606.22166, 2026.
* [_Testing for Reviewer Anchoring in Peer Review: A Randomized Controlled Trial_](https://arxiv.org/abs/2307.05443), arXiv 2307.05443.
* _What makes a successful rebuttal in computer science conferences? A perspective on social interaction_, Journal of Informetrics, 2023.

_Last updated: 2026-08_
