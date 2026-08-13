# 20 — Generator Problem and Plan

**Prev:** [10 — Taxonomy development](10-taxonomy-development.md) | **Next:** [30 — Learning approach and world model](30-learning-approach-and-world-model.md) | **Related:** [Section index](index.md)

## Working claim
The generator is valid only if requested structure is either **guaranteed by construction** or **measured after play**, with explicit handling of unattainable requests.

## Problem statement
Given a domain description and taxonomy vocabulary, generate game instances that satisfy requested dependence patterns, or report precisely why the request cannot be realized.

## Solving-plan spine

| Step | Expected outcome |
|---|---|
| Verify amendment state | reconcile 07-24 edits and recover missing rationale |
| Define request language | formal schema over type/degree/entities |
| Classify request types | construction-guaranteed vs play-emergent |
| Translate domain to game form | explicit loss accounting during translation |
| Generate environments + strategies | modular generation with interference checks |
| Handle unattainable requests | reject or approximate with distance report |
| Define corruption interface | controlled mismatch between planted and observed structure |
| Implement + inspect | text-to-code implementability check |

## Acceptance criteria
- Every requested structure is labeled as construction-guaranteed or play-measured.
- Unattainable requests are detected and reported with reason codes.
- Approximation mode exposes request-vs-achieved distance.

---
**Prev:** [10 — Taxonomy development](10-taxonomy-development.md) | **Next:** [30 — Learning approach and world model](30-learning-approach-and-world-model.md) | **Related:** [90 — Artifacts and source index](90-artifacts-and-source-index.md)
