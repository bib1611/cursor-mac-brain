# 2026-06-12 12:27 CDT - Codex - Kickbacks campaign live tracking started

Adam completed the Kickbacks Stripe checkout and asked Codex to track the campaign.

Verification:

- Kickbacks public leaderboard showed the paid campaign live:
  - Display name: `Dead Hidden`
  - Ad line: `Read the Bible like source code`
  - Bid: `$12.01`
  - Target: `4,000` impressions
  - First observed at ~12:23 CDT: rank `11`, `133 / 4,000` impressions served
- Second tracker snapshot at 12:26 CDT:
  - Rank: `11`
  - Served: `824 / 4,000`
  - Remaining: `3,176`
  - Rank 10 bid: `$12.50`
  - Stripe Kickbacks-attributed checkout sessions: `0`
  - Stripe Kickbacks-attributed paid sessions: `0`
  - Vercel last-30-min page-path requests for `/store/how-to-count-your-bible`: `6`
  - Vercel checkout API requests: `0`

Tracking assets:

- Tracker script: `/Users/adamjohnsson/Documents/Codex/2026-06-12/fix-hermes-desktop-agent-init-failed/work/track_kickbacks_count_bible.py`
- Latest status: `/Users/adamjohnsson/Documents/Codex/2026-06-12/fix-hermes-desktop-agent-init-failed/outputs/kickbacks-count-bible-live-status.md`
- Latest JSON snapshot: `/Users/adamjohnsson/Documents/Codex/2026-06-12/fix-hermes-desktop-agent-init-failed/outputs/kickbacks-count-bible-live-snapshot.json`
- Snapshot log: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-12-kickbacks-ad-test/snapshots.jsonl`
- Ops status mirror: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-12-kickbacks-ad-test/LAST_STATUS.md`

Automation:

- Created Codex heartbeat automation `track-kickbacks-count-bible-ad`.
- Schedule: every 30 minutes for 8 checks.
- Task: run the tracker and report Kickbacks rank/impressions, Stripe Kickbacks-attributed checkout/paid sessions, and Vercel page-path/checkout API counts.

Boundary:

- No Kickbacks extension installed.
- No Hermes/Codex/Claude runtime patched.
- No bid increase performed.
- No public post made.
- No further spend or account mutation performed.
