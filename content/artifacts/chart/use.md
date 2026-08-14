# Use

CHART is used in two roles at once: an experimental platform for controlled behavioural studies, and a structured data generator for adaptive-AI training. The workflow is the same either way — configure a structure, run sessions under it, read the linked trace.

## Configure the team

In the lobby, assemble the teammates, assign roles, and choose each AI teammate's capability profile — how aggressive or cautious it is in raising alerts and taking action. Then draw the dependency graph: pick a starting agent, an ending agent, and the dependency type on the edge between them. The result is a contract the software will enforce and a work plan the participants can preview — which tasks are sequential, which run in parallel, which need approval or synchronization.

Decide who does this configuration. Letting the experimenter fix it studies how people react to an imposed structure; letting participants build it studies how they choose to organize themselves. Both are supported, and the difference is a manipulation.

## Run under the structure

During a mission, the modalities carry the coordination and the instrumentation records it. Actions on control edges wait in an approval queue; the explanation panel logs how often and how deeply humans consult it; the chat logs message content, timing, and targets. The dependency checks fire automatically — a temporal edge blocks containment until forensics completes, a pool edge holds a composite action until the threshold is met.

## Vary one thing at a time

The point of the testbed is controlled comparison. Tighten an authority boundary; shrink a pool; add a synchrony requirement; change which actions require approval; move an escalation timeout from auto-approve to abort. Each is a single, named change to the structure, and the traces let you read its effect on resilience, trust, workload, and outcome.

## Read the results

Every interaction feeds the Input–Process–Outcome record with microsecond timestamps and cross-stream identifiers, so events can be reconstructed even in concurrent multi-agent sessions. Because the streams are linked, you can ask questions isolated logs can't answer — did the explanation consultation improve the approval that followed it, did the chat clarification reduce the modification rate — and export the same traces as preference data for reinforcement learning from human feedback.

Cybersecurity is the motivating case, but the configuration is domain-agnostic: the same dependency types and modalities describe emergency response, healthcare, or autonomous-vehicle coordination.

_Last updated: 2026-08_
