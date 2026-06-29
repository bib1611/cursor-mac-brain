# TBM roll-call newsletter sent and watcher reloaded

## Summary

After Adam explicitly said "Send the newsletter now," Codex published/sent Biblical Man draft `202711652` as an `everyone` newsletter.

Public post: `https://biblicalman.substack.com/p/can-you-still-see-this`

## Proof

- Publish proof: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-19-tbm-substack-rollcall-staging/publish-result.json`
- Public screenshot: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-19-tbm-substack-rollcall-staging/published-public-page.png`
- Watcher: `/Users/adamjohnsson/.deadhidden-os/ops/bin/tbm-rollcall-watch`
- Launchd: `/Users/adamjohnsson/Library/LaunchAgents/com.biblicalman.tbm-rollcall-watch.plist`
- Ledger: `/Users/adamjohnsson/.deadhidden-os/ops/data/tbm-rollcall-watch.sqlite3`

## Verification

- Publish API returned post id `202711652`, slug `can-you-still-see-this`, `post_date=2026-06-19T12:30:23.642Z`, and `email_sent_at=2026-06-19T12:30:23.756Z`.
- Public page returned HTTP `200`.
- Watcher `py_compile` and `--self-test` passed.
- Plist lint passed.
- Launchd reloaded with `TBM_ROLLCALL_LIVE_SUBSCRIBERS=1`, `TBM_ROLLCALL_SEND_EMAILS=0`, and latest scheduled run exited `0`.
- As of `2026-06-19 07:41 CDT`, watcher ledger showed `5` comments captured: `4` tagged `here`, `1` tagged `other`.
- `5` outreach rows were queued as `needs_email` because live subscriber searches timed out during enrichment.

## Boundary

One exact approved Substack publish/send only. No personal customer email was sent, no bulk/cron outbound email was enabled, no Substack subscriber tag mutation was performed, no X/Notes post, no Stripe/customer mutation, no deploy, no Linear/Notion write, no credential change, and no account-setting change.
