# 2026-06-11 18:36 CDT - Codex - Telegram Fable Lane Rewired

Adam asked Codex to wire Telegram back up to use Fable so he could go to it directly.

Codex booted from the local ops capsule, loaded the Telegram Operator skill, refreshed the team packet, checked Hermes config/status, verified the local Fable/Claude Max proxy, and restarted only the local Hermes gateway service.

Actions:

- Confirmed `/Users/adamjohnsson/.hermes/config.yaml` sets `model.default: claude-fable-5` and `model.provider: claude-max-opus`.
- Confirmed `dhc status` reports `Fable lock: unlocked` and public outbound lock still active.
- Confirmed `com.biblicalman.claude-max-proxy` is running and the local proxy health/model list includes `claude-fable-5`.
- Ran a direct Hermes Fable smoke: `TELEGRAM_FABLE_ROUTE_READY`.
- Restarted `ai.hermes.gateway` in the launchd `user/501` domain.
- Confirmed new gateway PID `43589`.
- Confirmed Telegram reconnected in polling mode.
- Confirmed the Telegram webhook remains blank, so cloud fallback was not enabled.
- Confirmed current Telegram session `20260611_090240_b1c66fa4` has no pinned model or model_config and will inherit the live default.
- Ran DHC/API smoke through Hermes after restart: `TELEGRAM_FABLE_AFTER_RESTART`.
- Updated `/Users/adamjohnsson/.deadhidden-os/ops/TELEGRAM.md` with the current Fable lane proof.

Verification:

- `hermes status` reports model `claude-fable-5`, provider `claude-max-opus`, Telegram configured, gateway running under launchd PID `43589`.
- Gateway log shows Telegram disconnected and reconnected in polling mode at 18:36 CDT.
- `cloud-relay-webhook status` returned an empty webhook URL with pending update count `0`.
- `/Users/adamjohnsson/.deadhidden-os/ops/bin/dhc chat 'Reply exactly: TELEGRAM_FABLE_AFTER_RESTART'` returned `TELEGRAM_FABLE_AFTER_RESTART`.

Boundary:

No Telegram webhook cutover, cloud relay mode change, credential/API-key change, public post, customer action, money action, deploy, SMS send, or manual Telegram test message was performed. Hermes automatically sent its normal gateway shutdown notification to configured home channels during the restart.
