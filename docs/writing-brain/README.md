# Writing Brain

A distilled, portable knowledge base built from the Masterclass 24/7 archive (an $8k+ paid Discord of X/Substack masterclasses) fused with Adam Johnsson's voice and anti-slop standard. Load it into any LLM to write content with years of operator-level craft, in Adam's voice.

## The one file you load
**`WRITING-BRAIN.md`** is the master file. Paste or attach it to any LLM (Claude, GPT, Codex, Cursor, Grok) before asking it to write or critique. It is self-contained.

## Folder structure
```
Writing-Brain/
  WRITING-BRAIN.md        # THE master distilled brain (load this)
  README.md               # this file
  swipe-files/
    hooks.md              # full hook + thread + reply + research swipe file
  distilled/by-channel/   # per-source distilled notes (one per recording/PDF)
  extracted-pdfs/         # plain-text of all 10 masterclass PDFs
  transcripts/            # whisper transcripts of the 44 recordings (filling in)
  pipeline/
    build_queue.py        # builds priority-ordered transcription queue
    queue.txt             # 44 files, writing/algorithm recordings first
    transcribe.sh         # resumable whisper batch (base.en)
    transcribe.log        # progress log
    distill-instructions.md  # how to turn each transcript into a brain note
```

## Status
- Voice + anti-slop standard: fused into `WRITING-BRAIN.md` PART 0 and PART 1.
- 10 PDFs: extracted to `extracted-pdfs/` and mined into the brain.
- 44 recordings (~8 GB): transcribing locally with whisper `base.en`, highest-value writing/algorithm files first. Runs at roughly 5x realtime on this machine.
- Distillation: PDFs + existing PINNED digests are folded in. Recording transcripts get distilled as they finish (see below).

## How transcription works
- `pipeline/transcribe.sh` reads `queue.txt` and writes one `.txt` per file into `transcripts/`. It is resumable: rerun it any time and it skips files already transcribed.
- To restart it: `cd pipeline && bash transcribe.sh` (or with a bigger model: `WHISPER_MODEL=small.en bash transcribe.sh`).
- Rebuild the queue if files change: `python3 pipeline/build_queue.py`.

## How to keep distilling (turning audio into brain)
When transcripts land, follow `pipeline/distill-instructions.md`: distill each transcript into a note in `distilled/by-channel/`, then fold genuinely new frameworks into `WRITING-BRAIN.md` and new hooks into `swipe-files/hooks.md`. Keep the brain tight; detail lives in the notes.

## Still to capture (Discord scrape was unfinished)
The original archive (`../_MASTER-INDEX.md`) notes more to pull: full non-pinned history on several channels, and two untouched servers (Course Builders, Masterclass 24/7 Fall). Those are separate from this distillation and can be added later.
