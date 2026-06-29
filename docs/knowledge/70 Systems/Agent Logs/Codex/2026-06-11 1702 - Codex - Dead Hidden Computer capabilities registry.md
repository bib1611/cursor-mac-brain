---
type: agent-log
date: 2026-06-11 17:02 CDT
agent: Codex
topic: Dead Hidden Computer capabilities registry
tags: [codex, dead-hidden-computer, capabilities, mcp, skills, plugins]
---

# Dead Hidden Computer Capabilities Registry

## Goal

Adam asked whether Dead Hidden Computer can add skills, MCP connectors, and plugins like Codex, Hermes, and Claude Desktop.

## What I Changed

- Added a native `Capabilities` section to the Dead Hidden Computer SwiftUI app.
- Added local discovery for:
  - Codex/shared/Claude/plugin `SKILL.md` files.
  - Claude Desktop MCP servers from `claude_desktop_config.json`.
  - Codex MCP servers from `~/.codex/config.toml`.
  - Hermes MCP servers from `~/.hermes/config.yaml`.
  - local MCP manifests found in known MCP paths.
  - enabled Codex plugins.
  - Codex app connector approval surfaces.
- Added capability search, kind filters, source-open actions, copy-index action, and local capability packet saving.
- Added capability counts to the Command dashboard.
- Updated the smart router so tasks mentioning skills, MCP, plugins, or connectors route through the Capability Registry lane.
- Updated the project README.

## Files Changed

- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/Support/Constants.swift`
- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/Models/CapabilityModels.swift`
- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/Services/CapabilityService.swift`
- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/Stores/OrchestratorStore.swift`
- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/Models/AppSection.swift`
- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/Views/ContentView.swift`
- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/Views/CapabilitiesView.swift`
- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/Views/OverviewView.swift`
- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/Services/SmartOrchestratorService.swift`
- `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/README.md`

## Proof

- `swift build` passed.
- `./script/build_and_run.sh --verify` passed and launched `DeadHiddenComputer`.
- `pgrep -ax DeadHiddenComputer` returned running PID `57092`.
- Visual screenshot confirmed the sidebar includes `Capabilities` and the Command dashboard loaded `495` capabilities.

Screenshot artifact:

- `/tmp/dead-hidden-computer-capabilities-check.png`

## Boundary

This was a read-only discovery and app-surface implementation. No public post, customer action, money action, deployment, credential change, connector grant, plugin install/removal, MCP config mutation, Fable proxy restart, SMS send, or external account mutation was performed.

The app does not print env values or secrets. MCP details intentionally redact environment/token fields and route installs/config changes into local approval packets.
