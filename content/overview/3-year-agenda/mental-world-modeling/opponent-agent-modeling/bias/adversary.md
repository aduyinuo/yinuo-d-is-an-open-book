---
icon: face-shaking-horizontal
---

# Challenging Attacker

<figure><img src="../../../../../.gitbook/assets/adversary-beeline-meander.gif" alt="B-line and Meander attackers moving through the same network, side by side"><figcaption><p>Both are heading for the operational server. They get there very differently.</p></figcaption></figure>

## B-line

A fixed route. The agent carries a prepared sequence of actions — discover, exploit, escalate, repeat — aimed straight at the operational server, with a jump table telling it where to fall back to when a step fails. It touches almost nothing it doesn't need.

Cheap to detect if you know the route. Almost impossible to detect from volume, because there isn't any.

## Meander

Breadth first. It scans every subnet it can see, discovers services on every address it has learned, exploits what it can, escalates where it can, and only then arrives at the same server. It leaves marks across the whole network on its way.

Loud, slow, and much harder to predict, because what it does next depends on what it happened to find.

##

## Slides

{% embed url="https://aduyinuo.github.io/yinuo-d-is-an-open-book/slides/mental-world-modeling--opponent-agent-modeling--bias--adversary.html" %}
Step through this project as slides, with the text for each slide below it.
{% endembed %}

## Publications

<table><thead><tr><th width="100"></th><th width="400">Paper</th><th>Authors</th><th></th></tr></thead><tbody><tr><td><img src="../../../../../.gitbook/assets/badge-tsc.png" alt="ACM TSC" data-size="original"></td><td><mark style="color:green;">A cyber-war between bots: cognitive attackers are more challenging for defenders than strategic attackers</mark><br>ACM Transactions on Social Computing, 8(3–4), 1–22</td><td><strong>Y. Du</strong>, <a href="https://sites.google.com/view/baptisteprebot">B. Prébot</a>, <a href="https://scholar.google.com/citations?user=jktsx4EAAAAJ">T. Malloy</a>, <a href="https://www.cmu.edu/dietrich/sds/ddmlab/cotyweb/">C. Gonzalez</a></td><td><a href="https://doi.org/10.1145/3712672"><img src="../../../../../.gitbook/assets/badge-paper.png" alt="paper" data-size="original"></a></td></tr><tr><td><img src="../../../../../.gitbook/assets/badge-hfes.png" alt="HFES" data-size="original"></td><td><mark style="color:green;">Towards autonomous cyber defense: predictions from a cognitive model</mark><br>Human Factors and Ergonomics Society Annual Meeting, 66(1)</td><td><strong>Y. Du</strong>, <a href="https://sites.google.com/view/baptisteprebot">B. Prébot</a>, X. Xi, <a href="https://www.cmu.edu/dietrich/sds/ddmlab/cotyweb/">C. Gonzalez</a></td><td><a href="https://doi.org/10.1177/1071181322661504"><img src="../../../../../.gitbook/assets/badge-paper.png" alt="paper" data-size="original"></a></td></tr></tbody></table>

## Collaborators

<table><thead><tr><th width="150"></th><th width="150"></th><th width="150"></th></tr></thead><tbody><tr><td><img src="../../../../../.gitbook/assets/collab-baptiste-prebot.png" alt="Baptiste Prébot" width="48"><br><a href="https://sites.google.com/view/baptisteprebot"><strong>Baptiste Prébot</strong></a><br>Carnegie Mellon University</td><td><img src="../../../../../.gitbook/assets/collab-tyler-malloy.png" alt="Tyler Malloy" width="48"><br><a href="https://scholar.google.com/citations?user=jktsx4EAAAAJ"><strong>Tyler Malloy</strong></a><br>University of Luxembourg</td><td><img src="../../../../../.gitbook/assets/collab-cleotilde-gonzalez.png" alt="Cleotilde Gonzalez" width="48"><br><a href="https://www.cmu.edu/dietrich/sds/ddmlab/cotyweb/"><strong>Cleotilde Gonzalez</strong></a><br>Carnegie Mellon University</td></tr></tbody></table>

_Last updated: 2026-08_
