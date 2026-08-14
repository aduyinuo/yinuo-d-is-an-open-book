# FOE-Dreamer

A world-model agent for network defense, built so that learning can happen where the network actually is rather than only in a simulator.

<figure><img src="../../.gitbook/assets/foe-dreamer-architecture.gif" alt="FOE-Dreamer architecture, animated"><figcaption>The architecture, traced in the order information moves through it.</figcaption></figure>

## Reading the diagram

The right side is the **factored world model**. An observation $$o_t$$ is split and passed through two encoders, $$Enc_z$$ and $$Enc_u$$. Each feeds a recurrent state-space model that carries its own history forward, producing two latents: $$z_t, h_t$$ for the part of the world the agent is modelling directly, and $$u_t$$ for the part it keeps factored out.

The left side is the **opponent model**. A window of recent latent-action pairs goes through a recurrent encoder into $$z^{opp}_t$$, a compact representation of who the agent is up against. Two decoders read it: $$Dec_{act}$$ predicts the opponent's next actions, $$Dec_{obs}$$ predicts what the opponent will observe.

The two sides meet at the concatenation. $$z^{opp}_t$$, $$z_t, h_t$$ and $$u_t$$ are joined and read by $$Dec_o$$ and $$Dec_r$$, which reconstruct the observation and the reward.

## Why factor it this way

Keeping the opponent in its own latent, rather than folding it into the world state, means the agent can be wrong about the adversary without being wrong about the network. It also makes the adversary model inspectable on its own terms — you can ask what the agent thinks the attacker will do next, and check it.

_Last updated: 2026-08_
