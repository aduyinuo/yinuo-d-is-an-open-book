---
description: Four projects, one sentence, and the word that means three things.
icon: spell-check
---

# Lexicon

Four projects sit in this cluster and they share one sentence. A human and an agent defend a network together, and I want to know whether the pair reached something neither would have reached alone. Every word in that sentence needs a definition before the sentence can be tested.

This page carries the terms more than one of the four projects uses, and the places where one word is doing two jobs across my own files. The rest stays with the project it belongs to.

## The question underneath

What is "Human-Centered Cybersecurity"? The question is on my [Headspace](../../../home/what-is-she-thinking.md) page with one link under it, and the link is a standards concept paper rather than a research program. That is already half the answer. The term is being fixed by an agency before the field has settled what it names.

NIST's definition is an approach that improves cybersecurity outcomes by putting people and their needs, abilities, and limitations at the forefront when designing, implementing, and making decisions about cybersecurity. The people in that sentence are the ones security is done to: the person choosing a password, the employee reporting a phish, the household configuring a device. The people in my cluster are the ones security is done by. The analyst on shift, and now the agent sitting next to her. Both start from the same refusal, that a person is a vulnerability to be contained. They part company on which person.

The concept paper also asks a question about itself that I recognize. Is human-centered cybersecurity an approach, measured by indicators of adoption and maturity, or an outcome, requiring measures of its own such as culture, trust, usability or resilience? That is my first challenge in a different vocabulary. If it is an outcome, somebody has to measure it, and nobody has said what the measurement is. Complementarity is the version of that measurement this cluster is trying to build.

The second Headspace question is the operational one: <mark style="color:$primary;">how much "human" do we want "in the loop" of cybersecurity decision-making?</mark> As posed it asks for a quantity, and there is no quantity. More human is not safer and less human is not faster, because the loop is not one loop. There is the loop where an action fires, the loop where an observation is seen, and the loop where a rationale is read, and a team can be tight in one and absent in another. The answerable version is structural. Which actions require whose authorization, who sees what before it happens, and in what order.

That is the whole cluster in one line. Turn a quantity question into a structure question, then make the structure the manipulation.

## The shared terms

Each entry gives a definition, what it is not, and the test I apply to decide whether it is in front of me.

### Complementarity

_**Complementarity.**_ The property that a human-agent pair produced a decision neither member would have produced alone. Not joint performance, and not the pair beating one member. Joint performance is what a scoreboard reports, and a pair can post the better number because one member carried it; that number is consistent with complementarity and also with total deference, and it does not separate them. The test: name the decision, point at the member who would not have made it alone, and say what the other member supplied. Three answers, or the claim is about the score.

_**Complementary team performance.**_ The field's working definition, as stated. Complementarity holds when the empirical loss of the team is strictly lower than the minimum of the two solo losses. Defined on aggregate loss and therefore checkable from a results table, where mine is defined per decision and is not. Compute three losses on the same instances and check two inequalities. A tie is a failure.

### Structure

_**Interdependence.**_ The patterned ways team members rely on one another for information, authorization, timing and execution. Not cooperation, which is a disposition of the members. Interdependence is a property of the task and the authority structure, and it holds whether or not anyone wants to cooperate. The test: can one member's action change what another member is able to do, without either of them communicating?

_**The structure is the manipulation.**_ The cluster's design commitment. The organization of the team is the independent variable, not a fixed setting inside which other variables are studied. Studying trust, workload or explanation quality under one fixed team gives real results, and none of them tells you whether the finding survives a change in how the team is organized. The test: between two conditions, can you name the single edge or policy that changed? If the manipulation cannot be written down as a change to the structure, the structure is still the backdrop.

_**Authority boundary.**_ The line between actions an agent may execute on its own and actions that require another teammate's authorization, as enforced by the software rather than as described in a protocol. Not an autonomy level, which is a property of the agent. A boundary is a property of the pair, and it can be tightened without touching the agent at all. The test: take the action out of the approval set and rerun. If the action fires where it previously waited, the boundary was real and you have just moved it.

### The three dependencies that cross projects

_**Control dependency.**_ An edge from a requester to an approver, carrying the set of actions that require authorization. Not a temporal dependency, which also blocks an action until something else happens; the blocker there is a prior action and can be satisfied by the requester acting alone. A control dependency can only be satisfied by another agent's decision. The test: who can clear the block?

_**Pool dependency.**_ An edge from each contributor into a pool node, which holds contributed actions until a threshold is met and then issues one composite action once. Not a shared budget, though both make two agents affect each other without communicating. They run in opposite directions: a pool needs contributions to accumulate before anything happens, a budget needs them to stay low so that something still can. The test: does the second contribution make the action possible, or impossible?

_**Informational dependency.**_ An edge carrying a filter over one agent's observation before another agent receives it. Not communication: a message is something a teammate chooses to send, and an informational edge is what the teammate is permitted to see whether or not anyone sends anything. The test: if both agents fall silent, does one of them still see less than the other? This is also the only dependency type that changes what the agent's own policy is conditioned on, which makes it the one that changes the learning problem and not only the interaction.

### Evidence

_**Trace.**_ A time-stamped record of an engagement whose entries are linked to one another, so that a sequence can be reconstructed rather than inferred from separate logs. Not a log. A log answers what happened. A trace answers what happened because of what, and the difference is the linking, not the volume. The test: take one decision in the record and ask what preceded it in a different stream. If you have to reconstruct that by hand from timestamps, you have logs.

