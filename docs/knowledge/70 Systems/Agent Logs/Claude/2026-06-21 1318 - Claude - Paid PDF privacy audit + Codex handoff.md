# 2026-06-21 13:18 CDT - Claude - Paid PDF privacy audit + Codex handoff

## What happened

Adam asked Claude Code to help the live Codex task. The live task (Codex thread
"Review X post" → security fix) was: move 18 paid product PDFs out of public
static paths into `private/` + serve them through a gated
`/api/serve/<slug>?session_id=<id>` endpoint, in repo
`/Users/adamjohnsson/code/deadhidden` branch `audit/store-seo-pricing-fixes`.

Claude ran an INDEPENDENT, READ-ONLY 5-dimension audit (workflow
`deadhidden-paid-pdf-privacy-audit`, 6 agents, ~396K tokens) plus its own live
probes. No files were edited and no build/dev server was started — zero collision
with Codex's live session.

## Findings (verified)

- LIVE LEAK CONFIRMED OPEN: every paid PDF returns HTTP 200 with full bytes at
  guessable URLs on BOTH `deadhidden.org` and `www.deadhidden.org`
  (e.g. `familiar-spirits.pdf` = real 92,022-byte `%PDF-1.7`, `x-vercel-cache: HIT`).
- Codex's code design is correct: server-side Stripe entitlement gate (paid +
  7-day + slug match), no path traversal, all fulfillment paths gated, helper is
  a true single source of truth (18 slugs ↔ 18 files), `outputFileTracingIncludes`
  valid and build-verified.
- BLOCKERS: fix is uncommitted (deletions unstaged, `private/` untracked) so prod
  was never rebuilt; deploying without committing `private/` would 503 every paid
  download; CDN/edge cache + old immutable deployments survive a plain redeploy;
  GitHub repo `bib1611/deadhidden` is PUBLIC with the PDF bytes in 18 commits of
  history.
- Codex already wrote `scripts/assert-private-product-files.ts` +
  `verify-local.sh` (correct regression guard) but they are not wired into
  prebuild.
- 3 PDFs left under `public/` are NOT paid leaks (free sample must stay; one free
  lead magnet orphaned; `kopher-breakdown.pdf` free/unwired — pending Adam
  confirm it was never sold).

## Actions taken

- Read-only audit + live verification only. No source, Stripe, customer, or
  payment mutation.
- Attempted to flip `bib1611/deadhidden` to PRIVATE per Adam's approval.
  BLOCKED: active gh account `biblicalman1611` has push but `admin:false`; the
  repo is owned by separate user `bib1611`. Visibility change requires the owner
  account. Left for Adam: `https://github.com/bib1611/deadhidden/settings` →
  Change visibility → Private, OR `gh auth login` as `bib1611` then
  `gh repo edit bib1611/deadhidden --visibility private --accept-visibility-change-consequences`.
- Created Codex hand-off work order:
  `70 Systems/Agent Bus/inbox/20260621-131815-codex-paid-pdf-privacy-fix.md`
  (priority high) with the ordered ship-steps and the slug curl-verification
  matrix.

## Boundary

Read-only audit/verification, one untracked-repo Agent Bus task file written, one
receipt written, and one ATTEMPTED-then-BLOCKED GitHub visibility change (no
state changed). No deploy, no commit, no Stripe/customer/payment change, no email,
no publish, no Linear/Notion write, no successful account-setting change.
