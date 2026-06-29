# Reconciliation Log — distilled/ root fork

Executes CURATION_CHECKLIST.md §1. The `distilled/` root held 17 notes that shared
filenames with `distilled/by-channel/` but had **different contents**. `by-channel` is
canonical (SCHEMA §2). Each root file was diffed against its twin by full read, unique
correct content was merged into the `by-channel` note, then the root copy was moved here
to `_deprecated/distilled-root-fork/`.

- Date executed: 2026-06-19
- Method: full read of both copies per pair (not filename trust), diff, merge-then-quarantine.
- Result: 17/17 reconciled. `distilled/` root now contains only `by-channel/`.
- Grafts applied: 1 (culture-critic). The other 16 had no material content missing from
  the canonical `by-channel` twin.

## Finding (consistent across all 17)
`by-channel` is the newer, richer distillation in every pair. Root copies are earlier,
more verbose drafts: longer prose, but fewer distinct frameworks and weaker brand
adaptations. Even where a root file had MORE lines (e.g. Tweeting-in-Reverse: root 104 vs
bc 66), the extra length was verbosity, not additional frameworks. So in 16 of 17 cases
nothing was grafted — the unique root prose was recoverable from quarantine if ever needed,
and the brain is kept tight per Adam's preference.

## Per-file log

| # | File | Action | Quarantined |
|---|------|--------|-------------|
| 1 | aaron-will-funnels-awareness-ladder.md | bc-canonical, nothing grafted | 2026-06-19 |
| 2 | amazon-book-launch-playbook.md | bc-canonical, nothing grafted | 2026-06-19 |
| 3 | book-subtitles-99-in-27-minutes.md | bc-canonical, nothing grafted | 2026-06-19 |
| 4 | consistency-systems--content-without-compromise-tyler-tott.md | bc-canonical; root-only retreat/live-event economics left in quarantine (tangential, recoverable) | 2026-06-19 |
| 5 | culture-critic--six-figures-writing-online.md | **GRAFTED** 1 bullet → bc twin | 2026-06-19 |
| 6 | first-1000-email-subs.md | bc-canonical, nothing grafted | 2026-06-19 |
| 7 | Tweeting-in-Reverse.md | bc-canonical (root longer but verbose, not richer) | 2026-06-19 |
| 8 | content-strategy--crush-writers-block-daily-engine.md | bc-canonical, nothing grafted | 2026-06-19 |
| 9 | decoding-the-algorithm-culture-explorer.md | bc-canonical, nothing grafted | 2026-06-19 |
| 10 | excalibur-x-2025-blueprint.md | bc-canonical, nothing grafted | 2026-06-19 |
| 11 | MC26-writing-personas.md | bc-canonical, nothing grafted | 2026-06-19 |
| 12 | offers--five-part-offer-framework.md | bc-canonical, nothing grafted | 2026-06-19 |
| 13 | qa-growing-on-x.md | bc-canonical (bc has fuller cadence/mentor/Notes detail) | 2026-06-19 |
| 14 | The_Builder_Identity_Worksheet_1.md | bc-canonical (bc has richer identity stack + brand app) | 2026-06-19 |
| 15 | unlocking-the-x-algorithm.md | bc-canonical, nothing grafted | 2026-06-19 |
| 16 | virality-blueprint-what-makes-threads-explode.md | bc-canonical (bc has more hooks: struggle rule, herd hook, Mary Sue) | 2026-06-19 |
| 17 | auto-dm-lead-magnet-capture.md | bc-canonical (bc has full hook + auto-DM templates) | 2026-06-19 |

## The one graft (detail)
**culture-critic--six-figures-writing-online.md** — grafted one root-unique framework into
the `by-channel` twin, after the "Sell on an established platform" bullet:

> **Persuasive writing is the load-bearing skill.** If you cannot write, you will struggle
> to grow no matter the tactics. Going from good to great with a coach is attainable; going
> from zero is brutal. Writing persuasively (and speaking) is one of the highest-ROI skills
> that exists — everything else here sits on top of it.

This was a genuine framework present in the root copy and absent from the canonical twin.
(Per §1, the merged note's `updated_at` should be bumped once frontmatter is added — these
distilled notes do not yet carry the SCHEMA §3 frontmatter block; that happens at the
brain/ refolder step.)

## Remaining §1 steps (NOT yet executed — require a destructive rename)
Per CURATION_CHECKLIST.md §1, once all 17 are reconciled:
- [ ] Rename `by-channel/` → `brain/` and refolder every note into its `category` (SCHEMA §5).
- [ ] Add SCHEMA §3 frontmatter to each note (these distilled notes currently have none).
- [ ] Regenerate `_INDEX.md`.
- [ ] After one clean release with no regressions, purge `_deprecated/distilled-root-fork/`.

These are held pending Adam's go-ahead because the rename + refolder is destructive and
reshapes the whole tree. The merge-then-quarantine reconcile (the safe part of §1) is done.
