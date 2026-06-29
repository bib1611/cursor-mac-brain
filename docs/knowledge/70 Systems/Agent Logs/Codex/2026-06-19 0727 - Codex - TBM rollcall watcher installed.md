# 2026-06-19 07:27 - Codex - TBM rollcall watcher installed

## Changed

- Updated Biblical Man Substack draft `202711652` (`Can You Still See This?`) to remove `No pitch today.`
- The draft had already had `I am not selling anything in this note.` removed.
- Added local watcher script:
  - `/Users/adamjohnsson/.deadhidden-os/ops/bin/tbm-rollcall-watch`
- Added launchd job:
  - `/Users/adamjohnsson/Library/LaunchAgents/com.biblicalman.tbm-rollcall-watch.plist`
- Added SQLite ledger:
  - `/Users/adamjohnsson/.deadhidden-os/ops/data/tbm-rollcall-watch.sqlite3`

## Behavior

- Runs every 300 seconds.
- Watches Substack comments for post/draft id `202711652`.
- Stores commenters in `contacts`.
- Stores public comment rows in `comments`.
- Tags each commenter locally as `rollcall,here`, `rollcall,missed`, or `rollcall,other`.
- Creates an `outreach_queue` row for later personal follow-up.

## Verification

- `/Users/adamjohnsson/.deadhidden-os/ops/bin/tbm-rollcall-watch --self-test` returned `self-test ok`.
- `plutil -lint /Users/adamjohnsson/Library/LaunchAgents/com.biblicalman.tbm-rollcall-watch.plist` returned `OK`.
- Manual watcher run returned `{"ok": true, "post_id": "202711652", "status": "ok", "seen": 0, "new": 0, ...}`.
- `launchctl print gui/501/com.biblicalman.tbm-rollcall-watch` showed `last exit code = 0`, `run interval = 300 seconds`, and `TBM_ROLLCALL_SEND_EMAILS => 0`.
- Live Substack draft readback showed `is_published=false`, `email_sent_at=null`, and the body no longer contains `No pitch today.` or `I am not selling anything`.

## Boundary

- No Substack publish/send/schedule.
- No X/Note post.
- No customer email sent.
- No Substack subscriber tag mutation.
- No Stripe/customer/money mutation.

Email sending is intentionally not enabled. The current comment API gives public commenter name/handle/user id, not email addresses. The job queues outreach candidates; sending needs confirmed email resolution and Adam approval of the exact email text.
