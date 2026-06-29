---
type: agent-log
date: 2026-06-19 11:25 CDT
agent: Codex
topic: CNVS configured for agent stack
tags: [codex, cnvs, hermes, agent-ops]
---

# CNVS Configured For Agent Stack

## Goal

Set up the purchased CNVS macOS app so Adam can use the local agent stack from one canvas: Codex, Claude Code, Cursor Agent, Grok, Hermes, and speech tooling.

## What I Checked

- Read the active ops capsule and team packet under `/Users/adamjohnsson/.deadhidden-os/ops/`.
- Verified CNVS is installed at `/Applications/CNVS.app`, version `1.3.3`, bundle `com.cnvs.canvas`.
- Verified CNVS control server is live through `cnvsctl`.
- Verified CNVS detects agent CLIs: `claude`, `codex`, `cursor`, and `grok`.
- Verified local CLIs:
  - `codex-cli 0.130.0`
  - `Claude Code`
  - `cursor 3.8.11`
  - `grok 0.2.22`
  - `Hermes Agent v0.16.0`
- Verified CNVS terminal PATH resolves `codex`, `claude`, `cursor`, `grok`, and `hermes`.

## What I Did

- Copied the existing OpenAI key from `/Users/adamjohnsson/code/openai-realtime-session-bridge/.env.local` into Hermes' speech-only env slot as `VOICE_TOOLS_OPENAI_KEY` in `/Users/adamjohnsson/.hermes/.env`.
- Left backup `/Users/adamjohnsson/.hermes/.env.bak-cnvs-20260619112256`.
- Restarted Hermes launchd gateway so it picks up the updated env.
- Added OpenAI and xAI/Grok keys to CNVS' macOS Keychain namespace after verifying CNVS stores provider keys in Keychain:
  - service `com.cnvs.canvas.openai_api_key`, account `openai_api_key`
  - service `com.cnvs.canvas.openai_key`, account `openai_key`
  - service `com.cnvs.canvas.grok_api_key`, accounts `grok_api_key` and `xai_api_key`
- Verified the OpenAI key reaches OpenAI with `GET /v1/models` returning `200`.
- Verified Grok with a local CLI smoke prompt returning `GROK_READY`.
- Added `/Users/adamjohnsson/AGENTS.md` so CNVS-spawned agents starting in `/Users/adamjohnsson` get the Dead Hidden ops-capsule boot rules.
- Added CNVS shared memory note pointing agents to the ops capsule, `dh-with-env`, Hermes API, Grok availability, and the OpenAI speech quota blocker.
- Opened a clean CNVS canvas with:
  - `CNVS Setup Check` terminal
  - `Hermes Ready` chat node

## Proof

- CNVS state reports current canvas `adamjohnsson`, project directory `/Users/adamjohnsson`, nodes `CNVS Setup Check` and `Hermes Ready`, and agent CLIs `claude`, `codex`, `cursor`, `grok`.
- CNVS voice prefs currently report methodology `gptRealtime`, wake engine `appleSpeech`, Grok voice `eve`, and spoken replies enabled.
- Screenshot: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/cnvs-setup-clean-20260619.png`.
- CNVS memory file: `/Users/adamjohnsson/.cnvs/memory/memory.jsonl`.
- Boot file: `/Users/adamjohnsson/AGENTS.md`.

## Blocker

OpenAI speech endpoints are locally wired but currently return `429 insufficient_quota` for both `/v1/audio/speech` and `/v1/audio/transcriptions`. This is an OpenAI account billing/quota issue, not a missing local key. Hermes can still use local STT and existing ElevenLabs/Grok-related tooling.

## 2026-06-19 11:35 CDT Update

Adam asked why Grok voice was not working. Diagnosis: CNVS voice prefs were still set to `methodology: gptRealtime`, which routes the live speech path through OpenAI Realtime. That kept failing because OpenAI audio returns `429 insufficient_quota`.

Codex verified the xAI/Grok TTS endpoint directly with the existing `XAI_API_KEY`: `POST https://api.x.ai/v1/tts` returned `200` and generated an MP3 using voice `eve`.

Codex backed up `/Users/adamjohnsson/Library/Preferences/com.cnvs.canvas.plist` to `/Users/adamjohnsson/Library/Preferences/com.cnvs.canvas.plist.bak-grok-voice-20260619113520`, changed CNVS voice prefs to `methodology: parakeet`, kept `grokVoice: eve`, kept `speakReplies: true`, relaunched CNVS, and verified the loaded prefs now report:

- `methodology: parakeet`
- `grokVoice: eve`
- `speakReplies: true`
- `activation: pushToTalk`
- `parakeetActivation: pushToTalk`

CNVS state returned to current canvas `adamjohnsson` and showed a Grok agent terminal. Boundary: local CNVS preference change and relaunch only. No secrets printed, no external messages sent, no public/account/customer/money mutation.

## Boundary

No secrets were printed. No public post, email, Stripe/customer/money mutation, deployment, Linear/Notion write, webhook change, or external account mutation was performed. Credential/config changes were limited to the requested local OpenAI speech key placement into Hermes' local env file plus CNVS Keychain entries for OpenAI and xAI/Grok.
