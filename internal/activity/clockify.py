#!/usr/bin/env python3
"""
Read time entries out of Clockify.

The free plan allows 30 requests per hour per workspace. One refresh uses
three: the workspace, the project list, and the entries. Results are cached to
clockify.json so a rerun inside the hour costs nothing.

The key lives in secrets.json, which is gitignored. Without a key everything
here returns empty and the rest of the board carries on without hours.
"""
import os, json, time, datetime, urllib.request, urllib.error, urllib.parse

from config import HERE, load_secrets

BASE = "https://api.clockify.me/api/v1"
CACHE = os.path.join(HERE, "clockify.json")
CACHE_TTL = 30 * 60          # half an hour


def _get(path, key, params=None):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"X-Api-Key": key,
                                               "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def check(key):
    """(ok, message) — used by the Test button in the control window."""
    if not key:
        return False, "No key yet."
    try:
        me = _get("/user", key)
    except urllib.error.HTTPError as e:
        return False, "Clockify said %s. Check the key." % e.code
    except Exception as e:
        return False, "Could not reach Clockify: %s" % e
    return True, "Connected as %s." % me.get("name", me.get("email", "you"))


def projects(key):
    """[(id, name)] of the projects in the active workspace."""
    if not key:
        return []
    try:
        me = _get("/user", key)
        ws = me.get("activeWorkspace")
        out, page = [], 1
        while True:
            batch = _get("/workspaces/%s/projects" % ws, key,
                         {"page": page, "page-size": 200, "archived": "false"})
            out += [(p["id"], p["name"]) for p in batch]
            if len(batch) < 200:
                break
            page += 1
        return sorted(out, key=lambda t: t[1].lower())
    except Exception:
        return []


def entries(key, days=400, force=False):
    """
    Time entries as {project_name: [{"at","hours","what"}]}, plus a
    {day: hours} tally per project for the heatmap.
    """
    if not key:
        return {}
    if not force and os.path.exists(CACHE):
        try:
            blob = json.load(open(CACHE, encoding="utf-8"))
            if time.time() - blob.get("at", 0) < CACHE_TTL:
                return blob["by_project"]
        except Exception:
            pass

    try:
        me = _get("/user", key)
        ws, uid = me["activeWorkspace"], me["id"]
        names = {pid: nm for pid, nm in projects(key)}
        start = (datetime.datetime.utcnow() - datetime.timedelta(days=days))
        got, page = [], 1
        while page <= 12:                      # 5000 entries is plenty
            batch = _get("/workspaces/%s/user/%s/time-entries" % (ws, uid), key,
                         {"start": start.strftime("%Y-%m-%dT%H:%M:%SZ"),
                          "page": page, "page-size": 500})
            got += batch
            if len(batch) < 500:
                break
            page += 1
    except Exception:
        return {}

    by = {}
    for e in got:
        ti = e.get("timeInterval") or {}
        s, t = ti.get("start"), ti.get("end")
        if not s or not t:
            continue                            # a timer still running
        try:
            sd = datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")
            td = datetime.datetime.strptime(t, "%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            continue
        name = names.get(e.get("projectId"), "")
        if not name:
            continue
        by.setdefault(name, []).append({
            "at": int(sd.replace(tzinfo=datetime.timezone.utc).timestamp()),
            "day": sd.strftime("%Y-%m-%d"),
            "hours": round((td - sd).total_seconds() / 3600.0, 2),
            "what": (e.get("description") or "").strip(),
        })

    for v in by.values():
        v.sort(key=lambda x: x["at"], reverse=True)
    try:
        json.dump({"at": int(time.time()), "by_project": by},
                  open(CACHE, "w", encoding="utf-8"), ensure_ascii=False)
    except OSError:
        pass
    return by


def key():
    return load_secrets().get("clockify_key", "")


if __name__ == "__main__":
    k = key()
    ok, msg = check(k)
    print(msg)
    if ok:
        by = entries(k, force=True)
        for name, rows in sorted(by.items()):
            print("  %-32s %5.1fh  %s" % (name, sum(r["hours"] for r in rows),
                                          rows[0]["what"][:40] if rows else ""))
