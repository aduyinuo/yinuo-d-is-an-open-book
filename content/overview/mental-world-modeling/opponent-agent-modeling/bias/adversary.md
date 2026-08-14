---
icon: face-shaking-horizontal
---

# Challenging Attacker

<figure><img src="../../../../.gitbook/assets/adversary-beeline-meander.gif" alt="B-line and Meander attackers moving through the same network, side by side"><figcaption><p>Both are heading for the operational server. They get there very differently.</p></figcaption></figure>

## B-line

A fixed route. The agent carries a prepared sequence of actions — discover, exploit, escalate, repeat — aimed straight at the operational server, with a jump table telling it where to fall back to when a step fails. It touches almost nothing it doesn't need.

Cheap to detect if you know the route. Almost impossible to detect from volume, because there isn't any.

## Meander

Breadth first. It scans every subnet it can see, discovers services on every address it has learned, exploits what it can, escalates where it can, and only then arrives at the same server. It leaves marks across the whole network on its way.

Loud, slow, and much harder to predict, because what it does next depends on what it happened to find.

##

_Last updated: 2026-08_
