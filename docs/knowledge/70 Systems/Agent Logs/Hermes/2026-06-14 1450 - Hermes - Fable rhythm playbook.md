# Hermes - Fable-5 rhythm playbook (Kashef video method)

Date: 2026-06-14 ~14:50
Trigger: Adam asked "can you do this with yourself" re youtu.be/B95cu7seTm8 — then "go for it."

## What ran (real, this session)
- Verified corpus: 1,019 Claude Code JSONL (1,000 sessions), 250 Codex, 245 Hermes.
- Verified model tags: opus-4-7 7063, sonnet-4-6 310, opus-4-8 236, fable-5 121.
- Wrote parser: ~/.hermes/scripts/fable_rhythm.py
- Output playbook: ~/.deadhidden-os/ops/fable-rhythm-playbook.md

## Key finding
Solid: Fable narrates ~70% less (245 chars/turn vs ~812-912) and is Bash-first (74% of calls).
Noisy: Fable edit-discipline % rests on n=6 edits — flagged as hint not law.
Highest-EV real fix: opus-4-7 read-before-edit only 32% on 448 real edits.

## Not done (by design)
Nothing auto-injected. Playbook is read-and-decide. No SOUL.md / CLAUDE.md / hook changes made.
