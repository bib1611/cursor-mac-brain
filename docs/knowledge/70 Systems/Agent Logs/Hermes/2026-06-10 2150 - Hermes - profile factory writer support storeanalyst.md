# Hermes Receipt — Profile Factory Build: writer / support / storeanalyst

Date: 2026-06-10 ~21:50
Agent: Hermes (Telegram operator)
Approved by: Adam (voice memo, this thread — "build the profiles")

## Models (per Adam's spec)

- **writer** → claude-fable-5 via claude-max-opus provider (Fable 5 Max, Claude Max subscription)
- **support** → gpt-5.5 via codex-gpt-5.5 provider (Codex subscription)
- **storeanalyst** → claude-fable-5 via claude-max-opus

All three profile shells + SOUL.md files already existed (created 2026-06-10 21:28 by the dashboard profile factory). Verified SOUL contents: lane-locked, refund hard-lock in support, posted-cash rule in storeanalyst, 60% women audience constraint in writer + storeanalyst.

## Changes made this session

1. **writer skills** — symlinked 12 standalone writing skills into `~/.hermes/profiles/writer/skills/`:
   tweet-generator, subject-line-system, x-article-writer, substack-notes-agent, twitter-algorithm-optimizer, morning-briefing, anti-slop-scorer, content-writer, content-atomizer, ghostwriter, confessional-miner (from ~/.claude/skills) + dead-hidden-tweet-coach (from ~/.agents/skills). Symlinks, so upstream skill patches propagate.
2. **Pruned junk skill groups** from all three profiles: gaming, smart-home, red-teaming, yuanbao (originals untouched in ~/.hermes/skills). Counts after: writer 36 groups, support 27, storeanalyst 31.
3. Swarm shells (swarm1/4/5/8/12) already absent from profile list — pruned before this session, nothing to do.
4. Smoke-tested all three with one-shot `hermes -p <profile> -z` runs (results in thread).

## Aliases

`writer`, `support`, `storeanalyst` wrapper scripts in ~/.local/bin (created by factory).

## Not done / open

- `hermes update` (17 commits behind; fixes profiles-page modal bug) — deferred because gateway restart kills the session-bound support-sweep cron (bca590e2). Needs a decided window + cron rebuild after.
- Photon/iMessage voice memos still arrive untranscribed — voice memos go to Telegram until fixed.
