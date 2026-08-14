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

## How you would measure it

Take a region. Hold it fixed and vary the opponent — passive, greedy, adaptive, deceptive. If the best action barely moves, the region is not strategic and can be solved as a decision problem. If the best action swings, the region is strategic and has to be treated as such.

That is the right panel: the same probe, run against four opponents. Wide spread means the region matters strategically. Flat means it doesn't.

Whether to define the spread through regret or through variance is still open, and the two are not obviously equivalent.

## Why it's worth the trouble

Game-theoretic reasoning is expensive. If most of a large game is strategically flat, an agent that knows _where_ the strategic structure sits can spend its reasoning there and treat the rest cheaply. Finding that structure — defining it, generating games that contain it by construction, then learning it back from data and checking the recovery — is what this line of work is about.


## Publications

<table><thead><tr><th width="100"></th><th width="400">Paper</th><th>Authors</th><th></th></tr></thead><tbody><tr><td><img src="../../.gitbook/assets/badge-preprint.png" alt="Preprint" data-size="original"></td><td><mark style="color:green;">Learning Strategic Structure in Sequential Adversarial Games</mark></td><td><strong>Y. Du</strong>, <a href="https://www.cs.utep.edu/kiekintveld/">C. Kiekintveld</a></td><td></td></tr></tbody></table>

## Collaborators

* [Christopher Kiekintveld](https://www.cs.utep.edu/kiekintveld/) — University of Texas at El Paso

_Last updated: 2026-08_
