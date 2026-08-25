---
icon: display-code
---

# Daedalus

A reinforcement-learning defender whose actions are *deception* — and whose environment is a real cloud network rather than a model of one.

<figure><img src="../../.gitbook/assets/mock-daedalus.png" alt="Daedalus: an RL blue agent choosing a deception action, passed through a gRPC C2 server to an eight-host AWS network, against a scripted attacker"><figcaption>The agent decides where to place deception; the C2 server makes it real on the host; the attacker walks into it.</figcaption></figure>

## The idea

Most autonomous-defence work happens in a simulator, and the results are only as trustworthy as the simulator's fidelity. Daedalus runs the defender against provisioned AWS infrastructure with real services, so the deception it deploys is a real honeypot on a real host rather than a flag in a state vector.

The defender's move is not "block" or "patch." It is to shape what the attacker *believes*: stand up a decoy service, fake a privilege-escalation path, plant bait data — and get the attacker to spend its next move on something that isn't real, while revealing itself in the process.

## The pieces

**The network.** Eight hosts across three subnets — two public web servers, a WEB tier of workstations, and an NTP/DB tier — each addressable, each with a value the attacker is trying to reach.

**The defensive actions.** Deploy a Cowrie honeypot (a fake node), deploy a SUID fake edge (a fake privilege path), plant fake data, or do nothing. Each is a real service the C2 server toggles on a real host.

**The attacker.** A scripted red agent that runs an actual WordPress exploit, escalates over SSH, and pivots inward — so the defender is measured against genuine tool execution, not a scripted abstraction of it.

**Two backends, one interface.** A fast simulator for the millions of steps reinforcement learning needs, and the live AWS deployment for evaluation — behind the same action and observation interface, so a policy trained cheaply can be tested honestly.

## More

* [Design](design.md) — the C2 architecture, the action and observation model
* [Use](use.md) — training in simulation, evaluating on the deployment

_Last updated: 2026-08_
