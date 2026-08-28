---
icon: diaspora
---

# CHART

Most teams describe how they work together and then hope. CHART writes it down as a graph and makes the software enforce it.

<figure><img src="../../../.gitbook/assets/chart-interaction.gif" alt="A CHART session: the dependency graph, an approval routed along the control edge, an agent-generated explanation, and a routed chat message"><figcaption><p>One session. The structure is not a description — it decides what can happen.</p></figcaption></figure>

CHART is a **Configurable Human-AI Research Testbed**. Existing platforms fix the team: CybORG and the CAGE challenges put the human outside the loop as an evaluator; the Team Defense Game brought the human in, but with one fixed coordination pattern. That makes it hard to ask the question that actually matters — whether a result about trust or workload survives a change in how the team is organised. CHART makes the structure of teamwork the independent variable.

## Two layers and a recorder

The inner layer is **taskwork interdependence**: a directed acyclic graph over teammates, human and AI, whose edges say who must coordinate with whom, under what condition, in what order.

The outer layer is **teamwork modalities**: the interaction mechanisms through which that coordination actually happens — pre-task configuration, approval workflows, explanation panels, chat.

Underneath both sits **data collection**, instrumenting every step with time-stamped traces. Together they support controlled structure × interaction experiments with reproducible comparisons on quality, time, error and human load.

## Five dependency types

Nodes are agents and pools; edges are typed. Each type is a coordination pattern that shows up in real security operations.

**Control** — an action requires authorization from another agent before it executes. Approval chains and escalation protocols: shutting down a production server, deploying a honeypot. Configurable with escalation chains, risk-tier gating, and a timeout policy that either auto-approves or auto-denies.

**Pool** — contributions must reach a threshold before a composite action fires. Isolating an enterprise-wide subnet takes concurrence from two of three analysts. Configurable with contribution weights, sliding windows, k-of-n quorum, and reset policy.

**Synchrony** — designated actions must occur in the same turn or window to take effect. Coordinated shutdowns to cut off lateral movement. Configurable with a tolerance window and precedence rules against other dependencies.

**Temporal** — strict ordering. Forensic analysis before containment, so evidence survives; scanning before remediation. Configurable with validity windows, evidence requirements, and exception roles allowed to bypass.

**Informational** — what one agent may see of another's observations. A junior analyst gets filtered alert logs; a senior responder integrates across sources. Configurable with redaction level, time-gated access, clearance conditions and event-triggered reveals.

The contribution is not the graph formalism. It's using the graph to vary authority distribution, information flow and sequencing across experiments, and then reading the effect on resilience, trust and performance.

## The modalities

**Pre-task configuration.** A lobby where teams assemble, roles are assigned, the AI teammate's capability profile is chosen, and the dependency graph is previewed before anyone starts. Either the experimenter sets it, or the participants do — which itself becomes a manipulation: how people react to an imposed structure versus one they wrote.

**Approval.** Actions on `#control` edges enter a queue visible to their supervisor, who can grant, deny, or ask for an explanation. Vary which actions need approval, vary the escalation delay, and the trade-off becomes measurable: auto-approve for throughput, abort for safety. The point is to externalize the authority mechanism — agents do not reliably self-regulate, and humans should not have to improvise oversight mid-incident.

**Explanation.** When the agent proposes an action, the panel shows a rationale: a short summary, a detailed view with links to the evidence. Humans can edit it as a decision tree or flowchart, adding and removing nodes, which steers the agent rather than just interrogating it. Consultation patterns are logged — how often, at what depth, and whether looking changed the approval.

**Communication.** Public channel, private messages, @-mentions. The agent posts status and asks clarifying questions; the system posts key events automatically. Researchers can restrict visibility to simulate compartmentalization, cap message length, or inject misinformation to test what a structural safeguard does against a lying channel. Conversation becomes an empirical variable rather than an uncontrolled one.

## What the traces are for