_**Over-reliance.**_ Accepting the agent's recommendation at a rate higher than its accuracy supports, including on the instances where it is wrong. Not trust, which is the disposition. Over-reliance is the behaviour, and the two come apart: a person can report low trust and still approve everything, because approving is fast and checking is not. The test: split acceptance by whether the recommendation was correct. Flat acceptance across the split means reliance is not tracking accuracy.

_**Trust calibration.**_ Reliance that tracks the agent's actual reliability, rather than being uniformly high or uniformly low. Not a trust level, since a high level is not a calibrated one. The calibrated quantity is the relation between reliance and reliability, which needs at least two reliability conditions to estimate at all. The test: do you have instances where the agent was wrong, and did the human behave differently on them? Without both, trust was measured and calibration was not.

### The seam

_**The seam.**_ The interface between the human and the agent, considered as a design variable: what content crosses it, in what form, at what moment. Not the interface as a user-experience surface. The seam is defined by what information is transferred, not by how it is rendered, and the over-reliance result is a result about content rather than about layout. The test: name the items that cross. Evidence, label, confidence, rationale, uncertainty. Remove one and rerun. If nothing changes, that item was decoration.

_**Tacit knowledge.**_ The knowledge each member holds and cannot completely externalize. The analyst's trained sense that something is off, on one side; the model's latent state, on the other. Not private information, which is knowledge one party has and could state if asked. Tacit knowledge cannot be stated on demand, which is why a protocol for moving it cannot start by demanding it be articulated. The test: ask the holder to write it down. If what comes back is thinner than what they act on, the remainder is the tacit part.

_**Human in the loop.**_ Any arrangement in which a person's decision sits between an agent's proposal and its execution. Not human on the loop, where the person monitors and can interrupt but is not in the execution path. The distinction is whether the action waits. The test: if the person does nothing, does the action happen? A timeout policy that auto-approves converts the second arrangement into the first without anyone editing the graph.

_**Human load.**_ The cost the coordination structure imposes on the person, read from the record rather than only from a questionnaire: queue depth, decision latency, how often an explanation was opened, how often a proposal was modified before approval. Not task difficulty, which belongs to the scenario. Two conditions can share a scenario and differ in load purely because one of them routes more actions through an approval queue.

## Where the senses disagree

_**One word, three positions, three files.**_ The overview page treats complementarity as something not yet measurable and sets making it measurable as the challenge. [FriendOrFoe](friendorfoe.md) imports the field's loss-based definition and then argues that definition cannot distinguish a failed structure from an absent one. The [Next](next.md) page rejects both and asks for a counterfactual measure. These are not three glosses of one idea. The first says the term has no measure, the second says it has one and the measure is blunt, the third says the measure has to be counterfactual. The experiment can only pre-register one of them.

_**Pool names two mechanisms that run in opposite directions.**_ The [Team Defense Game](team-defense-game.md) calls the shared budget a pool dependency, and there every action either defender takes leaves less for the other. [CHART](chart.md)'s pool edge is a threshold, with a pool node that fires a composite action once enough contributions arrive. One subtracts and one accumulates. A condition description that says pool without saying which one is ambiguous, and this is the term most likely to be read wrong by someone who learned it from the book chapter.

_**Five types on three pages, three on the fourth, and one name that has no edge.**_ The CHART research page, the CHART design page and the book chapter all name the same five: control, pool, synchrony, temporal, informational. FriendOrFoe names three, and one of them is not on that list, since it asks which of the leader, pool and informational dependencies carry the effect. The platform has no edge type called leader. What it has at the authorizing end of a control edge is a role. So the two pages are either describing one manipulation under two names or two different manipulations, and one line of the experiment's configuration decides which.

_**Three things called a trace.**_ CHART records the linked Input-Process-Outcome history of a team session, whose unit is a coordination sequence across several agents. [CyberAgentFlow](cyberagenttrace.md) records the execution history of one agent's tool use, whose unit is a prompt, a tool invocation and its output. The overview page uses the bare word for both, in one sentence. Both are traces by the definition above; they differ in what the linked entities are, and therefore in what a failure can be attributed to. A file that has to be precise says team trace or execution trace.

## What stays with the projects

[CHART](chart.md) keeps taskwork interdependence, teamwork modalities, the graph and its node types, synchrony and temporal dependencies, the configurable inputs, the four modalities, capability profile, the Input-Process-Outcome record, and preference data. [Team Defense Game](team-defense-game.md) keeps the pending strip, the shared budget as its own sense of pool, episode-end re-scoring, and the agent memory of situation, action and blended value. [FriendOrFoe](friendorfoe.md) keeps role dependency, the leader naming, the combination rule, and the ten scenario tables. [CyberAgentFlow](cyberagenttrace.md) keeps execution trace, interaction lifecycle, context budget, and the five failure patterns, each of which is a term.

There is a fifth name on the site, [SOC Game](soc-game.md), and behind that title is a question this cluster has already put to itself twice: whether the graph can express how a security operations centre or an incident response team actually works. Until that is answered it is a test of CHART's expressiveness rather than a separate project.

The check that closes this page is the two-way one. Every entry above names a nearest neighbour, and each of those neighbours has to name it back. Control names temporal and temporal names control. Complementarity names joint performance and complementary team performance names complementarity. Pool names the shared budget and the Team Defense Game entry has to name the threshold sense. Where a distinction runs one way only, one of the two definitions is wrong, and the pool pair is the one to watch.

[**Download the full cluster lexicon (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/project-lexicons/hac_shared.pdf)

_Last updated: 2026-08_
