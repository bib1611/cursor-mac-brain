# Codex - Hermes iMessage Repair Followup

Date: 2026-06-09 17:17 CDT

Adam reported that Hermes iMessage still was not working after Hermes attempted the repair.

## Findings

- Photon/iMessage inbound had reached Hermes earlier. Gateway logs showed an inbound iMessage at about 17:09 CDT, including mark-read behavior.
- The visible failure after delivery was the local model lane. Hermes was still defaulting to `claude-fable-5` through the single-concurrency local proxy at `http://127.0.0.1:3458/v1`; the Photon request spawned a `claude --print --model claude-fable-5` process that hung for minutes, making iMessage look dead.
- A stale Photon sidecar from an earlier restart was still holding `127.0.0.1:8789`; the new sidecar hit EADDRINUSE until the stale process was killed and the gateway restarted.
- The separate daily `com.adam.imessage-sync` job was also misconfigured. It still pointed at Command Line Tools Python and was failing with `sqlite3.DatabaseError: authorization denied`, even though the scoped iMessage interpreter already had access.

## Changes

- Patched `/Users/adamjohnsson/claude-max-proxy.js` so Photon/iMessage requests that ask for `claude-fable-5` are routed to `claude-opus-4-7` for chat latency, while preserving Fable for other work.
- Restarted `com.biblicalman.claude-max-proxy`.
- Killed the stale Photon sidecar process and restarted `ai.hermes.gateway`.
- Repointed `/Users/adamjohnsson/Library/LaunchAgents/com.adam.imessage-sync.plist` to `/Users/adamjohnsson/.deadhidden-os/bin/imessage-sync`.
- Patched `/Users/adamjohnsson/.hermes/scripts/imessage_to_vault.py` to catch `sqlite3.Error` so authorization failures exit cleanly with the intended Full Disk Access message instead of a traceback.

## Verification

- Synthetic Photon request to the local proxy, with requested model `claude-fable-5`, returned `PHOTON_FAST_OK` through `claude-opus-4-7` in about 9 seconds.
- Proxy logs showed `[route] Photon/iMessage requested Fable; using claude-opus-4-7 for chat latency`.
- Gateway logs showed Telegram connected, Photon sidecar listening on `127.0.0.1:8789`, Photon connected over sidecar stream, API server listening on `127.0.0.1:8642`, and gateway running with 3 platforms.
- `curl http://127.0.0.1:8642/health` returned ok for Hermes Agent `0.16.0`.
- Scoped iMessage DB read succeeded from `/Users/adamjohnsson/.deadhidden-os/imessage-brain/venv/bin/python3`, returning message count `59575`.
- `launchctl print gui/$(id -u)/com.adam.imessage-sync` showed the program now uses `/Users/adamjohnsson/.deadhidden-os/bin/imessage-sync`.

## Boundary

No real iMessage was sent from Codex. No public webhook, Cloudflare tunnel, phone-number, or Photon account configuration was changed. The old `com.deadhidden.photon-tunnel` LaunchAgent still exists from the earlier webhook setup, but the current adapter is operating through the local sidecar stream.
