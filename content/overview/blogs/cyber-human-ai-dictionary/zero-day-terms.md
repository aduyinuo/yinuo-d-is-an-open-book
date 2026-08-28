---
description: Five things the word names, and what the shot count is actually counting.
icon: almost-equal-to
---

# Zero-Day Terms

The question is mine, from [Headspace](../../../home/what-is-she-thinking.md), and it sat there for months looking like a riddle.

> What is zero-day? Is the defense against zero-days a zero-shot or few-shot challenge?

The short answer is that the second question cannot be asked until the first one is settled, because the word names five different things across my own files and the shot count comes out differently for each. The shot count is a property of the label space, not of the attack. Once you say whose label space, the question answers itself, and it answers itself differently every time.

## Five senses

_**Unknown to whoever could fix it.**_ The NIST glossary sense: an attack that exploits a previously unknown hardware, firmware or software vulnerability. The unknown party is the vendor, the maintainer, or the deploying organization, and the moment is before a patch exists. Its nearest neighbor is the n-day, which is public, has a CVE identifier and a patch, and is unpatched here anyway. Disclosure together with a patch is what converts one into the other.

_**A counting unit.**_ The k-zero-day safety metric counts the smallest number of distinct unknown vulnerabilities an attacker would need to reach an asset, and a larger count means a safer network. The identity of each flaw is deliberately left out of the model, because the point is to measure risk from flaws nobody can enumerate. Here a zero day is not an event and not a class. It is a unit of distance.

_**Absent from the training set.**_ The intrusion-detection sense: attack traffic not used in training the learning model. The unknown party is the fitted model and the moment is fit time, so age in the world is irrelevant. An attack disclosed a decade ago is a zero day to a model whose training set omitted it.

_**Outside the enumerated catalog.**_ My own paper's usage. Four CVE-class vulnerabilities are named in a table, the exploit paths for those four are real code, and everything else is out of scope by declaration. The word marks the boundary of an enumeration the testbed actually implements, and the exclusion is what makes the threat model finite.

_**New to the person being studied.**_ The [FriendOrFoe](../../3-year-agenda/human-ai-complementarity/friendorfoe.md) usage. The defender in the study has not seen this scenario before and the design turns on that. The attacks themselves can be historical, published and patched, and in some cases famous, without costing the design anything.

## Zero-shot or few-shot

Both terms presuppose a fixed label space in which the new thing is a class. Zero-shot needs no labeled examples of the unseen class, but it does need an attribute description of that class, expressed in a vocabulary shared with the seen classes. Few-shot needs a handful of labeled examples and no attribute channel. That is the whole distinction, and it is a distinction about what is supplied rather than about how hard the problem feels.

Now run the question through the five senses.

_**The vendor sense gives neither.**_ At the moment of the attack there is no example and no attribute vector, because the class is not in the label space at all. That is open-set detection: the decision is whether this belongs to any known class, not which unseen class it is. Calling it zero-shot imports an attribute channel that the sense says does not exist, without saying where it came from.

_**The training-set sense gives zero-shot, but only because someone built the attribute channel by hand.**_ Where this has been made to work, it works in two stages, mapping network features to semantic attributes learned from the known classes and then relating the unseen class to the known ones through those attributes. The honest statement of the limit is in the same results: it fails for the attacks whose feature distribution is furthest from the training classes. The method works where the new class was almost in the old vocabulary.

_**The enumeration sense gives no shots at all.**_ It is a scoping sentence in a threat model. Nothing is being learned in it.

_**The participant sense gives few-shot at most, and probably not even that.**_ A human analyst has years of examples of file encryption and of internal port scanning. The scenario is new. The constituent behaviors are not. What the study manipulates is familiarity with an assembled scenario, which is an experimental condition rather than a learning regime.

So the framing is right only after the word is disambiguated, and the version of the question worth carrying forward is this. Whose label space, and what plays the role of the attribute channel?

For FOE-Dreamer the second half already has an answer. The attribute channel is the factored representation, and the claim the factoring makes is that attacker-driven variation is separable enough to transfer while the rest of the state is not. That is a testable claim about an attribute channel, and it is a better question than counting shots. The success criterion I already fixed for that project is stated in the same shape: the detector fires before the attacker reaches the region the model is wrong about, at a false-alarm rate an operator will accept. That is an open-set criterion. It does not ask which unseen class arrived, and it does not need to.

## Where the senses disagree

_**My own paper and my own experiment use the word in opposite directions.**_ The paper excludes zero-days to bound what the testbed has to implement, so the four CVE-class vulnerabilities are the enumeration and the exclusion is what makes the threat model finite. The FriendOrFoe study includes zero-days as its central manipulation, and its zero-days are historical. One usage points outside a named list and the other points inside one. A reader holding both papers has no way to recover a single meaning.

_**A scenario set can be entirely patched and still be exactly right.**_ A human-subjects design needs unfamiliarity to the participant and nothing else, so published and remediated attacks do the job perfectly. Under the vendor sense not one of them qualifies. This is not a defect of the design. It is a defect of the label, and it will misfire the moment a security reader sees the file name.

_**The training-set sense makes the word depend on the reader's calendar.**_ The same traffic is a zero day for one detector and routine for another trained a month later, and nothing about the attack changed. This is why a reported zero-day detection rate without its held-out class list says nothing at all.

_**Countable and uncountable at the same time.**_ The k-zero-day metric requires zero days to be countable and interchangeable, since k of them, any k, is the whole content of the measurement. Every other sense treats a zero day as an event with an identity, something that happened on a date to a specific piece of software. A sentence reporting how many zero-days a defender survived is counting under a sense that does not license counting.

## The entry

_**Definition.**_ An attack whose enabling flaw was unknown, at the moment it was used, to the party who would otherwise have prevented it. Which party, and which moment, is not fixed by the word and has to be supplied.

_**Distinguishes it from.**_ The n-day, which is public, carries a CVE identifier and a patch, and is unpatched on this network anyway. Most of what is called a zero day in an experimental setting is an n-day that the person or the model in front of it has not met.

_**Operational test.**_ Name the party the attack is unknown to and the moment at which it is unknown. The vendor, at disclosure. The model's training set, at fit time. The participant, at the start of the session. If the sentence still reads correctly after you substitute a different party, it was not carrying a definition.

Then a second test, for whether the shot vocabulary applies at all. Ask what attribute description of the new class the method receives. If none, the problem is open-set detection and no shot count applies. If some, the problem is zero-shot and the attribute channel is the thing to argue about. If labeled examples arrive, it is few-shot and the count of examples is the parameter.

[**Download the full entry (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/cross-domain-dictionary/dict_zero_day.pdf)

_Last updated: 2026-08_
