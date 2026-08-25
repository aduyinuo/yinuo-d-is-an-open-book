"""The animation for Training in "Realistic" Environments.

Two backends behind one interface, and why sample efficiency is what decides
which of them a defender can actually be trained in.

    python internal/e_trainreal.py
"""
import os
from envlib import fig, rbox, txt, save, INK, MUTE, D, M, L, VL, OFF, OCH

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                   "content", ".gitbook", "assets", "training-in-realistic.gif")

SIM = "Simulator\nmillions of steps, minutes"
EMU = "Emulated deployment\nreal services, five-second polling"


def frame(step):
    f, ax = fig(w=8.2, h=3.9, xl=10, yl=5.0)

    txt(ax, 5.0, 4.70, "One action and observation interface", fs=9.5, c=INK, w="bold")
    rbox(ax, 5.0, 4.18, 6.6, 0.46, c=M, fill="white", lw=1.5)
    txt(ax, 5.0, 4.18, "the defender sees the same thing either way", fs=8.2, c=MUTE)

    # the two backends
    sim_on = step >= 1
    emu_on = step >= 2
    rbox(ax, 2.5, 2.95, 3.9, 1.15, c=M if sim_on else OFF,
         fill=VL if sim_on else "white", lw=1.5, alpha=1.0 if sim_on else 0.45)
    txt(ax, 2.5, 3.20, "Simulator", fs=9.5, c=D if sim_on else MUTE, w="bold",
        a=1.0 if sim_on else 0.5)
    txt(ax, 2.5, 2.82, "millions of steps in minutes\nfidelity is whatever was modelled",
        fs=7.8, c=INK if sim_on else MUTE, a=1.0 if sim_on else 0.5)

    rbox(ax, 7.5, 2.95, 3.9, 1.15, c=D if emu_on else OFF,
         fill=VL if emu_on else "white", lw=1.6, alpha=1.0 if emu_on else 0.45)
    txt(ax, 7.5, 3.20, "Emulated deployment", fs=9.5, c=D if emu_on else MUTE,
        w="bold", a=1.0 if emu_on else 0.5)
    txt(ax, 7.5, 2.82, "real services on real hosts\nfive-second polling, actions that land",
        fs=7.8, c=INK if emu_on else MUTE, a=1.0 if emu_on else 0.5)

    for x, on in ((2.5, sim_on), (7.5, emu_on)):
        if on:
            ax.plot([x, x], [3.60, 3.95], color=M, lw=1.3, zorder=2)

    # the budget bar: what a step costs, and what that leaves
    if step >= 3:
        txt(ax, 5.0, 1.95, "What a three-day budget on one GPU buys",
            fs=9.0, c=INK, w="bold")
        rbox(ax, 2.5, 1.30, 3.5, 0.42, c=M, fill=VL, lw=1.2)
        txt(ax, 2.5, 1.30, "steps are cheap, so spend them", fs=7.8, c=D)
        rbox(ax, 7.5, 1.30, 3.5, 0.42, c=D, fill="white", lw=1.4)
        txt(ax, 7.5, 1.30, "steps are dear, so few of them", fs=7.8, c=D)

    if step >= 4:
        txt(ax, 5.0, 0.62,
            "Sample efficiency is what decides whether the right-hand box is "
            "reachable at all.", fs=8.6, c=OCH, w="bold")
    if step >= 5:
        txt(ax, 5.0, 0.22,
            "And the difference between the two is itself a measurement of what "
            "the simulator left out.", fs=8.2, c=MUTE, style="italic")
    return f


if __name__ == "__main__":
    frames = []
    for s in range(6):
        frames += [frame(s)] * (3 if s else 4)
    save(frames, os.path.normpath(OUT), dur=520, hold=4, loop=0)
