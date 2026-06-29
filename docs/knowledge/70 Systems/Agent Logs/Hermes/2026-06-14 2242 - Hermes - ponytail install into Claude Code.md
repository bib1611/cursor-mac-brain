# Hermes Receipt — ponytail installed into Claude Code

Date: 2026-06-14 22:42 CDT
Operator: Hermes (Telegram)
Action: Installed `ponytail@ponytail` v4.4.0 into the Claude Code coding lane.

## What was done
- `claude plugin marketplace add DietrichGebert/ponytail` → success (HTTPS clone, validated)
- `claude plugin install ponytail@ponytail` → success, scope: user, enabled: true
- Verified via `claude plugin list --json`: ponytail v4.4.0, enabled=true

## Key finding — active config dir
The live `claude` CLI operates on **`~/.claude-account2/`**, NOT `~/.claude/`.
- Install landed at: `~/.claude-account2/plugins/cache/ponytail/ponytail/4.4.0/`
- First backups I made (`~/.claude/plugins/*.bak-ponytail-20260614-224139`) were the INACTIVE account — harmless but not the mutated files.
- In account2, all other plugins (telegram, vercel, codex, claude-code-setup) show enabled=false/scope=project. ponytail is the only user-scope enabled plugin.

## Security verification (installed copy)
- Hooks wired (hooks.json): SessionStart→ponytail-activate.js, UserPromptSubmit→ponytail-mode-tracker.js — identical to Codex install.
- Executing hooks clean: no network/fetch, no secrets (Stripe/Gmail/Resend/OpenRouter/Anthropic env), no child_process/eval.
- grep "hits" were confined to README/tests/benchmarks/marketplace.json (repo URLs) — not executing code.

## Known behavior (same as Codex)
- mode-tracker reads full prompt text every turn (local only, transmits nothing).
- activate.js nudges agent to upsell its own statusline when none configured.
- Claude Code may show a hook-trust prompt on next session start before hooks run.

## Scope
Codex + Claude Code now both run ponytail (code-writing discipline). Hermes content layer untouched.
