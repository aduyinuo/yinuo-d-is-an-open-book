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


## Publications

<table><thead><tr><th width="100"></th><th width="400">Paper</th><th>Authors</th><th></th></tr></thead><tbody><tr><td><img src="../../.gitbook/assets/badge-chb.png" alt="CHB: AI" data-size="original"></td><td><mark style="color:green;">Experimental evaluation of cognitive agents for collaboration in human-autonomy cyber defense teams</mark><br>Computers in Human Behavior: Artificial Humans, 4, 100148</td><td><strong>Y. Du</strong>, <a href="https://sites.google.com/view/baptisteprebot">B. Prébot</a>, <a href="https://scholar.google.com/citations?user=jktsx4EAAAAJ">T. Malloy</a>, <a href="https://feifang.info/">F. Fang</a>, <a href="https://www.cmu.edu/dietrich/sds/ddmlab/cotyweb/">C. Gonzalez</a></td><td><a href="https://doi.org/10.1016/j.chbah.2025.100148"><img src="../../.gitbook/assets/badge-paper.png" alt="paper" data-size="original"></a></td></tr><tr><td><img src="../../.gitbook/assets/badge-jcyb.png" alt="J. Cybersec." data-size="original"></td><td><mark style="color:green;">Learning about simulated adversaries from human defenders using interactive cyber-defense games</mark><br>Journal of Cybersecurity, 9(1), tyad022</td><td><a href="https://sites.google.com/view/baptisteprebot">B. Prébot</a>, <strong>Y. Du</strong>, <a href="https://www.cmu.edu/dietrich/sds/ddmlab/cotyweb/">C. Gonzalez</a></td><td><a href="https://doi.org/10.1093/cybsec/tyad022"><img src="../../.gitbook/assets/badge-paper.png" alt="paper" data-size="original"></a></td></tr><tr><td><img src="../../.gitbook/assets/badge-aaaiss.png" alt="AAAI Symposium" data-size="original"></td><td><mark style="color:green;">Turing-like experiment in a cyber defense game</mark><br>AAAI Symposium Series, 3(1), 547–550</td><td><strong>Y. Du</strong>, <a href="https://sites.google.com/view/baptisteprebot">B. Prébot</a>, <a href="https://www.cmu.edu/dietrich/sds/ddmlab/cotyweb/">C. Gonzalez</a></td><td></td></tr></tbody></table>

## Collaborators

* [Baptiste Prébot](https://sites.google.com/view/baptisteprebot) — Carnegie Mellon University
* [Tyler Malloy](https://scholar.google.com/citations?user=jktsx4EAAAAJ) — University of Luxembourg
* [Fei Fang](https://feifang.info/) — Carnegie Mellon University
* [Cleotilde Gonzalez](https://www.cmu.edu/dietrich/sds/ddmlab/cotyweb/) — Carnegie Mellon University

_Last updated: 2026-08_
