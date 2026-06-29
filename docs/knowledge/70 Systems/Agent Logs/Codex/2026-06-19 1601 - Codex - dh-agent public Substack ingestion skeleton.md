# Codex - dh-agent public Substack ingestion skeleton

- When: 2026-06-19 16:01 CDT
- Request: Draft the safe public-only Substack ingestion milestone skeleton with public archive/post-page fetch support, normalized parsing, artifacts/report writing, guardrails, parser tests, stubbed network by default, and capped live path behind a flag.

## Files Changed

- `/Users/adamjohnsson/code/dh-agent/package.json`
- `/Users/adamjohnsson/code/dh-agent/config.json`
- `/Users/adamjohnsson/code/dh-agent/src/cli.mjs`
- `/Users/adamjohnsson/code/dh-agent/src/orchestrator.mjs`
- `/Users/adamjohnsson/code/dh-agent/src/tools/fetch.mjs`
- `/Users/adamjohnsson/code/dh-agent/src/tools/report.mjs`
- `/Users/adamjohnsson/code/dh-agent/src/substack-parser.mjs`
- `/Users/adamjohnsson/code/dh-agent/src/public-policy.mjs`
- `/Users/adamjohnsson/code/dh-agent/test/substack-parser.test.mjs`

## What Changed

- Added parser module for public Substack archive payloads and post-page HTML into normalized `{ title, url, date, author }` records.
- Added public-policy validators for public HTTPS URLs, allowlisted domains, GET-only access, no auth/cookie headers, no token query params, forbidden private/admin paths, robots parsing, ToS acknowledgment gate, and live post cap.
- Updated `fetchTool` so network remains stubbed by default. A real fetch path exists only when input uses `live: true` and the task has `constraints.allowLiveNetwork`.
- Updated public ingest handler `ingest.substack.public` to check robots/ToS policy, fetch the public archive route via API adapter, fetch capped post pages via browser adapter, normalize posts, and write both report and JSON artifacts.
- Kept `ingest.substack.archive` as an alias to the new public ingestion handler.
- Added CLI `ingest-public`, stubbed by default. Capped live path requires `--allow-live --ack-tos` and caps pages to 3.
- Added package scripts `npm run ingest:dry-run` and `npm test`.

## Verification

- `find src test -name '*.mjs' -print0 | xargs -0 -n1 node --check` passed.
- `npm test` passed: `substack parser tests OK`.
- `npm run dry-run` passed with task `t-20260619-b6cfad24`.
- `npm run ingest:dry-run` passed with task `t-20260619-f120f429`.
- Dry-run artifacts:
  - `/Users/adamjohnsson/code/dh-agent/artifacts/t-20260619-f120f429/report.md`
  - `/Users/adamjohnsson/code/dh-agent/artifacts/t-20260619-f120f429/normalized-posts.json`
- Guard check: `node src/cli.mjs ingest-public --allow-live --limit 1` refused with `live run requires --ack-tos` before any network call.
- `/Users/adamjohnsson/code/dh-agent` is not a git repository, so there is no commit/status proof.

## Boundary

Local code edits, local parser tests, local stub dry-runs, local artifacts/logs, and receipt only. No live network fetch, no browser control, no authenticated Substack access, no email/send, no public post, no Stripe/customer/money action, no deploy, no Linear/Notion write, and no account change.
