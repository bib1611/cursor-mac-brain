# 2026-06-11 09:49 CDT - Codex - Hermes Telegram Provider Failure Triage

Adam sent a Telegram screenshot from the `blu` Hermes bot showing provider-failure messages after asking about a "5 dollar tripwire" task.

## Finding

The screenshot does not mean Hermes Desktop or the Mac Mini were down. It does mean that this specific Telegram request did not complete with a model answer.

## Live Checks

- Hermes API health returned:

```json
{"status":"ok","platform":"hermes-agent","version":"0.16.0"}
```

- Gateway API was listening on `127.0.0.1:8642`.
- Dashboard was listening on `127.0.0.1:9120`.
- Photon sidecar was listening on `127.0.0.1:8789`.
- `hermes gateway status` showed a live gateway process, but launchd was not managing it:

```text
Gateway process is running for this profile, but the service is not active
```

## Log Evidence

- `5 dollar tripwire` arrived from Telegram at `2026-06-11 09:27:52` in session `20260611_090240_b1c66fa4`.
- Primary model route failed after retries:

```text
provider=claude-max-opus model=claude-fable-5
HTTP 503 server_busy: Server busy - too many requests queued.
```

- Fallback activated, then failed after retries:

```text
provider=codex-gpt-5.5 model=gpt-5.5
HTTP 404: Not found
```

- Hermes sent the Telegram failure message at `09:28:07`.
- Adam's `Ok` at `09:40:01` hit the same primary 503 and fallback 404 pattern, and Hermes sent the same failure message at `09:40:16`.
- Request dumps were written under:

```text
/Users/adamjohnsson/.hermes/sessions/request_dump_20260611_090240_b1c66fa4_20260611_092807_500299.json
/Users/adamjohnsson/.hermes/sessions/request_dump_20260611_090240_b1c66fa4_20260611_094016_818250.json
```

## Related Context

The earlier Telegram task `Give me the preview of the new guide Adam to Noah` did complete at `09:16:10` with a 1399-character response. The later `5 dollar tripwire` task did not complete.

## Follow-Up: Desktop/TUI Session State

After Adam asked whether the desktop app session was done with its tasks, Codex checked the same live logs again at `09:55 CDT`.

- The Telegram session `20260611_090240_b1c66fa4` was finished-failed; it was not still processing.
- The separate Desktop/TUI session `20260611_065812_7e622b` had earlier completed several turns:
  - `06:58` content performance check finished at `07:03`.
  - `07:15` X article research turn finished at `07:26`.
  - `07:30` staging turn finished at `07:53`.
  - `08:01` tracking/watch turn finished at `08:07`.
  - `08:55` tripwire planning turn finished at `08:57`.
- The next Desktop/TUI turn began at `08:59:45` and did not show a clean `Turn ended` line by `09:55`.
- That turn hit empty model responses at `09:14:47`, `09:31:10`, and `09:46:46`, then opened another model request.
- Current operational read: the desktop app session is not cleanly done; the latest Desktop/TUI task appears stalled/hung in model runtime after the third empty-response retry.
- Codex Agent Bus inbox showed no pending Codex bus tasks, so this is a Hermes Desktop/TUI session issue rather than a queued Codex bridge task.

## Operational Read

The immediate issue is provider/proxy routing, not a dead desktop:

- Primary route through local proxy `127.0.0.1:3458/v1` returned queued/busy errors at task time.
- Fallback provider `codex-gpt-5.5` returned 404 for `gpt-5.5`.
- Later live check found `127.0.0.1:3458` not listening, so the local model proxy route needs repair before relying on this fallback.
- Gateway service management also needs cleanup because the gateway process is alive but not launchd-managed.
- Follow-up live check at `09:55` found `127.0.0.1:3458/v1/models` responding again, but gateway service management was still mismatched: live PID `97039`, launchd service not loaded.

## Boundaries

No Hermes restart, gateway restart, update, config edit, model-provider edit, public post, customer action, money action, or external account action was performed.
