# CybORG

**Cyber Operations Research Gym — the substrate under the CAGE challenges.**

<figure><img src="../../../.gitbook/assets/env-cyborg.gif" alt="CAGE Challenge 2: thirteen hosts across three subnets, the attacker&#x27;s reward accruing, and the restoring defender resetting a host"><figcaption><p>Thirteen hosts, three subnets, one mandatory waypoint — and a defender that undoes your work.</p></figcaption></figure>

CybORG is a network simulator built for reinforcement learning research in autonomous cyber defence. It handles concurrent red, blue, and green agents — attacker, defender, and ordinary users — across a network of connected hosts.

The CAGE Challenge 2 scenario is the version most of this work uses. Thirteen hosts across three subnets: five user workstations, three enterprise servers plus a Defender host, and an operational subnet holding three workstations and Op\_Server0. The operational subnet cannot be reached directly from the user subnet, so the enterprise layer is a mandatory waypoint.

The attacker begins with a permanent foothold on User0. Holding a user host pays 0.1 per step, an enterprise or operational server pays 1.0, and Impact on Op\_Server0 pays 10.0. Two defender configurations matter: one removes attacker sessions, the other restores hosts to a clean state. The restoring defender is what makes the environment non-stationary from the attacker's side.

**Use it for** comparable results — it is the closest thing the field has to a common baseline, and the B-line and Meander attackers are defined here.

## Publications

_Work of mine that runs on this environment._

<table><thead><tr><th width="100"></th><th width="400">Paper</th><th>Authors</th><th></th></tr></thead><tbody><tr><td><img src="../../../.gitbook/assets/badge-chb.png" alt="CHB: AI" data-size="original"></td><td><mark style="color:green;">Experimental evaluation of cognitive agents for collaboration in human-autonomy cyber defense teams</mark><br>Computers in Human Behavior: Artificial Humans, 4, 100148</td><td><strong>Y. Du</strong>, <a href="https://sites.google.com/view/baptisteprebot">B. Prébot</a>, <a href="https://scholar.google.com/citations?user=jktsx4EAAAAJ">T. Malloy</a>, <a href="https://feifang.info/">F. Fang</a>, <a href="https://www.cmu.edu/dietrich/sds/ddmlab/cotyweb/">C. Gonzalez</a></td><td><a href="https://doi.org/10.1016/j.chbah.2025.100148"><img src="../../../.gitbook/assets/badge-paper.png" alt="paper" data-size="original"></a></td></tr><tr><td><img src="../../../.gitbook/assets/badge-tsc.png" alt="ACM TSC" data-size="original"></td><td><mark style="color:green;">A cyber-war between bots: cognitive attackers are more challenging for defenders than strategic attackers</mark><br>ACM Transactions on Social Computing, 8(3–4)</td><td><strong>Y. Du</strong>, <a href="https://sites.google.com/view/baptisteprebot">B. Prébot</a>, <a href="https://scholar.google.com/citations?user=jktsx4EAAAAJ">T. Malloy</a>, <a href="https://www.cmu.edu/dietrich/sds/ddmlab/cotyweb/">C. Gonzalez</a></td><td><a href="https://doi.org/10.1145/3712672"><img src="../../../.gitbook/assets/badge-paper.png" alt="paper" data-size="original"></a></td></tr></tbody></table>

## Collaborators

<table><thead><tr><th width="150"></th><th width="150"></th><th width="150"></th><th width="150"></th></tr></thead><tbody><tr><td><p><img src="../../../.gitbook/assets/collab-baptiste-prebot.png" alt="Baptiste Prébot" data-size="original"></p><p><br><a href="https://sites.google.com/view/baptisteprebot"><strong>Baptiste Prébot</strong></a><br>Inria Bordeaux</p></td><td><p><img src="../../../.gitbook/assets/collab-tyler-malloy.png" alt="Tyler Malloy" data-size="original"></p><p><br><a href="https://scholar.google.com/citations?user=jktsx4EAAAAJ"><strong>Tyler Malloy</strong></a><br>University of Luxembourg</p></td><td><p><img src="../../../.gitbook/assets/collab-fei-fang.png" alt="Fei Fang" data-size="original"></p><p><br><a href="https://feifang.info/"><strong>Fei Fang</strong></a><br>Carnegie Mellon University</p></td><td><p><img src="../../../.gitbook/assets/collab-cleotilde-gonzalez.png" alt="Cleotilde Gonzalez" data-size="original"></p><p><br><a href="https://www.cmu.edu/dietrich/sds/ddmlab/cotyweb/"><strong>Cleotilde Gonzalez</strong></a><br>Carnegie Mellon University</p></td></tr></tbody></table>

_Last updated: 2026-08_
