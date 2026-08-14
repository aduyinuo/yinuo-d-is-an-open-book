# Use

Daedalus has two modes that share an interface: train in simulation, evaluate on the deployment. The workflow moves a policy from the cheap side to the honest side.

## Train in simulation

The simulator implements the same `(node, action)` interface as the live network, so training is ordinary reinforcement learning against a fast environment. The LSTM policy learns *where* to place deception and *when*, across far more episodes than a live network could afford.

```bash
cd CyberDreamer
python -m training.train --episodes 10
python -m training.evaluate_baseline
```

## Bring up the live network

Each host runs the C2 client; the C2 server is started with the set of vulnerabilities that host should expose, so the same machine image can present different attack surfaces per experiment.

```bash
# on each host, expose a chosen vulnerability set
python c2_server.py ssh sudo data
```

The server enumerates its non-loopback address, registers the host as a client, and stands ready to toggle Cowrie, the SUID fake edge, and the fake-data bait on command.

## Evaluate on the deployment

Point the trained policy at the live backend and let it defend a real engagement. The agent issues deception actions through the C2 server; the scripted attacker runs its WordPress-to-SSH-to-pivot intrusion; the observation layer feeds the agent the attacker's perceived state as it shifts.

What you read off the evaluation is not only whether the defence held, but *where the simulation lied* — the actions that worked in the simulator and failed against the real service stack are the fidelity gap made concrete, which is the point of running on real infrastructure at all.

## A note on scope

This is research infrastructure for studying deception policies, run against a scripted attacker on infrastructure you provision and control. It is not a tool for operating against systems you do not own.

_Last updated: 2026-08_
