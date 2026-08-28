# When We Say "A Realistic Cyber Environment"

Environments get described by the features they implement, or by a broad claim of being realistic. Neither tells you whether the environment supports the claim you want to make with it.

<figure><img src="../../../.gitbook/assets/metrion-method.gif" alt="The Metrion methodology: derive requirements from ATT&#x26;CK and D3FEND, cluster into dimensions, score them, validate with practitioners"><figcaption><p>Metrion, built from the question rather than from a feature list.</p></figcaption></figure>

## The failure it fixes

Picture a defender benchmark where attacks raise alerts but ordinary enterprise life is thin — few normal logins, little admin maintenance, hardly any background traffic. A defender scores well there because malicious behaviour is being read against a clean baseline. The result is valid for that benchmark and says nothing about an enterprise full of noisy legitimate activity.

The offensive side has the mirror image. In NASimEmu an action can succeed deterministically in the simulator and fail against the corresponding real service in the emulator, because the simulator abstracted away the service and operating-system fidelity that decides whether an exploit lands. PenGym reports the same gap.

So the score reflects the agent's capability _and_ which conditions the environment modelled or omitted, with no way to separate the two.

## The method

**Derive.** Start from a use case, decomposed on both sides — attacker goal, technique, procedure; defender posture, detection priority, countermeasure. Walk MITRE ATT\&CK and D3FEND, recording what each technique requires the environment to provide, model, or emit.

**Cluster.** Those per-technique requirements converge into eleven realism dimensions, in five groups: infrastructure (topological, operating system, service), organizational behaviour (identity, temporal, benign activity), security layer (defensive, telemetry), agent interface (action, observation), and external context (external ecosystem). Each is operationalised through concrete scoring elements — 115 of them — set at the level where a missing property makes a class of techniques inexpressible or unobservable.

**Score.** For a given objective, each element is critical, useful, or not needed. Coverage of each is full, partial, absent, or unknown. Critical weighs 2 and useful 1; full counts 1, partial 0.5, absent 0. The weighted average is a fit score from 0 to 1.

One rule overrides it: **if any critical requirement is absent, the environment is not suitable for that objective** — a single missing critical property can invalidate the evaluation. Otherwise, suitable above a working threshold of 0.75, partially suitable below, and incomplete when too much is unknown.

**Validate.** ATT\&CK and D3FEND are themselves curated abstractions, so the dimension set needs outside checking: interviews with academic, SecOps and pentesting practitioners, then a broader survey, asking what to add, remove, split or merge and whether people agree on what matters.

## What it shows

Applied to GOAD, an emulated multi-domain Active Directory environment: **suitable** for credential-based privilege escalation at a fit of 0.88, and **not suitable** for targeted data exfiltration at 0.39 with five critical requirements unmet — the same environment, unchanged.

Suitability is a property of the _pair_, not of the environment.

Across thirteen publicly inspectable enterprise environments two families appear. Real-software emulators reproduce service, operating-system and action-level realism. Abstract simulators reproduce topology and the agent interface but abstract away temporal dynamics, defensive controls, benign activity and telemetry. Those context dimensions are the least represented anywhere — which means the objectives that depend on them, including targeted exfiltration, evasive operations and threat hunting, are currently supported by no environment at all.

