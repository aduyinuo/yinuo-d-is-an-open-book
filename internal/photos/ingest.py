#!/usr/bin/env python3
"""
Step 1 of the photo pipeline: look at every photo once and write down what it is.

    python internal/photos/ingest.py <source-folder>

Reads EXIF (when, where, which camera), converts iPhone HEIC to JPEG, computes a
perceptual hash so near-identical frames can be spotted later, and scores
sharpness and exposure. Writes internal/photos/photos.json. Touches nothing else,
so it is safe to re-run.
"""
import os, sys, json, math, datetime, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "photos.json")
EXT = (".jpg", ".jpeg", ".png", ".heic", ".heif", ".webp", ".tif", ".tiff")


def _pil():
    from PIL import Image
    try:
        import pillow_heif                     # iPhone photos
        pillow_heif.register_heif_opener()
    except Exception:
        pass
    return Image


def exif_of(im):
    """when taken, gps, camera — tolerant of missing tags."""
    out = {"taken": None, "lat": None, "lon": None, "camera": None}
    try:
        ex = im.getexif()
        if not ex:
            return out
        from PIL.ExifTags import TAGS, GPSTAGS
        tags = {TAGS.get(k, k): v for k, v in ex.items()}
        # DateTimeOriginal lives in the Exif sub-IFD, not the top level
        try:
            sub = ex.get_ifd(0x8769)
            for k, v in (sub or {}).items():
                tags.setdefault(TAGS.get(k, k), v)
        except Exception:
            pass
        dt = tags.get("DateTimeOriginal") or tags.get("DateTime")
        if dt:
            try:
                out["taken"] = datetime.datetime.strptime(
                    str(dt), "%Y:%m:%d %H:%M:%S").isoformat()
            except ValueError:
                pass
        make, model = tags.get("Make"), tags.get("Model")
        out["camera"] = " ".join(str(x).strip() for x in (make, model) if x) or None
        gps_ifd = ex.get_ifd(0x8825) if hasattr(ex, "get_ifd") else None
        if gps_ifd:
            g = {GPSTAGS.get(k, k): v for k, v in gps_ifd.items()}
            def deg(v, ref):
                d, m, s = [float(x) for x in v]
                val = d + m / 60.0 + s / 3600.0
                return -val if ref in ("S", "W") else val
            if "GPSLatitude" in g and "GPSLongitude" in g:
                out["lat"] = round(deg(g["GPSLatitude"], g.get("GPSLatitudeRef", "N")), 6)
                out["lon"] = round(deg(g["GPSLongitude"], g.get("GPSLongitudeRef", "E")), 6)
    except Exception:
        pass
    return out


def phash(im, size=8):
    """Average hash — cheap, good enough to catch burst duplicates."""
    g = im.convert("L").resize((size, size))
    px = list(g.getdata()) if not hasattr(g, 'get_flattened_data') else list(g.get_flattened_data())
    avg = sum(px) / len(px)
    bits = "".join("1" if p > avg else "0" for p in px)
    return "%016x" % int(bits, 2)


def sharpness(im, side=256):
    """Variance of a Laplacian-ish difference. Higher is crisper."""
    g = im.convert("L")
    g.thumbnail((side, side))
    px = list(g.getdata()) if not hasattr(g, 'get_flattened_data') else list(g.get_flattened_data()); w, h = g.size
    if w < 3 or h < 3:
        return 0.0
    vals = []
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            i = y * w + x
            vals.append(abs(4 * px[i] - px[i-1] - px[i+1] - px[i-w] - px[i+w]))
    m = sum(vals) / len(vals)
    return round(sum((v - m) ** 2 for v in vals) / len(vals), 2)


def exposure(im, side=128):
    """Mean luminance 0..1 and the share of clipped pixels."""
    g = im.convert("L"); g.thumbnail((side, side))
    px = list(g.getdata()) if not hasattr(g, 'get_flattened_data') else list(g.get_flattened_data())
    dark = sum(1 for p in px if p < 8) / len(px)
    blown = sum(1 for p in px if p > 247) / len(px)
    return round(sum(px) / len(px) / 255.0, 3), round(dark + blown, 3)


def main(src):
    Image = _pil()
    rows, n = [], 0
    for dirpath, dirnames, files in os.walk(src):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        private = "private" in os.path.relpath(dirpath, src).lower().split(os.sep)
        for f in sorted(files):
            if not f.lower().endswith(EXT) or f.startswith("."):
                continue
            p = os.path.join(dirpath, f)
            try:
                with Image.open(p) as im:
                    im.load()
                    meta = exif_of(im)
                    lum, clipped = exposure(im)
                    rows.append({
                        "path": p,
                        "rel": os.path.relpath(p, src),
                        "folder": os.path.relpath(dirpath, src),
                        "private": private,
                        "w": im.width, "h": im.height,
                        "portrait": im.height > im.width,
                        "phash": phash(im),
                        "sharpness": sharpness(im),
                        "luminance": lum,
                        "clipped": clipped,
                        **meta,
                    })
                    n += 1
                    if n % 100 == 0:
                        print("  read %d..." % n, flush=True)
            except Exception as e:
                print("  skipped %s (%s)" % (f, e))
    doc = {"source": os.path.abspath(src),
           "scanned": datetime.datetime.now().isoformat(timespec="seconds"),
           "photos": rows}
    json.dump(doc, open(OUT, "w", encoding="utf-8", newline="\n"),
              ensure_ascii=False, indent=1)
    withgps = sum(1 for r in rows if r["lat"] is not None)
    withdate = sum(1 for r in rows if r["taken"])
    print("read %d photos — %d with a date, %d with GPS" % (len(rows), withdate, withgps))
    print("wrote", OUT)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("usage: ingest.py <source-folder>")
    main(sys.argv[1])
