# AGENTS — Writing Contract

Updated: 2026-06-28

**If you write ANY prose in Adam's name, load this file first, then obey the gate.**
This is NOT limited to brand content. It covers tweets, X articles, threads, Substack
posts, Notes, emails, reader replies, product copy, subtitles, and hooks. It ALSO covers
resumes, cover letters, job-application copy, bios, and spec or sample writing, including
commercial and off-brand pieces. The test is simple: if Adam's name will be on it, the
gate applies. There is no carve-out for "this is not brand content." Applies to Codex,
Claude Code, Hermes/blu, Chorus/Jarvis, Stanley, and any dispatched sub-agent.

(2026-06-23: scope widened after em dashes shipped in off-brand DR job samples that
skipped the gate on a "not brand content" rationalization. The gate is content-agnostic.)

This file is a **router + contract**, not a copy of the brain. The voice rules and
craft library each have exactly ONE canonical home (below). Do not fork them here.

---

## 1. The gate (non-negotiable, every draft)

Before you write, load the canonical voice contract:

- `/Users/adamjohnsson/voice-DNA.md` — the single-file voice gate (banned phrases,
  rhythm rules, verbatim samples, pre-flight checklist). **This is canonical. Read it.**
  Mirror: `~/Documents/Obsidian Vault/70 Systems/Voice/voice-DNA.md`.

Before you ship, run the **pre-flight checklist** (voice-DNA.md §1) and the
**8-dimension anti-slop score** (WRITING-BRAIN.md PART 1). Pass = 7+ on every
dimension, 60+ total, zero instant-kill words. Adam would rather kill a draft than
ship slop. If any box fails, rewrite — do not ship.

### Hard backstop (works even if the files above are offloaded)
- **KJV only.** Quote exactly, never paraphrase. Never NIV/ESV/NLT/NASB/NKJV/MSG/CSB
  (FaithWall is the only exception). One verse carried, never a stack. It appears
  mid-thought; never "The Bible says."
- **Voice:** staccato, fragments, periods over commas, heavy white space. ~7–8
  words/sentence on X, ~9.5 on Substack. "That's you. That's me." Stand in the dirt
  with the reader, never preach down. Write from the wound, not from theory.
- **No em dashes. No emojis in content. No hedging. No cheerleader openers.**
- **No links in tweet bodies.** Post clean, drop the link in the self-reply.
- **Substack links:** `open.substack.com/pub/biblicalman/p/<slug>?r=2t2o3r&utm_medium=ios`.
- **Sign-off is literally `Adam`.** Public byline is `Adam Johnson` (single s).
- **Cold opens lead with "Bible," not "KJV."** Save the translation stance for warm/
  discipleship content.
- **No pastor-bashing. No listicles by default** (confessional prose outperforms).
  **Never fabricate Adam's personal history** (dates, routes, dollar amounts, year counts).
- **60% of readers are women.** Thread female biblical stories alongside male.

If the backstop and the canonical files ever disagree, the canonical files win —
re-read them. The backstop exists only so an offline agent still writes on-voice.

---

## 2. The brain (craft library — route by task)

Canonical synthesis: **`…/Masterclass-Archive/Writing-Brain/WRITING-BRAIN.md`**
(PART 0 = voice, PART 1 = the quality gate, PARTS 2–13 = craft; patched 2026-06-29 with Substack/email direct-response rules in PARTS 5, 6, and 14). Per-source notes
live in `brain/<category>/`, indexed in `_INDEX.md`, governed by `SCHEMA.md`.

Full base path (Google Drive, local mount — may be cloud-offloaded; if a Read fails,
the file is offloaded, not missing — open it in Finder to pull it down, or fall back
to the §1 backstop):

```
/Users/adamjohnsson/Library/CloudStorage/GoogleDrive-thebiblicalman1611@gmail.com/My Drive/Masterclass-Archive/Writing-Brain/
```

### Load only what the task needs (never dump the whole brain)

| Task | Load |
|---|---|
| Tweet / hook | PART 3 (5 hooks) + PART 8 (laws) + `swipe-files/hooks.md` + `brain/x-craft/` |
| Thread | PART 4 (architecture) + PART 3 + `brain/x-craft/` + `brain/x-growth/` |
| Reach / algorithm question | PART 2 + `brain/x-algorithm/` |
| Replies / comments / growth | PART 13 (comment engine) + PART 9 + `brain/x-growth/` |
| Substack post | PART 5 (engine + editorial / launch / repair direct-response modes) + `brain/substack/` |
| Email | PART 6 (modern email + offers: deliverability, MPP, segmentation, lifecycle) + `brain/email/` |
| Offer / pricing / product | PART 6 + PART 14 SKU freshness guard + `brain/offers/` |
| Book / PDF launch | PART 10 + `brain/book-launch/` |
| Subtitle / product page | PART 6 (Lisec) + `brain/book-launch/joshua-lisec--book-subtitles.md` |
| De-slopping AI output | PART 7 (Lisec 6.5 tells) + `brain/content-creation/joshua-lisec--ai-rehumanizing.md` + `writing/ai-tells-guard.md` (local guard) |
| Cadence / writer's block / daily plan | PART 9 + PART 12 + `brain/content-strategy/` + `brain/consistency-systems/` |
| Persona / writing-to-one-reader | PART 10 + `brain/personas/` |
| Story-led DR / sales email / launch (Dakota register) | `writing/dakota-robertson-voice-profile.md` (local, always readable) + `swipe-files/dakota-ed-writing-dna.md` |
| Images / thumbnails | PART 11 |

Tier the load (SCHEMA §8): Tier 1 is always the voice gate. Tier 2 is the category
folder(s) the task needs. Tier 3 is semantic search over `brain/` + `swipe-files/`.

---

## 3. Prompting other models

If you dispatch this writing task to another model (GPT-5.5, Grok, a sub-agent),
load the prompt gate first: **`/Users/adamjohnsson/prompt-DNA.md`** — drop the role,
name the files, demand the report.

---

## 4. Canonical homes (do not duplicate — edit at the source)

| Layer | Canonical file | Never re-copy into |
|---|---|---|
| Voice gate | `~/voice-DNA.md` | this folder, agent souls, cowork |
| Quality gate / rubric | `WRITING-BRAIN.md` PART 1 | — |
| Craft library | `WRITING-BRAIN.md` PARTS 2–13 | — |
| Per-source notes | `brain/<category>/*.md` | — |
| Hooks / swipe assets | `swipe-files/hooks.md` | — |
| Prompt gate | `~/prompt-DNA.md` | — |

When the brain learns something new, fold it into the canonical file and bump its
`updated_at`. This router only points; it holds no craft of its own.
