#!/usr/bin/env python3
"""
Step 2: turn thousands of photos into a shortlist worth looking at.

    python internal/photos/curate.py [--per-event 6]

Groups photos into events by time and place, drops near-duplicate frames, throws
out the blurred and the badly exposed, and keeps the best few per event. Writes
internal/photos/shortlist.json — the only file a human (or I) then looks at.

Nothing is deleted. Curation is a set of decisions recorded in JSON.
"""
import os, json, math, argparse, datetime, collections

HERE = os.path.dirname(os.path.abspath(__file__))
PHOTOS = os.path.join(HERE, "photos.json")
PLACES = os.path.join(HERE, "places.json")
OUT = os.path.join(HERE, "shortlist.json")


def haversine(a, b, c, d):
    R = 6371.0
    p1, p2 = math.radians(a), math.radians(c)
    dp, dl = math.radians(c - a), math.radians(d - b)
    x = math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2 * R * math.asin(math.sqrt(x))


def place_of(lat, lon, places):
    if lat is None or lon is None:
        return None
    best, bestd = None, 1e9
    for a in places["anchors"]:
        d = haversine(lat, lon, a["lat"], a["lon"])
        if d < bestd:
            best, bestd = a["name"], d
    return best if bestd <= places.get("radius_km", 60) else None


def hamming(a, b):
    return bin(int(a, 16) ^ int(b, 16)).count("1")


def parse(ts):
    try:
        return datetime.datetime.fromisoformat(ts)
    except Exception:
        return None


def main(per_event, gap_hours, dup_bits):
    doc = json.load(open(PHOTOS, encoding="utf-8"))
    places = json.load(open(PLACES, encoding="utf-8"))
    ph = [p for p in doc["photos"] if not p.get("private")]

    for p in ph:
        p["place"] = place_of(p.get("lat"), p.get("lon"), places)
        p["dt"] = parse(p.get("taken") or "")

    dated = sorted([p for p in ph if p["dt"]], key=lambda p: p["dt"])
    undated = [p for p in ph if not p["dt"]]

    # events: a break in time, or a change of place, starts a new one
    events, cur = [], []
    for p in dated:
        if cur:
            prev = cur[-1]
            gap = (p["dt"] - prev["dt"]).total_seconds() / 3600.0
            if gap > gap_hours or (p["place"] != prev["place"]):
                events.append(cur); cur = []
        cur.append(p)
    if cur:
        events.append(cur)
    if undated:
        events.append(undated)

    shortlist, dropped = [], collections.Counter()
    for ev in events:
        kept = []
        for p in sorted(ev, key=lambda x: -x["sharpness"]):
            if p["sharpness"] < 25:
                dropped["blurred"] += 1; continue
            if p["clipped"] > 0.35 or not (0.12 <= p["luminance"] <= 0.94):
                dropped["exposure"] += 1; continue
            if any(hamming(p["phash"], k["phash"]) <= dup_bits for k in kept):
                dropped["duplicate"] += 1; continue
            kept.append(p)
        for p in kept[:per_event]:
            p2 = {k: v for k, v in p.items() if k != "dt"}
            p2["event"] = (ev[0]["dt"].date().isoformat() if ev[0].get("dt") else "undated")
            shortlist.append(p2)
        dropped["beyond_quota"] += max(0, len(kept) - per_event)

    for p in shortlist:
        p.setdefault("tags", [])       # food / plant / cat / street / view / people
        p.setdefault("caption", "")
        p.setdefault("collection", p.get("place") or "")

    json.dump({"generated": datetime.datetime.now().isoformat(timespec="seconds"),
               "events": len(events), "dropped": dict(dropped),
               "photos": shortlist},
              open(OUT, "w", encoding="utf-8", newline="\n"),
              ensure_ascii=False, indent=1)

    print("%d photos in, %d events, %d shortlisted" % (len(ph), len(events), len(shortlist)))
    for k, v in dropped.items():
        print("  dropped %-14s %d" % (k, v))
    byplace = collections.Counter(p.get("place") or "unknown place" for p in shortlist)
    for k, v in byplace.most_common():
        print("  %-18s %d" % (k, v))
    print("wrote", OUT)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-event", type=int, default=6)
    ap.add_argument("--gap-hours", type=float, default=6.0)
    ap.add_argument("--dup-bits", type=int, default=6)
    a = ap.parse_args()
    main(a.per_event, a.gap_hours, a.dup_bits)
