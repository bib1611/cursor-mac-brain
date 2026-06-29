# Ponytail plugin — installed into Codex

Date: 2026-06-14 ~22:36 CDT
Owner: Hermes (Telegram operator), at Adam's explicit "install it so we can use it"

## What was done
- `codex plugin marketplace add DietrichGebert/ponytail` → marketplace registered (`[marketplaces.ponytail]`).
- Cloned to `/Users/adamjohnsson/.codex/.tmp/marketplaces/ponytail` (plugin.json v4.4.0, MIT).
- Enabled: appended `[plugins."ponytail@ponytail"]` `enabled = true` to `~/.codex/config.toml`.
- Backup: `~/.codex/config.toml.bak-ponytail-20260614-223640`.
- TOML re-validated with tomllib → parses clean.

## Verified
- codex-cli 0.130.0; `plugin marketplace add` is real.
- Two hooks present and match the files cleared earlier from GitHub source:
  - SessionStart → hooks/ponytail-activate.js
  - UserPromptSubmit → hooks/ponytail-mode-tracker.js
- Hooks cleared: no network, no secrets/env reads (Stripe/Gmail/keys untouched), no shell-exec, 5s timeout, silent-fail.
- Skills bundled: ponytail, ponytail-audit, ponytail-debt, ponytail-help, ponytail-review.

## Remaining human step
- `trusted_hash` for ponytail = 0. On next Codex session start, Codex will prompt Adam to TRUST the ponytail hook before it runs. That approval is required — it is a security gate, not a failure.

## Scope note
- Installed into CODEX only (the lane that stalled on familiar-spirits). NOT Claude Code, NOT Hermes content layer. Ponytail is code-writing discipline; it does not touch content/revenue.
