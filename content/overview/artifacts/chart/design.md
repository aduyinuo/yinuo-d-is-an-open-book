# Design

## Two layers over a recorder

The inner layer is **taskwork interdependence** — a directed acyclic graph over teammates, human and AI, whose typed edges say who must coordinate with whom, under what condition, in what order. The outer layer is **teamwork modalities** — the interfaces through which that coordination actually happens. Underneath both, a data-collection layer time-stamps every step.

Because the structure is a DAG, it can be walked and queried rather than only read. Authority becomes a property of the graph: an action on a control edge can be approved only by the teammate on the other end of that edge, no matter how sensible it looks to anyone else.

## Five dependency types

Each edge type is a coordination pattern from real security operations, with its own configurable inputs:

**Control** — an action needs authorization before it fires. Configurable with escalation chains, risk-tier gating, and a timeout that auto-approves or auto-denies.

**Pool** — contributions must reach a threshold before a composite action triggers. Configurable with contribution weights, sliding windows, k-of-n quorum, and reset policy.

**Synchrony** — designated actions must occur in the same window. Configurable with a tolerance window and precedence against other dependencies.

**Temporal** — strict ordering, e.g. forensics before containment. Configurable with validity windows, evidence requirements, and bypass exceptions.

**Informational** — what one agent may see of another's observations. Configurable with redaction level, time-gated access, and clearance conditions.

## The modalities

**Pre-task configuration** — a lobby where teams assemble, roles are assigned, the AI's capability profile is chosen, and the graph is previewed. Who sets the structure — experimenter or participant — is itself a manipulation.

**Approval** — actions on `#control` edges enter a supervisor's queue to grant, deny, or query. Which actions require approval and how long the escalation waits are both variables.

**Explanation** — a rationale panel with summary and detail; humans can edit it as a decision tree to steer the agent, not just interrogate it.

**Communication** — public channel, private messages, mentions, with visibility and length manipulable and misinformation injectable for robustness tests.

## The trace

Data is organized on the Input–Process–Outcome cycle, and the value is in the linking. A single sequence — propose isolation, open the explanation, ask a clarifying question, modify to quarantine, approve, check that scanning already happened — arrives as one connected object. That supports causal questions flat logs cannot: whether consulting an explanation improves approval quality, whether trust calibrates differently under synchrony than under control. The same traces double as RLHF preference data — approvals mark acceptable behaviour, denials mark boundaries, modifications mark the preferred alternative.

_Last updated: 2026-08_
