# Cyber Wheel

**A configurable RL environment where the defender's main move is deception.**

Cyberwheel is a reinforcement learning simulation environment for training and evaluating autonomous cyber defence models, built for modularity. Networks, services, host types, and both offensive and defensive agents are specified through configuration files, and the reward function, observation space, and action space can be redefined without rewriting the environment.

The blue agent's characteristic action is deploying decoys — the aim is to get the red agent to spend its attack on a decoy server rather than a real one. Recent versions support training red and blue agents simultaneously, each learning against the other.

For transfer work it makes a good **source** environment: a competent policy arrives under a modest training budget, its kill-chain observation is compact with a high proportion of decision-relevant features, and hosts and subnets are fully configurable through YAML.

_Last updated: 2026-08_
