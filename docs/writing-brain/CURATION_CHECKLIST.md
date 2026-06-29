# Writing Brain — Curation Checklist

Operating procedures for keeping the brain clean. Pairs with `SCHEMA.md` (the canon).
Run these when reconciling forks, distilling new transcripts, or doing weekly hygiene.

Last updated: 2026-06-19

---

## 1. Reconcile the divergent `distilled/` root fork (one-time)

The `distilled/` root holds 17 notes that share filenames with `distilled/by-channel/`
but have **different contents**. `by-channel` is canonical (SCHEMA §2). Merge, then quarantine.

For each of the 17 root files:
- [ ] Diff root vs `by-channel` twin. Read both fully — do not trust filename equality.
- [ ] Identify unique, correct content in the root copy (paragraphs, examples, frameworks
      not present in `by-channel`).
- [ ] Merge that unique content into the `by-channel` note. Keep the `by-channel` structure.
- [ ] Bump `updated_at` on the merged note.
- [ ] Move the root copy to `_deprecated/distilled-root-fork/` (do NOT delete).
- [ ] Log the reconciliation: filename, what was merged, date.

When all 17 are done:
- [ ] `distilled/` root contains only `by-channel/`.
- [ ] Rename `by-channel/` → `brain/` and refolder every note into its `category` (SCHEMA §5).
- [ ] Regenerate `_INDEX.md`.
- [ ] After one clean release with no regressions, purge `_deprecated/distilled-root-fork/`.

---

## 2. Dedupe divergent / overlapping notes (recurring)

Two notes "overlap" when they teach the same framework or cover the same recording.

- [ ] Cluster candidates: same `instructor`, same `category`, or embedding cosine > ~0.85.
- [ ] For each cluster, read all members. Decide one of:
  - **Merge** → fold into one note, set the others' `status: deprecated`, move to `_deprecated/`.
  - **Keep both** → if genuinely distinct angles, set `related` ids on each and move on.
  - **Supersede** → newer note sets `supersedes: [old-id]`; old note `status: deprecated`.
- [ ] Exactly one note per cluster keeps `canonical: true`.
- [ ] Never have two `canonical: true` notes teaching the same framework.
- [ ] Bump `updated_at` on anything edited; regenerate `_INDEX.md`.

---

## 3. Distill a new transcript / PDF into the brain

- [ ] Source sits in `raw/transcripts/` or `raw/extracted-pdfs/` (immutable).
- [ ] Extract only named frameworks, numbered systems, reusable swipe examples.
      Skip filler, small talk, intros.
- [ ] One framework per `##` section (this is the chunk boundary, SCHEMA §4).
- [ ] Create the note in `brain/<category>/<instructor>--<topic>.md` (SCHEMA §7).
- [ ] Write full frontmatter (SCHEMA §3). Required fields must all be present:
      `title, category, tags, source_url, source_drive_id, status, updated_at`.
- [ ] Set `source_file` + `source_drive_id` pointing at the raw source.
- [ ] Report back three lists:
  1. New frameworks worth folding into `WRITING-BRAIN.md` (candidates only — don't auto-fold).
  2. New hooks/CTAs/subject lines for the `swipe-files/`.
  3. Overlaps with existing notes (give their `id`s) → route to §2.

---

## 4. Fold into the master (`WRITING-BRAIN.md`)

A framework earns a place in the master ONLY if it changes how you write.

- [ ] Reference material, single-source claims (`confidence: low`), and worksheets
      stay as notes — do NOT fold them.
- [ ] When folded, set the note's `status: folded` and `folded_into_master: true`.
- [ ] Keep PART 0 (voice) and PART 1 (rubric) untouched unless the voice spec itself changes.
- [ ] Master must stay loadable as Tier-1. If it bloats, push detail back down to notes.

---

## 5. Weekly hygiene

- [ ] `pipeline/lint.py` passes (see §6) — no missing frontmatter, no unknown tags,
      no duplicate `id`, no broken `source_file`.
- [ ] Every new `raw/` source has a `brain/` note; every `brain/` note has a valid source.
- [ ] No two `canonical: true` notes teach the same framework (§2).
- [ ] `folded_into_master` flags match reality (spot-check 3 notes against the master).
- [ ] `_INDEX.md` regenerated from frontmatter.
- [ ] Changed notes re-chunked + re-embedded into the vector index.
- [ ] `_deprecated/` reviewed — purge anything past one clean release.

---

## 6. Lint rules (enforce before any brain commit)

`pipeline/lint.py` must fail the build on any of:
- [ ] A `brain/` note missing required frontmatter keys
      (`title, category, tags, source_url, source_drive_id, status, updated_at`).
- [ ] `category` not in the SCHEMA §5 taxonomy.
- [ ] Any `tag` not in the SCHEMA §6 controlled vocabulary.
- [ ] Duplicate `id` across notes.
- [ ] A `source_file` path that does not exist on disk.
- [ ] A note in the wrong folder for its `category`.
- [ ] Two `canonical: true` notes sharing the same framework cluster (warn, don't hard-fail).

---

## 7. Definition of done (a clean brain)

- One canonical distilled layer (`brain/`), foldered by category, no forks.
- Every note has valid frontmatter and a live provenance link to `raw/`.
- No divergent duplicates; every overlap resolved to merge/keep/supersede.
- `WRITING-BRAIN.md` carries synthesis only and still loads small.
- `_INDEX.md` and the vector index reflect current state.
- `_deprecated/` is empty or scheduled for purge.
