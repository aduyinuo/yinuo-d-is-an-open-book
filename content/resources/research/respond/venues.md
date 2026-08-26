---
icon: building-columns
---

# Venues

## What the security chairs ask for

The instruction is unusually consistent across the top security venues, and it is narrower than what journal advice suggests.

The IEEE Symposium on Security and Privacy tells authors to focus exclusively on factual errors in the reviews and on concrete questions the reviewers asked, and adds that new results may be discussed when they clarify an open question. USENIX Security uses close to the same wording across several years: focus on questions posed by reviewers and on significant factual corrections. ACSAC phrases it as primarily addressing specific questions or concerns, and as clarifying misunderstandings or correcting misconceptions.

**A general defense of the work is off-brief.** Restating the contribution, arguing that the problem matters, or explaining why the design is novel is not merely wasteful. It sits outside what the venue asked for. At the IEEE Symposium on Security and Privacy the instructions carry a stated consequence: failure to follow them, for example by going over the word count, is listed as grounds for immediate rejection. The ICLR data agrees from the other direction, since weak novelty justification is a validated negative.

**Scope is limited; depth is not.** The instruction is easy to over-read. What the venues restrict is which comments a response addresses and how many words it spends. Nothing in any of them says the answers must be shallow. A factual correction that reaches the root of a problem is still a factual correction, and it is worth more than one that fixes the symptom. Where an objection is fundamental, an answer pitched at the surface is the failure mode the ICLR analysis calls inadequate explanation, which carries the largest negative odds ratio in the validated set at 0.31.

**A factual correction is the highest-value move available.** It is the one thing every security venue explicitly invites. A reviewer who has misread a number or a table is asking, without meaning to, for the cheapest possible score movement.

**Questions are obligations.** A question a reviewer wrote and the response did not answer is the clearest form of the failure the ICLR study calls superficial concern addressal.

## Word limits and the shape they force

The IEEE Symposium on Security and Privacy and ACSAC both cap the non-interactive response at 750 words. That is roughly one and a half pages of prose, or eight short paragraphs. With three reviews and twenty or more comments, per-comment answers are not affordable.

The forced structure is thematic. Group the comments that share a root, answer the group once, and let the presentation items collapse into a single closing paragraph. Reviewers can still find their point as long as the grouping is named in their own vocabulary.

The IEEE Symposium on Security and Privacy also runs an interactive variant for some papers, where authors and reviewers exchange messages and not every reviewer participates. ACSAC does not, so the single submission has to carry everything.

## The revision path changes what a promise is worth

This is where security venues diverge most from machine learning venues, and it is the reason the ICLR finding on vague promises needs local adjustment.

ACSAC offers three outcomes: Accepted, Minor Revision, Rejected. Minor Revision is a conditional acceptance with an assigned program committee shepherd who guides the revision and leads the discussion of the revised paper. The call places formal experiments there rather than in the response, and asks that they be feasible within a limited time frame.

A promise made in the response therefore has somewhere to land. The committee is not being asked to take it on faith. They are being asked whether the work is shepherdable. That reframes the drafting question from _can we prove this now_ to _is this specific enough that a shepherd could check it inside the revision window_.

The corollary is that an unspecific promise is worse here than elsewhere, because the reader is actively evaluating whether the promised revision is bounded. Promises are also enforceable: a program committee can reject a camera ready that fails to deliver what the response promised.

USENIX Security runs a different model again, with major revision cycles across submission rounds, and the IEEE Symposium on Security and Privacy with monthly deadlines and revise-and-resubmit. In all three the same principle holds. Find out what the venue's revision machinery is, and write promises the machinery can accept.

Whether new results may appear at all is venue law rather than custom, and the rules differ. The IEEE Symposium on Security and Privacy forbids new research results and additional material outright in its non-interactive rebuttal, while permitting them in the interactive one. ACSAC is silent, and security custom fills the silence: a small new number that answers a reviewer's question is normal, and a new topic is not.

## Where machine learning venues differ

Machine learning venues run a longer, noisier, more interactive process, and the advice that circulates in that community reflects it.

**Length.** NeurIPS, ICML, and ICLR allow far more than 750 words, and ICLR allows a threaded discussion rather than a single submission. Responses there routinely include new tables. A security response has to pick.

**Interaction.** At ICLR the exchange continues, and the empirical finding is stark. Reviews with at least one author reply rose 27.0 percent of the time against 2.7 percent for reviews with none. Where a venue permits a second turn, taking it is most of the value.

**New experiments.** The expectation at machine learning venues is that a rebuttal can contain results run during the window. That expectation leaks into how reviewers there read a promise: if you could have run it and did not, the promise reads as an admission. Security reviewers, whose venues have explicit revision machinery, read promises more generously, but only when they are specific.

## The request you cannot satisfy in the window

This is the case worth having a rehearsed answer for, because it arrives in almost every review.

What the evidence says not to do: promise vaguely, treat the request as unreasonable, or answer a different question. Vague promises about future work and superficial treatment of a concern are both validated negatives.

What works, in descending order of strength:

1. **Run it.** Baseline completion carries the largest positive odds ratio in the ICLR feature set, 1.64. If the experiment fits in the window at all, it beats every rhetorical alternative.
2. **Show that the question is already answered by something in the paper.** A missing baseline is sometimes a baseline the reviewer did not recognize. Naming the equivalence, for instance that an ablation configuration _is_ the standard baseline being asked for, completes the baseline without running anything.
3. **Give a partial result or a bound.** An upper bound computed from numbers already in the paper is weaker than a measurement and much stronger than a promise, and it can be checked on the spot.
4. **Commit specifically.** Name the configuration, the table it will appear in, and the window it will appear by.
5. **Narrow the claim instead.** If the evidence supports something smaller than what the paper claims, saying so and rewriting the claim removes the objection permanently. This is unpopular and undervalued. It converts a dispute about evidence into a promise about wording, which is cheap to keep.

## What security reviewers read as evasion

Drawn from venue instructions and from the failure modes in the ICLR analysis:

* Answering a methodological objection with a presentation fix. If a reviewer questions whether a comparison is fair, promising to rewrite the sentence that describes it does not answer the question.
* Pointing at a section number instead of stating the content. The reviewer has already read the section. That is how they formed the objection.
* Treating a threat-model gap as out of scope without saying what the scope is and why the boundary sits there.
* Claiming an artifact settles a question the response does not answer. If the artifact is anonymized and linked, a reviewer or an artifact evaluator can read it, so a claim about the implementation should match the code.
* Silence on a reviewer's question, however minor.

## Sources

* ACSAC calls for papers, for the response instructions and the Minor Revision language.
* IEEE Symposium on Security and Privacy calls for papers, 2025 through 2027.
* [USENIX Security](https://www.usenix.org/conference/usenixsecurity26/call-for-papers) submission policies and instructions, 2022 to 2024, and the messages from the program co-chairs for 2022 and 2024.
* [_Rebuttals Move Peer-Review Scores, but Initial-Review Structure Bounds the Movement_](https://arxiv.org/abs/2606.22166), arXiv 2606.22166, 2026, for the failure modes.
* [_Insights from the ICLR Peer Review and Rebuttal Process_](https://arxiv.org/abs/2511.15462), Farhat et al., arXiv 2511.15462, 2025.

_Last updated: 2026-08_
