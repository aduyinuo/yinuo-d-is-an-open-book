---
icon: computer-speaker
---

# General CS Problem-Solving

<figure><img src="../../../../.gitbook/assets/ps-cs-graph.gif" alt="A problem-solving graph being built step by step as a session unfolds"><figcaption><p>The same session as a graph, drawn as it happens.</p></figcaption></figure>

## Solving as a graph

A session isn't a list. Reading the spec spawns two things at once — a plan to split the problem into cases, and the memory of a similar bug. The plan spawns two pieces of implementation. Running the tests produces a failure, the failure produces a hypothesis, and the hypothesis produces both a patch and a note about the pattern that will outlive this problem.

Drawn this way, the shape of the solve is visible: where it branched, where it looped back, and which step turned out to be the hinge.

## The question

When someone works through a computing problem, what are they doing at each moment? Reading, decomposing, recalling something they've seen before, planning, implementing, testing, revising.

Naming those operations is easy. Getting independent observers to agree on where one ends and the next begins is not, and that agreement is the whole ballgame — a construct nobody can code reliably isn't a construct.

## Can observers agree on it

<figure><img src="../../../../.gitbook/assets/ps-cs-consensus.gif" alt="Three coders annotating one solving session with mental operations, and the consensus track underneath"><figcaption><p>One session, three independent coders, one consensus track.</p></figcaption></figure>

Three coders labelling the same session, segment by segment, with the consensus track underneath. Where all three agree, the consensus block is solid and outlined. Where they don't, it fades.

The running agreement figure is deliberately not flattering. Disagreement is treated as the finding rather than the noise: the segments where coders split are the segments where the operation genuinely is ambiguous, and those are worth studying rather than smoothing away.

## The instrument

The coding in that animation is not done by hand on paper. It runs in **Astrolabe**, a local research app built for this work.

Astrolabe takes in transcripts — typed, uploaded, or recorded in the browser and transcribed with Whisper — and lets multiple annotators code the same session against a shared scheme. It then reports stage-level percent agreement and Cohen's kappa between coders, and exports the agreement report and the full annotation bundle for downstream analysis.

It also carries the question-card structure the project is organised around, with hypergraph overlays for grouping operations at different scales, and reusable prompt scaffolds when a language model is used to propose candidate operations or concepts.

Two design commitments worth naming: it runs entirely on the researcher's own machine, nothing hosted; and it never writes to the source material. It reads a snapshot, keeps all app state in its own database, and hands changes back as text you paste yourself.

## Where it connects

This is the layer underneath the tooling. If mental operations can be identified reliably, then a system that watches a work session can say something useful about _where_ someone is stuck rather than only that they are — which is what the assistive side of the work needs in order to be more than a faster autocomplete.

## Two evidence channels under one name

The animations above answer the index question in the register of a coding study: a recorded session, three coders, a consensus track, an agreement figure that is deliberately not flattering. The same project answers it in a second register, that of a population study: thirteen million submissions to two online judges, no transcripts, no verbalisation, and a research question about what survives when the rich record is thrown away.

That is not a contradiction. It is the design. The two channels are put against each other on purpose, and the bridge between them is a third question: which components of the framework survive reduction from a rich record to a submission archive. Most of the vocabulary below means something slightly different in each channel, so both are kept in view.

## The codebook, and why it has twenty codes

The seven operations named above are the informal statement of the question. The codebook is the answer, and its first act is to separate them. Twelve object-level codes carry the work on the problem: represent, recognize or retrieve, relate or analogize, decompose or compose, design or derive, translate or implement, predict or simulate, test or probe, diagnose or localize, repair, verify or explain, reuse or abstract. Eight regulatory codes sit above them.

Six of the seven land in the object-level set. One does not. Planning is a regulatory code by construction, above the object-level work rather than mixed with it, so the informal list of seven crosses the exact boundary the codebook exists to draw. Anywhere the two appear together, say which one is being used.

