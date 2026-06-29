# Codex Receipt - FaithWall, OpenRouter, Discord Focus Lanes

Date: 2026-06-18 11:07 CDT
Agent: Codex

Adam named three focus lanes: recover FaithWall Verse from the TestFlight/phone trail, check Cursor/OpenRouter setup for GLM 5.2 and Fusion, and keep the Discord/Masterclass extraction moving toward a central writing/planning corpus.

## FaithWall Verse

Codex read the active ops capsule and current recovery findings. Verified the local FaithWall Verse shell project at:

`/Users/adamjohnsson/iCloud Drive (Archive)/Documents/GitHub/faithwall-verse-ios/FaithWallVerse.xcodeproj`

Manifest truth: bundle `org.deadhidden.faithwall.companion`, team `7VD84G35MB`, version `1.0`, build `13`, sources `FaithWallVerseApp.swift`, `Models.swift`, `Stores.swift`, `Views.swift`, `WordStudy.swift`, and resources `KJV.json`, `CrossReferences.json`, `FirstMention.json`, `Scofield.json`, `Webster1828.json`.

Verified the local project folder is only a `.xcodeproj` shell, not full Swift source. Verified the Downloads export is a different bundle, `org.deadhidden.faithwall`, build `2`, useful as a pattern/source bank but not the exact TestFlight lane. Xcode archives were empty and the local FaithWall DerivedData folder was only 36K. The iPhone is visible over USB, but the phone/TestFlight route does not yield Swift source or `Views.swift`.

Chrome history showed App Store Connect app id `6766338824`; a live App Store Connect page check redirected to Apple login, so no current App Store Connect status was claimed.

## Cursor / OpenRouter

Verified Keychain service `OpenRouterAPI` exists. Ran:

`/Users/adamjohnsson/.deadhidden-os/ops/bin/openrouter-fusion-smoke`

Result: `DRACO/OpenRouter API key: available` and `Fusion smoke test OK`.

Ran:

`/Users/adamjohnsson/.deadhidden-os/ops/bin/cursor-openrouter-setup`

This backed up Cursor state DB to:

`/Users/adamjohnsson/Library/Application Support/Cursor/User/globalStorage/state.vscdb.bak-openrouter-20260618-110448`

and patched Cursor local state to:

- `useOpenAIKey: true`
- `openAIBaseUrl: https://openrouter.ai/api/v1/cursor`
- `aiSettings.userAddedModels: ["z-ai/glm-5.2","openrouter/fusion"]`
- `aiSettings.modelOverrideEnabled` includes `composer-2.5`, `z-ai/glm-5.2`, and `openrouter/fusion`

Remaining Cursor UI caveat: if Cursor does not use the key after reload, paste/save the same OpenRouter key in Cursor Settings -> Models -> API Keys -> OpenAI API Key. Codex did not restart Cursor because active Cursor agents were running.

## Discord / Masterclass / Writing Brain

Verified the archive at:

`/Users/adamjohnsson/Library/CloudStorage/GoogleDrive-thebiblicalman1611@gmail.com/My Drive/Masterclass-Archive`

Observed: about 1.2G locally visible, 13 channel transcripts, 58 videos, 17 audio files, and 10 PDFs under Masterclass-24-7. Verified the central brain file:

`/Users/adamjohnsson/Library/CloudStorage/GoogleDrive-thebiblicalman1611@gmail.com/My Drive/Masterclass-Archive/Writing-Brain/WRITING-BRAIN.md`

Transcription state before intervention: 14 of 44 recordings completed, 1 distilled note present. The prior transcription run had stopped during item 15. Codex first tried background/nohup and launchd restarts, but this environment killed detached child jobs and launchd was blocked by macOS/Google Drive File Provider permissions from reading `transcribe.sh` (`Operation not permitted`).

Codex then transcribed item 15 manually in the foreground:

`YOUR_FIRST_1000_EMAIL_SUBS_.mp4`

Result: transcript count is now 15 of 44. Created transcript:

`/Users/adamjohnsson/Library/CloudStorage/GoogleDrive-thebiblicalman1611@gmail.com/My Drive/Masterclass-Archive/Writing-Brain/transcripts/YOUR_FIRST_1000_EMAIL_SUBS_.txt`

Reliable resume command for the remaining recordings from an attended Terminal/Cursor terminal:

`cd "/Users/adamjohnsson/Library/CloudStorage/GoogleDrive-thebiblicalman1611@gmail.com/My Drive/Masterclass-Archive/Writing-Brain/pipeline" && /bin/bash transcribe.sh`

Created focus packet:

`/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-18-focus-lanes/FOCUS-STATUS.md`

Boundary: no App Store Connect mutation, no build submission, no public post, no email, no Stripe/customer/money action, no deploy, no file deletion, no Cursor restart, no persistent launchd job left installed, and no API key printed.
