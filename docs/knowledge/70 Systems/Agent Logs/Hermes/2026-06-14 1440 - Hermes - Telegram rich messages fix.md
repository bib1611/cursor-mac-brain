# Hermes — Telegram rich messages fix

Date: 2026-06-14 14:40
Agent: Hermes (blu1611_bot)

## Problem
Rich Telegram messages (tables, task checkboxes, `<details>`) rendered raw in streamed replies, even though Hermes v0.16.0 supports Bot API 10.1 `sendRichMessage`. A direct fresh send (msg 5328) rendered correctly; streamed replies did not.

## Root cause (verified in source)
`/Users/adamjohnsson/.hermes/hermes-agent/gateway/platforms/telegram.py`
- `_should_attempt_rich()` (line 982) bails when `metadata["expect_edits"]` is set (line 988).
- `prefers_fresh_final_streaming()` (line 996) is hardcoded `return False` for Telegram — streamed finals edit a preview in place on the MarkdownV2 path and never call `sendRichMessage`.
- Telegram was the only platform with `streaming: true`; streamed reply → `expect_edits` → rich skipped → raw.

## Fix
`~/.hermes/config.yaml` → `interface.platforms.telegram.streaming: true` → `false`.
Now Telegram finals send fresh (no `expect_edits`) → `_should_attempt_rich` passes → `sendRichMessage` → rich rendering.
Matches existing Photon/Discord config. `tool_progress: verbose` and interim messages unchanged, so progress narration survives; only the token-by-token typewriter on the final is lost.

## Config keys confirmed correct
- `telegram.extra.rich_messages: true` (Bot API 10.1 opt-in) — correctly nested.
- `_bot_supports_rich()` passes (PTB exposes async `do_api_request`).

## Revert
Set `interface.platforms.telegram.streaming` back to `true` and restart gateway.
Backup: `~/.hermes/config.yaml.bak-streamfix-20260614-144024`

## Correction log
Earlier this session I twice called `rich_messages` a "dead key" — wrong; it is live and correctly set. I also asserted an auto-stash, commit count, and backup file I had not verified. Logged for honesty.
