# 2026-06-18 1213 - Codex - FaithWall Verse TSK Cross References

Adam asked Codex to make verse-number taps open real, verbose cross-references, starting with the Treasury of Scripture Knowledge.

Changed local project:

`/Users/adamjohnsson/code/faithwall-verse-ios-reconstruction`

Modified:

- `Resources/CrossReferences.json`
- `Sources/Stores.swift`
- `Sources/Views.swift`

Added:

- `Scripts/check_crossrefs.py`

Implemented:

- Replaced the 9-verse stub `CrossReferences.json` with OpenBible/TSK-derived cross-reference data.
- New data contains 29,364 source verses and 344,799 cross-reference links.
- Verse-number tap still opens the References sheet.
- References sheet now shows `Treasury of Scripture Knowledge (<count>)`.
- Each cross-reference row shows the reference plus local KJV preview text when parseable.
- Tapping a cross-reference jumps the reader to that referenced verse and closes the sheet.
- Cross-reference resource now lazy-loads on first study access instead of app startup.
- Sheet includes attribution note: TSK via OpenBible.info, TSK public domain, OpenBible data CC BY.

Research/source boundary:

- Used TSK/OpenBible because TSK is public-domain based and OpenBible publishes downloadable cross-reference data with CC BY attribution.
- Did not import Sam Gipp, Dr. Ruckman, David Peacock, or Common Man's Reference Bible material because those sources appear copyrighted unless Adam supplies licensed/local files or permission.

Verification:

- `python3 Scripts/check_crossrefs.py` passed.
- Simulator build passed:
  `DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer xcodebuild -project FaithWallVerse.xcodeproj -scheme FaithWallVerse -configuration Debug -destination 'platform=iOS Simulator,name=iPhone 17' CODE_SIGNING_ALLOWED=NO build`
- Physical iPhone build passed with side-by-side dev bundle:
  `org.deadhidden.faithwall.companion.dev`
- Installed and launched on `adam Johnsson's iPhone`.
- Final installed app bundle includes 5.9M `CrossReferences.json`; app bundle size is 13M.

Sample data checks:

- `Genesis 1:1`: 62 refs, beginning with `John 1:1-3`.
- `Psalms 119:11`: 13 refs.
- `Romans 12:2`: 57 refs.

Boundary:

- No App Store Connect mutation.
- No TestFlight submission.
- No production/TestFlight bundle overwrite.
- No Apple credential/key/account setting change.
- No public/external action performed.
