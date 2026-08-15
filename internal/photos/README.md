# Photo pipeline

Turns a pile of photos into walls on the site. Nothing needs picking by hand.

## Running it

    python internal/photos/ingest.py  "<folder of photos>"
    python internal/photos/curate.py  --per-event 6
    python internal/photos/build_wall.py

`ingest` reads every photo once: when it was taken, where, which camera, a
perceptual hash, sharpness, exposure. iPhone HEIC is handled if `pillow-heif`
is installed. `curate` groups photos into events by time and place, drops
near-duplicate frames and the blurred or badly exposed, and keeps the best few
per event. `build_wall` writes web copies and the pages.

    pip install pillow pillow-heif

## Where photos come from

Anything on disk. An iCloud shared album downloaded to a folder, a Google Drive
folder, an export — the pipeline only needs a path. Photos in a folder named
`private` anywhere in the tree are read but never published.

## What is automatic and what is not

Automatic: grouping into events, place names, ordering, deduplication, quality
filtering, resizing, EXIF and GPS stripping on the published copies, page
generation.

By hand, in `shortlist.json` after curation: the `tags` on each photo (food,
plant, cat, street, view, people — these become the by-subject walls), the
`caption`, and `collection` if a photo belongs somewhere other than its place.
Editing that file is the whole editorial step; re-run `build_wall.py` after.

## Places

`places.json` maps GPS to place names offline, by nearest anchor within
`radius_km`. Add a line per new place. A photo with no GPS, or one too far from
every anchor, lands in "Elsewhere" rather than being guessed at.

## Output

Web copies in `content/.gitbook/assets/photos/`, two sizes per photo: a
thumbnail for the wall and a larger copy behind the link. Pages in
`content/personal/photo-collections/`, one per collection plus `by-subject.md`.
The walls are plain tables of images, which GitBook renders natively.
