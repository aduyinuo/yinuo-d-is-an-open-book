---
description: Three names for the thing, one unit of work, and the words the two branches share.
icon: spell-check
---

# Lexicon

The [cluster page](README.md) opens with two challenges and neither of them is a question about cybersecurity. They are conditions on whether the rest of the cluster can be asked at all. The first is that a long history of work on mental operations never settled on a single canonical definition. The second is that the methods have to recover strategy from sparse, sometimes adversarial traces.

One is a definition problem and the other is a measurement problem, and the two branches split along exactly that line. [Problem-Solving](problem-solving/) takes the definition problem and pays for it in resolution, holding the vocabulary coarse enough that two people coding one solve will agree. [Social World Modeling](opponent-agent-modeling/) takes the measurement problem and pays for it by putting structure on the adversary in advance, in a reward function or in a category, so that something is left to recover when the trace is thin.

This page is the vocabulary those two halves share. Where a term means two things across two projects, both meanings stay. That is the entry most worth having.

## Three names, and which one is the working unit

The cluster is called Mental World Modeling. The concept its own page says has no consensus is the Mental Model. The unit every project underneath actually works in is the mental operation. Those are three different objects, and the difference is not cosmetic, because only one of them is something a coder can be asked to find in a transcript.

The Mental Model is the inherited term the cluster declines to adopt, and nothing else here uses the phrase again. The mental world model is the object being built, and on disk it is specified: a directed, multi-relational, weighted hypergraph whose nodes are questions and whose hyperedges are mental operations. That is a model of a solver's world of open questions, not a model inside the solver's head. The mental operation is the unit of work, and it is what every project page and every section of the framework's definitions actually operates on. The three are kept apart everywhere below.

There is a second collision, in the other branch, and it is a naming collision rather than a sense one. The adversarial half is reached by a link called Opponent (Agent) Modeling, its own page is headed Social World Modeling, the folder is `opponent-agent-modeling`, and the navigation calls it Strategic Interaction. Four live names for one branch. Its child page has the same problem: the link says Iterated Strategic Interaction, the file is `social-intelligence.md`, and the heading is Iterated Prisoner's Dilemma.

## The unit and its scale

_**Mental operation.**_ A discrete act of thought that transforms one mental state into another, held at a stated grain. In the formal version it is a directed, typed, weighted hyperedge over questions, carrying a relation type and a time-indexed confidence that the edge is valid. It is not an action. An action is the smallest observable unit of solving behaviour, an utterance fragment, a command, a click, a test, and it is observed directly; an operation is inferred from a window of actions and is never read off one. The gap between them is where all the measurement difficulty sits. Give two coders the same segment and the same label set. If they cannot put the same label on it, what you have is a name, not an operation.

Where it appears: [General CS](problem-solving/general-cs.md) as a twenty-code scheme, twelve object-level and eight regulatory. [Capture-the-Flag](problem-solving/capture-the-flag.md) as six phases with the specific operations living inside them. The core framework as the hyperedge. [Small Groups](problem-solving/small-groups.md) is the one project that does not use the term at all, because its unit is an utterance in a conversation.

_**Grain.**_ The temporal and semantic scale at which the operation vocabulary is fixed. Three scales that do not reduce to one another: elementary acts on the order of a fraction of a second, strategies composed of many of them, and regulation over a whole attempt. Grain is not the resolution of the recording. It is a decision about the label set, and a keystroke log is fine-resolution data that can still be coded at Polya scale. Name the duration band the vocabulary is meant to occupy. If one list mixes keystroke-scale acts with whole-attempt heuristics, the grain was never fixed, it was defaulted. Newell's time scale of human action is the nearest thing the literature has to a shared ordering across the three scales, and it orders operations by duration without saying which operations populate which band.

_**The control layer.**_ The layer that selects among operations, monitors whether a line is working, and decides when to quit. Planning before, monitoring during, evaluating after. It is not one more operation of the same kind sitting in the same list. In the CS codebook the two are separated by construction, the eight regulatory codes above the twelve object-level ones, and the boundary cases are written into the codebook rather than left to the coder. Ask whether the label describes a change to the problem or a change to the plan for working on the problem. The second one is regulation. In the cyber setting the two concrete versions are tool selection and knowing when to stop, and both look less like steps inside a solve than like an optimal-stopping problem sitting on top of one.

A citation correction belongs with that entry, because the cluster rests on it. Flavell 1979 named metacognition and mapped its knowledge component, the person, task and strategy knowledge a solver has about cognition. The regulation triad usually wanted, planning, monitoring, evaluating, is Brown 1987. The two are routinely merged in citations and they are not the same claim.

## The standard the vocabulary is held to

