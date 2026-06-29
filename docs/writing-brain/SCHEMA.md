# Writing Brain — Information Architecture & Schema

Governance spec for the Masterclass 24/7 writing brain. This file is canon for
how the brain is structured, named, tagged, and chunked. If a tool, script, or
agent disagrees with this file, this file wins.

Last updated: 2026-06-19

---

## 1. Source-of-truth folders

There is exactly **one** canonical home for each layer. No layer may exist in two places.

```
Writing-Brain/
  WRITING-BRAIN.md        # MASTER synthesis. Tier-1 load. Voice (PART 0) + rubric (PART 1).
  SCHEMA.md               # this file — IA + schema canon
  CURATION_CHECKLIST.md   # how to dedupe, distill, and keep the brain clean
  _INDEX.md               # GENERATED. Table of every note + its frontmatter. Never hand-edit.

  brain/                  # CANONICAL distilled notes, foldered by category (see §5)
    x-algorithm/
    x-craft/
    x-growth/
    content-creation/
    content-strategy/
    consistency-systems/
    offers/
    email/
    book-launch/
    substack/
    personas/
    meta-frameworks/

  swipe-files/            # CANONICAL reusable, copy-paste assets
    hooks.md
    ctas.md
    subject-lines.md

  raw/                    # CANONICAL source layer (provenance, never loaded for writing)
    transcripts/          # whisper transcripts of recordings
    extracted-pdfs/       # plain text of source PDFs

  pipeline/               # build/transcribe/lint scripts + logs
  _deprecated/            # quarantine for retired forks (see §2). Not loaded, not indexed.
```

### Canonical-vs-derived rule
- `raw/` is **immutable source**. Never edit a transcript or extracted PDF to "fix" content; corrections live in the distilled note.
- `brain/` is the **single distilled layer**. One note per source recording/PDF.
- `WRITING-BRAIN.md` is **synthesis only** — a framework earns a place here only if it changes how you write. Everything else stays a note and surfaces via retrieval.

---

## 2. Deprecation of the orphaned `distilled/` root fork

**Decision:** `distilled/by-channel/` is the canonical distilled set. The 17 notes in
`distilled/` **root** are a divergent older fork and are **deprecated**.

The two forks share filenames but have **different contents** (verified 2026-06-19),
so the root copies may hold unique paragraphs. They must be **merged, then quarantined**,
never blind-deleted.

Procedure (run via CURATION_CHECKLIST.md §1 before retiring):
1. For each root file, diff against its `by-channel` twin.
2. Merge any unique, correct content into the `by-channel` (canonical) note.
3. Move the root copy to `_deprecated/distilled-root-fork/` with a dated note.
4. Once all 17 are reconciled, the `distilled/` root holds only `by-channel/`, which
   is then renamed to `brain/` and refoldered by category (§5).

`_deprecated/` is excluded from Tier-1/2/3 retrieval and from the vector index.
It exists only as a recovery net; purge after one clean release.

---

## 3. Frontmatter schema

Every note in `brain/` MUST open with YAML frontmatter. Required fields first;
optional extension block second.

```yaml
---
# --- REQUIRED ---
title: "TTT — Everything About Growing on X"   # human title, quoted
category: x-growth                              # exactly one, from §5 taxonomy
tags: [reach, reply-strategy, posting-cadence]  # from §6 controlled vocab only
source_url: ""                                  # web link to recording/PDF, or "" if none
source_drive_id: "1AbC...xyz"                   # Google Drive file ID of the source
status: distilled                               # see status lifecycle below
updated_at: 2026-06-19                          # ISO date of last edit to THIS note

# --- OPTIONAL (add when known; lint does not require) ---
id: x-growth-ttt-everything                     # stable slug; never changes once set
instructor: "TTT"                               # source author/channel, canonical spelling
source_file: raw/transcripts/TYTODT.txt         # local provenance path
platform: [x]                                   # x | substack | email | book | cross
funnel_stage: [awareness, engagement]           # awareness|engagement|capture|offer|retention
canonical: true                                 # the one true copy if duplicates exist
supersedes: []                                  # ids this note replaces
related: [x-algorithm-decoding]                 # sibling note ids
folded_into_master: false                       # is this content already in WRITING-BRAIN.md?
confidence: high                                # high|medium|low (corroborated vs single-source)
---
```

