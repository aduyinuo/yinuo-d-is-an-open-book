---
icon: hackerrank
---

# Capture-the-Flag

## TLDR

<figure><img src="../../../../.gitbook/assets/ps-ctf-phases.gif" alt="Six phases of CTF problem solving, with phases two to four iterating and a belief layer underneath"><figcaption><p>A solve, traced through the six phases. Phases two to four are a loop, not a line.</p></figcaption></figure>

### The six phases

Orientation. Information gathering and reconnaissance. Hypothesis formation. Strategy selection and execution. Monitoring and regulation. Verification and transfer.

Beneath all six sits a layer that isn't a phase at all — belief systems and affective states. What the solver thinks this kind of challenge usually requires, and how they feel about being stuck, colour every phase above.

### Two deliberate choices

**The middle is a loop.** Gathering, hypothesising and executing don't run once in order. A solver cycles through them, and the cycling is the solve.

**The grain is coarse.** Finer metacognitive coding schemes have a history of collapsing under inter-rater disagreement, so the phases stay broad and the specific operations live inside them. That's a reliability decision, not an omission.

### Getting the data

Concurrent think-aloud is the gold standard and too intrusive for a timed competition. Retrospective think-aloud invites invention. Experience sampling interrupts. Cognitive task analysis interviews are expensive and depend on having an expert on hand. Platform logs are cheap but only tell you behaviour.

The workable combination is stimulated recall — replay the solver their own session as a retrieval cue — anchored to submission logs, so the recall has timestamps to hang on.

## What sits inside each phase

The phase is the coding unit and the operation is what the phase contains. A phase is broad enough that two annotators agree on where it starts, and it describes the solver rather than the challenge, which is why phases two to four recur many times in one solve while a stage of a scripted attack chain does not.

<table><thead><tr><th width="230">Phase</th><th>What it contains</th></tr></thead><tbody><tr><td><strong>0. Orientation</strong></td><td>Problem framing, crypto, forensics, web; scope assessment; resource inventory, what do I know and what tools or documentation exist; belief activation, skip it against worth investing time</td></tr><tr><td><strong>1. Information gathering</strong></td><td>Reading and comprehending provided materials; environmental exploration, scanning, traversal, inspecting artifacts; pattern recognition, this looks like base64; signal and noise discrimination</td></tr><tr><td><strong>2. Hypothesis formation</strong></td><td>Abductive reasoning; analogy to prior experience; decomposition into sub-problems; mental simulation, if I try X what happens</td></tr><tr><td><strong>3. Strategy selection and execution</strong></td><td>Tool selection; command formulation; parameter tuning; iterative refinement, try, observe, adjust</td></tr><tr><td><strong>4. Monitoring and regulation</strong></td><td>Progress assessment; strategy switching; time management; help-seeking decisions; frustration management</td></tr><tr><td><strong>5. Verification and transfer</strong></td><td>Solution validation, flag-format checks; error detection and diagnosis; knowledge consolidation for the next challenge</td></tr><tr><td><strong>Cross-cutting: beliefs and affect</strong></td><td>Confidence calibration; competition-driven rushing; intimidation by unfamiliar domains; the satisfaction and reward experience</td></tr></tbody></table>

The cross-cutting layer is not phase four. Monitoring and regulation is something the solver does; a belief is something the solver holds, and it changes the cost of every operation above without appearing as a step anywhere. Could the item be true of the solver before the challenge was opened? If yes, it is a belief and not a phase. Schoenfeld's fourth knowledge category is the ancestor of this layer, and it is what explains the instruction-skipping pattern designers report: a belief failure about what a competition rewards, compounded by a control failure.

The loop is a later amendment rather than an original feature. It was agreed after the first coding pass, and the version of the taxonomy that carries it is the copy inside the framework document rather than the original writeup. The test for whether it is being honoured is countable: count the transitions from phase three back to phase one in a coded solve, and if the count is zero across a corpus, the phases are being coded as a script.

## Grain, and the layer above the operations

