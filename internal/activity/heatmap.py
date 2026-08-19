#!/usr/bin/env python3
"""
GitHub-style contribution heatmaps.

One wide one for the projects ticked in the settings window, and a small one
per project. A day is shaded by the hours logged against it in Clockify, or by
how much of the project was touched when there are no hours.
"""
import os, datetime
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# empty -> most
LEVELS = ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"]
LEVELS_DARK_EMPTY = "#ebedf0"
MUTE = "#8a9199"

RANGES = {"1m": 31, "3m": 92, "6m": 183, "1y": 365, "all": 1460}


def window(range_key, custom=None):
    """(first day, last day) for a range key, or an explicit custom pair."""
    today = datetime.date.today()
    if custom and custom.get("from") and custom.get("to"):
        try:
            a = datetime.date.fromisoformat(custom["from"])
            b = datetime.date.fromisoformat(custom["to"])
            return (a, b) if a <= b else (b, a)
        except ValueError:
            pass
    days = RANGES.get(range_key, RANGES["6m"])
    return today - datetime.timedelta(days=days - 1), today


def _tally(projects, first, last):
    """{day: weight} summed over the given projects, clipped to the window."""
    out = {}
    for p in projects:
        hours = p.get("hours") or {}
        days = p.get("days") or {}
        for d, h in hours.items():
            out[d] = out.get(d, 0.0) + float(h)
        for d, n in days.items():
            if d not in hours:
                out[d] = out.get(d, 0.0) + min(float(n) * 0.25, 3.0)
    lo, hi = first.isoformat(), last.isoformat()
    return {d: v for d, v in out.items() if lo <= d <= hi}


def _level(v, top):
    if v <= 0:
        return 0
    if top <= 0:
        return 1
    q = v / top
    return 1 if q <= 0.25 else 2 if q <= 0.5 else 3 if q <= 0.75 else 4


def draw(projects, out_path, range_key="6m", custom=None, cell=11, gap=3,
         labels=True, title=None):
    """Write a heatmap PNG. Returns the total weight it drew."""
    first, last = window(range_key, custom)
    tally = _tally(projects, first, last)
    total_hours = sum(sum((p.get("hours") or {}).values()) for p in projects)

    start = first - datetime.timedelta(days=(first.weekday() + 1) % 7)   # back to Sunday
    weeks = ((last - start).days // 7) + 1
    top = max(tally.values(), default=0.0)

    unit = (cell + gap) / 72.0
    fig_w = weeks * unit + (0.75 if labels else 0.1)
    fig_h = 7 * unit + (0.62 if labels else 0.1)
    fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=170)
    ax.set_xlim(0, weeks)
    ax.set_ylim(0, 7 + (1.15 if labels else 0))
    ax.axis("off")
    ax.invert_yaxis()

    months = []
    for w in range(weeks):
        for d in range(7):
            day = start + datetime.timedelta(days=w * 7 + d)
            if day < first or day > last:
                continue
            lv = _level(tally.get(day.isoformat(), 0.0), top)
            y = d + (1.15 if labels else 0)
            ax.add_patch(FancyBboxPatch(
                (w + 0.08, y + 0.08), 0.84, 0.84,
                boxstyle="round,pad=0,rounding_size=0.18",
                fc=LEVELS[lv], ec="none"))
            if day.day <= 7 and d == 0:
                months.append((w, day.strftime("%b")))

    if labels:
        for w, name in months:
            ax.text(w, 0.85, name, fontsize=7.4, color=MUTE, va="bottom")
        if title:
            ax.text(0, 0.05, title, fontsize=8.6, color=MUTE, va="bottom")

    plt.subplots_adjust(0, 0, 1, 1)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    fig.savefig(out_path, transparent=True, bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)
    return total_hours


def legend_line(total_hours, range_key, custom=None):
    first, last = window(range_key, custom)
    span = {"1m": "the last month", "3m": "the last three months",
            "6m": "the last six months", "1y": "the last year",
            "all": "all time"}.get(range_key)
    if not span:
        span = "%s to %s" % (first.strftime("%b %d, %Y"), last.strftime("%b %d, %Y"))
    if total_hours > 0:
        return "%d hours logged in %s" % (round(total_hours), span)
    return "Work across %s" % span
