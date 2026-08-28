---
icon: tty-answer
---

# CyberAgentFlow

Most evaluations of agentic cyber tools ask whether the task got done. That tells you almost nothing about how it got done, or what it cost.

<figure><img src="../../../.gitbook/assets/cyberagenttrace.gif" alt="A pivoting engagement recorded phase by phase, with observed time against time without the waste"><figcaption><p>One pivoting engagement, instrumented. The gap on the right is the finding.</p></figcaption></figure>

## What gets recorded

Cyber-Agent-Flow instruments the whole interaction lifecycle of an agent-driven engagement: prompts, model responses, tool invocations, command outputs, analyst annotations, and timing. Sessions are archived as structured execution traces, and an analysis model inspects them afterwards for inefficiency.

The stack runs locally. Tools are exposed through Model Context Protocol interfaces — Kali utilities like nmap and Metasploit behind an MCP server — with the language model hosted privately through Ollama and a LiteLLM gateway handling routing and access control. That's a deliberate choice: cloud-hosted agents send prompts and network telemetry off-site, which is not acceptable on a real engagement.

The analyst stays in the loop through a web interface: issuing objectives in natural language, watching actions as they happen, annotating throughout, and constraining what the agent may touch through tool permissions and IP allowlists. Long engagements are handled with a context budget that summarises older history while keeping recent exchanges intact.

## What it found

The scenario is a pivot. The agent starts on an externally reachable host, works through reconnaissance and service identification, exploits a vulnerable web server, and uses it to route into an internal server it could not reach directly.

It completed the task. The interesting part is where the time went — exploit selection, exploit attempts, and pivot setup dominated. Reaching the pivot took roughly **50 minutes**. With the identified waste removed, the estimated time is roughly **11 minutes**.

## The failure patterns

Five recurring ones, visible only because the trace existed:

**Redundant tool invocations** — the same reconnaissance command run again with unchanged parameters, when the earlier result was still valid.

**Command-context confusion** — commands written for the system shell issued inside Metasploit, or Meterpreter commands issued outside a session. Sometimes hallucinated outright, sometimes correct for a different tool version.

**Exploit retry loops** — module after module tried with minimal parameter changes, without folding in what the previous failure revealed.

**Environment constraint violations** — commands assuming shell features or permissions the environment doesn't offer.

**Pivot configuration complexity** — routing requires coordinating Meterpreter session commands with Metasploit modules, and the agent struggles to keep straight which command belongs to which.

## Why this matters

The lesson is not that the agent is bad at reasoning. It reached the objective. The lesson is that orchestrating the tools it already has may matter as much as choosing them well — and that you cannot see any of this from a success rate.

_Observations come from a single run. They illustrate common failure modes rather than establishing their frequency._

## What a record has to hold before a failure can be named

_**Execution trace.**_ The stored record of one engagement, in which every prompt, model response, tool invocation, command output, analyst annotation and timestamp is kept in sequence and kept together, so the engagement can be replayed rather than summarised. Three thinner records are derivable from it and none of them can be turned back into it. A transcript keeps what was said and drops what the tools returned. A tool log keeps what the tools returned and drops what the model was reasoning about when it asked. A benchmark result keeps only whether the run ended in success. The test: take any command in the record and ask two questions, what prompt produced it and what its output changed about the next step. If either answer requires guessing, the record is a log.

_**Interaction lifecycle.**_ The span from the objective being issued to the objective being reached or abandoned, treated as one recordable object with six kinds of entry. Lifecycle is the right word because it commits to recording the two things that have no turn boundary: the annotation a person writes after watching something go wrong, and the wall clock that keeps running while the model is deciding. Five of the six kinds come from the machine. One, the annotation, comes from the person watching, and it is the only place a human enters the record at all.

_**Analyst annotation.**_ A note written into the trace by the person supervising the engagement while it runs, entered as a first-class entry with the same standing as a command output. Not a code assigned afterwards by a researcher reading the transcript. The annotation is written by the person who was there, at the moment, with the state of the engagement in front of them, and it lands inside the record rather than beside it.

_**Context budget.**_ The rule governing what an agent carries forward once an engagement outruns the model's window: recent exchanges kept whole, older history compressed. Not a context window, which is a capacity rather than a policy. Two agents on the same model can hold the same window and spend it differently, and only the spending is a design decision. It is also the first suspect for the first of the five failure patterns, because a command re-issued with unchanged parameters is the signature of a result that was summarised away, and that is an architecture fault rather than a reasoning fault.

_**Waste.**_ Entries that consumed wall clock and changed nothing about what the agent knew or what the target was. Not failure. A failed exploit that eliminated a module is not waste, it is information bought at a price. Waste is the second attempt at the module the first attempt already eliminated. The test: delete the entry from the trace and ask whether any later entry becomes unexplainable. This is exactly why the trace has to hold the outputs and not only the calls, since a record of what was invoked cannot tell you whether the answer was already known.

## Why the stack is local, and what that costs

_**Local stack.**_ Every component touching engagement data, which is the model, the gateway, the tool servers and the trace store, runs on hardware the engagement's owner controls. Not a data-handling policy, which is a promise about what a third party does with material it holds. The local stack is the arrangement under which the third party never holds it. List the outbound connections opened during an engagement; if any of them carries a prompt or a command output, the stack is not local.

