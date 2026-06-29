# 2026-06-09 12:40 CDT - Codex - Hermes Fable 5 High Attempt

Adam asked Codex to switch Hermes to "Fable 5 high."

Codex booted from the local ops capsule, refreshed `TEAM_CONTEXT.md`, and checked Hermes live routing before changing anything.

What was verified:

- Hermes was on provider `claude-max-opus` with model `claude-opus-4-8`.
- The local Claude/OpenAI-compatible proxy at `http://127.0.0.1:3458/v1/models` advertised `claude-opus-4-8`, `macproxy/adam-writing-opus-4-8`, `claude-opus-4-7`, `macproxy/adam-writing-opus-4-7`, `claude-sonnet-4-6`, and `claude-haiku-4`.
- The proxy did not advertise `fable-5` or any Fable model.
- A direct Claude CLI test with `--model fable-5 --effort high` failed with the model unavailable/access message.

Change made:

- Backed up Hermes config to `/Users/adamjohnsson/.hermes/config.yaml.bak-fable5-high-attempt-20260609-1236`.
- Set the real Hermes key `agent.reasoning_effort` from `xhigh` to `high`.
- Removed the accidental unused plural `agents.reasoning_effort` block that was created during the first config attempt.
- Kept live routing on `claude-max-opus` / `claude-opus-4-8` because exact Fable 5 was not available on this Mac/account path.

Verification:

- Restarted Hermes gateway. Launchd reported the known stale-service/manageability issue and Hermes started the gateway as a background process.
- Gateway status showed PID `66522`.
- `rg` verified the active config now has `reasoning_effort: high` on the real agent key.
- Default Hermes smoke test returned exactly `HERMES_HIGH_READY`.

Boundary:

- No secrets were printed or changed.
- No public post, Telegram message, Substack action, X action, deploy, checkout, customer action, or external send was performed.
- Fable 5 was not claimed active; the safe applied change is Hermes high effort on the current live Claude Opus 4.8 route.
