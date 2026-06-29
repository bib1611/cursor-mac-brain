---
type: agent-log
date: 2026-06-11 17:06 CDT
agent: Codex
topic: Dead Hidden Computer chat mode fix
tags: [codex, dead-hidden-computer, chat, mac-app]
---

# Dead Hidden Computer Chat Mode Fix

## Goal

Adam reported that using the Chat tab produced routing boilerplate:

`Primary brain: Fable 5 is configured but locked. Active lane: Codex 5.5 fallback/harness until Adam re-enables Fable.`

The problem was that the local chat generator always returned an operator route/status template.

## What I Changed

- Added `ChatResponseMode` with `Chat` and `Route`.
- Made `Chat` the default behavior.
- Added a segmented Chat/Route picker to the Chat header.
- Replaced the old single generator with:
  - conversational local replies in Chat mode
  - the prior proof/route template only in Route mode
- Updated the new-session greeting to stop advertising the routing policy as the first chat response.
- Updated `README.md`.

## Files Changed

- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/Models/ChatModels.swift`
- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/Stores/OrchestratorStore.swift`
- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/Services/SessionMemoryService.swift`
- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/Views/ChatView.swift`
- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/README.md`

## Proof

- `swift build` passed.
- `./script/build_and_run.sh --verify` passed.
- `pgrep -ax DeadHiddenComputer` returned running PID `66832`.

## Boundary

This was a local app behavior fix only. No public post, customer action, money action, deploy, credential change, connector grant, plugin install/removal, MCP config mutation, Fable proxy restart, SMS send, or external account mutation was performed.
