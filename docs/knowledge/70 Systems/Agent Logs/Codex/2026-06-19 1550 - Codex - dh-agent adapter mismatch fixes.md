# Codex - dh-agent adapter mismatch fixes

- When: 2026-06-19 15:50 CDT
- Request: Address the reported `dh-agent` mismatches only: CLI path, dedicated router, split browser/API adapters, minimal rate-limit/backoff helper, keep repo/fetch as stubs, rerun dry-run, stop before new features.

## Files Changed

- `/Users/adamjohnsson/code/dh-agent/package.json`
- `/Users/adamjohnsson/code/dh-agent/src/backoff.mjs`
- `/Users/adamjohnsson/code/dh-agent/src/router.mjs`
- `/Users/adamjohnsson/code/dh-agent/src/tools/api.mjs`
- `/Users/adamjohnsson/code/dh-agent/src/tools/browser.mjs`
- `/Users/adamjohnsson/code/dh-agent/src/tools/fetch.mjs`
- `/Users/adamjohnsson/code/dh-agent/src/orchestrator.mjs`
- `/Users/adamjohnsson/code/dh-agent/src/cli.mjs`

## What Changed

- `package.json` now points `bin.dh-agent` to `./src/cli.mjs` and adds `npm run dry-run`.
- Added `src/router.mjs` as the dedicated tool router and task context builder.
- Added `src/tools/api.mjs` and `src/tools/browser.mjs` as thin wrappers over the existing `fetchTool`.
- Added `src/backoff.mjs` with in-memory rate limiting and minimal exponential backoff helpers.
- Kept `repoTool` and `fetchTool` as stubs, but `fetchTool` now accepts `surface`, uses the shared rate limiter interface, and wraps the stub result in `withBackoff`.
- Updated the orchestrator to use the router instead of importing a local tool map directly.
- Updated `dry-run` to run `demo.adapter.dry_run`, exercising `repo`, `api`, `browser`, and `report` routes with no live network.

## Verification

- `find src -name '*.mjs' -print0 | xargs -0 -n1 node --check` passed.
- `npm run dry-run` passed.
- Dry-run task: `/Users/adamjohnsson/code/dh-agent/tasks/t-20260619-9d11979e.json`
- Dry-run artifact: `/Users/adamjohnsson/code/dh-agent/artifacts/t-20260619-9d11979e/report.md`
- Dry-run route results:
  - `repo` -> `repo`, `ok: true`, `stub: true`
  - `api` -> `api`, `ok: true`, `stub: true`
  - `browser` -> `browser`, `ok: true`, `stub: true`
- `dh-agent` directory is not a git repository, so there is no commit/status proof.

## Boundary

Local code edits, local dry-run task/artifact/log, and receipt only. No real network fetch, browser control, email/send, public post, Stripe/customer/money action, deploy, Linear/Notion write, or account change.
