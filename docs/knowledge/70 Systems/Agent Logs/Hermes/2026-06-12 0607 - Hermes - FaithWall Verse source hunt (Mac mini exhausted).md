# FaithWall Verse source hunt — Mac mini exhausted

Date: 2026-06-12 06:07 CDT
Agent: Hermes (Fable 5)
Context: Adam chose Lane B (recover source, fix verse-tap bug, build 4, then App Store submission). This session hunted for the missing FaithWall Verse source.

## Missing manifest (from pbxproj, read this session)

Project: `/Users/adamjohnsson/iCloud Drive (Archive)/Documents/GitHub/faithwall-verse-ios/FaithWallVerse.xcodeproj`
Expected but absent:

- Swift: `FaithWallVerseApp.swift`, `Models.swift`, `Stores.swift`, `Views.swift`, `WordStudy.swift`
- JSON: `KJV.json`, `CrossReferences.json`, `FirstMention.json`, `Scofield.json`, `Webster1828.json`

## Locations checked — all dry

1. iCloud archive project folder: shell only (pbxproj + workspace + scheme, 3 files, no `.icloud` placeholders anywhere in archive).
2. Mac mini disk-wide Spotlight: only old-lineage `org.deadhidden.faithwall` export in `~/Downloads/faithwall-export/` (different bundle, different source set).
3. Mac mini Xcode: no Archives folder; DerivedData has only old `FaithWall-*`, not FaithWallVerse. Build 3 was NOT archived on this Mac mini.
4. GitHub (`gh repo list`, all 13 repos): `biblicalman1611/faithwall` is the Vite web launch site — no iOS source in tree. No other candidate repo.
5. Time Machine: no destinations configured.
6. MacBook (`thebi@100.91.48.107`): SSH timed out — unreachable. **Prime remaining suspect** since build 3 (uploaded 2026-05-24) had to be archived on some machine and it was not this one.

## Next step

Adam wakes the MacBook / gets it on Tailscale. Then SSH search: `~/Library/Developer/Xcode/Archives`, DerivedData, and mdfind for `FaithWallVerse` / `WordStudy`.

Fallback if MacBook is dry: rebuild. 5 Swift files is a 1–2 day rebuild; KJV data exists in old export (`KJVBible.swift`), Scofield notes and Webster 1828 are public domain datasets.

Boundary: read-only investigation. No builds, no App Store Connect, no Stripe, no publish, no file changes outside this receipt.