The operation itself is a typed, directed step from a set of held questions to a set of new ones, carrying a confidence and an attribution to the person or the tool that made it. That is not a tool invocation. A command is an act in the world; an operation is the step in the head that decided to run it, and the two are recorded against each other on purpose, because the attribution field is what lets an agent-assisted solve be separated from an unassisted one. Can you name the questions it consumed and the questions it produced? If the step cannot be written as questions in and questions out, it is an action and it belongs in the trace.

Questions are the nodes, not subgoals. A subgoal is something to achieve and is satisfied or not; a question is something to determine and can be answered wrongly, which is what makes the backtracking in a real solve representable. The annotation protocol asks the annotator to name the question before naming the operation, so operations are recovered as the links between questions rather than as a free-standing list of verbs. Each link carries one of four relation types: compositional, causal, co-occurrence, and dependency. Only the dependency edges form the acyclic prerequisite structure, which is why criticality is defined on that graph alone, and why a question can be a prerequisite without being a cause.

Grain is the size of the unit an operation is coded at, and there is no principled unit, so it is chosen per purpose and held fixed for the study that uses it. A finer grain buys detail and spends agreement, and past attempts have spent more than they bought. Is the grain stated in the protocol before the first solve is coded? A grain chosen after seeing the disagreement figures is a selection, not a decision. The protocol fixes it at the smallest unit of action, and the reliability cost of not fixing it was the first thing raised against the protocol in review.

Control is the layer that decides which operation to run next, notices that a line is not working, and decides when to abandon it. Can the item be performed without reference to how the solve is going? If it can, it is an operation. If it needs the state of the attempt, it is control. Schoenfeld's result is that control, and not the stock of heuristics, is what separates experts from novices, so a taxonomy that folds control into the operation list has lost the discriminating half.

_**Tool selection sits in two places and both are defensible.**_ The taxonomy puts it inside phase three, as the first item under strategy selection and execution. The cluster's [open-problems page](../next.md) puts it above the phases, with knowing when to stop, as an optimal-stopping problem sitting on top of the solve. Coded inside phase three, choosing a tool is one operation among four. Coded as control, it is the thing the study is actually about, since it is the operation an agent solver does not make the same way a person does. The taxonomy of record keeps it in phase three. That is the compromise, not the resolution.

## The six methods, and what each buys

<table><thead><tr><th width="190">Method</th><th width="220">What it gives</th><th>The verdict here</th></tr></thead><tbody><tr><td><strong>Concurrent think-aloud</strong></td><td>Real-time verbalisation during the solve; the gold standard for access to process</td><td>Too intrusive for a timed competition; usable in a lab, outside the event</td></tr><tr><td><strong>Retrospective think-aloud</strong></td><td>Narration after the fact, no interference</td><td>Invites invention; the solver reconstructs rather than reports</td></tr><tr><td><strong>Experience sampling</strong></td><td>Self-report at trigger points, such as a short popup after a submission</td><td>Interrupts, and items get skipped under time pressure, so the missing data is biased toward the most competitive solvers</td></tr><tr><td><strong>Cognitive task analysis interview</strong></td><td>Structured recovery of one concrete incident, in deepening passes</td><td>Expensive, and depends on having an expert on hand</td></tr><tr><td><strong>Platform logs</strong></td><td>Timestamped submissions, selection order, error patterns, at large scale</td><td>Cheap, and tells you behaviour only</td></tr><tr><td><strong>Stimulated recall</strong></td><td>Narration cued by the solver's own screen replay</td><td>The workable one, once it is anchored to the logs</td></tr></tbody></table>

The last two rows are a pair rather than two independent choices. The submission log supplies the moments worth asking about, and without it the screen recording is a continuous stream that questions cannot be addressed to. The recall interval is minimised, same session and ideally immediately after, and probes are anchored on log events. The worked example of a probe is a run of three wrong submissions, asked about as a run rather than as three separate events.

