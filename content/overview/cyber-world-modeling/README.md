---
icon: connectdevelop
---

# Cyber World Modeling

Before an agent can defend a network, it has to hold a model of one — and of whoever is moving through it.

Two questions sit under that. What should the model contain, and how should it be factored so that being wrong about the adversary doesn't mean being wrong about the network? And where in a large interaction does the strategic part actually live, given that most of it isn't strategic at all?

* [**FOE-Dreamer**](environment.md) — a factored world model with the opponent kept in its own latent, so the adversary model stays separable and inspectable.
* [**Learn Structure**](strategic-structure.md) — defining strategic dependence, generating games that contain it, then learning it back and checking the recovery.

_Last updated: 2026-08_
