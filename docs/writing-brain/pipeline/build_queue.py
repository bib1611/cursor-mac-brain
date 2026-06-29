#!/usr/bin/env python3
"""Build a priority-ordered transcription queue from the masterclass archive.

Highest-value writing/algorithm/virality recordings are placed first so the
distillation layer can begin as soon as the most useful transcripts land.
"""
import os
import sys

ARCHIVE = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "Masterclass-24-7")
)
OUT = os.path.join(os.path.dirname(__file__), "queue.txt")

MEDIA_EXTS = {".mp4", ".m4a", ".mp3", ".mov", ".wav", ".webm"}

# Channel base weights (higher = earlier).
CHANNEL_WEIGHT = {
    "content-creation": 60,
    "business-systems": 50,
    "growth-strategies": 40,
    "tip-of-the-day": 30,
    "create247": 25,
    "personal-branding": 20,
    "marketing-and-sales": 20,
}

# Filename keyword bonuses (writing craft + algorithm first).
KEYWORD_BONUS = [
    (40, ["virality", "viral", "explode"]),
    (40, ["writers_block", "writing", "hypnotic", "reverse", "lisec"]),
    (38, ["algorithm", "decoding", "growing on x", "ttt"]),
    (32, ["content_strategy", "content strategy", "infinite", "idea", "blueprint"]),
    (30, ["hook", "tweet", "offers", "offer"]),
    (28, ["email", "subs", "comment", "substack"]),
    (24, ["builder_identity", "monetize", "aaron", "tytodt", "eddy", "culture", "cole"]),
    (16, ["tips", "101", "spaces"]),
]


def score(path):
    rel = os.path.relpath(path, ARCHIVE).lower()
    channel = rel.split(os.sep)[0]
    s = CHANNEL_WEIGHT.get(channel, 10)
    name = os.path.basename(rel)
    for bonus, kws in KEYWORD_BONUS:
        if any(k in name for k in kws):
            s += bonus
            break
    return s


def main():
    files = []
    for root, _dirs, names in os.walk(ARCHIVE):
        if os.path.basename(root) != "attachments":
            continue
        for n in names:
            if os.path.splitext(n)[1].lower() in MEDIA_EXTS:
                files.append(os.path.join(root, n))

    # Sort by score desc, then smaller file first (quick wins within a tier).
    files.sort(key=lambda p: (-score(p), os.path.getsize(p)))

    with open(OUT, "w") as f:
        for p in files:
            f.write(p + "\n")

    total_bytes = sum(os.path.getsize(p) for p in files)
    print(f"queued {len(files)} files, {total_bytes/1e9:.1f} GB -> {OUT}")
    for p in files[:8]:
        print(f"  [{score(p):>3}] {os.path.relpath(p, ARCHIVE)}")


if __name__ == "__main__":
    main()