_**Reliability, and what it costs.**_ The admission standard. Independent coders agree on where one operation ends and the next begins, or the vocabulary does not enter the analysis. It is not validity, which asks whether the label names anything real. Reliability is the cheaper question and it is asked first, on the argument that an unreliable construct cannot be shown valid anyway. The price is resolution: fine schemes are dropped in favour of coarse ones that survive. Three coders, one session, agreement reported before any labels are merged. Agreement computed after merging the labels coders confused is a different number and it is not the one to report. The commitment appears in three vocabularies across three pages and a fourth time in the conference prep notes, always as a limit on all of it.

_**Disagreement as finding.**_ The rule that a split between coders is retained and reported as a location, not resolved by adjudication and then forgotten. Low reliability is a verdict on the scheme; this is a verdict on a segment. A scheme can hit acceptable agreement overall and still have a handful of segments that split every time, and those are the ones that say where the construct is soft. After adjudication, can you still say which segments disagreed and who took which side? If the consensus track overwrote them, the finding was thrown away.

## Getting the strategy out of the person

_**Elicitation.**_ The method by which a solver's strategy is recovered, given that much of what an expert does is tacit and genuinely unavailable to introspection. It is not instrumentation. Platform logs are cheap and always available and they tell you behaviour, which is not strategy. Ask whether the method runs during the task or after it. During gives valid contents of working memory and distorts the task. After leaves the task alone and invites invention. Everything else is an attempt to buy some of both.

Six methods are in play across the branch, and the Capture-the-Flag page rules out five by name.

<table><thead><tr><th width="260">Method</th><th>Verdict</th></tr></thead><tbody><tr><td><strong>Concurrent think-aloud</strong></td><td>The gold standard, and too intrusive for a timed competition</td></tr><tr><td><strong>Retrospective think-aloud</strong></td><td>Invites invention</td></tr><tr><td><strong>Experience sampling</strong></td><td>Interrupts</td></tr><tr><td><strong>Cognitive task analysis interviews</strong></td><td>Expensive, and depend on having an expert on hand</td></tr><tr><td><strong>Platform logs</strong></td><td>Cheap, and only tell you behaviour</td></tr><tr><td><strong>Stimulated recall</strong></td><td>The workable one, anchored to submission logs so the recall has timestamps to hang on</td></tr></tbody></table>

_**Stimulated recall.**_ Replay the solver their own session as a retrieval cue, after the task, and record what they say about it. It is not retrospective think-aloud, which asks for the same report without the cue. The cue is the whole difference, and it is what makes the report a recall rather than a reconstruction. Is there a timestamped record to anchor the replay to? Without one there is nothing to hang the recall on and the method degrades into the retrospective case.

The core framework proposes a different answer to the same problem, validation by convergence across five methods with different blind spots, on the argument that the object is fixed not by one measurement but by the agreement of several.

## Reading the other agent

_**Type, and typing another agent.**_ A compressed category assigned to another agent from what that agent has been observed to do, standing in for a full model of them. It is not a strategy. A strategy is what the other agent does; a type is what the modeller carries instead, because carrying the strategy is too expensive. The compression is the point, not an approximation forced on you. Ask whether the category is assigned against a fixed threshold or against the rest of the population. Relative assignment means the same behaviour lands in different categories depending on who else is in the room.

