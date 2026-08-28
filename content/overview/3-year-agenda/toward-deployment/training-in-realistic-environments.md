---
icon: dumbbell
---

# Training in "Realistic" Environments

If transfer from a simulator is where the fidelity is lost, train where the fidelity is.

<figure><img src="../../../.gitbook/assets/training-in-realistic.gif" alt="Two backends behind one action and observation interface: a cheap simulator and a live emulated deployment, with sample efficiency deciding which is reachable"><figcaption><p>Same interface, two costs per step. Which box is reachable is a question about sample efficiency.</p></figcaption></figure>

## What the field usually does, and what it costs

Most autonomous cyber defense trains in a simulator and transfers the resulting policy. Simulators omit authentication delays, partial action failures, service dependencies, and realistic user traffic. Simulator-trained policies succeed only 66% of the time on the matching emulator, and realistic training environments and sim-to-real transfer remain the field's two principal open problems.

[FOE-Dreamer](../cyber-world-modeling/environment.md) takes the other route: it trains the defender directly in an emulated operational network, with no simulator stage. The architecture that makes that possible is on its own page; what this page is about is whether the route pays, and what "realistic" is doing in the sentence.

## The environment it trains in

[Daedalus](../../../artifacts/daedalus/) is an eight-host OpenStack network across three subnets — two public web servers, a workstation tier, and an NTP and database tier — provisioned with real services, so its behaviour is executed rather than modelled.

A gRPC command-and-control server carries each defender action to the host it names, enabling or disabling an actual service on an actual operating system. The attacker is a scripted red agent that executes a genuine web exploit, establishes persistence over SSH, and pivots toward the interior hosts, so a defender is measured against real tool execution. Background user activity is generated rather than assumed away.

Two backends sit behind one action and observation interface: a fast simulator for the millions of steps reinforcement learning requires, and the live emulated deployment for evaluation. A policy can be trained cheaply and tested honestly — and the difference between the two is itself a measurement of what the simulator abstracted away.

## The experiment

Against both scripted attacker profiles, FOE-Dreamer roughly halves episode loss relative to Rainbow and IQN under matched compute, and trains inside a three-day budget on one GPU.

Ablations show the factoring and the opponent model each contribute — the result is not one of them carrying the other.

The number that matters for this page is the budget, not the loss. Three days on one GPU is what makes training in an emulated network a real option rather than a thought experiment. Every step there costs seconds of wall-clock and a real state change on a real host, so what limits the result is sample efficiency, not asymptotic performance.

## What "realistic" is doing in that sentence

Narrowly, and deliberately so. The substrate, the services, the exploit paths, the five-second polling and the consequences of defender actions are real. The user and attacker populations and the CVE catalogue are emulated.

That distinction is the whole point of the quotation marks in the title. An environment is not realistic or unrealistic; it is realistic in some respects and not others, and which respects it got right is what decides whether a result transfers. Deciding that per claim rather than per environment is what [When We Say "A Realistic Cyber Environment"](when-we-say-a-realistic-cyber-environment.md) is for, and [Sim2Sim before Sim2Real](transfer-to-realistic-environments.md) is how the gap gets measured without an operational network to measure against.

## What the defender's actions actually are

The defender on this testbed has no removals and no repairs. Every action stands something up, and the target of the action is the attacker's belief rather than the attacker's access.

_**Deception policy.**_ A defender whose action space contains only placements: a decoy service, a false privilege path, planted data. Not containment or remediation, whose actions are isolate, patch, restore, and which change the network. A deception action changes what the network appears to be, and leaves the real access it is hiding intact. The test: after the action fires, is the attacker's actual position different? If only the attacker's picture of it changed, the action was deception.

_**Fake node.**_ A honeypot deployed on a real host, presenting a service the attacker can reach and interact with, and which exists to be reached. Not a decoy host in a simulator, which is a flag in a state vector with no service behind it.

_**Fake edge.**_ A permission bit placed so that the host appears to offer a privilege-escalation path it does not really offer. The word edge is the graph term: the defender is adding an edge to the attack graph the attacker believes it is on. A fake node adds a vertex; this adds a transition between two hosts or two privilege levels the attacker already knows about, which is a cheaper lie and a more specific one.

_**Bait data.**_ Planted data on a real host, placed so that an attacker looking for something worth taking finds it and takes it. The other two alter the attacker's route. This one alters the attacker's objective, and it is the only one of the three that pays off after the attacker has already succeeded at something.

_**Do nothing.**_ The fourth action, and a deliberate one. Every placement costs something, and a defender that must place on every step is not being asked the question the environment is built to ask. It is not an action mask: the policy may take this action when others are legal, so choosing it is a decision and gets scored as one. The policy learns where to place deception and when, and this action is the entire when.

