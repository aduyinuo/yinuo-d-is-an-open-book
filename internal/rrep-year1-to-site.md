# RREP Year-1 report → what the site can take from it

Every file in `C:\[2025-2026][postdoc][utep]\RREP-Year1` read against the site,
2026-08-21. Thirteen sections, two notes files, the bibliography, the figure and
the two tools.

## Done

* **Collaborators.** Nine people the site never named are on the map: Grace
  Roessling, Sai Mounika Errapotu, Siyu Liu and Brad Edwards at Palo Alto
  Networks, and the four AAAI Summer Symposium co-organizers — Arunesh Sinha,
  Kimberly J. Ferguson-Walter, Quanyan Zhu, Sridhar Venkatesan. Carlos A.
  Catania has an affiliation at last, CTU Prague.
* **Funding outcomes.** Kaizen and the ARL BAA marked not funded with their
  figures; URI given its $5,000 and December 2025 date; the Kaizen role
  corrected from co-PI to Additional University PI; the Pilot Grant given the
  Errapotu letter of collaboration.

## Already in sync — nothing to do

`publications.md` carries every work at the same venue and status. Both
reading-group terms match speaker for speaker. Both mentor pages match. The
Service page is in fact *richer* than the report — it carries CMU-era committees
and the AAMAS, CogSci and GameSec reviewing the report omits.

---

## 1 · The agenda pages are thinner than section 03

Section 03 is 58KB of cited prose. The agenda pages carry the intuition and the
architecture; the report carries the evidence. Nothing on the site is wrong — it
stops earlier.

**Cyber World Modeling.** `environment.md` explains the FOE-Dreamer architecture
and ends. It has no results at all. The report has the eight-host OpenStack
testbed with CVE-bound exploits and GHOSTS-generated traffic, a three-day budget
on one GPU, roughly halved episode loss against both scripted attacker profiles
versus Rainbow and IQN under matched compute, ablations showing the factoring
and the opponent model each contribute, and the honest narrowing of the word
"operational" — substrate, services, exploit paths, five-second polling and the
consequences of defender actions real; user and attacker populations and the CVE
catalogue emulated.

`strategic-structure.md` gives the intuition for strategic dependence. The
report classifies it: five mechanisms carrying one player's behaviour into
another's best action — time, space, control, cause, information — each with an
ordered scale and a test separating adjacent levels, plus four conditions that
must all fail before a structure can be ignored. It positions graphical games,
influence-based abstraction, information-theoretic influence and attention
weights against it, excludes value-based abstraction as a contrast case, and
names two gaps nothing currently measures. None of that is on the site.

Neither ongoing-work line is on the site: model error, with a failure taxonomy,
a drift detector, a stated fallback if the adversary latent is not identifiable,
and a success criterion fixed in advance; and strategy search, whose deliverable
is the crossover point below which imagination stops paying. The new
AcceleratePSRO page states the question but not the experiment.

**Mental World Modeling.** The report opens on a finding the site carries
nowhere: six years of population-scale data from a competitive cybersecurity
platform, median time to first solve on hard challenges falling from a
40-to-340-minute band to five minutes in 2026, hard solve rates roughly
tripling. That is the empirical basis of the 5-year vista page *What Makes it So
Difficult?*, which has none. It also works out what a mental operation is across
four traditions that agree thinking decomposes and disagree on what individuates
an act, the grain problem from GOMS onward, and heuristics versus control.

**Human-AI Complementarity.** **FriendOrFoe appears nowhere on the site.** The
report describes it as the experiment CHART was built for and the first to run
on it — whether role dependencies raise complementarity against zero-day
attacks, and which of the leader, pool and informational dependencies carry the
effect. Design fixed, platform built. It needs a page. Also absent: that trust
measurements do not inform the question, and that joint performance does not
separate complementarity from one party carrying the other.

**Toward Deployment.** The report's framing is sharper: verification and
validation of a model of a natural system are impossible in principle, so the
answerable question is not whether an environment is realistic but realistic
*for what*. It carries three audits of security machine learning a decade apart
reaching the same verdict, gain attribution, the 91% benchmarking figure, and
the split between solving a simulator and using one as a proxy for deployment.
The site has Metrion but not the argument underneath it.

## 2 · The research overview has no argument, and there is one

`notes/research-statement-logic-flow.md` is the whole agenda argument written
out, and `research/overview.md` is a much thinner version of it. It gives:

* the numbers the programme is answering — 14-day median dwell time, 29-minute
  average breakout, 27 seconds fastest recorded, initial access handed on a
  median of 22 seconds after compromise, cited to M-Trends 2026 and CrowdStrike
