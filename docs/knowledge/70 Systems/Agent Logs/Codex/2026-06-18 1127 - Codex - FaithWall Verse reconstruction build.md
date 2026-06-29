# 2026-06-18 1127 - Codex - FaithWall Verse reconstruction build

Codex rebuilt a safe local FaithWall Verse reconstruction at:

`/Users/adamjohnsson/code/faithwall-verse-ios-reconstruction/FaithWallVerse.xcodeproj`

The app keeps the recovered TestFlight lane metadata: `org.deadhidden.faithwall.companion`, version `1.0`, build `13`, iOS `16.0`.

Restored missing project files:

- `Info.plist`
- `Sources/FaithWallVerseApp.swift`
- `Sources/Models.swift`
- `Sources/Stores.swift`
- `Sources/Views.swift`
- `Sources/WordStudy.swift`
- KJV and study resources under `Resources/`

Verification:

- `DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer xcodebuild -project FaithWallVerse.xcodeproj -scheme FaithWallVerse -configuration Debug -destination 'platform=iOS Simulator,name=iPhone 17' CODE_SIGNING_ALLOWED=NO build`
- Result: `BUILD SUCCEEDED`
- Installed and launched on iPhone 17 simulator UDID `04713C46-7037-4E85-962F-601A691B95E7`
- Launch returned process id `97405`
- Screenshot saved at `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-18-faithwall-verse-rebuild/faithwall-verse-simulator-final.png`

Boundary:

- Local reconstruction only.
- No App Store Connect mutation, TestFlight submission, device install, Stripe/email/publishing action, credential change, or system `xcode-select` change.