### Field rules
- **title** — quoted string. No leading `#`. The note body still opens with an `# H1`.
- **category** — exactly one value from §5. Drives the folder it lives in.
- **tags** — list, lowercase, from §6 only. Unknown tags fail lint.
- **source_url** — canonical external link if one exists (Drive share URL, YouTube, etc.). Empty string allowed, never omit the key.
- **source_drive_id** — the Google Drive file ID (the `…/d/<ID>/…` segment). This is the durable pointer back to source even if the file is renamed/moved in Drive.
- **status** — lifecycle: `raw` → `distilled` → `folded` → `deprecated`.
  - `raw`: stub exists, not yet distilled.
  - `distilled`: complete note, lives in `brain/`.
  - `folded`: distilled AND its new frameworks merged into `WRITING-BRAIN.md`.
  - `deprecated`: superseded; sits in `_deprecated/`, excluded from retrieval.
- **updated_at** — bump on every content edit. Used to detect staleness in `_INDEX.md`.

---

## 4. Chunking rules (for the vector index)

Chunk on **meaning**, not token count.

1. **One framework per chunk.** A named concept, a numbered system, or a single
   worksheet = one chunk. Never split a numbered list across chunks.
2. **Target 200–500 tokens, hard cap ~800.** If a section exceeds the cap, split on
   `##` headings only — never mid-example, never mid-list.
3. **Swipe assets are atomic.** One hook = one chunk. One CTA = one chunk. One subject
   line = one chunk. Retrieval must return whole, usable examples.
4. **Inherit frontmatter as chunk metadata.** Every chunk carries its note's
   `category`, `tags`, `instructor`, `platform`, `id`. Enables filtered queries
   (`category:offers AND platform:x`).
5. **Breadcrumb prefix.** Prepend each chunk with `[category / instructor / section]`
   so an out-of-context chunk still self-identifies.
6. **Never chunk `raw/`.** Only `brain/` and `swipe-files/` are indexed. Raw is provenance.

---

## 5. Category taxonomy

Exactly twelve categories. One per note. Category = folder.

| category | scope |
|---|---|
| `x-algorithm` | how the X algorithm ranks and distributes |
| `x-craft` | tweet/thread/hook mechanics, roasts, structure |
| `x-growth` | followers, replies, comment strategy, reach |
| `content-creation` | idea→draft engine, identity, rehumanizing AI output |
| `content-strategy` | cadence, writer's block, daily systems |
| `consistency-systems` | showing up without burnout |
| `offers` | offer design, pricing, validation |
| `email` | list building, email craft, subject lines |
| `book-launch` | Amazon, subtitles, launch playbooks |
| `substack` | Substack-specific growth + strategy |
| `personas` | writing personas, voice modeling |
| `meta-frameworks` | cross-cutting synthesis that spans categories |

If a note truly spans two, pick the dominant category and add the other as a `related` id.

---

## 6. Controlled tag vocabulary

Tags are retrieval facets. Pick from this list; do not free-type. Extend the list
deliberately (via PR to this file), never inline.

- **Mechanics:** `hook`, `thread-structure`, `reply-strategy`, `cta`, `subject-line`,
  `offer-stack`, `pricing`, `lead-magnet`, `auto-dm`, `posting-cadence`, `reach`,
  `engagement-bait`, `repurposing`
- **Outcomes:** `growth`, `monetization`, `retention`, `authority`
- **Format:** `swipe`, `worksheet`, `framework`, `case-study`, `checklist`

---

## 7. Naming conventions

### Distilled notes (`brain/<category>/`)
```
<instructor-kebab>--<topic-kebab>.md
```
- Lowercase, kebab-case. `--` separates instructor from topic, nothing else.
- Category lives in the folder, NOT the filename (no `business-systems--` prefix).
- Examples: `ttt--everything-growing-on-x.md`, `schenck--five-part-offer-framework.md`,
  `culture-critic--tweet-roast.md`.
- If no clear instructor, use the source: `mc26--writing-personas.md`.

### Swipe files
Single topical file per asset type: `hooks.md`, `ctas.md`, `subject-lines.md`.

### Raw sources (`raw/`)
Keep the original source filename. Do not rename. The distilled note's
`source_file` + `source_drive_id` are the link back.

### IDs (`id` frontmatter field)
```
<category>-<instructor>-<topic>
```
Stable forever once assigned. Renaming a file does not change its `id`.

---

## 8. Retrieval tiers (how the brain is loaded)

1. **Tier 1 — always:** `WRITING-BRAIN.md` PART 0 (voice) + PART 1 (rubric).
2. **Tier 2 — intent-routed:** load the category folder(s) the task needs
   (thread → `x-craft/` + `x-growth/` + `swipe-files/hooks.md`; offer → `offers/`).
3. **Tier 3 — semantic:** vector search over `brain/` + `swipe-files/` chunks with
   metadata filters, for cross-category "what did anyone say about X" questions.

Never dump the whole brain. Tier 2 + 3 keep context lean and answers sharp.
