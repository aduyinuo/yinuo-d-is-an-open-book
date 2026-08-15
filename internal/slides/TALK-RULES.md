# How these decks are built

Distilled from Jonathan Shewchuk, *Giving an Academic Talk*, and Simon Peyton
Jones, *How to Give a Great Research Talk*.

## What a 20-minute talk is for

An advertisement for the paper, not a replacement for it. The goal is that
people leave wanting to read it. Peyton Jones: the paper is the beef, the talk
is the advertisement — don't confuse the two.

## The four questions every deck must answer

1. Why is this problem worth solving?
2. What does this method accomplish that no previous method does — and what idea
   makes that possible? (Both halves. Most talks answer only the second.)
3. What is the evidence, and under what circumstances?
4. What is the one idea to take home? One, not five.

## Shape (20 minutes, ~18–20 slides, roughly a slide a minute)

| Minutes | Slides | What |
|---|---|---|
| 0–4  | 4–5 | The problem, why it matters, the gap in prior work |
| 4–9  | 5–6 | The idea, then the method — picture first, formalism after |
| 9–16 | 6–7 | Setup, then results, one claim per slide |
| 16–18 | 2 | Limitations and what's next |
| 18–20 | 1 | The one idea again, and where to find the paper |

Onion, not clew: state the main message early, then add layers, returning to it.
A listener who drifts for a minute should still be able to rejoin.

## Slide rules

* Twelve words on a slide is already too many. Pictures first, text only where a
  picture fails.
* Titles carry the message. A title says what the slide argues, not what it
  contains: "Factoring keeps the adversary's error contained", not "Architecture".
* Body text 38pt, titles 42–50pt, sans-serif only.
* No logos, no running titles, no wasted margins.
* Label the variables inside a formula, on the slide, every time it appears.
* One idea per slide.

## Annotation

Slides are not the speaker's index cards. Everything the speaker would say goes
in the notes, not on the slide. In this repository the notes are the annotation
shown beneath each slide on the site, so they are written to be read as well as
spoken: full sentences, no telegraphese.

`---` alone on a line in the notes splits the narration so it advances in steps
while the slide stays up.

## Where the words come from

Before writing a deck, read that project's meeting notes, Max's own drafts, and
the papers it cites. Take the vocabulary from those. Where a sentence already
exists that expresses the point, use it rather than inventing a new one — the
source phrasing is almost always plainer and more accurate than a fresh attempt.

Do not address the audience as "you". Do not reach for showy constructions,
rhetorical questions used as decoration, or contrast-for-effect. Plain
declarative sentences in the project's own terms.

## Unfinished work

Where a result is not in yet, the slide says so in the open, marked
`[PLACEHOLDER]`, with the note recording what would have to be true for the
claim to hold. Nothing is asserted that the folder does not support.