* the one-line statement of what you do: *"I design practical AI agents that can
  be deployed in operational cyber environments with humans in the loop"*
* the four-part derivation, with its sources in brackets — Simon, Conant &
  Ashby, Richens/Abel/Everitt for the artifact bound by what it represents;
  Hutchins and Hollnagel & Woods for the pair being a property of the two
  together; Klein for mutual predictability, common ground and directability;
  Oreskes/Shrader-Frechette/Belitz and Winsberg for why a model of an open
  system can only be confirmed relatively
* why the thrusts are ordered as they are, and an honest evidence-class ranking
  of the four, including that Thrust IV has the most work still to do

This is what the research-agenda diagram task was asking for, and it already
exists in prose.

## 3 · There is a finished diagram of the four thrusts

`figures/thrusts.svg` — outer world (the network, its users, an adversary) and
the operator, with the four thrusts between them. 890×546, hand-authored SVG,
green palette close to the site's. The site has no research-agenda diagram at
all. `tools/svg2pdf.py` sits beside it.

## 4 · The reading list is missing 90 of the report's 124 citations

Some are your own papers, but most of the remainder are exactly the foundation
layer the reading-list page was meant to carry alongside the insight papers:

Newell & Simon, *Human Problem Solving* · Pólya, *How to Solve It* · Schoenfeld,
*Mathematical Problem Solving* · Chase & Simon on perception in chess · Card,
Moran & Newell, *The Psychology of Human-Computer Interaction* · Flavell on
metacognition, and Nelson & Narens · Ericsson & Simon, *Protocol Analysis* ·
Klein's critical decision method · Sutton, Precup & Singh on options · Ellis
et al., DreamCoder · Pearl, *Causality* · Wellman on empirical game-theoretic
analysis · Kearns on graphical games · Oliehoek on influence-based abstraction ·
Boutilier on factored representations · Diuk on object-oriented RL · Hafner,
DreamerV3 · CybORG · GHOSTS · Švábenský on CTF knowledge and skills · the green
security games line.

## 5 · The artifact pages are one-paragraph sketches

| Artifact | Site | Report adds |
|---|---|---|
| CHART | 175 words | the five dependency types — control, pool, synchrony, temporal, informational; the teamwork modalities layered above; the linked trace that lets a failure be attributed to a structural feature; and the four questions the next version must answer |
| Daedalus | 342 words | three subnets and their composition, the gRPC command-and-control server, the red agent's actual behaviour, the two backends behind one interface, and three named extensions in progress |
| Astrolabe | 393 words | question-cards with structural and origin edges, inter-coder agreement by percent and Cohen's κ, eleven graph metrics for blocking, decisiveness and relevance, and the two commitments that make it usable on human-subjects data |
| Agentic Lab | 282 words | the five annotation dimensions, the versioned consent gate, weekly drift diagnostics, and the evidence motivating it — the randomized trial where experienced developers were slowed 19% while believing they had been sped up 20% |

**Spelling.** The site uses *Daedelus* in four places and *Daedalus* in eight,
including in `SUMMARY.md`. The report uses *Daedalus* throughout.

## 6 · Teaching has content the site does not carry

`overview-2/` has the guest-lecture page but not what the lectures were on:
Graduate Research Methods on giving a talk that carries one point and finishes
on time; Introduction to AI on why a Q-table stops working and what a network
buys as an approximator.

Two further pieces are absent entirely: the intent to submit the capture-the-flag
challenge set as a **NICE Framework success story**, mapping challenges onto Work
Roles and reporting which Task, Knowledge and Skill statements students actually
reached; and the classroom-research loop — instrumented A/B testing across
sections producing a dataset that exists nowhere else.

**Teaching post-rigorously** is a written philosophy — Tao's pre-rigorous,
rigorous and post-rigorous stages, with stalling at the second as the failure it
designs against. `overview-2/learn-w-me.md` is an empty stub, and this is its
register, stated.

## 7 · There is a prose-audit tool, and the site is prose

`notes/writing-standard.md` and `tools/prose_audit.py` define ten detectable
habits of machine prose with thresholds — em dashes at 0–2 per 1000 words in
human prose against 6–12+ in machine prose, negative parallelism as the single
most-cited tell, sentence-length standard deviation under 10 as a warning — plus
four more that need reading. Two uses: `resources/research/write/` has English,
Mathematical Writing, Rigor and Structure pages and no page on this; and the
tool could be run over the site's own prose.

## Still unresolved

* **Omkar Thakoor** and **T. Guerra** have no affiliation anywhere — off the map.
* **Baptiste Prébot**: the report says only "France". The map places him at
  Inria Bordeaux, marked inferred.
