# Codex - Proton Support Watcher Scaffold

Time: 2026-06-19 15:07 CDT

Adam asked for a small service and scheduler that periodically checks a Proton Mail inbox for customer support issues and takes appropriate customer-service actions.

## Created

- `/Users/adamjohnsson/.deadhidden-os/ops/services/proton-support-watch/`
- `/Users/adamjohnsson/.deadhidden-os/ops/bin/proton-support-watch`

The service is a Python stdlib project using Proton Mail Bridge IMAP/SMTP:

- secure config through environment variables or macOS Keychain command variables
- configurable polling interval
- SQLite idempotency store
- dry-run mode by default
- local logging
- local escalation markdown files
- optional SMTP acknowledgements gated by `PROTON_SUPPORT_REPLY_ENABLED=1`
- launchd plist template and installer script, dry-run by default

## Verification

- `python3 -m compileall proton_support_watch` passed.
- `python3 -m unittest discover -s tests` passed.
- `plutil -lint launchd/com.deadhidden.proton-support-watch.plist.example` passed.
- `proton-support-watch --help` works.
- Sanitized config check against `.env.example` fails safely because no real Bridge password is present.

## Boundary

Local scaffold, wrapper, docs, tests, and receipt only.
No Proton account login, no Proton Bridge configuration change, no email send, no mailbox mutation, no Stripe/customer/money mutation, no refund/cancellation/card change, no Substack/X/public post, no deploy, no Linear/Notion write, and no launchd scheduler install/load were performed.

## Next

Fill `.env` from Proton Mail Bridge Mailbox details or macOS Keychain, run a dry-run poll, inspect the SQLite/log/escalation output, then install launchd if the dry-run is clean.
