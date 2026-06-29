# Codex - Hermes Desktop Agent Init Fix

Date: 2026-06-12 0922 CDT

## Request

Adam asked Codex to fix Hermes Desktop after agent startup failed with:

`No Anthropic credentials found. Set ANTHROPIC_TOKEN or ANTHROPIC_API_KEY, run 'claude setup-token', or authenticate with 'claude /login'.`

## Diagnosis

Hermes was configured to run `claude-fable-5` through the raw `anthropic` provider:

```yaml
model:
  default: claude-fable-5
  provider: anthropic
```

The usable local lane was already configured under `providers.claude-max-opus`, pointing to the local proxy:

`http://127.0.0.1:3458/v1`

No `ANTHROPIC_TOKEN` or `ANTHROPIC_API_KEY` was present in shell or `/Users/adamjohnsson/.hermes/.env`.

## Change

Backed up the live config:

`/Users/adamjohnsson/.hermes/config.yaml.bak-agent-init-failed-20260612-0913`

Changed `/Users/adamjohnsson/.hermes/config.yaml`:

```diff
-  provider: anthropic
+  provider: claude-max-opus
```

No Anthropic credential was added, printed, stored, or changed.

## Verification

- `hermes status` reports model `claude-fable-5` and provider `claude-max-opus`.
- Local Fable/Claude Max proxy health at `http://127.0.0.1:3458/health` reports `status: ok`, provider `codex-gpt-5.5-with-claude-fallback`, active account `thebiblicalman2`.
- Hermes API health at `http://127.0.0.1:8642/health` returned ok.
- Direct Hermes smoke before restart returned `HERMES_DEFAULT_AGENT_OK`.
- Restarted Hermes gateway with `hermes gateway restart`; new gateway PID after restart was `11268`.
- Quit and relaunched Hermes Desktop from `/Users/adamjohnsson/.hermes/hermes-agent/apps/desktop/release/mac-arm64/Hermes.app`.
- Desktop dashboard status at `http://127.0.0.1:9120/api/status` reports version `0.16.0`, gateway running, gateway PID `11268`, Telegram/API connected, active sessions `0`.
- Visual check screenshot showed Hermes Desktop open, gateway ready, `Agents 1 running`, and model `Fable 5 - Fast Max`.
- Agent log after the fix shows agent init using `provider=custom base_url=http://127.0.0.1:3458/v1 model=claude-fable-5`, not raw Anthropic.
- Proxy `/v1/models` lists `claude-fable-5`.
- Direct proxy smoke for `gpt-5.5` returned `PROXY_GPT_OK`.
- Direct proxy smoke for `claude-fable-5` returned `PROXY_FABLE_OK`.

## Photon Cleanup

While verifying Hermes, Codex found merge-conflict markers left in Photon customizations from the prior Hermes update:

- `/Users/adamjohnsson/.hermes/hermes-agent/plugins/platforms/photon/adapter.py`
- `/Users/adamjohnsson/.hermes/hermes-agent/plugins/platforms/photon/sidecar/index.mjs`

Codex resolved the conflicts on disk, preserving the Photon message/reaction/read-marking customizations and the fresh `httpx.AsyncClient(timeout=120.0)` behavior.

Verification:

- `rg -n '<<<<<<<|=======|>>>>>>>' plugins/platforms/photon/adapter.py plugins/platforms/photon/sidecar/index.mjs` found no conflict markers.
- `python -m py_compile plugins/platforms/photon/adapter.py` passed.
- `node --check plugins/platforms/photon/sidecar/index.mjs` passed.
- `git diff --check` passed.
- `git status --short` now shows both Photon files as staged modifications, not unresolved conflicts.

Codex did not restart Hermes again after the Photon cleanup because the desktop had an active Fable job running behind the proxy. Photon changes are ready to load on the next safe gateway restart.

## Current State

At 2026-06-12 0922 CDT:

- Hermes Desktop is running.
- Hermes gateway is running.
- Dashboard API is healthy.
- Local Fable proxy is healthy.
- Proxy queue reported `active: 1`, `queued: 1`; the active process was `claude --print --model claude-fable-5`, likely the desktop-started Fable run.

## Boundary

No public post, customer action, money action, deploy, webhook change, credential change, API key print, Anthropic key install, browser account mutation, or external account write was performed. Hermes gateway restart may have sent its normal shutdown/startup notifications to configured channels.