Data is organized along the Input-Process-Outcome cycle. Inputs: session setup, AI selection, graph configuration. Processes: approvals, explanation consultations, chat, execution under dependency checks. Outcomes: mission results, trust and workload signals, and behaviour that feeds forward into the next mission.

The value is in the linking, not the individual streams. A single sequence — agent proposes isolation, human opens the explanation, asks a clarifying question in chat, modifies the proposal to quarantine instead, approves the revision, system checks that scanning already happened — arrives as one connected object. That supports questions isolated logs cannot answer: whether consulting an explanation improves approval quality, whether chat clarification reduces modification rates, whether trust calibrates differently under synchrony than under control.

The same traces double as training data. Approvals mark acceptable behaviour, denials mark boundaries, modifications identify the preferred alternative — structured preference data for RLHF. Explanation edits reveal how people structure causal reasoning. Configuration traces encode the authority boundaries an agent should be trained never to violate.

Scientific transparency comes first: reproducible, auditable logs, with learning layered on top as an optional consumer of the same data.

## Beyond cyber

Cybersecurity is the motivating case — tiered authority, compartmentalized access, decisions on a timescale where hesitation costs. But the design principles carry to any high-stakes interdependent domain: emergency response, healthcare, autonomous vehicle coordination.

## Four sources, four emphases

CHART is written down in four places and each one carries something the others do not. A description that quotes only one of them will be missing something the others hold.

**This page** carries the five dependency types and the four modalities in full, and the sentence that fixes the scope: the contribution is not the graph formalism, it is using the graph to vary authority distribution, information flow and sequencing across experiments.

**The [artifact pages](../../../artifacts/chart/)** carry the software. Two sentences appear nowhere else. Because the structure is a directed acyclic graph it can be walked and queried rather than only read, and authority becomes a property of the graph, so an action on a control edge can be approved only by the teammate on the other end of it however sensible it looks to anyone else.

**The book chapter** carries the argument and the parameters. Its dependency table is the only place the required and optional inputs of each type are written down, and its data-stream table is the only place the streams are set against their research and their training uses. It also gives the reason each modality exists, stated as a gap in what agents can do for themselves: agents that cannot request permission, agents that defer on everything, agents that produce fluent rationales that are not faithful, agents that cannot track mention targets in a multi-party conversation.

**The code** carries what is actually built.

## Where the four sources disagree

_**The graph is called acyclic and one edge type makes a cycle.**_ This page, the artifact design page and the chapter all say directed acyclic graph, and the design page rests an argument on it. The synchrony call adds two edges, one in each direction, with the same sync group, and the container permits multiple edges and does not enforce acyclicity in the first place. This is not a bug in the running system, because synchrony is checked symmetrically by design. It is a naming problem with a consequence: any analysis assuming a topological order over the whole graph is unsound on a session that used synchrony. Either the acyclicity claim is scoped to the constraining edge types, control and temporal and pool, or the synchrony pair is represented as one undirected edge and the walk skips it.

_**Five types on the page, seven in the implementation.**_ The code defines a sixth, a temporal-informational edge carrying a turn count and a list of dependent observations, which models delayed information sharing: what a teammate may see, but not yet. The API specification lists a seventh, a trigger edge from a pool node out to the environment carrying an approval requirement for the composite action, which is what lets a control constraint sit on a collective action rather than on an individual one. Both are compositions rather than new primitives, which is a defensible reason to keep the taxonomy at five. It is not a reason to leave them undocumented. A delayed reveal and an approval on a composite action are the two configurations a security operations centre would ask for first, and neither is reachable from this page.

## What the next version has to answer

CHART so far captures the syntax of human-agent teamwork, and whether that syntax is complete or succinct has not been tested. Three questions follow, ordered by how much they cost.

_**Complete.**_ Can the graph express how a security operations centre or an incident response team actually works? Answerable now, and cheaply, by taking one written incident response procedure and attempting to encode it. Every constraint that will not go into an edge is either a missing type or evidence that five is enough. That test is the [SOC Game](soc-game.md).

