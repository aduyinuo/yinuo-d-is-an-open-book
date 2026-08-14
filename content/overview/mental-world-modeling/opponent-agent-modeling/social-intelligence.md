# Iterated Strategic Interaction

## Dynamic Sociality

<figure><img src="../../../.gitbook/assets/social-ipd-network.gif" alt="Agents playing iterated prisoner&#x27;s dilemma on a network"><figcaption><p>Eight agents, twelve ties, fourteen rounds. Green edges are mutual cooperation.</p></figcaption></figure>

Each agent plays its neighbours repeatedly, and each carries a fixed strategy — tit-for-tat, always cooperate, always defect, grim. Nobody sees the strategy list; they only see what happened last round.

Watch what the always-defect nodes do to their neighbourhoods. A tit-for-tat agent next to a defector stops cooperating, and its other ties go cold too. The damage is not confined to the pair that caused it, because the retaliating agent cannot separate the neighbour who exploited it from the neighbours who didn't. Payoffs on the right make the cost visible: defection pays early and then starves the neighbourhood it depends on.

## Catagorization

<figure><img src="../../../.gitbook/assets/social-categorization.gif" alt="One agent categorising nine partners into types as evidence accumulates"><figcaption><p>One agent, nine partners, sorted and re-sorted as evidence arrives.</p></figcaption></figure>

The second animation drops the network and takes a single agent's point of view. It plays each partner in turn and keeps a running estimate of how often each one cooperates.

It does not track nine separate people. It compresses them into a small number of types — cooperative, conditional, exploitative — because carrying nine independent models is not what people do.

The categories are relative, not absolute. A partner is classified against the group mean, not against a fixed threshold, so the same behaviour lands in different categories depending on who else is in the room. Move a mildly cooperative partner into a generous group and they become the exploiter; move them into a harsh one and they become the cooperator. That is the contrast effect, and it is doing real work here: identical evidence, different judgement.

## _Contrast_

_Last updated: 2026-08_
