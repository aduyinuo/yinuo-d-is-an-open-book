# Adversary

Two attackers, the same network, the same objective. Watching them move is the fastest way to see why "the adversary" is not one thing.

<figure><img src="../../.gitbook/assets/adversary-beeline-meander.gif" alt="B-line and Meander attackers moving through the same network, side by side"><figcaption>Both are heading for the operational server. They get there very differently.</figcaption></figure>

## B-line

A fixed route. The agent carries a prepared sequence of actions — discover, exploit, escalate, repeat — aimed straight at the operational server, with a jump table telling it where to fall back to when a step fails. It touches almost nothing it doesn't need.

Cheap to detect if you know the route. Almost impossible to detect from volume, because there isn't any.

## Meander

Breadth first. It scans every subnet it can see, discovers services on every address it has learned, exploits what it can, escalates where it can, and only then arrives at the same server. It leaves marks across the whole network on its way.

Loud, slow, and much harder to predict, because what it does next depends on what it happened to find.

## Why this matters for defense

A defender trained against one of these learns a policy that reads the other badly. B-line teaches you to watch a corridor; Meander teaches you to watch volume. Neither lesson transfers.

The interesting part sits between them: real attackers are neither perfectly routed nor exhaustive. They are shaped by cost, by habit, and by what they believe about the network — which is what modelling the adversary is actually for.

_Last updated: 2026-08_
