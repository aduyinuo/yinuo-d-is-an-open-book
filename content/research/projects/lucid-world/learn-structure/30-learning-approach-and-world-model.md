# 30 — Learning Approach and World Model

**Prev:** [20 — Generator problem and plan](20-generator-problem-and-plan.md) | **Next:** [90 — Artifacts and source index](90-artifacts-and-source-index.md) | **Related:** [Section index](index.md)

## Working claim
The learner should be an object-centered factored world model that separates controllable, exogenous, and opponent-conditioned dynamics while learning cross-device coupling.

## Candidate pipeline

| Stage | Core move |
|---|---|
| Per-device encoding | preserve entity identity from local observations |
| Within-device factorization | split controllable and exogenous dynamics |
| Opponent embedding | infer adversary context from trajectory history |
| Cross-device attention | learn strategic coupling (`A`) and environmental coupling (`B`) |
| Decode + policy | decode state/reward; act over controllable/opponent factors |

## Why this fits the subproject
- Promotes structured dependence learning rather than black-box prediction.
- Enables recovery-style validation (fidelity/readback variants).
- Supports adaptation under partial observability and adversarial pressure.

## Immediate clarity requirements
- Lock the learning setting (what is learned vs fixed/manipulated).
- Choose two-way vs full IFactor-style factorization.
- Add pseudocode aligned to implementation and evaluation checkpoints.

---
**Prev:** [20 — Generator problem and plan](20-generator-problem-and-plan.md) | **Next:** [90 — Artifacts and source index](90-artifacts-and-source-index.md) | **Related:** [Section index](index.md)
