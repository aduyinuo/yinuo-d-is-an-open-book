---
icon: dice-d20
---

# How To Make RL Work

Twenty six columns, applied to every paper in the same order, so answers are comparable and silence is recorded rather than filled in. Grouped by what they check.

_**Statistical practice.**_ Seeds. Variance reporting. Random source control. Statistical tests. Diverged-run handling.

_**Hyperparameters and convergence.**_ Reporting. Sensitivity. Convergence demonstration.

_**Comparison.**_ Calibration baselines. Baseline tuning. Implementation matching. Environment selection. Comparison style.

_**The problem as posed.**_ Episode length. Discount factor. Reward function. Observation construction. Action space.

_**Learning machinery.**_ Exploration. Credit assignment. Replay buffer. Offline support.

_**Evidence.**_ Generalization. Ablation discipline. Sample complexity against compute. Action latency budget.

## How many seeds

Four sources answer this and none agrees on a number. All four agree five is too few.

| Source | What they ran | What they concluded |
| --- | --- | --- |
| Henderson et al., AAAI 2018 | 5 trials, shared preset seeds | Split 10 trials into two groups of 5, same algorithm, same hyperparameters: significantly different at t = −9.0916, p = 0.0016 |
| Colas et al. | Power analysis, worked example | At N = 5 the bootstrap test gave a ~10% false positive rate against a nominal 5% |
| Agarwal et al., NeurIPS 2021 | 100 runs per algorithm and game | The field would need "closer to 50–100 runs ... far too many to be computationally feasible for most research projects" |
| Engstrom et al., ICLR 2020 | "at least 80 agents for each estimate" | Added agents where variance was high rather than widening the interval |

Henderson also argues against selecting the top N trials: the seed experiment shows "this can be potentially misleading."

## Where they disagree, and it stays unresolved

Colas recommends a significance test and names Welch's t-test, with a Bonferroni correction and a significance level below 0.05. Agarwal recommends against significance tests "because of their dichotomous nature ... and common misinterpretations," and puts stratified bootstrap confidence intervals, performance profiles, the interquartile mean, the optimality gap, and the average probability of improvement in their place.

Both are defensible and they produce different tables. Choose one, say which, and do not mix them.

## Three ways a comparison fails, kept separate

_**Calibration baselines**_ ask whether a trivial policy would have done as well. Random and do-nothing bracket the range and cost almost nothing.

_**Baseline tuning**_ asks whether the comparison method got the same care as the proposed one. Untuned baselines and designer bias are endemic.

_**Implementation matching**_ asks whether both methods came from the same code. Henderson compared three codebases for one algorithm and found the codebase itself changed the result. Engstrom ran everything from one codebase, listed every parameter, and acknowledged its own bug.

## Two rules before any of the above

Do not form the hypothesis after seeing the results. Put the question, the hyperparameter sets, and the seed budget in writing before the runs start.

Convergence goes in the body, not the appendix. And a learning curve can hide a local optimum, so the curve alone does not establish that the policy is doing what its score suggests.

[**Download the full notes (.pdf)**](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/research-craft-notes/t10_making_rl_work.pdf) · [all craft notes in one file](https://github.com/aduyinuo/yinuo-d-is-an-open-book/raw/main/templates/research-craft-notes.pdf)

_Last updated: 2026-08_
