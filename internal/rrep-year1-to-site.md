# RREP Year-1 report → what the site can take from it

Checked `C:\[2025-2026][postdoc][utep]\RREP-Year1` against the site, section by
section, 2026-08-21.

## Already in sync — nothing to do

`publications.md` carries every work in the report at the same venue and status.
Both reading-group terms match, speaker for speaker. Both mentor pages match.
The tools — CHART, Daedalus, Astrolabe, Agentic Lab — are covered under
`artifacts/` and `tools/`.

## Done

* **Collaborators.** Nine people the site never named are on the map: Grace
  Roessling, Sai Mounika Errapotu, Siyu Liu and Brad Edwards at Palo Alto
  Networks, and the four AAAI Summer Symposium co-organizers — Arunesh Sinha,
  Kimberly J. Ferguson-Walter, Quanyan Zhu, Sridhar Venkatesan. Carlos A.
  Catania has an affiliation at last (CTU Prague).
* **Funding outcomes.** Kaizen and the ARL BAA both marked not funded, with
  their figures. URI given its $5,000 and December 2025 date. Kaizen's role
  corrected from co-PI to Additional University PI. Pilot Grant given the
  Errapotu letter of collaboration.

## The real gap — the agenda pages are thinner than the report

This is the bulk of it, and it is not a detail. Section 03 is 58KB of cited
prose across the four thrusts. The agenda pages carry the intuition and the
architecture; the report carries the evidence. Nothing on the site is wrong —
it simply stops earlier.

### Cyber World Modeling

`environment.md` explains the FOE-Dreamer architecture and then ends. It has no
results at all. The report has them:

* eight-host OpenStack testbed, CVE-bound exploits, GHOSTS-generated user traffic
* trains inside a three-day budget on one GPU
* roughly halves episode loss against both scripted attacker profiles, against
  Rainbow and IQN under matched compute
* ablations: the factoring and the opponent model each contribute
* and the honest narrowing of the word "operational" — the substrate, services,
  exploit paths, five-second polling and the consequences of defender actions
  are real; the user and attacker populations and the CVE catalogue are emulated

`strategic-structure.md` gives the intuition for strategic dependence. The
report classifies it: five mechanisms carrying one player's behaviour into
another's best action — time, space, control, cause, information — each with an
ordered scale and a test separating adjacent levels, plus the four conditions
that must all fail before a structure can be ignored. It also positions the
existing measures (graphical games, influence-based abstraction,
information-theoretic influence, attention weights) and names two gaps in the
measure set. None of that is on the site.

Neither ongoing-work line is on the site either: the model-error work, with its
failure taxonomy and drift detector and a success criterion fixed in advance,
and the strategy-search work, whose deliverable is the crossover point below
which imagination stops paying. The new AcceleratePSRO page states the question
but not the experiment.

### Mental World Modeling

The report opens on a finding the site does not carry anywhere: six years of
population-scale data from a competitive cybersecurity platform showing median
time to first solve on hard challenges falling from a 40-to-340-minute band to
five minutes in 2026, with field-wide hard solve rates roughly tripling. That
is the empirical basis of the 5-year vista page *What Makes it So Difficult?*,
which currently has none.

It also works out what a mental operation is across four traditions, the grain
problem from GOMS onward, and the heuristics-versus-control distinction. The
problem-solving pages state the framework without this grounding.

### Human-AI Complementarity

**FriendOrFoe does not exist anywhere on the site.** The report describes it as
the experiment CHART was built for and the first to run on it — whether role
dependencies raise complementarity against zero-day attacks, and which of the
leader, pool and informational dependencies carry the effect. Design fixed,
platform built. It needs a page.

The measurement problem is also absent: that trust measurements do not inform
the question, and that joint performance does not separate complementarity from
one party carrying the other.

### Toward Deployment

The report's framing is sharper than the site's: verification and validation of
a model of a natural system are impossible in principle, so the answerable
question is not whether an environment is realistic but realistic *for what*.
It carries three audits of security machine learning a decade apart reaching the
same verdict, gain attribution, the 91% benchmarking figure, and the distinction
between solving a simulator and using one as a proxy for deployment. The site
has Metrion but not the argument underneath it.

## Still unresolved

* **Omkar Thakoor** and **T. Guerra** have no affiliation anywhere — off the map.
* **Baptiste Prébot**: the report says only "France". The map places him at
  Inria Bordeaux, marked inferred.
