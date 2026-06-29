# Codex Receipt - The Table Membership Backend PR48

Time: 2026-06-15 21:57 CDT

Repo: `/Users/adamjohnsson/code/deadhidden/.worktrees/table-membership`
Branch: `codex/table-membership-backend`
Commit: `5bcb3689a5e80065991037f9c637c96a7f6413f3`
PR: https://github.com/bib1611/deadhidden/pull/48

What changed:
- Added The Table subscription backend routes, member ledger, Stripe Checkout session creator, webhook handling, dunning queue, gated member email/tag stubs, and billing portal handoff.
- Added active Table-member access path for `/api/serve/[slug]` using `member_email` plus `member_id`.
- Added founding-seat reservation enforcement for the 500-seat founding cap and expired Checkout reservation release.
- Added regression script: `npx tsx scripts/assert-the-table-membership.ts`.
- Added Stripe creation helper: `scripts/create-the-table-stripe-prices.mjs`.

Boundaries kept:
- No merge.
- No launch CTA or homepage/store promotion.
- No buyer/member emails sent.
- No test charge fired.
- No Stripe payment links or subscriptions created.

Gates:
- `npm ci --dry-run` passed.
- `npx tsx scripts/assert-the-table-membership.ts` passed.
- `npx tsc --noEmit` passed.
- `npx eslint` on touched files passed.
- `npm run build` passed.
- Vercel preview checks for PR #48 passed.

Known blocker:
- Live Stripe Table prices were not created. Stripe search worked and verified the connector sees Dead Hidden PBM2 products, but mutation helpers failed before reaching Stripe with `Unknown tool: create_product`. The local repo Stripe key was also not usable for live creation. The PR expects `THE_TABLE_MONTHLY`, `THE_TABLE_ANNUAL`, and `THE_TABLE_FOUNDING` to be set before launch.
