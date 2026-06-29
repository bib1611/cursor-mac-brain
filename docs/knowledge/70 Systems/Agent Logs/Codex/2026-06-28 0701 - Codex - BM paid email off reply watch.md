# 2026-06-28 0701 - Codex - BM paid email off reply watch

Automation: `bm-paid-email-off-reply-watch`

Profile confirmed: Biblical Man Gmail connector profile `thebiblicalman1611@gmail.com`.

Runbook: `/Users/adamjohnsson/Downloads/bm-email-off-reply-watch-runbook.md`

Searches:

- Paid email-off: `in:inbox newer_than:30d subject:"Quick check on your Biblical Man emails" -from:thebiblicalman1611@gmail.com`
- Dormant free: `in:inbox newer_than:30d subject:"Still want Biblical Man in your inbox?" -from:thebiblicalman1611@gmail.com`

Result:

- Paid campaign returned 3 inbox message ids, all already logged in SQLite (`reply_events.id = 22..24`), so they were skipped by dedupe.
- Dormant free returned 0 inbox message ids.

SQLite proof: `/Users/adamjohnsson/Downloads/bm-email-off-reply-watch.sqlite3`, `agent_runs.id = 7264`, `created_at = 2026-06-28 12:01:39` UTC.

Boundary: no message body reads, email send/draft, label, archive, delete, spam mark, unsubscribe, refund, cancellation, Substack/customer change, Stripe/customer/money mutation, public post, deploy, Linear/Notion write, credential change, or account-setting change happened.