Two fields per host carry the lie. **Manipulated value** is the value of a host as the defender has arranged for it to appear, held separately from the value it really has, so the environment can score a lie as a lie rather than as a change to the network. **Perceived state** is the attacker's model of a node, carried as environment state. The defender does not observe the attacker's reasoning. It observes the standing result of that reasoning, per node, and acts on it. The gap between perceived state and node state is the defender's product, and a deception policy that never opens a gap has done nothing whatever its score says.

## The interface, and what sits in the transition function's chair

The agent never touches a host directly. Each host is a client, and a command-and-control server holds the connections and decides which host a given action applies to. That server occupies the position a transition function occupies in a simulator: it receives an action, resolves it to a machine, and performs it there, and what comes back is what the machine did. A step function computes the consequence of an action from a model of the world. This one causes the consequence and then reports it, which means it can be wrong about nothing and can also fail.

An action is a node index and a defensive action, so the policy chooses a placement and a target in one emission rather than selecting from a flat list of host-action combinations. The factoring is what lets the same policy shape run against a network of a different size, and the simulator backend implements the same pair, which is what makes the two backends interchangeable at all.

The live deployment is the honest end. Slow, expensive, and real. It is not a validation set, which is a held-out sample of the same distribution; it is a different implementation of the same interface, and what it is held out from is the modelling itself. Does a step cost wall-clock seconds and change a running machine? That is the honest end, and the number of steps available there is the budget the whole project is written against.

What evaluation reads off that arrangement is not only whether the defence held. It is the per-action disagreement between the two backends: the list of actions whose outcome differs, which names the omission rather than sizing it. Can you name the action and the service it failed against? If the answer is a percentage, the gap has been sized and not made concrete.

## The two lists, given in full

Five items real: the substrate, the services, the exploit paths, the five-second polling, and the consequences of defender actions. Three emulated: the user population, the attacker population, and the vulnerability catalogue. Nothing is left to inference, and every claim the project makes has to survive being read against them. For any component, ask whether replacing the emulation with the real thing would change the defender's observation stream. If yes, it belongs on the real list and is not there yet.

Two more choices are stated rather than implied. **Depth over breadth**: eight hosts each carrying real services, real exploit code paths and real consequences, rather than a larger topology of thinner hosts. Scale-first testbeds buy host count with per-host fidelity, and neither is a shortfall of the other. They are answering different claims, which is the [Metrion](when-we-say-a-realistic-cyber-environment.md) point applied to this project's own design. And **the scripted red agent** is scripted in its decision rule and real in its execution: the exploit, the key generation, the pivot inward are performed against the running hosts. Split the attacker in two. Is the choice of next action computed, and is the action itself executed? Scripted choice with real execution is this.

## Why the budget is the number

The loss result establishes that the method works. The budget result establishes that the route is available to anyone, and only the second is what this page argues. Would the argument survive a smaller improvement in loss? Yes. Would it survive a thirty-day budget? No. That asymmetry is what the sentence about the budget is naming.

Three days on one GPU is wall-clock spent waiting for a network to change state, and a bigger machine does not recover it. Divide the budget by the per-step wall-clock and see how many real transitions the run could have contained. If the answer is small relative to what the algorithm class normally consumes, sample efficiency is carrying the result. That is also why the ablations matter: the two components have to be shown to contribute inside that budget rather than asymptotically.

The vocabulary, tier by tier, with what each term is not and how to tell: [**download the lexicon for this route (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/project-lexicons/td_training_in_realistic_environments.pdf)

## Publications

<table><thead><tr><th width="100"></th><th width="400">Paper</th><th>Authors</th><th></th></tr></thead><tbody><tr><td><img src="../../../.gitbook/assets/badge-preprint.png" alt="Preprint" data-size="original"></td><td><mark style="color:green;">FOE-Dreamer: Deployment-Efficient Learning of Cyber Defense Policies in Operational Networks</mark></td><td><strong>Y. Du</strong>, <a href="https://www.cs.utep.edu/kiekintveld/">C. Kiekintveld</a></td><td>Under review, ACSAC</td></tr></tbody></table>

## Collaborators

<table><thead><tr><th width="150"></th></tr></thead><tbody><tr><td><img src="../../../.gitbook/assets/collab-christopher-kiekintveld.png" alt="Christopher Kiekintveld" width="48"><br><a href="https://www.cs.utep.edu/kiekintveld/"><strong>Christopher Kiekintveld</strong></a><br>University of Texas at El Paso</td></tr></tbody></table>

_Last updated: 2026-08_
