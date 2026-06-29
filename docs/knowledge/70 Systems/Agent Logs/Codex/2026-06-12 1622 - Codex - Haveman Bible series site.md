# Codex Receipt - Haveman Bible Series Site

Date: 2026-06-12 1622 CDT

## Summary

Built the Dead Hidden Next.js section for Pastor David Haveman's `How We Got Our Bible` series and prepared source/transcript deliverables.

## Source Collection

- Source: `https://brnsermons.com/davidhaveman/`
- Rechecked BRN WordPress API on 2026-06-12.
- Found 13 public posts through L14:
  L1, L2, L3, L4, L5, L8, L9, L9 PT2, L10, L#11b, L12, L13, L14.
- Missing public lessons: L6 and L7.
- Odd public slugs preserved in manifest: L1 at `how-we-got-our-bible-l2`, L2 at `how-we-got-our-bible-l2-2`, L8 at `how-we-got-our-bible-l6`.

## Artifacts

- Output package:
  `/Users/adamjohnsson/Documents/Codex/2026-06-12/you-are-building-a-website-that/outputs/haveman-how-we-got-our-bible`
- Manifest:
  `source/manifest.json`, `source/manifest.csv`
- Raw transcripts:
  `raw-transcripts/`
- Edited chapters:
  `edited-chapters/`
- Verification:
  `verification/kjv-reference-checks.md`, `verification/chapter-editing-notes.md`, `verification/build-and-test.md`

## Site Changes

- Added `/how-we-got-our-bible` index page.
- Added `/how-we-got-our-bible/[slug]` lesson pages.
- Added `src/data/how-we-got-bible.ts`.
- Added `src/content/how-we-got-our-bible/*.md`.
- Updated sitemap to include the index and all lesson pages.
- Every lesson page includes Pastor Haveman/Sunrise Baptist credit, Sunrise link, BRN source link, source MP3/audio player, Article JSON-LD, and a separated Dead Hidden CTA.

## Verification

- Targeted ESLint passed.
- `npm run build` passed.
- Local Chrome render checks passed for desktop/mobile index and L1 lesson page.
- Sitemap contains index plus all 13 lesson URLs.
- KJV explicit-reference ledger has no unresolved detected references after manual L2 Ezekiel correction.

## Caveat

The edited chapters are a conservative first pass. The script verified explicit detected references against the local KJV database, but this is not a full human quote-by-quote audit of every partial oral Bible quotation. Final publication should still receive human KJV quote review if the standard is every Scripture phrase exactly verified by hand.

