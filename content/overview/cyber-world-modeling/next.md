---
icon: crystal-ball
---

# Next

Three questions follow from the two lines in this thread.

The first concerns acting on an inaccurate model. A model learned from data is wrong in some parts of the state space. In an adversarial setting this error is not random, because an adversary has an incentive to locate the regions where the defender's model is wrong and to act there. Treating model error as noise to be averaged over is therefore not appropriate. The question is how a defender should act when its model is most likely to be wrong exactly where the adversary is operating. This includes detecting when the model of the adversary has become unreliable, limiting the cost of acting on a model that is wrong, and determining whether a model that represents its own uncertainty is safer to use than one that is confident and wrong.

The second concerns what an inaccurate model is still useful for. A world model can be used not only to predict but to reduce the cost of computing strategic responses. In PSRO, each new response is learned through repeated interaction with the environment, and a world model can supply some of those interactions as simulated rollouts, lowering the number of real interactions required. Co-learning a world model with the empirical game has been done before, in Dyna-PSRO. The open question is what happens when the model is inaccurate: whether simulated rollouts still reduce the total cost of reaching a strategically robust policy, or whether the model's errors bias the empirical game and the responses computed from it. Under what conditions does using the model help, and when is it worse than slower interaction with the real environment?

The third concerns whether this can be done under deployment constraints. The defender this thread is aimed at must adapt quickly to a new adversary, learn from limited data, and remain robust as the adversary changes, on hardware that cannot run a large model. Meta-learning addresses fast adaptation, a factored world model addresses sample efficiency, and PSRO addresses robustness to a changing opponent. Each pair of these has been combined before, but not all three together, and not under the compute and communication limits of a real deployment. Whether they can be combined without one undermining another, and whether the result is feasible on constrained hardware, is open.

_Last updated: 2026-08_
