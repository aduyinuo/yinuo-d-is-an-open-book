---
icon: head-side-gear
---

# Mental World Modeling

To work with a person or against one, an agent needs a model of that person: what they intend, what they are attending to, and how they understand the situation. This is difficult for reasons that are not specific to cybersecurity. Describing how someone solves a problem requires a set of operations to describe it with, and research on mental operations has not settled on a single agreed set. The appropriate level of detail depends on the scale of analysis, and the same solution can be described as a few steps or as many. General problem-solving heuristics transfer poorly, because knowing a heuristic and knowing when to apply it are different abilities, and the second is the harder one. Much of what an expert does is not available to introspection, so it has to be recovered indirectly rather than reported.

Cybersecurity adds two further difficulties. The other party is often an adversary who is deliberately deceptive and who departs from optimal play in systematic ways, so a defender trained only against an optimal attacker is prepared for an opponent it will not meet. And the problem-solving one wants to study, whether an analyst at work or a competitor in a capture-the-flag event, takes place under time pressure, where the most reliable method for eliciting reasoning, having the person think aloud while they work, cannot be used.

The thread has two lines. [Problem-Solving](problem-solving/) studies how people solve problems in small groups, in general programming work, and in capture-the-flag competitions, using a description of the process coarse enough that different observers agree on it, and eliciting reasoning afterward by replaying a person their own session as a prompt. [Opponent (Agent) Modeling](opponent-agent-modeling/) studies the adversarial case: how agents infer one another's type over repeated interaction, and how to model an attacker whose systematic biases are represented explicitly, so that a defender trained against it faces a realistic opponent.

Two questions remain open: whether these operations can be learned by an agent rather than specified in advance, and whether inferring a cooperative partner's type and modeling an adversary's biases are the same problem. They are described on the [next](next.md) page.

_Last updated: 2026-08_
