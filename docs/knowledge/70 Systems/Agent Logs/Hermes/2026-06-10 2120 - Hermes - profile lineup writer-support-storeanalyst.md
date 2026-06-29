# Profile lineup: writer / support / storeanalyst — 2026-06-10 21:20

Adam approved (voice memo, Telegram): build the three-profile lineup, no Opus anywhere.

## Models (per Adam's spec)
- writer → claude-fable-5 via claude-max-opus Mac proxy (Fable 5 = top Claude Max tier; no separate "max" model ID exists)
- support → gpt-5.5 via codex-gpt-5.5 Mac proxy (= Codex 5.5)
- storeanalyst → claude-fable-5 via claude-max-opus Mac proxy

All three profiles already existed with correct models; no model edits needed.

## Changes made
1. support SOUL.md replaced — was a verbatim copy of the main Hermes operator SOUL (identity bleed). Now: customer-rescue lane, refund hard-lock to Adam, reader-reply lock (sign "Adam", no em dashes), no-invented-records rule. Backup: SOUL.md.bak-20260610.
2. storeanalyst SOUL.md replaced — same operator-SOUL clone problem. Now: conversion/offer analyst, read-mostly, posted-cash-only, no live-page or price edits without Adam. Backup: SOUL.md.bak-20260610.
3. Skills symlinked:
   - support/skills: deadhidden-commerce-ops → ~/.codex/skills/deadhidden-commerce-ops
   - storeanalyst/skills: deadhidden-store, cro, conversion-ops, churn-prevention (→ ~/.claude/skills/*), deadhidden-commerce-ops (→ ~/.codex/skills/)
4. writer untouched — already had proper Writer SOUL + adam-writing-imports skills + fable-5.

## Notes
- Earlier-session swarm shells (swarm1/4/5/8/12) no longer present in `hermes profile list` — nothing to prune.
- Smoke tests dispatched for all three profiles (one-shot chat -q).
- Pending separately: `hermes update` (17 commits behind, profiles-page modal fix) — NOT run; it restarts the gateway and would kill the session-bound support-sweep cron bca590e2.