The construction principle is stated plainly in the design: no validated universal taxonomy spans algorithm design, program comprehension, debugging, implementation, and self-regulation. So the codebook is hybrid and hierarchical, with general theory supplying the parents and programming studies the domain-specific children, and parent labels are retained only when independent coders can distinguish them at the selected temporal grain.

Every code carries positive evidence cues and one explicit exclusion, and the exclusion is the part that does the work. Reading is not Represent without evidence of a constructed representation. Keystrokes are not Translate, because they do not reveal what plan is being implemented. Judge acceptance is not Verify. If the evidence you have only clears the exclusion, the label is not supported.

## Two failure modes usually reported as one number

Segmentation is the assignment of boundaries. Coding is the assignment of labels to what segmentation produced. Two coders can agree completely on the vocabulary and disagree completely on where a stretch begins, and if the instrument forces the two together the two error sources cannot be told apart afterwards.

Labels overlap by design here, which makes this sharper than usual. Recognising that a test falsifies an approach and then replacing the algorithm spans monitoring, replanning, diagnosis, design and implementation at nested spans, so a segment is not a partition. Macro spans hold strategy cycles, meso spans hold one operation, and micro cues are the verbal, behavioural or artifact evidence underneath.

Agreement is reported by two figures for the same reason. Percent agreement counts matches; Cohen's kappa discounts the matches chance would produce, so a scheme with one dominant label can post high agreement and near-zero kappa. If one label is carrying most of the segments, quote kappa, and quote percent agreement only next to it.

## Evidence strength, graded before agreement is computed

Three coders can agree perfectly on a label whose evidence is weak, and in the reduced channel that is the common case. So support for a single label is graded on its own scale, separately from coder agreement.

<table><thead><tr><th width="150">Grade</th><th>What it rests on</th></tr></thead><tbody><tr><td><strong>A, direct</strong></td><td>Concurrent verbalisation names the operation and is aligned in time with the behaviour</td></tr><tr><td><strong>B, triangulated</strong></td><td>Behaviour, an artifact or test change, and the outcome jointly support it</td></tr><tr><td><strong>C, inferential</strong></td><td>The trace is consistent with the operation and permits plausible alternatives</td></tr><tr><td><strong>D, unsupported</strong></td><td>The label rests only on a verdict, a delay, or static code</td></tr></tbody></table>

Strip the verbalisation from the record and re-read the segment. If the label still follows, it was not A. Strong claims about operations require A or B, and the reduced channel will often support only C. The rule is that it carries that uncertainty rather than rounding it up.

The validation cycle around all of this is written out in advance: open coding on a diverse pilot sample, merge the labels coders cannot distinguish, add sublabels only when they have distinctive evidence cues, then test the revised codebook on held-out episodes and tasks. Reporting includes per-label prevalence and reliability, agreement before and after merging, cross-task stability, negative cases, and a version history. Sublabels enter primary analysis only after the parent labels are reliable. The output is meant to be a validated working ontology of recoverable programming operations, not an exhaustive inventory of cognition.

## What the reduced channel is, and is not

The population the empirical claims cover is narrow and is stated as narrow: timestamped submissions made by one anonymised user to one judged task, in closed online-judge programming episodes from two archives. It is narrower than programming, than software engineering, than computer-science learning, and than computer-science problem solving in general. This page is named General CS Problem-Solving and the study is not general. The generality is the ambition; the population is the claim.

The non-claims are enumerated rather than implied. The study does not treat submissions, verdicts, time gaps, or syntax-tree changes as mental operations. It does not claim accepted programs are unique, optimal, or proof-correct. It does not infer expertise or learning from anonymised identifiers. It does not treat verbal reports as infallible cognition. It does not generalise to professional, collaborative, open-ended, or non-programming work.

The archive holds 13,916,868 submissions, 7,460,588 accepted artifacts, 4,053 problems and 55 languages, over 6,764,563 user and problem trajectories. 2,532,957 of those trajectories, 37.44%, hold more than one submission, and 2,328,506, 34.42%, hold more than one in a single language. That is adequate for population-scale revision analysis and not for unqualified claims about mental content. The dataset was not designed or validated as a representation of cognitive process, and I say so about my own primary source.