[Interactive scorecard](https://stratosphereips.github.io/realism-framework/)

_Metrion is a poster at ACM CCS 2026, with Maria Rigaki and Carlos A. Catania. The current comparison uses dimension-level proxy grades rather than element-level scoring, and is not yet validated._

## The second layer

Three things the eleven dimensions do not capture, and none of them is a twelfth dimension. They sit above the catalog as a separate layer, and the distinction is the methodological point most likely to be lost when this work is summarized by somebody else.

_**Environment realism against scenario validity.**_ Environment realism is what the environment can represent, and it is the eleven dimensions. Scenario validity is whether a given scenario uses those capabilities in a way that makes the claim meaningful. An evaluation is defensible only when both hold. An environment can be detailed and faithful and still be run with a scenario no real attacker would have: full prior knowledge of the network, no time pressure, and an objective like compromise every host. Two questions in order. Does the environment provide the capabilities the objective requires? Does the scenario connect them through persistent state, causal progression, plausible timing, consequences and coherent evidence? A no to the first is a missing dimension. A no to the second is a valid environment being misused.

_**Failure-mode realism.**_ Whether the modelled capabilities fail, degrade, interact and produce side effects the way real ones do. Do not ask only whether services exist, ask whether they crash, return partial results, expose inconsistent versions, and fail under load. Do not ask only whether an exploit action exists, ask whether it can partially succeed, corrupt state, trigger detection and leave traces that change the next step. It cuts across six dimensions, and it is a property of how each one is implemented rather than of whether it is present.

_**Campaign consistency.**_ Whether a scenario connects its techniques into one campaign. Six properties: goal continuity, so actions serve an objective rather than instantiate a checklist; state continuity, so credentials and footholds and discoveries and alerts persist and change later possibilities; causal continuity, so later actions are explainable from earlier ones and the attacker cannot use what it never obtained; temporal continuity, so phases run at plausible and different timescales; cost and risk continuity, so loud or destructive actions are not free; and trace continuity, so the evidence forms one correlatable story. The point is not to add axes, it is to require that the axes compose. Break any of the six and the agent may still solve individual tasks while campaign success stops meaning campaign success.

_**The opponent-model scale.**_ A requirement attached to a use case rather than to an environment: what kind of opposing actor exists, what each side can observe, whether either adapts, and how one side's actions change the other's options. Six levels. Level 0, no opposing actor. Level 1, static environment effects, where controls or traces exist but nobody decides anything during the run. Level 2, a scripted opponent. Level 3, a policy-driven opponent that chooses on observations without adapting its strategy. Level 4, an adaptive opponent that changes behaviour on observed actions, failures or inferred intent. Level 5, co-adaptive or human.

That scale exists because defensive realism was doing two jobs. It was conflating defender _implementation_, the sensors and controls and tooling, with defender _behavioural richness_, the blue action space and policy. While the acting agent is the attacker the conflation is invisible, because the one dimension happens to capture opposing-actor quality. Turn it around and the gap opens: when the defender is the learner, the attacker is the opposing actor and no dimension measures its richness at all. A defender environment with a scripted attacker is less realistic for defender objectives than one with an adaptive attacker, and the eleven-dimension scoring cannot see the difference. The resolution is not a twelfth dimension. It is the scale, applied symmetrically to whichever side is opposing, with each use case stating its minimum level. Worm spread wants level 1 or 2. Evasive operation wants at least 3 and often 4. Attack-defense co-evolution is level 5 by definition.

## Simulator, emulator, range, benchmark, testbed

These are the words the project used interchangeably for months, and the fix was not better definitions of each. It was noticing that they were never on one axis.

**Implementation** says what the environment is built out of. **Usage** says how it is packaged or used to evaluate. Most real environments are a pair, one from each, and asking whether something is a cyber range or an emulator is a category error because it can be both. Metrion cares about implementation, because the eleven dimensions ask what the environment can represent.

A **simulator** is a programmatic model of a network, hosts and agent actions in which services, operating-system behaviour and exploit outcomes are abstractions: typed services, probabilistic exploit success, symbolic state vectors. An **emulator** is a network of real software components running real operating systems, services and security tools, wrapped in a controlled topology and exposed through a programmatic agent interface, so agent actions become real system calls. The absence of a real operating system and service layer is the whole of the difference; being fast is a consequence rather than a criterion. Inside emulation, substrate matters again: container-based emulators cannot host kernel-level adversary behaviour, and virtual-machine-based ones close that gap.

A **cyber range** is a platform for delivering interactive environments for training, exercise, test and evaluation. What makes it one is the packaging: team formation, a scenario library, an instructor interface, scoring, repeated or persistent runs. It is orthogonal to implementation, and the authoritative definitions allow hardware without requiring it. A **benchmark** is a curated, scored collection of tasks used to compare agents against a fixed rule, and it too may run on any implementation. A **testbed** is research infrastructure used primarily to generate datasets or study phenomena rather than to score agents.

An **adversary-emulation platform** is software whose role is to execute attacker tradecraft against an arbitrary target and report results. Its realism is whatever it is deployed against; the platform is not the environment, and many published evaluations of such a platform are really evaluations of the platform plus a particular emulator or range. **Agent scaffolding**, the prompt templates and tool wrappers and memory and planning loops that turn a language model into an agent, is orthogonal to environment choice, and confusing the two is how a scaffolding result gets reported as an environment result.

## What may be compared with what

Three tiers. Tier 1 is the filter: domain, implementation, and the use-case scope the authors claim. Tier 2 is descriptive and non-realism: scale, sides modelled, operating regime, hardware integration, scenario openness, evaluation purpose, license, determinism. Tier 3 is the eleven realism dimensions.

Realism scores are methodologically valid only within a Tier 1 cell. An attacker-focused abstract simulator, a two-sided virtual-machine emulator and a single-host capture-the-flag benchmark belong to different cells, and comparisons across them are mostly artifacts of that conflation. An enterprise simulator and an industrial control testbed are so different that scoring them on identical dimensions is not unfair, it is meaningless.

A **use case** is a category of attacker or defender activity defined by what the agent is trying to accomplish and under what real-world constraints, and it is the unit against which environments are evaluated. Not a scenario, which is one instantiation with a topology and an attacker script, and not an ATT&CK tactic, which is one adversary goal rather than an operation with a success criterion and a tension. Exfiltration trades collection thoroughness against detection probability; ransomware trades speed against coverage. A use case without a tension is a task list. The use cases are derived from **group archetypes**, patterns of attacker behaviour shared across multiple named threat groups and clustered by objective and operational style rather than by attribution, so a use case cannot be dismissed as an academic construction and also cannot be defended by pointing at one actor.

One failure belongs to the scenario rather than to the environment and is worse in one respect. An **unrealistic objective** is one no real attacker or defender would hold: compromise all hosts, maximize compromised nodes, find all flags, or an undefined defend the network. An agent trained to take over everything will never learn stealth, prioritization or persistence maintenance, because none of those serve its objective.

## What kind of method this is, and what it inherits

Metrion is an analytical evaluation method: a set of heuristics plus a procedure by which expert evaluators, not users, inspect an artifact and predict whether it is fit for a purpose. Heuristic evaluation and cognitive walkthrough are its siblings. The eleven dimensions are the heuristics, the 115 elements are the scorable form, critical and useful and not needed is a severity scale, and the fit score is an aggregation rule. Who applies it, an expert or a user? An expert. That single answer places the method and imports its literature.

It also imports the known failure mode. Two trained evaluators applying the same heuristics to the same artifact disagree badly: in one study only about a fifth of problems were found by all four evaluators and nearly half by exactly one, and heuristic evaluation has been assessed as the broadest and least reliable of eight analytic methods, precisely because what counts as consistent is left to the evaluator. The full-partial-absent-unknown judgment has exactly this exposure, and it implies a third study the plan did not have: a paired-rating study of the rubric itself.

So three studies rather than one. Interviews buy realism, a survey buys generalizability, and a paired-rating study buys precision. Those three cannot be jointly maximized, and naming which each buys is the triangulation argument rather than a list of three activities. Two design decisions carry the most weight and both are about anchoring. The dimension list is the analysis frame, not stimulus material, so it should not be shown in the interviews at all: once a participant has seen it, nothing after it can serve as independent corroboration. And the participant supplies the case while the researcher does the abstraction, so a written objective is a comparison probe late in the session rather than the opening prompt.

## What the poster asks its readers

Whether the eleven dimensions and their decomposition into 115 elements are at the right granularity. Whether three levels are enough to represent what an objective requires. And whether deriving requirements from ATT&CK and D3FEND, rather than cataloguing what environments implement, is a sound basis for comparison at all.

Underneath them sits the one that cannot go on a poster. The completeness argument runs through the archetypes, and the archetypes are a curated abstraction of the groups, so if that abstraction is wrong or incomplete the use cases inherit the error and the dimension set inherits it after them. Every dimension traces back to a technique, which is the property that makes the catalog refutable. It is also the property that makes it exactly as good as the catalog it was derived from.

The immediate work is smaller than any of that. Convert the coarse grades into per-element evidence tables for one abstract simulator, one emulator, and one real-infrastructure environment, with a link behind every judgment. Then the interviews, which are the only thing that can say whether practitioners recognize any of this.

The vocabulary, tier by tier, with what each term is not and how to tell: [**download the Metrion lexicon (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/project-lexicons/td_realistic_cyber_environment.pdf)

## Publications

<table><thead><tr><th width="100"></th><th width="400">Paper</th><th>Authors</th><th></th></tr></thead><tbody><tr><td><img src="../../../.gitbook/assets/badge-ccs.png" alt="ACM CCS" data-size="original"></td><td><mark style="color:green;">Realistic Enough for What? Metrion: A Multidimensional Framework for Evaluating Cyber Environments</mark><br>Poster, ACM CCS 2026</td><td><strong>Y. Du</strong>, M. Rigaki, C. A. Catania</td><td></td></tr></tbody></table>

## Collaborators

<table><thead><tr><th width="150"></th><th width="150"></th></tr></thead><tbody><tr><td><img src="../../../.gitbook/assets/collab-maria-rigaki.png" alt="Maria Rigaki" width="48"><br><a href="https://mariarigaki.github.io/"><strong>Maria Rigaki</strong></a><br>Czech Technical University in Prague</td><td><img src="../../../.gitbook/assets/collab-carlos-a-catania.png" alt="Carlos A. Catania" width="48"><br><strong>Carlos A. Catania</strong><br>Czech Technical University in Prague</td></tr></tbody></table>

## Why "is it realistic?" is the wrong question

Verification and validation of a model of a natural system are impossible in principle, because such systems are never closed and model results are never unique. What remains available is partial confirmation, in relative terms, against what is already trusted. So the answerable question is not whether an environment is realistic, but realistic **for what**.

## Three audits, a decade apart, same verdict

Security machine learning has now been audited three times, and each audit reached the same conclusion about its own generation.

<table><thead><tr><th width="290">Audit</th><th>What it found</th></tr></thead><tbody>
<tr><td>Supervised security learning</td><td>ten pitfalls</td></tr>
<tr><td>Large-language-model security research</td><td>nine pitfalls, present in every one of 72 papers at leading security and software-engineering venues; only 15.7% of instances explicitly acknowledged</td></tr>
<tr><td>Deep reinforcement learning for cybersecurity</td><td>eleven pitfalls across 66 papers, 2018-2025, averaging 5.8 per paper: 71.2% show no evidence of policy convergence, 66.7% neglect variance analysis, 60.6% leave partial observability unmitigated, 40.9% evaluate in oversimplified or contrived environments</td></tr>
</tbody></table>

The consequence drawn is the one that motivates this thread: the pitfalls obscure whether a reported improvement comes from genuine algorithmic advance or from artifacts of simplified environments and incomplete evaluation.

## Gain attribution

The recurring mechanism has a name. **Gain attribution** is improvement that stems from information or capability engineered into the environment rather than from the learned policy. The remedy is to evaluate a random-action baseline in the same environment, and to compare approaches under equivalent state and action spaces.

The sharpest illustration comes from outside security. On one widely used tool-use benchmark a trivial agent returning empty responses scores 38% and outperforms a frontier-model agent, because impossible tasks are graded as successes. Issues of this kind move reported capability by up to 100% in relative terms, and 24% of the top fifty leaderboard positions on a prominent coding benchmark are wrong. Cost is the second unmeasured axis, and ignoring it has made the best-performing agents needlessly complex.

## Not only security

Benchmarking is the primary form of experimentation in 91% of empirical reinforcement-learning papers, and doing it rigorously enough to support the claims made carries computational costs that are often prohibitive — an argument for an additional experimental paradigm rather than for better benchmarking alone. Assessed against 46 best practices, widely used AI benchmarks show large quality differences, and most report no statistical significance and cannot easily be replicated.

_Last updated: 2026-08_
