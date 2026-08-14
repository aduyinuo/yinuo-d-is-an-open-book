# CybORG

**Cyber Operations Research Gym — the substrate under the CAGE challenges.**

CybORG is a network simulator built for reinforcement learning research in autonomous cyber defence. It handles concurrent red, blue, and green agents — attacker, defender, and ordinary users — across a network of connected hosts.

The CAGE Challenge 2 scenario is the version most of this work uses. Thirteen hosts across three subnets: five user workstations, three enterprise servers plus a Defender host, and an operational subnet holding three workstations and Op_Server0. The operational subnet cannot be reached directly from the user subnet, so the enterprise layer is a mandatory waypoint.

The attacker begins with a permanent foothold on User0. Holding a user host pays 0.1 per step, an enterprise or operational server pays 1.0, and Impact on Op_Server0 pays 10.0. Two defender configurations matter: one removes attacker sessions, the other restores hosts to a clean state. The restoring defender is what makes the environment non-stationary from the attacker's side.

**Use it for** comparable results — it is the closest thing the field has to a common baseline, and the B-line and Meander attackers are defined here.

_Last updated: 2026-08_
