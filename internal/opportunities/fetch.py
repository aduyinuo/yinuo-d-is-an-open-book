#!/usr/bin/env python3
"""
Step 1 of the opportunity scout: pull every source and normalise what comes back.

    python internal/opportunities/fetch.py

Writes internal/opportunities/raw.json. Every record carries the source it came
from and the URL it was read at, so any line on the published page can be traced
back. A source that fails is reported and skipped; the others still run.
"""
import os, io, re, json, ssl, time, datetime, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "raw.json")
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"}

try:
    import certifi
    CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    CTX = ssl.create_default_context()


def get(url, data=None, ctype=None, timeout=30):
    req = urllib.request.Request(url, data=data, headers=dict(UA))
    if ctype:
        req.add_header("Content-Type", ctype)
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        return r.read().decode("utf-8", "replace")


def item(stream, title, url, deadline=None, when=None, where=None,
         detail="", source="", confidence="stated"):
    return {"stream": stream, "title": " ".join((title or "").split()),
            "url": url or "", "deadline": deadline, "when": when, "where": where,
            "detail": " ".join((detail or "").split())[:400],
            "source": source, "deadline_confidence": confidence}


def _date(v):
    """A date out of whatever the feed felt like giving."""
    if not v:
        return None
    if isinstance(v, (datetime.date, datetime.datetime)):
        return v.strftime("%Y-%m-%d")
    s = str(v).strip()
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", s)
    if m:
        return m.group(0)
    for fmt in ("%d %b %Y", "%b %d, %Y", "%B %d, %Y", "%d %B %Y", "%m/%d/%Y", "%Y%m%d"):
        try:
            return datetime.datetime.strptime(s[:20].strip(), fmt).strftime("%Y-%m-%d")
        except ValueError:
            pass
    return None


# ---------- one reader per kind ----------

def read_yaml_ccfddl(src):
    import yaml
    out = []
    for conf in yaml.safe_load(get(src["url"])) or []:
        for c in conf.get("confs", []) or []:
            for tl in c.get("timeline", []) or []:
                out.append(item("conferences",
                                "%s %s — %s" % (conf.get("title", ""), c.get("year", ""),
                                                conf.get("description", "")),
                                c.get("link", ""), _date(tl.get("deadline")),
                                c.get("date"), c.get("place"),
                                tl.get("comment", ""), src["name"]))
    return out


def read_yaml_secdeadlines(src):
    import yaml
    out = []
    for c in yaml.safe_load(get(src["url"])) or []:
        for d in (c.get("deadline") or []):
            out.append(item("conferences",
                            "%s %s" % (c.get("name", ""), c.get("year", "")),
                            c.get("link", ""), _date(d), c.get("date"),
                            c.get("place"), "", src["name"]))
    return out


def read_yaml_aideadlines(src):
    import yaml
    out = []
    for c in yaml.safe_load(get(src["url"])) or []:
        out.append(item("conferences",
                        "%s %s — %s" % (c.get("title", ""), c.get("year", ""),
                                        c.get("full_name", "")),
                        c.get("link", ""), _date(c.get("deadline")),
                        c.get("date"), c.get("place"), "", src["name"]))
    return out


def read_rss(src):
    xml = get(src["url"])
    out = []
    for m in re.finditer(r"<item>(.*?)</item>", xml, re.S):
        b = m.group(1)

        def tag(t):
            mm = re.search(r"<%s>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</%s>" % (t, t), b, re.S)
            return re.sub(r"<[^>]+>", " ", mm.group(1)).strip() if mm else ""
        desc = tag("description")
        # WikiCFP puts the submission deadline inside the description
        dl = None
        dm = re.search(r"[Ss]ubmission [Dd]eadline[:\s]*([A-Za-z0-9,\s]{6,20})", desc)
        if dm:
            dl = _date(dm.group(1))
        out.append(item(src["stream"], tag("title"), tag("link"), dl,
                        None, None, desc, src["name"],
                        "parsed" if dl else "unknown"))
    return out


def read_grants_gov(src):
    out = []
    for kw in src.get("keywords", []):
        body = json.dumps({"rows": 40, "keyword": kw,
                           "oppStatuses": "forecasted|posted"}).encode()
        try:
            blob = json.loads(get("https://api.grants.gov/v1/api/search2",
                                  body, "application/json"))
        except Exception as e:
            print("    grants.gov %-28s %s" % (kw, str(e)[:44]))
            continue
        for h in (blob.get("data") or {}).get("oppHits", []) or []:
            out.append(item(src["stream"], h.get("title", ""),
                            "https://www.grants.gov/search-results-detail/" +
                            str(h.get("id", "")),
                            _date(h.get("closeDate")), None,
                            h.get("agencyName") or h.get("agencyCode"),
                            "%s · %s" % (h.get("agencyCode", ""), h.get("oppStatus", "")),
                            src["name"]))
        time.sleep(0.5)
    return out


def read_ajo(src):
    """AcademicJobsOnline has no feed, so the listing itself is read.

    Each institution is an <h3> heading followed by an <ol> of positions; a
    position is a link to /ajo/jobs/<id> whose text is the category, with the
    job title in the <span> beside it.
    """
    html = get(src["url"])
    out, seen = [], set()
    blocks = re.split(r'<h3 class="x1">', html)[1:]
    for block in blocks:
        head = re.sub(r"<[^>]+>", " ", block.split("</h3>")[0])
        where = " ".join(head.split())[:90]
        for m in re.finditer(
                r'<a href="/ajo/jobs/(\d+)"[^>]*>(.*?)</a>\]?\s*'
                r'(?:<span[^>]*>(.*?)</span>)?', block, re.S):
            jid, cat, title = m.group(1), m.group(2), m.group(3) or ""
            if jid in seen:
                continue
            seen.add(jid)
            cat = " ".join(re.sub(r"<[^>]+>", " ", cat).split())
            title = " ".join(re.sub(r"<[^>]+>", " ", title).split())
            label = ("%s — %s" % (where, title or cat)).strip(" —")
            out.append(item("jobs", label,
                            "https://academicjobsonline.org/ajo/jobs/" + jid,
                            None, None, where, cat, src["name"], "unknown"))
    return out


READERS = {"yaml_ccfddl": read_yaml_ccfddl, "yaml_secdeadlines": read_yaml_secdeadlines,
           "yaml_aideadlines": read_yaml_aideadlines, "rss": read_rss,
           "grants_gov": read_grants_gov, "ajo": read_ajo}


def main():
    with io.open(os.path.join(HERE, "sources.json"), encoding="utf-8") as fh:
        sources = json.load(fh)["sources"]

    rows, failed = [], []
    for src in sources:
        reader = READERS.get(src["kind"])
        if reader is None:
            failed.append((src["name"], "no reader for kind %s" % src["kind"]))
            continue
        try:
            got = reader(src)
        except Exception as e:
            failed.append((src["name"], str(e)[:70]))
            print("  FAIL %-40s %s" % (src["name"], str(e)[:60]))
            continue
        print("  ok   %-40s %4d" % (src["name"], len(got)))
        rows += got

    # Same opportunity from two feeds: keep the one that knows a deadline.
    best = {}
    for r in rows:
        key = re.sub(r"[^a-z0-9]", "", r["title"].lower())[:46] or r["url"]
        prev = best.get(key)
        if prev is None or (not prev["deadline"] and r["deadline"]):
            best[key] = r

    payload = {"fetched": int(time.time()), "items": list(best.values()),
               "failed": failed}
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=1)
    print("\n%d rows, %d after dedupe, %d source(s) failed"
          % (len(rows), len(best), len(failed)))


if __name__ == "__main__":
    main()