_**Reduction**_ is the operation that takes a rich record, with editor events, keystrokes, outcomes and think-aloud, and returns what a submission archive would have kept. It is not sampling, which keeps fewer records of the same kind. Reduction keeps every record and removes channels from each, which is a different loss and it falls unevenly across the codebook. The comparison is designed blind: code the rich record, code the reduced record without seeing the first, then compare, with the reporting categories fixed in advance as supported, ambiguous, and unidentified. No channel is treated as ground truth, including the think-aloud.

One thing the dataset does not supply is a **concept layer**. Its rating, tags and complexity fields are empty or unused, so the concept backbone is built from curricula and algorithm sources, versioned, double-annotated, annotated for task relevance, with typed relations between concepts and activation recorded per episode. Accepted artifacts are never substituted for mental solution paths, and program graphs count as structural evidence rather than as prerequisites. Three of the five primary empirical claims are reproducible from the dataset alone. The concept graph is not one of them.

## Inside the instrument

A **question card** is one question parsed from the source document and carried as a node. Structural edges run parent to child and record decomposition. Origin edges, drawn dashed, record which question spawned which. Would removing the parent make the child unanswerable, or merely unmotivated? The first is structural, the second is origin. The timeline view lays the cards out in the topological order of the origin edges, which is not the order they were written in, and the difference between those two orders is itself readable.

The **hinge** is the step in a solve that the rest of the solve turned on. Not the longest step, and not the step where the solver was most stuck. It is computed from graph structure rather than from duration or affect, using eleven scores over blocking, decisiveness, relevance and their combinations, and the highest-scoring card is shaded. The graph-theoretic version of the test is to remove the step and ask whether the goal question is still reachable, which is why criticality in the framework is defined as value of information on the dependency graph rather than as a property of the step itself. The claim is a claim about method: which subproblem was the hinge becomes visible rather than argued.

Two neighbours are worth naming so the work is not mistaken for them. **Process mining** discovers process structure from timestamped event logs, and discovered sequences carry no intrinsic cognitive interpretation, so process discovery is a baseline the construct account has to beat rather than the account itself. **Learning analytics** predicts learning or performance from submissions, errors, test results and educational records, and predicting whether someone will succeed does not identify the questions, hypotheses, or operations that organise one episode.

One word is used in both channels for two objects and should be disambiguated on sight. A snapshot in the instrument is the single read of the source material Astrolabe takes on first load. A snapshot in the reduced channel is the submitted source of one submission.

## What is still open

The list of seven operations is a sentence, not a scheme, and the codebook that turns it into one has not yet been through the pilot that merges its confusable labels. Until it has, the twenty codes are candidates and their count will change.

The two channels have not been joined. The reduction question is written, the reporting categories are fixed, and the blinded comparison is designed, but the rich record it needs is the recorded, coded sessions above, and the population it needs is the submission archive. Nothing yet runs both ends.

The mapping between the instrument's two edge kinds, structural and origin, and the framework's four relation types is not written down anywhere. That is a small gap and it becomes a large one the moment a coded session is exported into the hypergraph and the edge labels have to be chosen.

The order of work is fixed by the dependency this page ends on, and I hold to it. An intervention enters the study only if the validation identifies an assistance target that recurs, is recoverable, and matters. Nothing is built until then.

[**Download the full lexicon (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/project-lexicons/mwm_general_cs.pdf)

## Publications

_In preparation. Astrolabe, the annotation instrument this work runs on, is described under_ [_Artifacts_](../../../../artifacts/astrolabe/)_._

## Collaborators

<table><thead><tr><th width="150"></th></tr></thead><tbody><tr><td><img src="../../../../.gitbook/assets/collab-anantaa-kotal.png" alt="Anantaa Kotal" width="48"><br><a href="https://anantaakotal.github.io/"><strong>Anantaa Kotal</strong></a><br>University of Texas at El Paso</td></tr></tbody></table>

_Last updated: 2026-08_
