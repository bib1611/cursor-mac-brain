# 2026-06-11 06:55 CDT - Codex - Hermes Update

Adam asked Codex to update Hermes after seeing a new update prompt, including the desktop app and Telegram surface, and to check whether Hermes has an auto-update feature.

## Actions

- Booted from the local ops capsule and refreshed `TEAM_CONTEXT.md`.
- Verified Hermes was 51 commits behind `origin/main`.
- Ran the official updater:

```bash
/Users/adamjohnsson/.local/bin/hermes update --backup --yes
```

- Relaunched the rebuilt desktop app from:

```text
/Users/adamjohnsson/.hermes/hermes-agent/apps/desktop/release/mac-arm64/Hermes.app
```

## Result

- Hermes source is now at `4717989c1 fix(matrix): isolate room context and restore reliable inbound dispatch (#18505)`.
- `hermes version` reports `Hermes Agent v0.16.0 (2026.6.5) - upstream 4717989c` and `Up to date`.
- `hermes update --check` reports `Already up to date`.
- Desktop app was rebuilt and relaunched. Build stamp:

```json
{
  "commit": "4717989c1014af020b60de1eddeabd3dc5f03ef5",
  "branch": "main",
  "builtAt": "2026-06-11T11:49:52.787Z",
  "dirty": true,
  "source": "local"
}
```

- `dirty: true` is expected because local Photon customizations were restored after update. `git status --short --branch` now shows no behind/ahead drift and only:

```text
M plugins/platforms/photon/adapter.py
M plugins/platforms/photon/sidecar/index.mjs
```

- Gateway is running under launchd as PID `97039`.
- Telegram reconnected in local polling mode and registered the command menu.
- API health returned:

```json
{"status": "ok", "platform": "hermes-agent", "version": "0.16.0"}
```

- Authorized `/v1/capabilities` returned the Hermes API capabilities object.
- `hermes mcp test agentmemory` connected and discovered 51 tools.
- `hermes doctor` passed core install checks and reported only non-update blocker warnings: AWS Bedrock token invalid, optional providers not configured, and memory provider setup warning despite the agentmemory MCP test passing.
- Computer Use driver refresh ran during update. `cua-driver --version` reports `cua-driver 0.5.1`.

## Auto-Update Check

Official Hermes docs and local code show:

- `hermes update` is the update command.
- `/update` can be sent from Telegram and other messaging platforms; it updates Hermes, streams progress, and restarts the gateway.
- The desktop app performs passive update checks on launch, focus, and every 30 minutes, then shows an update notification/toast.
- One `hermes update` covers every profile on the machine and syncs bundled skills to all profiles.
- Hermes has update behavior settings under `updates:`:

```yaml
updates:
  pre_update_backup: false
  backup_keep: 5
  non_interactive_local_changes: stash
```

I did not find an official setting that silently auto-applies updates on a schedule. I did not install a custom launchd auto-updater because that would change local automation/update behavior and should be an explicit operator decision.

## Backup

Pre-update full backup:

```text
/Users/adamjohnsson/.hermes/backups/pre-update-2026-06-11-064805.zip
```

Pre-update snapshot:

```text
20260611-114907-pre-update
```

## Boundaries

No public post, customer action, money action, production deploy, webhook cutover, API key change, credential print, or custom auto-update launchd job was performed. Internal Hermes shutdown/restart notifications may have been sent to Adam's configured home channels as part of the gateway restart.
