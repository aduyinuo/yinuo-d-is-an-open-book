---
icon: rectangles-mixed
---

# FOE-Dreamer

A world-model agent for network defense, built so that learning can happen where the network actually is rather than only in a simulator.

<figure><img src="../../../.gitbook/assets/foe-dreamer-architecture.gif" alt="FOE-Dreamer architecture, animated"><figcaption><p>FOE-Dreamer, traced in the order information moves through it.</p></figcaption></figure>

The right side is the **factored world model**. An observation $$o_t$$ is split and passed through two encoders, $$Enc_z$$ and $$Enc_u$$. Each feeds a recurrent state-space model that carries its own history forward, producing two latents: $$z_t, h_t$$ for the part of the world the agent models directly, and $$u_t$$ for the part it keeps factored out.

The left side is the **opponent model**. A window of recent latent-action pairs runs through a recurrent encoder into $$z^{opp}_t$$, a compact representation of who the agent is up against. Two decoders read it: $$Dec_{act}$$ predicts the opponent's next actions, $$Dec_{obs}$$ predicts what the opponent will observe.

The two sides meet at the concatenation. $$z^{opp}_t$$, $$z_t, h_t$$ and $$u_t$$ are joined and read by $$Dec_o$$ and $$Dec_r$$, which reconstruct the observation and the reward.

## Results

Trained and evaluated in [Daedalus](../../../artifacts/daedalus/): an eight-host OpenStack network across three subnets, provisioned with real services, with CVE-bound exploits and GHOSTS-generated background user traffic.

Against both scripted attacker profiles, FOE-Dreamer roughly halves episode loss relative to Rainbow and IQN under matched compute, and trains inside a three-day budget on one GPU. Ablations show the factoring and the opponent model each contribute.

## What "operational" means here

Narrowly. The substrate, the services, the exploit paths, the five-second polling and the consequences of defender actions are real. The user and attacker populations and the CVE catalogue are emulated.

## Ongoing work: where the model is wrong

Every learned model is inaccurate somewhere, and an adversary searches for the region where it is confidently inaccurate. Model-based reinforcement learning already knows this failure under two names — objective mismatch, where the model minimises prediction error across the data distribution while the policy needs accuracy only where it will act, and model exploitation, where a policy drifts into states the model never saw and profits from the error there. In both the drift is an artefact of the training loop. Here it is an opponent's objective, so uniform predictive loss is selected against.

Predictive accuracy does not measure this. The questions are which errors a defender survives, whether drift in the opponent latent can be detected before it is exploited, and whether a model with wide uncertainty is preferable to a confident one that is wrong. The planned output is a failure taxonomy for factored world models and a drift detector, evaluated on the FOE-Dreamer environments.

One assumption may not hold: the adversary latent may not be identifiable from defender-side observation at all. Against an adversary living off the land it may be recoverable only up to the defender's own intervention power, and under a coarse action space not at all. The fallback is drift detection on the joint latent, which surrenders attribution and keeps the alarm.

Success is fixed in advance. The detector fires before the attacker reaches the region the model is wrong about, at a false-alarm rate an operator will accept, and planted structure is recovered against known ground truth.

## Publications

<table><thead><tr><th width="100"></th><th width="400">Paper</th><th>Authors</th><th></th></tr></thead><tbody><tr><td><img src="../../../.gitbook/assets/badge-preprint.png" alt="Preprint" data-size="original"></td><td><mark style="color:green;">FOE-Dreamer: Deployment-Efficient Learning of Cyber Defense Policies in Operational Networks</mark><br><em>Under review, ACSAC</em></td><td><strong>Y. Du</strong>, <a href="https://www.cs.utep.edu/kiekintveld/">C. Kiekintveld</a></td><td></td></tr></tbody></table>

## Collaborators

<table><thead><tr><th width="150"></th></tr></thead><tbody><tr><td><img src="../../../.gitbook/assets/collab-christopher-kiekintveld.png" alt="Christopher Kiekintveld" width="48"><br><a href="https://www.cs.utep.edu/kiekintveld/"><strong>Christopher Kiekintveld</strong></a><br>University of Texas at El Paso</td></tr></tbody></table>

_Last updated: 2026-08_
