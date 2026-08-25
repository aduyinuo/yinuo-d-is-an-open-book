#!/usr/bin/env python3
"""
Step 2: score each opportunity for fit, and say why.

    python internal/opportunities/score.py

Reads raw.json and profile.json, writes scored.json. The score is a sum of the
profile terms that appear in the title or the description, and every term that
fired is recorded, so a ranking can be argued with rather than trusted.

Ranking, not filtering: nothing is dropped for scoring low. Only things that
have already closed are dropped, and things past the horizon.
"""
import os, io, re, json, time, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw.json")
OUT = os.path.join(HERE, "scored.json")


def load(name):
    with io.open(os.path.join(HERE, name), encoding="utf-8") as fh:
        return json.load(fh)


def score(row, profile):
    hay = (row["title"] + " " + (row.get("detail") or "") + " "
           + (row.get("where") or "")).lower()
    total, why, against = row.get("base", 0), [], []
    if total:
        why.append("from %s" % row.get("source", "a field-specific source"))
    for term, w in profile["weights"].items():
        if term.lower() in hay:
            total += w
            why.append(term)
    for term, w in profile["penalties"].items():
        if term.lower() in hay:
            total += w
            against.append(term)
    return total, why, against


def days_left(deadline, today):
    if not deadline:
        return None
    try:
        d = datetime.date.fromisoformat(deadline)
    except ValueError:
        return None
    return (d - today).days


def main():
    raw = load("raw.json")
    profile = load("profile.json")
    today = datetime.date.today()
    horizon = profile.get("deadline_horizon_days", 400)

    kept, closed, far = [], 0, 0
    for row in raw["items"]:
        low = row["title"].lower()
        if any(b.lower() in low for b in profile.get("must_not_contain", [])):
            continue
        left = days_left(row.get("deadline"), today)
        if left is not None:
            if left < 0:
                closed += 1
                continue
            if left > horizon:
                far += 1
                continue
        s, why, against = score(row, profile)
        row.update({"score": s, "why": why, "against": against, "days_left": left})
        kept.append(row)

    # Soonest first among things with a deadline, then by fit. A deadline you
    # can still make is worth more than a good fit you cannot date.
    kept.sort(key=lambda r: (r["days_left"] is None,
                             r["days_left"] if r["days_left"] is not None else 0,
                             -r["score"]))

    by_stream = {}
    for row in kept:
        by_stream.setdefault(row["stream"], []).append(row)

    doc = {"scored": int(time.time()), "today": today.isoformat(),
           "streams": by_stream, "dropped_closed": closed, "dropped_far": far,
           "failed_sources": raw.get("failed", [])}
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1)

    print("%d kept, %d already closed, %d beyond the horizon" % (len(kept), closed, far))
    for s, rows in sorted(by_stream.items()):
        dated = sum(1 for r in rows if r["days_left"] is not None)
        print("  %-12s %4d  (%d with a date)" % (s, len(rows), dated))


if __name__ == "__main__":
    main()