One thing to keep straight, because my own files split on it. The methods writeup pairs retrospective think-aloud and stimulated recall under one heading and gives the pair one verdict. This page splits them and gives them opposite verdicts. The split is the one to keep, and the cue is the reason: without it the solver reconstructs a plausible account, and with it the solver is answering about a specific moment that is on the screen in front of them. Is there a cue on the screen at the moment the question is asked? If the interviewer is asking from memory, it is retrospective think-aloud however it was labelled.

## The design side

Solvers are one population. Designers are the other, and they are interviewed about one concrete challenge of their own rather than about design in general. A designer sets the challenge and never sees most of the solvers, which is why the scoring paradigm is **predict-then-test**: the designer predicts where solvers will stall and what they will try, and those predictions are scored against what the solvers did. A rating is a claim about the artifact; a prediction is a claim about people, and only the second one can be wrong in a way that is informative. It is run on the designer's own challenge rather than on a challenge set, so a wrong prediction cannot be attributed to unfamiliarity.

Two design levers have names because the pilots described both without having words for either.

_**A bottleneck**_ is a point in a challenge that only lets through solvers who perform a particular operation, with the hint system placed to rescue the rest. That is targeted at an operation, and raising the technical demand of every step raises difficulty without selecting for anything. Name the operation the gate requires. If it cannot be named, the step is hard rather than selective. The strongest pilot transcript describes a branching structure narrowing from five candidate paths to one, gated on noticing a planted anomaly, with hints existing to rescue the solvers who do not notice. That is a designer targeting an operation without a word for it, which is the whole case for supplying the vocabulary.

_**A hint ladder**_ is an ordered set of hints of increasing information content, with the first tier calibrated against the point where a novice abandons the challenge. A single hint either arrives too early and removes the operation, or too late and loses the solver; the ladder is what makes the amount of assistance a design variable rather than a binary. Does each tier collapse a different part of the search space? If two tiers reveal the same thing at different wordings, it is one hint written twice. One designer calibrates by solving his own challenge as if he were a beginner, having observed that students abandon a brute force attempt within five to ten minutes, and his tiers escalate from the encoding, to the cipher stack on top of it, to the wordlist theme that collapses the search space.

## Difficulty, in three senses, all of them mine

Structural: a vector over solution size, the length of the optimal solution; concept load, the number of concepts held and related at once; and search burden, the effort of finding the operations rather than applying them. A rating is one number and hides which of the three moved, which is precisely the information a designer needs in order to change one of them. Difficulty and ability are two sides of one relation, so the vector is indexed by the solver, and where no solution exists difficulty is maximal rather than undefined, because certifying that a closed problem has no solution is itself a co-NP task.

Relational: a designer's account in which the same artifact is trivial or impossible depending on what the student notices, so the levers are hint placement and what is left observable.

Experiential: hills and valleys, difficulty modulated across a sequence of challenges rather than within one task.

The three do not contradict each other and they do not compose either. The vector is a property of a problem and a solver. The relational account is a property of a problem and what was left visible. The experiential account is a property of an ordered set of problems. A question about difficulty is underspecified until it says which of the three is meant, and my interview guide asks all three without saying so.

## The agent in the room

AI attacker agents can now solve many challenges on their own, which lowers the skill floor: work that used to take a trained person can be done by running a tool. Banning the tools is a losing game. The better response is to adapt the format to a world where the tools exist, and the position that follows is short. The hard part of a CTF is the thinking, not the typing. Agents can run the tools, so what is worth teaching and testing is the set of mental moves a solver makes.

An **agent solver** completes a challenge end to end without a person choosing the steps, and it is a condition of the environment here rather than a subject of the study. It is not an assistive tool used during a human solve, which appears in the attribution field of an operation and leaves the solve a human solve. Who chose the next step? If no person did, at any point, it is an agent solve.

**Human against agent divergence** is the gap between the operations a challenge demands of a person and the operations it demands of an agent. It is not a capability gap, and it is not about which of the two is better. It is about which operations each finds expensive, and those sets differ in both directions. A designer named it before we did: humans in a competition skim and rush by choice, while an agent would dissect and digest the entire instructions. His conclusion is that instructions as a source of difficulty penalise humans differentially, which is a design finding rather than a complaint.

