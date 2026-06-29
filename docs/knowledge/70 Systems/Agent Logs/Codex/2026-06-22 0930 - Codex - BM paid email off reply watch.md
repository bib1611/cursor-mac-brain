# 2026-06-22 09:30 CDT - Codex - BM paid email off reply watch

Automation `bm-paid-email-off-reply-watch` ran against the Biblical Man Gmail connector profile `thebiblicalman1611@gmail.com`.

Searched the exact runbook inbox scopes:

- Paid Email-Off: `in:inbox newer_than:30d subject:"Quick check on your Biblical Man emails" -from:thebiblicalman1611@gmail.com`
- Dormant Free: `in:inbox newer_than:30d subject:"Still want Biblical Man in your inbox?" -from:thebiblicalman1611@gmail.com`

Result: paid campaign returned 3 inbox message ids, all already logged in SQLite, so they were skipped by the dedupe rule. Dormant free returned zero message ids.

Recorded SQLite no-action run: `/Users/adamjohnsson/Downloads/bm-email-off-reply-watch.sqlite3`, `agent_runs.id = 5034`, `created_at = 2026-06-22 14:30:13` UTC.

Boundary: no email read beyond candidate id search, no send/draft, label, archive, delete, spam mark, unsubscribe, refund, cancellation, Substack/customer change, Stripe/customer/money mutation, public post, deploy, Linear/Notion write, credential change, or account-setting change happened.
