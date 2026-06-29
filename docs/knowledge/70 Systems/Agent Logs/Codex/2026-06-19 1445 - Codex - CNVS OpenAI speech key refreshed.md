# Codex - CNVS OpenAI Speech Key Refreshed

Date: 2026-06-19 14:45 CDT

Adam supplied a new OpenAI project key for CNVS real speech. Codex installed it locally without writing the key value into receipts.

Changed:

- Updated Hermes speech env slot `VOICE_TOOLS_OPENAI_KEY` in `/Users/adamjohnsson/.hermes/.env`.
- Backed up the prior Hermes env to `/Users/adamjohnsson/.hermes/.env.bak-openai-speech-20260619144355`.
- Updated macOS Keychain entries for CNVS:
  - `com.cnvs.canvas.openai_api_key` / `openai_api_key`
  - `com.cnvs.canvas.openai_key` / `openai_key`
- Left CNVS running to preserve active agent sessions.
- Restarted Hermes gateway through launchd so Hermes picked up the refreshed env.
- Added a global CNVS memory note with the redacted setup result.

Verification:

- CNVS voice prefs decode to `methodology: gptRealtime`, `gptVoice: verse`, and `speakReplies: true`.
- OpenAI `/v1/models` returned HTTP `200`.
- OpenAI `/v1/audio/speech` with `gpt-4o-mini-tts` and voice `verse` returned HTTP `200` and wrote `/tmp/cnvs-openai-speech-test.mp3`.
- OpenAI `/v1/audio/transcriptions` with `gpt-4o-mini-transcribe` returned HTTP `200`.
- OpenAI Realtime WebSocket handshake without the deprecated beta header returned `session.created` for `gpt-realtime-2`.
- A control attempt with the old `OpenAI-Beta: realtime=v1` header returned `beta_api_shape_disabled`; `strings` inspection did not find that deprecated header embedded in the installed CNVS binary.
- Hermes status after restart reported gateway running with PID `39501`.

Boundary:

- Local credential/config update, local Keychain update, local Hermes restart, provider health checks, CNVS memory note, and receipts only.
- No public post, email/send, Stripe/customer/money mutation, deploy, Linear/Notion write, webhook change, or external account mutation.
- No API key value is recorded in this receipt.
