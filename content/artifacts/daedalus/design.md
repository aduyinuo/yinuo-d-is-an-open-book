# Design

## Command-and-control as the environment interface

The agent never touches a host directly. It emits an action as a pair — a node index and a defensive action — and a gRPC command-and-control server carries that action to the machine it names. Each host in the network is a gRPC client; the C2 server holds the connections and decides which host a given action applies to. Deploying a honeypot on the WEB host is action `(2, deploy_honeypot)`; the server resolves index 2 to that machine and enables the real service.

This is what makes the "environment" real. There is no simulated effect model for a honeypot — the server enables Cowrie, or toggles a SUID binary, or swaps in bait data, on an actual operating system. What the attacker then encounters is whatever that system genuinely presents.

## The network

Eight hosts, indexed 0–7, across three subnets: two public web servers, a WEB tier of workstations, and an NTP/DB tier. Each host carries an IP, a value, a *manipulated* value the defender can shift, and per-host deception state — whether a honeypot, a fake edge, or fake data is currently deployed — plus the attacker's *perceived* state of that node, which is the quantity the whole design is trying to bend away from the truth.

## The observation

A translation layer turns the raw network state into the vector the agent reads: per node, its manipulated value, its node state, the three deception flags, and the attacker's perceived state. The agent sees the board as the attacker would, plus what it has done to distort that view — which is exactly the information a deception policy needs and nothing it shouldn't have.

## The attacker

A scripted red agent, compiled to a standalone binary, that performs a real intrusion: exploit a WordPress vulnerability on a public host, generate SSH keys and establish persistence, then pivot toward the valuable interior nodes. Because the attack is genuine tool execution rather than a transition function, a defence that looks good against it is being tested against the thing it will actually face.

## Two backends behind one interface

The simulator reproduces the same action and observation spaces so a policy can be trained across the millions of steps reinforcement learning needs without paying live-infrastructure cost per step. The AWS deployment is the honest end — slow, expensive, and real. A policy is trained in the first and evaluated in the second, and the gap between the two is itself a finding about how much the simulation abstracted away.

_Last updated: 2026-08_
