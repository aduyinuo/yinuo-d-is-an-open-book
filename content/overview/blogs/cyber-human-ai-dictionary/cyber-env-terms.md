---
description: One word, six senses, and the four words it costs to fix it.
icon: almost-equal-to
---

# Cyber Env Terms

What is a cyber environment? The word does six separate jobs across the two places I use it most, and neither place ever says which job is meant.

So I counted them. Forty-nine occurrences carried into the census, six senses, and twenty sentences where a second pass through the same words lands somewhere the first pass did not. The twenty stay ambiguous. They are the entries worth having.

The two corpora are the eleven pages of [Cyber Environments & Benchmarks](../cyber-environments-and-benchmarks/) on this site, and the realism evaluation behind [When We Say "A Realistic Cyber Environment"](../../3-year-agenda/toward-deployment/when-we-say-a-realistic-cyber-environment.md), fifteen environments scored on eleven dimensions with a written justification in every cell.

## Six senses

_**The package.**_ A named, distributable piece of software that you clone, configure and run, with a version and a repository. It exists before anyone decides who is playing: Cyberwheel is one package and supports red-only training, blue-only training, and simultaneous training of both. The test is whether you can name its version without naming an agent. This is the dominant sense, the majority of the census and the default reading of every heading in both corpora.

_**The decision problem.**_ Everything outside the learner. Observation space, action space, reward, transition dynamics, episode boundary, which is the environment in the sense reinforcement learning means it. One package presents as many decision problems as it has agent seats and opponent configurations. The test is whether swapping the opponent, with no change to the code, gives you a different one. CybORG with the session-removing defender and CybORG with the host-restoring defender are two decision problems and one package.

_**The modeled system.**_ The estate being represented. Hosts, subnets, services, accounts, directories, logs, the traffic a workday produces. This is what the eleven realism dimensions score, and realism is a property of this sense and never of the package, because a well-engineered package can model almost nothing. The test is whether you can ask if a real technique would work in it, Kerberoasting say, and get an answer that is not about the code.

_**The substrate.**_ The provisioned infrastructure underneath. Virtual machines, KVM or Vagrant or Terraform, the range, the wire. What is there before any scenario is loaded onto it. The substrate is what the scenario runs on and the modeled system is what the scenario says, so the test is whether it would still be there if you deleted every scenario file. CALDERA has no modeled system of its own and inherits one from whatever it is deployed against.

_**The experimental role.**_ A position one environment occupies relative to another inside a particular study. Source, target, far target, reference point. This is a property of the experiment and not of the software, so the test is whether the word carries a modifier naming a position in a study rather than a property of a system. Cyber Wheel is a good source because of the pairing. CyberVAN is a reference point rather than a training environment, and only for this work.

_**The third party.**_ What is neither the attacker nor the defender. Benign users, service load, maintenance windows, background traffic, the green agent. This is the sharpest collision in the file, because under the decision-problem sense the opponent is inside the environment by definition, and here the opponent is explicitly outside it and the environment is the third term in a list of three. The test is whether removing it would leave the attacker as the only source of activity.

## Where the two passes disagree

Twenty of forty-nine, and the shapes repeat.

_**The sentence the whole tree turns on.**_ Every claim about an autonomous cyber agent is a claim about the environment it was measured in. Read as the package, it says results do not travel between repositories, which is a reproducibility claim and a mild one. Read as the decision problem, it says a result does not survive a change of opponent inside the same package, which is much stronger and is the claim the CybORG page supports two clicks later.

_**Fidelity against tractability, on one noun.**_ Closeness to a real system is a property of the modeled system. Affordability of training is a property of the decision problem. The noun in the middle of that trade is doing both jobs in one sentence, which is why the trade sounds like a law rather than a fact about current engineering.

_**A target with no defender in it.**_ GOAD is a target, not a defended target. That can mean the modeled estate carries no SIEM, no EDR and no detection, or it can mean there is nobody in there but the attacker. GOAD's cells support both. One is a missing subsystem and the other is a missing occupant, and a fix for one is not a fix for the other.

What the two passes never disagreed on is the useful part. Every occurrence that names who is on the other side of the boundary was assigned the same sense twice. From the attacker's side. Attacker, defender, environment. The attacker agent is the only source of activity. Naming the second party is what fixes the word, and it costs four words.

## Three communities, three defaults

The reason this word is worth a page is that the same string arrives from three directions, each with its own idea of what would make an environment more realistic, and the three answers do not overlap at all.

Reinforcement learning defaults to the decision problem. Realism means the decision problem is hard in the right way: partial observability, non-stationarity, delayed credit. The blunt phrase for a package that fails this is that it is an adversary emulation tool and not an RL environment, and the failing property is a complete report rather than a poor estate.

Security operations defaults to the modeled system, with the substrate close behind. Realism means a real technique would work, and the eleven dimensions are the operational form of that. Nothing in that list is about an interface.

Human factors defaults to the task setting a person is put in. HackIT exists to put real people in front of a network and watch what they do when some of it is fake, and what it buys is an attacker who is actually surprised. Its constraint is stated as a warning rather than as a missing capability: the loop runs at human speed.

So the diagnostic is one question. Ask what would make this environment more realistic. The RL answer adds noise and a moving opponent. The operations answer adds Active Directory, event forwarding, and people doing their jobs. The human factors answer adds task pressure and a cover story the participant believes. A conversation in which all three answers are called realism will not converge, and none of the three is wrong.

## Two more words that swap places

Fidelity and realism are the same distinction with reversed labels in my two corpora. The blog says fidelity for the aggregate and never says realism. The evaluation says fidelity only of one named layer, service, OS, telemetry, and reserves realism for the whole. Anyone reading the two together will take CyberVAN aiming at the highest fidelity short of the real thing as a claim about eleven dimensions at once, and it is not one.

Scenario carries two senses of its own. On the blog a scenario is a configuration of one package, thirteen hosts and three subnets and a reward table. In the evaluation a scenario is an attack script, a sequence of adversary behavior with phishing in it.

## What to say instead

Six senses, six phrases, none longer than the word it replaces. Name the package and the version. Name the seat and the opponent, and say so when the opponent changes, because the decision problem changed. Say the estate, or say the network, and score it on eleven dimensions rather than on one word. Say the substrate, or say the infrastructure. Say source and target, and say which study. Say benign activity, or say green agents, and never let that one ride on the bare noun, because it is the sense the bare noun destroys most completely.

[**Download the full entry (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/cross-domain-dictionary/dict_cyber_env.pdf)

_Last updated: 2026-08_