**Self-management as difficulty** is difficulty that comes from regulating the attempt rather than from the technical content: deciding when to abandon a line, resisting the pull of a sunk cost, tolerating being stuck. Technical difficulty is what an agent absorbs, so this is the residue the whole position depends on, and it is the category that has to be measurable if the position is to be worth anything. Would the challenge get easier for a solver with unlimited patience and no time pressure, holding knowledge constant? If yes, part of its difficulty is self-management. One of the five items on the beliefs and affect scale asks it directly from the student side: I kept working longer than I should have because I had already invested time.

## Where two of my files disagree

<table><thead><tr><th width="330">The disagreement</th><th>Where it sits</th></tr></thead><tbody><tr><td>The construct is unsettled, and the first hypothesis is stated over it</td><td>mental operation</td></tr><tr><td>Tool selection inside phase three, or above the phases as control</td><td>control</td></tr><tr><td>Stimulated recall as its own method, or paired with retrospective think-aloud</td><td>stimulated recall</td></tr><tr><td>Difficulty as a vector, as a relation to what is observable, and as a curve across a set</td><td>difficulty</td></tr></tbody></table>

The first of those is worth stating rather than leaving for the room. The framework treats the missing definition as the work itself, since the strength of any hypothesis stated in terms of mental operations depends on how the term is fixed. The poster treats it as settled enough to build on. Both are mine and both are current, and the answer is that the empirical claim is a claim about inter-rater recoverability under a fixed grain, not a claim that the construct has been settled.

One further gap belongs here rather than in an argument. The index question asks about the era of agent solvers, and the page above answers the first half of it and stops. The answer to the second half is the section on the agent in the room.

[**Download the full lexicon (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/project-lexicons/mwm_capture_the_flag.pdf)

## Slides



## Publications

<table><thead><tr><th width="100"></th><th width="400">Paper</th><th>Authors</th><th></th></tr></thead><tbody><tr><td><img src="../../../../.gitbook/assets/badge-sigcse.png" alt="SIGCSE" data-size="original"></td><td><mark style="color:green;">Capture-The-Flag Universe: Design Considerations, System Behavior, and Player Experiences</mark><br><em>Under review, SIGCSE Virtual 2026</em></td><td><strong>Y. Du</strong>, Y. Keim, <a href="https://expertise.utep.edu/profiles/apiplai">A. Piplai</a>, <a href="https://www.utep.edu/cs/people/faculty-websites/jacosta.html">J. Acosta</a>, <a href="https://anantaakotal.github.io/">A. Kotal</a></td><td></td></tr></tbody></table>

## Collaborators

<table><thead><tr><th width="150"></th><th width="150"></th><th width="150"></th><th width="150"></th></tr></thead><tbody><tr><td><p><img src="../../../../.gitbook/assets/Keim.jpg" alt="Yansi Keim" data-size="original"></p><p><br><a href="https://www.albany.edu/business/faculty/yansi-keim"><strong>Yansi Keim</strong></a><br>University of Texas at El Paso</p></td><td><p><img src="../../../../.gitbook/assets/collab-aritran-piplai.png" alt="Aritran Piplai" data-size="original"></p><p><br><a href="https://expertise.utep.edu/profiles/apiplai"><strong>Aritran Piplai</strong></a><br>University of Texas at El Paso</p></td><td><p><img src="../../../../.gitbook/assets/collab-jaime-acosta.png" alt="Jaime Acosta" data-size="original"></p><p><br><a href="https://www.utep.edu/cs/people/faculty-websites/jacosta.html"><strong>Jaime Acosta</strong></a><br>University of Texas at El Paso / DEVCOM ARL</p></td><td><p><img src="../../../../.gitbook/assets/collab-anantaa-kotal.png" alt="Anantaa Kotal" data-size="original"></p><p><br><a href="https://anantaakotal.github.io/"><strong>Anantaa Kotal</strong></a><br>University of Texas at El Paso</p></td></tr></tbody></table>

_Last updated: 2026-08_
