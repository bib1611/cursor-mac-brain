# 2026-06-11 10:52 CDT - Codex - Hermes Desktop Fable 5 recovery

## Request

Adam asked Codex to see what was going on with Hermes Desktop and Fable 5 and get it fixed ASAP.

## Findings

- Hermes Desktop was open, but the Fable 5 lane was wedged behind a long-running local proxy request.
- Local proxy health before recovery showed queue state `active:1 queued:0`.
- The active child was a `claude --print --model claude-fable-5 --effort high` job from Hermes/Desktop.
- Proxy logs showed repeated large Fable requests around 21,578 prompt chars, with earlier runs timing out after the proxy's 15 minute timeout.
- Gateway error logs showed the Telegram/provider failure pattern:
  - primary `claude-fable-5` via `http://127.0.0.1:3458/v1` returned 503 `Server busy - too many requests queued`.
  - fallback `codex-gpt-5.5` / `gpt-5.5` returned 404 against the same local proxy path.
- The fallback 404 was observed but not patched in this pass. The immediate live failure was the blocked Fable queue.

## Actions

- Quit Hermes Desktop and terminated lingering dashboard/TUI helper workers that were feeding the stale request back into the proxy.
- Restarted the local Claude/Fable proxy launchd service:
  - label: `com.biblicalman.claude-max-proxy`
  - script: `/Users/adamjohnsson/claude-max-proxy.js`
- Restarted Hermes gateway with the correct command:
  - `/Users/adamjohnsson/.local/bin/hermes gateway --accept-hooks restart`
- Reopened Hermes Desktop from:
  - `/Users/adamjohnsson/.hermes/hermes-agent/apps/desktop/release/mac-arm64/Hermes.app`

## Verification

- Gateway health:
  - `http://127.0.0.1:8642/health`
  - result: `{"status":"ok","platform":"hermes-agent","version":"0.16.0"}`
- Proxy health:
  - `http://127.0.0.1:3458/health`
  - result after recovery: queue `active:0 queued:0`.
- Raw Fable high proxy smoke:
  - request: `claude-fable-5` with `reasoning_effort: high`
  - result: `FABLE_HIGH_OK`
  - proxy log confirmed `model=claude-fable-5 effort=high`.
- Hermes-level Fable smoke:
  - command: `/Users/adamjohnsson/.local/bin/hermes -z 'Reply exactly: HERMES_FABLE_OK' --provider claude-max-opus --model claude-fable-5 --ignore-rules --toolsets clarify`
  - result: `HERMES_FABLE_OK`
- Desktop reopened without replaying the old large Fable job.
- Telegram gateway log after restart:
  - `Connected to Telegram (polling mode)`
  - `Gateway running with 3 platform(s)`

## End State

- Hermes Desktop is running.
- Hermes gateway is running under launchd.
- Telegram is connected in polling mode.
- Fable 5 high route is responding through the live local proxy.
- Proxy queue is clear.
- No Hermes config or proxy code was changed in this pass.

