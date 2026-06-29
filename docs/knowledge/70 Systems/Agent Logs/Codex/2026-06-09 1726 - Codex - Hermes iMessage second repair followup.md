# Codex - Hermes iMessage Second Repair Followup

Date: 2026-06-09 17:26 CDT

Adam sent an iMessage test after the first Codex follow-up and saw no read receipt or reply.

## Findings

- The live `Test` message did reach Hermes at 17:21 CDT. Gateway logged inbound Photon text, so inbound was not dead.
- The reply lane still used a streaming/interim path for Photon, which made the local proxy open `stream=true` requests even after the Photon/Fable fast-route was added.
- Gateway restarts were still able to connect to an orphaned sidecar first, then the newly spawned sidecar crashed on `EADDRINUSE`.
- The earlier Hermes receipt claimed Photon sidecar timeouts had been bumped from 30s to 120s, but the active adapter file still used `30.0` for the HTTP client, `/send`, and standalone send helper.
- A stale auto-resumed blank Photon turn attempted to reply after restart and hit the 30s send timeout. That response should be ignored if it lands late.

## Changes

- Added explicit Photon final-answer-only display overrides in `/Users/adamjohnsson/.hermes/config.yaml`:
  - `display.platforms.photon.streaming: false`
  - `interim_assistant_messages: false`
  - `long_running_notifications: false`
  - `busy_ack_detail: false`
  - `tool_progress: off`
- Patched `/Users/adamjohnsson/.hermes/hermes-agent/plugins/platforms/photon/adapter.py`:
  - sidecar HTTP client timeout `30.0` to `120.0`
  - per-call `/send` timeout `30.0` to `120.0`
  - standalone send helper timeout `30.0` to `120.0`
  - send exceptions now include the exception class so `ReadTimeout` is not logged as an empty string
- Patched `/Users/adamjohnsson/.hermes/hermes-agent/plugins/platforms/photon/sidecar/index.mjs` to log outbound `/send` start and success with char count and message id.
- Killed orphan sidecars and stale Claude/update children, then restarted `ai.hermes.gateway` cleanly.

## Verification

- Final steady state:
  - `ai.hermes.gateway` running as PID 77903.
  - Photon sidecar running as child PID 78260.
  - `127.0.0.1:8642` and `127.0.0.1:8789` listening.
  - `curl http://127.0.0.1:8642/health` returned ok.
  - No active `claude --print`, `hermes update --check`, or `git-remote-https` children.
  - Gateway logs show Telegram connected, Photon sidecar listening, Photon connected, API server listening, and gateway running with 3 platforms.

## Boundary

No real outbound iMessage test was sent by Codex. No public webhook, Photon account, Cloudflare tunnel, credential, or phone-number configuration was changed. Fresh Adam-side iMessage test still required to verify end-to-end read and send.
