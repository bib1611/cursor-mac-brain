# 2026-06-10 21:50 — Hermes — Profile lanes finalized, persistent support sweep, Hermes update

Adam approved (voice memo, Telegram, ~21:30): build the three profiles on subscription models, no more Opus burn, run the update.

## Profile state (verified via `hermes profile show`)

- **writer** — claude-fable-5 on claude-max-opus (Fable 5, Claude Max sub). 36 curated skills (writing-imports, confessional-miner, ghostwriter, anti-slop-scorer, dead-hidden-tweet-coach, content-atomizer). SOUL.md dated 2026-06-10. Alias `writer`.
- **support** — gpt-5.5 on codex-gpt-5.5 (Codex 5.5 sub). Lean commerce/email loadout. SOUL.md carries the refund hard-lock (refunds/cancellations/card changes = Adam only). Alias `support`. Full .env incl. mail access.
- **storeanalyst** — claude-fable-5 (Max). cro, conversion-ops, deadhidden-store, churn-prevention. Posted-cash-only rule in SOUL.md. Alias `storeanalyst`.

Models were already correct from the dashboard profile-factory session earlier today — no changes needed. Dead swarm profiles (swarm1/4/5/8/12) already pruned. Remaining profiles (blank, grokbuild, kanban, librarian, openclaw, qwenlocal, tactical, workhorse) left untouched — intentional lanes.

## Support sweep made permanent

- Old sweep `bca590e2` was session-bound (would die on gateway restart; `hermes cron list` showed zero registered jobs).
- New gateway-level cron: **`8ce1b1257abf` "support-sweep"** — `*/30 7-21 * * *`, runs under **support profile** (Codex 5.5, cheap lane), skills himalaya + deadhidden-commerce-ops, delivers to Telegram, NO_REPLY-silent when inbox is clean. First run 2026-06-11 07:00.
- Refund hard-lock baked into the job prompt: never moves money, flags refund asks, escalates broken delivery routes immediately.

## Update

- Hermes v0.16.0, 20 commits behind origin/main (includes profiles-page modal fix).
- `hermes update --yes` + gateway restart fired detached at ~21:51. Old session-bound cron dies with the restart (replaced above).

— Hermes