_**Prescriptive.**_ Can teamwork written in CHART be prescribed and enforced as well as recorded? The control, temporal and pool edges already enforce. The gap is that a team's own intended protocol is not currently expressible as anything the system checks it against, so there is no notion of the team deviating from its own plan.

_**Diagnosable.**_ Can a session be monitored while it runs and diagnosed afterwards, so a structural fault surfaces while it is still correctable? This is the one with a design problem inside it. A monitor that watches the graph during a mission is an authority in the session, and nothing in the architecture says who it reports to.

Succinctness is the fourth and nobody has asked it yet. Two graphs can enforce identical constraints and differ in how many edges they take, and if the count moves with the encoding rather than with the team, then edge count is not a measure of coordination demand and no result should be read as if it were.

The vocabulary, tier by tier, with what each term is not and how to tell: [**download the CHART lexicon (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/project-lexicons/hac_chart.pdf)

## Publications

<table><thead><tr><th width="100"></th><th width="400">Paper</th><th>Authors</th></tr></thead><tbody><tr><td><img src="../../../.gitbook/assets/badge-book.png" alt="Book" data-size="original"></td><td><mark style="color:green;">CHART: A Configurable Testbed for Human-AI Teaming Research in Cybersecurity Operations</mark><br><em>Advancements in Human Agent Teaming Research Infrastructure: Testbeds, Metrics, and Concepts. CRC Press, Taylor &#x26; Francis.</em></td><td><strong>Y. Du</strong>, V. Miloserdov, M. J. Ferreira, B. Prébot, T. Malloy, C. Gonzalez</td></tr><tr><td><img src="../../../.gitbook/assets/badge-chb.png" alt="CHB: AI" data-size="original"></td><td><mark style="color:green;">Experimental evaluation of cognitive agents for collaboration in human-autonomy cyber defense teams</mark><br><em>Computers in Human Behavior: Artificial Humans, 4, 100148</em></td><td><strong>Y. Du</strong>, B. Prébot, T. Malloy, F. Fang, C. Gonzalez</td></tr></tbody></table>

## Collaborators

<table><thead><tr><th width="150"></th><th width="150"></th><th width="150"></th><th width="150"></th><th width="150"></th></tr></thead><tbody><tr><td><p><img src="../../../.gitbook/assets/collab-volodymyr-vlad-miloserdov.png" alt="Volodymyr (Vlad) Miloserdov" data-size="original"></p><p><br><a href="https://www.linkedin.com/in/vladmiloserdov/"><strong>Volodymyr (Vlad) Miloserdov</strong></a><br>Carnegie Mellon University</p></td><td><p><img src="../../../.gitbook/assets/collab-maria-jose-ferreira.png" alt="Maria José Ferreira" data-size="original"></p><p><br><a href="https://www.cmu.edu/dietrich/sds/people/post-docs/maria-jose-rodrigues-ferreira.html"><strong>Maria José Ferreira</strong></a><br>Carnegie Mellon University</p></td><td><p><img src="../../../.gitbook/assets/collab-baptiste-prebot.png" alt="Baptiste Prébot" data-size="original"></p><p><br><a href="https://sites.google.com/view/baptisteprebot"><strong>Baptiste Prébot</strong></a><br>Carnegie Mellon University</p></td><td><p><img src="../../../.gitbook/assets/collab-tyler-malloy.png" alt="Tyler Malloy" data-size="original"></p><p><br><a href="https://scholar.google.com/citations?user=jktsx4EAAAAJ"><strong>Tyler Malloy</strong></a><br>University of Luxembourg</p></td><td><p><img src="../../../.gitbook/assets/collab-cleotilde-gonzalez.png" alt="Cleotilde Gonzalez" data-size="original"></p><p><br><a href="https://www.cmu.edu/dietrich/sds/ddmlab/cotyweb/"><strong>Cleotilde Gonzalez</strong></a><br>Carnegie Mellon University</p></td></tr></tbody></table>

## Acknowledgements

_This project is supported by_ [_URI_](../../../funding.md)_._&#x20;

_Last updated: 2026-08_