Three formulations of one thing sit across the cluster: how agents read each other into kinds across repeated interaction, on the cluster page; the compression into cooperative, conditional and exploitative, on the [Iterated Prisoner's Dilemma](opponent-agent-modeling/social-intelligence.md) page; and one account of how an agent types another, on [Next](next.md). The adversarial version carries none of that vocabulary and calls the same object a behavioural fingerprint.

_**Two senses of type, and the cluster says so itself.**_ On the cooperative page a type is an empirical category the focal agent builds from a running estimate of how often each partner cooperates, assigned relative to the group mean. On the Next page a type is hidden and is recovered from behaviour while the other party adapts, which is the type of a Bayesian game: a property the other agent already has and the modeller does not observe. One is constructed by the observer and would not survive a change in the reference group. The other is a fact about the observed agent. The cluster's own open problem asks for them to be folded into a single account, which is the right request and is not the same as asserting they already are one. Left open.

_**Realistic opponent.**_ An adversary model that departs from optimal play in structured, repeatable ways, rather than an expected-utility maximiser. It is not a hand-written rule set, which also departs from optimal play but does not generalise past the cases that were written down. The [biased attacker](opponent-agent-modeling/bias/biased-attacker.md) line puts the departure in the reward function instead, so it generalises by construction. Change the environment and see whether the departure survives. A bias in the reward moves with the agent. A rule stays where it was written.

_**Behavioural fingerprint.**_ A pattern in an agent's trajectory that identifies which kind of agent produced it, given that the network, the action space and the objective were held fixed. It is not a signature in the detection sense, which identifies an attack. A fingerprint identifies an attacker, and it survives the attacker changing which attack they run. Two conditions, both required: systematic, so the deviation recurs, and separable, so two kinds do not produce the same pattern.

## The object being built

_**Question graph.**_ The directed, multi-relational, weighted hypergraph whose nodes are questions and whose hyperedges are mental operations, reconstructed from a solver's action trace. A problem is a pair of initial questions and a goal predicate, a solving state is a sub-hypergraph, and a solution is a minimal set of operations reaching a goal question, which is a hyperpath because every source of an applied operation is required. It is not a concept map, which has concepts as nodes; here concepts are carried by the questions and the concept graph is a projection. Can an edge have more than one source question, with all of them required? If not, it is a graph and the hypergraph machinery is unused. Its maturity is worth carrying with it: definitions drafted, zero data through the framework itself.

_**Difficulty.**_ A vector over three components rather than a single number, because the three sources are not commensurable: solution size, the length of the optimal solution; concept load, the number of concepts held and related at once; and search burden, the effort of finding the operations rather than applying them. Where no solution exists difficulty is maximal rather than undefined, since certifying that a closed problem has no solution is itself a co-NP task. It is not an item difficulty parameter, which is one number fitted to a population. This one is relative to a solver, and difficulty and ability are two sides of one relation. Can two problems be incomparable? Under a vector they can, and that is the intended behaviour.

## Working terms

_**Action.**_ The smallest observable unit of solving behaviour, taken as a primitive and observed directly. Action mining inherits the ambiguity of where one unit of behaviour ends and the next begins, which is not fixed across utterances, commands and tests.

_**Relation type.**_ The label every operation carries, from a vocabulary of four: compositional, the part-whole relation; causal, resolving the sources enables the target; co-occurrence, undirected, with no claim of order or cause; and dependency, the target cannot be resolved until its sources are. None of the four is chronological order, which is what a trace gives you for free. Dependency is the one that induces an acyclic graph.

_**Criticality.**_ The value of information of a question on the dependency graph. Not the causal relation, and the framework says so: a question can be a prerequisite without being a cause.

_**Trace.**_ The observed sequence of actions in one session, from which the graph is reconstructed. The structure inference problem is exactly the gap between the trace and the graph, and the framework bounds it: the operation labeling is recoverable from a trace only up to a tolerance, since distinct labelings can fit the same trace.

_**Inter-rater agreement.**_ Stage-level percent agreement and Cohen's kappa between coders labelling the same session. Not consensus, which is what you build after measuring agreement. Reporting the consensus track without the agreement figure hides the number the scheme is being judged on.

_**Categorization and contrast.**_ Categorization compresses many partners into a small number of types. Contrast makes the assignment relative: a partner is classified against the group mean, so identical evidence yields a different judgement depending on who else is in the room. Neither is an absolute threshold rule, which is what most opponent classifiers use.

_**Episode.**_ One bounded stretch of solving, segmented from the trace. Not the session, which is the whole recording. One session contains many episodes and the boundaries are inferred, which is where coders most often split.

## The three open problems

The [Next](next.md) page states them and they are the reason this page is arranged the way it is.

**Operations as learned actions, not a fixed taxonomy.** Every account here takes its operations as given, named in advance and then looked for in the data. If they were learned and composable instead, the grain problem softens, because the agent finds the grain that pays, and the model stops depending on a taxonomy no one has agreed on. Hierarchical reinforcement learning's options and program synthesis's reusable libraries are the two existing shapes an answer could take.

**The control layer.** A distinct problem from the operations it governs, and the under-modeled one.

**One account of typing another agent.** The cooperative side reads a partner into a kind, the adversarial side models an attacker's built-in bias, and the claim is that these are the same inference done twice with different vocabulary. This is the one that can be acted on now, because both vocabularies are already written down and can be laid against each other without new data. The other two need data the cluster does not yet have.

## What crosses out of this cluster

<table><thead><tr><th width="150">Term</th><th width="240">Here</th><th>In Cyber World Modeling</th></tr></thead><tbody><tr><td><strong>world model</strong></td><td>A hypergraph of a solver's questions and operations</td><td>A learned per-device latent dynamics model with a controllable, exogenous and opponent factoring</td></tr><tr><td><strong>opponent model</strong></td><td>A category assignment over a partner's behavioural profile</td><td>A per-device embedding inferred from defender-observable signals</td></tr><tr><td><strong>operation</strong></td><td>A discrete act of thought, or a typed hyperedge</td><td>Not used; the nearest term is the defender action</td></tr><tr><td><strong>difficulty</strong></td><td>A three-component vector over solution size, concept load and search burden</td><td>Not used; the nearest term is sample efficiency</td></tr><tr><td><strong>transfer</strong></td><td>Whether taught heuristics carry to a new problem</td><td>Policy transfer across environments</td></tr></tbody></table>

The first row is the one to watch. Two folders are both called world modeling and they share almost no vocabulary. Whether the parallel is a claim or a naming convenience is not settled anywhere in either of them, and this page does not settle it either. What it does is keep the two definitions in one place so the question can be asked with both in view.

[**Download the full lexicon (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/project-lexicons/mwm_shared.pdf)

_Last updated: 2026-08_
