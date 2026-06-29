# Codex - Dead Hidden Computer App

Time: 2026-06-11 16:44 CDT

## Request

Adam asked Codex to use Hermes, research Perplexity Computer / Personal Computer, and build an app on the Mac mini that works as an orchestrator for his LLMs and intel.

## Research Used

Official Perplexity pages checked:

- `https://www.perplexity.ai/personal-computer`
- `https://www.perplexity.ai/personal-computer-setup`
- `https://www.perplexity.ai/changelog/personal-computer-for-all-users-on-mac`
- `https://www.perplexity.ai/changelog/what-we-shipped---march-13-2026`

Key pattern translated locally:

- always-on Mac worker
- local files/apps/browser context
- multi-model orchestration
- approval gates, audit trail, and kill switch

Dead Hidden translation:

- Codex stays harness/operator/verifier.
- Hermes provides local gateway/profile/runtime state.
- Comet/Chrome/X/YouTube/source-intel are local context feeds.
- Ops capsule and receipts are the source of truth.
- `OUTBOUND_LOCKDOWN.md` remains the kill switch.

## Built

Created a native SwiftUI app:

`/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer`

Generated app bundle:

`/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/dist/DeadHiddenComputer.app`

Configured Codex Run action:

`/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/.codex/environments/environment.toml`

Build/run entrypoint:

`/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/script/build_and_run.sh`

## MVP Features

- Command overview: Hermes health, Fable lock state, local intel packet count.
- Hermes LLM roster: reads `hermes profile list`, `hermes status`, `hermes proxy status`, and gateway health.
- Status redaction: app-side redaction hides provider key prefixes from Hermes status output.
- Chat sessions and local memory notes under the ops artifact folder.
- Voice output via AVFoundation and permission-gated dictation.
- Smart orchestrator: Fable 5 is the primary brain, Codex 5.5 is fallback/harness, helper lanes selected by task.
- Persistent agent bridge view for Telegram/Hermes, iMessage/Photon, Chorus/Jarvis, and Stanley in iMessage.
- Mac Control view for Full Disk Access, Accessibility, browser CDP, microphone/speech, and password/login boundaries.
- Media view for local screen capture, media inspection, and local-transcription CLI handoff.
- Files view for local Markdown creation into app artifacts, Obsidian inbox/drafts, or Hermes workspace outputs.
- Store Ops view for commerce task packets with proof/approval checklist.
- Intel view: reads source-intel and X-bookmark intel artifacts plus team context and receipts.
- Route composer: saves local Markdown route packets under `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/dead-hidden-computer/routes/`.
- Blueprint view: documents how Perplexity Personal Computer maps onto Adam's local system.
- Receipts view: shows recent ops receipt entries.
- Guardrails view: surfaces `OUTBOUND_LOCKDOWN.md` and names blocked actions.

## Verification

- `swift build` passed.
- `./script/build_and_run.sh --verify` passed.
- App launched as a real macOS `.app` bundle with process `DeadHiddenComputer`.
- Visual check confirmed the main window loaded and refreshed to:
  - Hermes: healthy
  - Fable: locked
  - Intel: 4 local packets loaded
- Visual check confirmed expanded sidebar surfaces: Orchestrator, Chat, Memory, Agents, Mac Control, Media, Files, Store, Routes, Blueprint, Receipts, Guardrails.

## Boundary

No public post, Substack action, email/customer action, Stripe action, deploy, credential change, provider change, Hermes proxy restart, Fable run, SMS/code send, password/keychain export, or external-account mutation was performed.
