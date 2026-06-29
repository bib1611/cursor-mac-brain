# 2026-06-28 0901 - Codex - BM paid email off reply watch

Automation `bm-paid-email-off-reply-watch` ran against the Biblical Man Gmail connector profile `thebiblicalman1611@gmail.com`.

Searched the exact runbook inbox scopes for `Quick check on your Biblical Man emails` and `Still want Biblical Man in your inbox?`.

Result:

- Paid email-off candidates: 3 inbox message ids.
- Paid email-off new after SQLite dedupe: 0.
- Dormant free candidates: 0 inbox message ids.
- Dormant free new after SQLite dedupe: 0.

Paid candidate dedupe proof:

- `19eef738a2e1ab96` already logged as `reply_events.id = 22`.
- `19eef9a78e07f776` already logged as `reply_events.id = 23`.
- `19eef9aaf2f4af3e` already logged as `reply_events.id = 24`.

Recorded SQLite no-action run: `/Users/adamjohnsson/Downloads/bm-email-off-reply-watch.sqlite3`, `agent_runs.id = 7526`, `created_at = 2026-06-28 14:01:45` UTC.

Boundary: no message body reads, email send/draft, label, archive, delete, spam mark, unsubscribe, refund, cancellation, Substack/customer change, Stripe/customer/money mutation, public post, deploy, Linear/Notion write, credential change, or account-setting change happened.