_**Tool permission and IP allowlist.**_ The two constraints the analyst sets: which tools the agent may invoke at all, and which addresses it may reach with them. Not an approval, which is per-action and arrives after the agent has proposed something. A permission is per-capability and set in advance, and the agent never sees the action it was not allowed to consider. This is the authority mechanism this project has, and it is coarser than [CHART](chart.md)'s on purpose. There is no queue, no denial and no timeout to record, only a boundary the agent is never offered. That is the right design for a live engagement against a real target and the wrong one for studying how a person decides, which is why the two projects do not share an authority vocabulary.

_**The analyst in the loop.**_ Four verbs, and none of them is approve: set the objective, set the boundary, watch, and write into the record. Take the person out of the room mid-engagement. If the agent stops, the person was a gate. If it keeps going within the allowlist, the person was a supervisor.

## The two clocks

The result is not fifty minutes and it is not eleven. It is the gap. The second number is the same commands in the same order with the repetitions and the uninformative retries deleted from the sequence, so nothing in it runs faster than it did. Try to reconstruct it from the trace by deleting entries and nothing else; if it needs an assumption about what a better agent would have done instead, it is a different measure and a weaker one.

That is also the charge against a success rate. Ask what the metric would report about two runs that both succeeded, one in eleven minutes and one in fifty. If the answer is the same number twice, it is a success rate. The complaint is not that the number is wrong. It is that the number is thin, and that the field currently has almost nothing else.

## Where the words disagree

_**Two things called a trace.**_ CHART records the linked Input-Process-Outcome history of a human-AI team session. Its unit is a coordination sequence across several teammates, and a failure in it is attributed to a structure: an approval that routed wrong, an explanation that never arrived. This project records the execution history of one agent driving real tools. Its unit is a prompt, a tool invocation and its output, and a failure in it is attributed to a wasted call. Both are traces under the shared definition. They differ in what the linked entities are, and therefore in what a failure can be attributed to. Any page that has to be precise says team trace or execution trace.

_**Two authority designs, for stated reasons.**_ CHART externalizes the authority mechanism so that approving, denying and the delay before either becomes measurable. This project sets the boundary before the engagement starts and records nothing about it, because a live engagement against a real host is not a place to study a person's approval behaviour. Two projects in one cluster with opposite designs. The vocabulary should keep them apart rather than reconcile them.

_**Complexity of the task against confusion of the agent.**_ Command-context confusion and pivot configuration complexity produce the same symptom. The second has a task-level reason behind it, because routing genuinely requires two contexts driven in alternation. Ask whether the correct sequence can be written down inside a single tool's command set. If it cannot, the difficulty belongs to the configuration and not to the agent.

_**Four spellings, and a fifth scope.**_ The page file is `cyberagenttrace.md`, the heading is CyberAgentFlow, the body writes Cyber-Agent-Flow, and the site navigation writes Cyber AgentFlow. The published abstract adds something that is not a spelling but a scope, presenting the framework as AgentFlow, general to agent-driven workflows, with cybersecurity as the domain it is aimed at. CyberAgentFlow is the project. The paper title is Cyber-Agent-Flow. AgentFlow is the framework without the domain.

The vocabulary, tier by tier, with what each term is not and how to tell: [**download the CyberAgentFlow lexicon (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/project-lexicons/hac_cyber_agentflow.pdf)

## Publications

<table><thead><tr><th width="100"></th><th width="400">Paper</th><th>Authors</th><th></th></tr></thead><tbody><tr><td><img src="../../../.gitbook/assets/badge-aaai.png" alt="AAAI-Summer Symposium" data-size="original"></td><td><mark style="color:green;">Cyber-Agent-Flow: Execution Trace Instrumentation and Analysis for Cybersecurity Agent Workflows</mark><br>Extended abstract, AAAI Symposium Series, 9(1), 337-340</td><td><a href="https://www.utep.edu/cs/people/faculty-websites/jacosta.html">J. Acosta</a>, M. T. B. Nazim, T. Guerra, <strong>Y. Du</strong>, <a href="https://expertise.utep.edu/profiles/paggarwal">P. Aggarwal</a></td><td><a href="https://doi.org/10.1609/aaaiss.v9i1.42950"><img src="../../../.gitbook/assets/badge-paper.png" alt="paper" data-size="original"></a></td></tr></tbody></table>

## Collaborators

<table><thead><tr><th width="150"></th><th width="150"></th><th width="150"></th><th width="150"></th></tr></thead><tbody><tr><td><img src="../../../.gitbook/assets/collab-jaime-acosta.png" alt="Jaime Acosta" width="48"><br><a href="https://www.utep.edu/cs/people/faculty-websites/jacosta.html"><strong>Jaime Acosta</strong></a><br>University of Texas at El Paso / DEVCOM ARL</td><td><img src="../../../.gitbook/assets/collab-mohammad-taneem-bin-nazim.png" alt="Mohammad Taneem Bin Nazim" width="48"><br><a href="https://scholar.google.com/citations?user=v3qB098AAAAJ"><strong>Mohammad Taneem Bin Nazim</strong></a><br>University of Texas at El Paso</td><td><img src="../../../.gitbook/assets/collab-thomas-guerra.png" alt="Thomas Guerra" width="48"><br><strong>Thomas Guerra</strong><br>University of Texas at El Paso</td><td><img src="../../../.gitbook/assets/collab-palvi-aggarwal.png" alt="Palvi Aggarwal" width="48"><br><a href="https://expertise.utep.edu/profiles/paggarwal"><strong>Palvi Aggarwal</strong></a><br>University of Texas at El Paso</td></tr></tbody></table>

_Last updated: 2026-08_
