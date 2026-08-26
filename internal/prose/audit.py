#!/usr/bin/env python3
"""
Find the sentences that announce, validate, or perform instead of stating.

    python internal/prose/audit.py                 # the site
    python internal/prose/audit.py <dir> [<dir>]   # anywhere else

The rule underneath all of it: **acknowledge with a fact, not with an
evaluation.** Not "B5 is right that the sentence does not establish parity" but
"The sentence in Section 6.1 claims parity without establishing it." The second
concedes more, costs fewer words, and sounds like someone who found the problem
rather than someone agreeing that a problem was found.

Five families, each with its own reason for being wrong:

  announce    A sentence about the reply that follows, doing none of the work
              the next sentence does. Throat-clearing.
  validate    Granting someone permission to have been right — "the concern is
              valid", "that is a fair point", "X is real". They did not need it,
              and it reverses who is judging whom.
  competence  Turning a concession into a display of understanding. Reviewers
              read it as spin, and it makes the concession less credible.
  intensify   Claiming precision in advance. It either shows up in the next
              three sentences or it does not; saying so only raises the bar.
  perform     Announcing structure instead of having it. "Three questions,
              three answers."

Every hit is a candidate, not a verdict. A contrast that carries meaning is
doing work. Read the line before changing it.
"""
import io, os, re, sys, glob

FAMILIES = [
    ("announce", re.compile(
        r"(?i)\b("
        r"the (?:short |real |honest )?answer is"
        r"|what follows"
        r"|this (?:section|page|note|report) (?:sets out|explains|describes|covers|will)"
        r"|here is (?:why|what|how)"
        r"|let me (?:explain|start|begin)"
        r"|to be clear"
        r"|worth (?:saying|noting) (?:that|here)"
        r"|the point is"
        r"|in short"
        r")\b")),

    # Only validation of a person or their argument. "real services" and "the
    # hosts are real" are facts about the world, not permission to have been
    # right, so the subject has to be a claim or an objection.
    ("validate", re.compile(
        r"(?i)("
        r"(?:that|this|the|your|their|his|her)\s+"
        r"(?:concern|point|objection|criticism|comment|question|worry|reading|"
        r"inconsistency|complaint|observation|critique)\s+"
        r"(?:is|was|are|were)\s+"
        r"(?:real|valid|fair|right|correct|reasonable|legitimate|well[- ]taken)"
        r"|(?:is|are|was|were) right (?:that|to)"
        r"|correctly (?:notes|points out|observes|identifies|says)"
        r"|rightly (?:notes|points|observes|says)"
        r"|good (?:catch|point|question)"
        r"|you(?:'re| are) right"
        r"|fair (?:point|enough)"
        r"|a fair (?:point|criticism|reading)"
        r")")),

    # Turning a concession into a display of understanding. "Dyna-PSRO does
    # exactly this" is a fact about Dyna-PSRO; "that is precisely the problem"
    # is a performance.
    ("competence", re.compile(
        r"(?i)("
        r"(?:that|this|which) is (?:precisely|exactly) (?:the|what|why|where|how)"
        r"|precisely the (?:problem|question|issue|reason|point|difficulty)"
        r"|the real (?:problem|question|issue|reason|point) (?:is|was)"
        r"|what (?:is|was) (?:really|actually) (?:going on|happening|at stake)"
        r"|to be precise"
        r")")),

    ("intensify", re.compile(
        r"(?i)\b("
        r"precisely|exactly|genuinely|truly|deeply|profoundly|fundamentally"
        r"|essentially|ultimately|crucially|importantly|notably|indeed"
        r"|simply|actually|clearly|obviously|of course"
        r")\b")),

    ("perform", re.compile(
        r"(?i)("
        r"\b(?:two|three|four|five) (?:questions|answers|things|reasons|points|parts)\b"
        r"[,.]?\s*(?:two|three|four|five)?\b"
        r"|\bThe (?:first|second|third|fourth) is\b"
        r"|\b(?:first|second|third)ly\b"
        r"|\bas (?:noted|mentioned|discussed) (?:above|below|earlier)\b"
        r")")),
]

SKIP_DIRS = {".git", "node_modules", ".gitbook", "__pycache__", "build",
             "dist", ".latex-build"}


def strip_markup(s, tex=False):
    if tex:
        s = re.sub(r"(?m)^%.*$", "", s)
        s = re.sub(r"\\(?:begin|end)\{[^}]*\}", " ", s)
        s = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?", " ", s)
        s = re.sub(r"[{}&$]", " ", s)
    else:
        s = re.sub(r"(?s)^---.*?\n---\n", "", s)          # frontmatter
        s = re.sub(r"(?s)```.*?```", " ", s)              # fenced code
        s = re.sub(r"(?s)<table.*?</table>", " ", s)      # generated tables
        s = re.sub(r"(?s)<figure.*?</figure>", " ", s)
        s = re.sub(r"<[^>]+>", " ", s)
        s = re.sub(r"\{%.*?%\}", " ", s)
        s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)    # links keep their text
    return s


def sentences(t):
    for para in t.split("\n"):
        para = para.strip()
        if not para or para.startswith(("|", "#", "*", "-", ">")):
            continue
        for s in re.split(r"(?<=[.!?])\s+", para):
            s = s.strip()
            if len(s.split()) >= 4:
                yield s


def audit_file(path):
    tex = path.endswith(".tex")
    try:
        raw = io.open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return []
    text = strip_markup(raw, tex)
    hits = []
    for s in sentences(text):
        for name, rx in FAMILIES:
            m = rx.search(s)
            if m:
                hits.append((name, m.group(0).strip(), s))
    return hits


def walk(roots):
    for root in roots:
        if os.path.isfile(root):
            yield root
            continue
        for dirpath, dirnames, files in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for f in files:
                if f.endswith((".md", ".tex")):
                    yield os.path.join(dirpath, f)


def main():
    roots = sys.argv[1:] or [os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "..", "content")]
    totals, per_file = {}, []
    for path in sorted(walk(roots)):
        hits = audit_file(path)
        if not hits:
            continue
        per_file.append((path, hits))
        for name, _phrase, _s in hits:
            totals[name] = totals.get(name, 0) + 1

    for path, hits in per_file:
        print("\n%s  (%d)" % (os.path.relpath(path), len(hits)))
        for name, phrase, s in hits:
            print("  %-11s %-24s %s" % (name, '"' + phrase[:22] + '"', s[:96]))

    print("\n" + "-" * 60)
    for name, _rx in FAMILIES:
        print("  %-12s %4d" % (name, totals.get(name, 0)))
    print("  %-12s %4d across %d file(s)"
          % ("TOTAL", sum(totals.values()), len(per_file)))


if __name__ == "__main__":
    main()
