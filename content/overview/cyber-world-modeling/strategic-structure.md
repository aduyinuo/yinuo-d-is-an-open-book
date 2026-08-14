---
icon: diagram-project
---

# Learn Structure

Not every part of a game is strategic. Most of it isn't.

<figure><img src="../../.gitbook/assets/strategic-dependence.gif" alt="A map of strategic dependence across a state-action space, shifting as the opponent changes"><figcaption><p>Left: how much the best action depends on the opponent, across the space. Right: probing one region against four opponent behaviours.</p></figcaption></figure>

## The intuition

**Strategic dependence** is how much a player's best action, in a given region of states and actions, turns on what the other player does.

Two parts to it. First, dependence: sometimes your choice genuinely hinges on the opponent, and often it doesn't. Second, what that implies for the right action: where dependence is strong, the region needs game-theoretic reasoning; where it's weak or absent, the region collapses into an ordinary single-agent decision.

The dependence is not uniform. It concentrates in pockets, and those pockets move during a single interaction as the opponent shifts.

