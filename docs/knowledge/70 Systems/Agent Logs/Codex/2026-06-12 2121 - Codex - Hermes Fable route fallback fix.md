# 2026-06-12 21:21 CDT - Codex - Hermes Fable Route Fallback Fix

## Trigger

Adam reported Hermes returning:

`There's an issue with the selected model (claude-fable-5). It may not exist or you may not have access to it. Run --model to pick a different model.`

## Finding

Hermes config was still pointed at the intended local route:

- `model.default: claude-fable-5`
- `model.provider: claude-max-opus`
- proxy: `http://127.0.0.1:3458/v1`

The failure was inside `/Users/adamjohnsson/claude-max-proxy.js`: a Fable request launched the Claude CLI, the CLI exited code 1, and the proxy returned the CLI's model-access text as a normal assistant response.

Direct checks:

- `claude-fable-5` through the proxy returned the selected-model/access error.
- `claude-opus-4-7` through the same proxy returned `OPUS_PROXY_SMOKE_OK`.
- `/opt/homebrew/bin/claude --version` remained `2.1.116`.
- `claude update` installed `@anthropic-ai/claude-code@2.1.177` under `/Users/adamjohnsson/.hermes/node`.
- `/Users/adamjohnsson/.hermes/node/bin/claude --version` returned `2.1.177`.
- Direct Fable with the updated CLI still failed for `/Users/adamjohnsson/.claude-account2`.
- Other local Claude account dirs returned subscription-access disabled errors.

Conclusion: this is current account/model entitlement for Fable, not a Hermes config issue.

## Actions

Patched `/Users/adamjohnsson/claude-max-proxy.js`:

- Added `CLAUDE_BIN`, defaulting to `/Users/adamjohnsson/.hermes/node/bin/claude`.
- Added `CLAUDE_FABLE_5_AVAILABLE`; Fable is considered enabled only when this env var is `1`.
- Added `CLAUDE_FABLE_FALLBACK_MODEL`, defaulting to `claude-opus-4-7`.
- Route Fable-shaped requests to `claude-opus-4-7` while Fable is not enabled on the current account.
- Changed Claude spawns to use `CLAUDE_BIN` instead of resolving the stale global `claude` shim.

Restarted only:

`com.biblicalman.claude-max-proxy`

## Verification

- `node --check /Users/adamjohnsson/claude-max-proxy.js` passed.
- `launchctl print gui/501/com.biblicalman.claude-max-proxy` showed the service running with PID `14588`.
- Raw proxy model list still exposed the expected model aliases.
- Raw proxy Fable-shaped smoke returned `FABLE_PROXY_FALLBACK_OK`.
- Raw proxy Opus smoke returned `OPUS_PROXY_STILL_OK`.
- Proxy log recorded:

`claude-fable-5 not enabled for current Claude account; routing request to claude-opus-4-7`

- Hermes health returned:

`{"status": "ok", "platform": "hermes-agent", "version": "0.16.0"}`

- Hermes end-to-end smoke returned:

`HERMES_FABLE_ROUTE_FIXED`

Command:

`/Users/adamjohnsson/.local/bin/hermes chat -q 'Reply exactly: HERMES_FABLE_ROUTE_FIXED' --provider claude-max-opus -m claude-fable-5 -t '' -Q`

## Boundary

No Anthropic API key was added, printed, stored, or changed.

No public post, customer action, money action, deploy, Telegram webhook change, account mutation, or external send was performed.

This is a local proxy fallback. To restore true Fable, first prove direct access with:

`CLAUDE_CONFIG_DIR=/Users/adamjohnsson/.claude-account2 /Users/adamjohnsson/.hermes/node/bin/claude --print --model claude-fable-5`

Then set `CLAUDE_FABLE_5_AVAILABLE=1` in the proxy launch environment and restart `com.biblicalman.claude-max-proxy`.
