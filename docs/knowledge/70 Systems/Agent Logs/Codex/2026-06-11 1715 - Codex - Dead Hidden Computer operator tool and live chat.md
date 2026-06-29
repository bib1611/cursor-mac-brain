---
type: agent-log
date: 2026-06-11 17:15 CDT
agent: Codex
topic: Dead Hidden Computer operator tool and live chat
tags: [codex, dead-hidden-computer, operator-tool, live-chat, kimi]
---

# Dead Hidden Computer Operator Tool And Live Chat

## Goal

Adam said the Chat tab was still unusable because it returned canned text, then redirected the goal: make Dead Hidden Computer something Codex can use as an additional operator tool to rival Hermes, Perplexity Computer, and OpenClaw.

## What I Changed

- Added live chat backend support to the SwiftUI app.
- Chat mode now calls a live model instead of returning canned text.
- While `OUTBOUND_LOCKDOWN.md` is active, Chat avoids the locked Fable/Claude Max proxy and uses the configured Kimi/Moonshot fallback.
- If live model calls fail, the app saves an operator packet instead of pretending to chat.
- Added `LiveChatService`.
- Added `ChatBackendResult`.
- Added operator packet support in `WorkspaceService`.
- Added project CLI:
  - `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/script/dhc`
  - stable wrapper: `/Users/adamjohnsson/.deadhidden-os/ops/bin/dhc`
- CLI commands:
  - `dhc status`
  - `dhc context`
  - `dhc packet`
  - `dhc chat`
  - `dhc open`
- Updated `README.md`.

## Files Changed

- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/Support/Constants.swift`
- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/Models/ChatBackendModels.swift`
- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/Services/LiveChatService.swift`
- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/Services/WorkspaceService.swift`
- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/Stores/OrchestratorStore.swift`
- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/Views/ChatView.swift`
- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/script/dhc`
- `/Users/adamjohnsson/.deadhidden-os/ops/bin/dhc`
- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/README.md`

## Proof

- Hermes API health returned `{"status": "ok", "platform": "hermes-agent", "version": "0.16.0"}`.
- Direct Kimi smoke test returned `Chat is working.`
- `/Users/adamjohnsson/.deadhidden-os/ops/bin/dhc status` returned live status, Fable lock active, capability counts, and latest intel paths.
- `/Users/adamjohnsson/.deadhidden-os/ops/bin/dhc chat 'Reply with one short sentence: dhc chat is live'` returned `DHC chat is live.`
- `/Users/adamjohnsson/.deadhidden-os/ops/bin/dhc packet 'Make Dead Hidden Computer a Codex-side operator tool' --source smoke --kind operator` saved:
  `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/dead-hidden-computer/operator/2026-06-11-171444-operator-packet.md`
- `swift build` passed.
- `./script/build_and_run.sh --verify` passed.
- `pgrep -ax DeadHiddenComputer` returned running PID `79187`.

## Boundary

No public post, customer action, money action, deploy, credential change, connector grant, plugin install/removal, MCP config mutation, Fable proxy restart, SMS send, or external account mutation was performed.

Live fallback chat sends the user's prompt to Kimi/Moonshot while Fable is locked. It does not send bulk local files, passwords, receipts, customer data, or private message databases.
