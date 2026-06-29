# 2026-06-21 2040 - Codex - BM paid email off reply watch

Automation: `bm-paid-email-off-reply-watch`

Confirmed Gmail connector profile is the Biblical Man account `thebiblicalman1611@gmail.com`.

Read the local runbook at `/Users/adamjohnsson/Downloads/bm-email-off-reply-watch-runbook.md` plus the active ops capsule files.

Searched the exact runbook inbox scopes:

- Paid Email-Off: `in:inbox newer_than:30d subject:"Quick check on your Biblical Man emails" -from:thebiblicalman1611@gmail.com`
- Dormant Free: `in:inbox newer_than:30d subject:"Still want Biblical Man in your inbox?" -from:thebiblicalman1611@gmail.com`

Result: zero matching Gmail message ids for both campaigns.

SQLite proof: `/Users/adamjohnsson/Downloads/bm-email-off-reply-watch.sqlite3`, `agent_runs.id = 4591`, `created_at = 2026-06-22 01:40:56` UTC.

Boundary: no email send/draft, label, archive, delete, spam mark, unsubscribe, refund, cancellation, Substack/customer change, Stripe/customer/money mutation, public post, deploy, Linear/Notion write, credential change, or account-setting change happened.
