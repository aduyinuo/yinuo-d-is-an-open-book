---
icon: connectdevelop
---

# Cyber World Modeling

A defender that acts autonomously needs an internal model of the network it protects and of the adversary operating within it. The two change for different reasons. A network's dynamics are relatively stable and follow from its configuration and load. An adversary's behavior is not stable: it responds to the defender, avoids observation, and changes as the defender begins to model it. If a single learned representation does not distinguish these two sources of change, it will misattribute one to the other, treating an adversary's action as ordinary network behavior or an ordinary change in the network as an adversary's action. This thread asks what a defender needs to represent, and how to divide that representation, so that error in the model of the adversary does not degrade the model of the network.

The cybersecurity setting adds two constraints. The observations available to the model are incomplete and partly controlled by the adversary: sensor data is noisy or tampered with, and the adversary acts to remain unobserved. The model also has to run under limited compute and time, close to where decisions are made. Under these constraints a defender cannot represent the whole state space in equal detail, so what to represent, and where to concentrate effort, is itself part of the problem.

The thread has two lines. [FOE-Dreamer](environment.md) is a learned world model that places the adversary in a separate latent variable from the environment, so that the model of the adversary can be estimated and examined on its own. [Learn Structure](strategic-structure.md) studies where in an interaction a defender's best action actually depends on the adversary's. It defines that dependence as a measurable quantity, constructs environments containing a known amount of it, and tests whether it can be recovered from data, so that costly game-theoretic computation can be applied only where it is needed.

Both lines raise questions this page does not settle: how a defender should act when its learned model is inaccurate, and whether an inaccurate model can still be used to reduce the cost of computing strategic responses. These are described on the [next](next.md) page.

_Last updated: 2026-08_
