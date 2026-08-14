# Team Defense Game

Two defenders, one network, one attacker working against them. The question isn't which of them is better. It's what passes between them.

<figure><img src="../../.gitbook/assets/tdg-interaction.gif" alt="A human and an agent defending one network: proposals, approvals, a shared pool, and the agent's memory updating"><figcaption>One episode. Watch the three channels connecting the two defenders.</figcaption></figure>

## Approval

The agent doesn't simply act. Actions that carry a **control dependency** are proposed and then wait — they sit in the pending strip until the human signs off. Approved, the action executes. Left alone, it expires and the moment passes.

This is where authority actually lives. Not in a policy document, but in whether the action fires.

## The shared pool

Both defenders draw from the same budget. Every action either of them takes leaves less for the other, whether or not they coordinated.

That's a **pool dependency**, and it means the two are coupled even when they're working on opposite ends of the network. The human spending on one host quietly narrows what the agent can do about another.

## Learning from the partner

On the right, the agent's memory. Each entry is a situation paired with an action, and a value blended from the instances it has stored.

The values shift as the episode runs — including from outcomes the human produced. The agent never chose those actions, but it lives with their consequences, so it learns from them.

At the end of the episode the whole thing re-settles at once: every instance from that episode is re-scored against how the episode actually went. Credit isn't assigned move by move. It's assigned in retrospect, to everything the team did.

## Why build it this way

Interdependence is usually described and then assumed. Writing approval and pooling into the game makes it something you can vary and measure — you can tighten the authority boundary, shrink the pool, and see what it does to the pair.

_Last updated: 2026-08_
