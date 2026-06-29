# Codex Receipt - Hermes Opus 4.8 Switch

Time: 2026-06-13 07:58 CDT

## Request

Adam asked Codex to switch Hermes off Fable 5 and onto Opus 4.8 after the model picker showed Fable 5 unavailable.

Codex treated the screenshot and Adam's instruction as the operational model-availability source. Codex did not verify any legal or government-ban claim.

## Changed

- `/Users/adamjohnsson/.hermes/config.yaml`
  - `model.default` changed from `claude-fable-5` to `claude-opus-4-8`
  - `providers.claude-max-opus.model` changed from `claude-fable-5` to `claude-opus-4-8`
- `/Users/adamjohnsson/.hermes/profiles/writer/config.yaml`
  - `model.default` changed from `claude-fable-5` to `claude-opus-4-8`
  - `providers.claude-max-opus.model` changed from `claude-fable-5` to `claude-opus-4-8`
  - added `claude-opus-4-8` and `macproxy/adam-writing-opus-4-8` model entries
- `/Users/adamjohnsson/.hermes/profiles/storeanalyst/config.yaml`
  - `model.default` changed from `claude-fable-5` to `claude-opus-4-8`
  - `providers.claude-max-opus.model` changed from `claude-fable-5` to `claude-opus-4-8`
- `/Users/adamjohnsson/.deadhidden-os/ops/TEAM_CONTEXT.md`
  - replaced stale Fable lane with current Opus lane and reload caveat
- `/Users/adamjohnsson/.deadhidden-os/ops/TELEGRAM.md`
  - replaced stale Fable lane with current Opus lane and reload caveat

Backups:

- `/Users/adamjohnsson/.hermes/backups/manual-model-switch-20260613-0749/config.yaml`
- `/Users/adamjohnsson/.hermes/backups/manual-model-switch-20260613-0749/writer-config.yaml`
- `/Users/adamjohnsson/.hermes/backups/manual-model-switch-20260613-0749/storeanalyst-config.yaml`

## Verification

- YAML validation passed for the three edited Hermes config files.
- `hermes status` reports `Model: claude-opus-4-8` and `Provider: claude-max-opus`.
- `hermes --profile writer status` reports `Model: claude-opus-4-8` and `Provider: claude-max-opus`.
- `hermes --profile storeanalyst status` reports `Model: claude-opus-4-8` and `Provider: claude-max-opus`.
- `launchctl print user/501/ai.hermes.gateway` reports gateway running as PID `11268`.
- `launchctl print gui/501/com.biblicalman.claude-max-proxy` reports proxy running as PID `14588`.
- `/Users/adamjohnsson/claude-max-proxy.log` shows direct `claude-opus-4-8` requests completed successfully at 07:52 and 07:54 CDT.

## Blocker

Codex could not restart or reload the live gateway process from the sandbox:

- `hermes gateway restart` failed with `Could not kickstart service "ai.hermes.gateway": 1: Operation not permitted`.
- `launchctl kickstart -k user/501/ai.hermes.gateway` failed with `Operation not permitted`.
- `kill -TERM 11268` failed with `operation not permitted`.

The running gateway still exists as PID `11268`. Its last real Telegram turn before this switch initialized an agent with `claude-fable-5` at 07:46 and completed at 07:47. Because that agent may remain cached, Telegram may not fully rotate to Opus until `/new` or `/reset`, cache eviction, or a manual gateway restart.

The Hermes CLI smoke test from Codex also failed because the sandbox blocked local socket access (`Operation not permitted`) before requests reached the proxy. That is a Codex sandbox limitation, not proof that Opus 4.8 is unavailable.

## Practical Use

For the next Hermes Telegram task, send `/new` first. The Hermes slash-command code clears the cached agent on `/new` or `/reset`, which should force a fresh agent using the new global default `claude-opus-4-8`.

No public posts, emails, customer actions, money actions, deployments, credential changes, or webhook changes were performed.
