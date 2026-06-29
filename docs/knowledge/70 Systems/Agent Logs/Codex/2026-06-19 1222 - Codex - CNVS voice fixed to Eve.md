# 2026-06-19 12:22 CDT - Codex - CNVS Voice Fixed To Eve

Adam pointed at the Codex agent fixing voice on CNVS / canvas.

Codex refreshed the Dead Hidden ops capsule and team packet, read the current CNVS handoff, inspected live CNVS state, decoded the CNVS voice prefs blob, checked `voice-feedback.jsonl`, and verified the active CNVS canvas.

Findings:

- CNVS microphone/transcription was working through `parakeet`, but `voice-feedback.jsonl` showed recent spoken phrases were all classified as `miss`.
- CNVS app voice prefs had drifted to `grokVoice: ara`, while the earlier handoff and CNVS memory expected Grok `eve`.
- Hermes local TTS was already aligned to `tts.provider: xai` and `xai.voice_id: eve`.
- The active CNVS canvas had been rewritten into a simpler layout: Chase/Codex, Skye/Claude, Rubble/Grok, plus Forge.

Changes:

- Backed up CNVS prefs to `/Users/adamjohnsson/Library/Preferences/com.cnvs.canvas.plist.bak-voice-fix-20260619121900`.
- Backed up CNVS canvas state to `/Users/adamjohnsson/Library/Application Support/CNVS/canvases.json.bak-voice-fix-20260619121900`.
- Updated CNVS voice prefs to:
  - `methodology: parakeet`
  - `grokVoice: eve`
  - `speakReplies: true`
  - `activation: pushToTalk`
  - `parakeetActivation: pushToTalk`
  - `wakeWordEnabled: true`
- Saved a global CNVS memory note with the voice fix and the current recipe limitation.

Verification:

- Decoded CNVS voice prefs now report `methodology=parakeet`, `grokVoice=eve`, `speakReplies=true`, and push-to-talk enabled.
- Hermes config still reports `tts.provider: xai` and `xai.voice_id: eve`.
- xAI TTS smoke through Adam's local env wrapper returned `HTTP 200` and wrote a valid MP3 at `/tmp/cnvs-eve-tts-test.mp3` using `voice_id: eve`; the current xAI schema requires `text` plus `language`.
- CNVS state returned `ok` and showed the active canvas with Chase/Codex, Skye/Claude, Rubble/Grok, plus Forge.

Limit:

- Direct edits to save a CNVS canvas recipe were overwritten by the running CNVS app. Codex did not quit or relaunch CNVS because that would risk killing active canvas agents. Persisting the boot recipe should be done through the CNVS UI's "Save current layout as recipe" command, or by quitting CNVS first and then patching the state file while the app is not rewriting it.

Boundary:

Local CNVS preference/config inspection, local CNVS prefs change, local backup files, xAI TTS smoke, and receipts only. No public post, email/send, Stripe/customer/money mutation, deployment, Linear/Notion write, webhook change, credential change, session deletion, or external account mutation performed. No secrets printed.
