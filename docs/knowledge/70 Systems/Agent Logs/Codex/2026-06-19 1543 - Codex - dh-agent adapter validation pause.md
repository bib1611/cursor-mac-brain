# Codex - dh-agent adapter validation pause

- When: 2026-06-19 15:43 CDT
- Request: Fix environment skill validation errors, then pause and validate the existing `dh-agent` tool adapter/evaluator stubs against the shared task schema and queue shape before adding new features.

## Files Changed

- `/Users/adamjohnsson/.agents/skills/higgsfield-product-photoshoot/SKILL.md`
- `/Users/adamjohnsson/.agents/skills/higgsfield-generate/SKILL.md`
- `/Users/adamjohnsson/.agents/skills/hellyeah/SKILL.md`
- `/Users/adamjohnsson/.codex/plugins/cache/openai-curated-remote/heygen/2.2.4/skills/heygen-avatar/SKILL.md`
- `/Users/adamjohnsson/.codex/plugins/cache/openai-curated-remote/heygen/2.2.4/skills/heygen-video/SKILL.md`

Only overlong frontmatter descriptions were shortened. Skill body instructions were left intact.

## Validation

- Full `SKILL.md` description scan passed: no descriptions over 1024 characters.
- `node --check` passed for:
  - `/Users/adamjohnsson/code/dh-agent/src/schema.mjs`
  - `/Users/adamjohnsson/code/dh-agent/src/queue.mjs`
  - `/Users/adamjohnsson/code/dh-agent/src/guardrails.mjs`
  - `/Users/adamjohnsson/code/dh-agent/src/tools/repo.mjs`
  - `/Users/adamjohnsson/code/dh-agent/src/tools/fetch.mjs`
  - `/Users/adamjohnsson/code/dh-agent/src/tools/report.mjs`
- Dry-run task created and saved through the existing queue shape:
  - `/Users/adamjohnsson/code/dh-agent/tasks/t-20260619-2f871cbc.json`
  - local artifact: `/Users/adamjohnsson/code/dh-agent/artifacts/t-20260619-2f871cbc/report.md`
- Dry-run routed through current adapters only:
  - `repo` -> `repoTool`, stub read
  - `api` -> `fetchTool`, stub GET, no real network call
  - `browser` -> `fetchTool`, stub GET, no real browser or network call
  - `report` -> `reportTool`, local artifact write
- Evaluator result: `ok: true`, `violations: []`.

## Mismatches / Gaps

- `package.json` points bin/scripts to `src/cli.mjs`, but `src/cli.mjs` does not exist.
- There is no dedicated router module yet; the dry-run used an inline route map from route names to existing adapters.
- Browser and API are not separate adapters yet; both currently route through `fetchTool`.
- Rate-limit/backoff helper is not implemented yet; `fetchTool` only has TODO comments for this behavior.
- `repoTool` and `fetchTool` are stubs and do not perform real file reads or network calls.
- `evaluate()` checks generic output presence plus optional custom validation, but it does not yet score task quality beyond caller-provided validation.

## Boundary

Local files, local queue dry-run, local log/artifact, and receipt only. No real network fetch, no browser control, no email/send, no public post, no Stripe/customer/money action, no deploy, no Linear/Notion write, and no account change.
