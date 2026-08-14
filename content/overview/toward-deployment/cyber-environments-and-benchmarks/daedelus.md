# Daedelus

**Live command-and-control on provisioned infrastructure.**

Daedelus sits at the emulation end of the range. Rather than modelling an attack, it runs one: a command-and-control stack deployed onto provisioned network infrastructure, with attacker tooling executing real exploits against real services.

That places it in a different category from the simulators. There is no abstract action space to argue about, because the actions are tool invocations, and no observation schema to align, because what you see is whatever the system emits.

The cost is the usual one. Setup is heavy, episodes are slow, and you cannot run the millions of steps that reinforcement learning wants. Its role is as the honest end of the pipeline — the place a policy trained cheaply elsewhere has to survive.

**Use it for** checking whether something learned in simulation does anything at all against live services.

_Last updated: 2026-08_
