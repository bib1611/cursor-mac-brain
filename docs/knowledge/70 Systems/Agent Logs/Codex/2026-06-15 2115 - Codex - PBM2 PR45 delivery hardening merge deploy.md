# PBM2 PR45 Delivery Hardening Merge Deploy

Date: 2026-06-15 21:15 CDT
Operator: Codex
Repo: `/Users/adamjohnsson/code/deadhidden`

## Adam Instruction

Merge and deploy PR #45 `polly/pbm2-delivery-harden`. Do not touch Stripe keys, send buyer emails, or fire a test charge.

## Readiness Gate

- PR #45 was open, not draft, and mergeable.
- Branch HEAD: `1e4758fafd3c594f60ed5c887ac98c18383c6b2d`
- Cache fix present in `src/lib/pbm2-delivery.ts`:
  - `cachedPbm2LineItemIdsBySessionId = new Map<string, Set<Pbm2LineItemId>>()`
  - cache set/get uses `session.id`
  - no `WeakMap` cache keyed by the session object
- Regression script includes:
  - `$28` manual + worksheets case, asserting manual + workbook only
  - `$9` worksheets-only case, asserting workbook only

Commands passed:

- `npx tsx scripts/assert-pbm2-delivery-fallback.ts`
- `npx tsc --noEmit`
- `npm run lint -- scripts/assert-pbm2-delivery-fallback.ts src/lib/checkout-product-identity.ts src/lib/pbm2-delivery.ts src/lib/pbm2-products.ts`
- `npm run build`

Build note: `audit-slugs` emitted existing warn-only stale-reference warnings, then passed; Next build passed.

## Merge And Deploy

- PR #45 merged.
- Merge commit: `e8d6327ef7563e7120cd1e8af79bfbdc975c60d8`
- GitHub: `https://github.com/bib1611/deadhidden/pull/45`
- Vercel statuses for the merge commit: success.
- Production alias: `https://deadhidden.org`
- Current production deployment resolved by Vercel CLI:
  - id: `dpl_3LJmtc2jyoRv7ujsKF7DNMBW647V`
  - url: `https://deadhidden-qgr4biuv9-bib1611s-projects.vercel.app`
  - status: Ready

## Read-Only Smoke

- `GET https://deadhidden.org/store/plain-bible-2.0` returned 200.
- Cold page still renders:
  - two checked order bumps
  - `$37` running total
  - `Get the Complete System - $37`
  - `Already own the manual?` bar
- `GET https://deadhidden.org/store/plain-bible-2.0?upgrade=1` returned 200.
- Upgrade path still renders:
  - zero checked order bumps
  - `$15` add-on bundle copy

Vercel runtime log check:

- `vercel logs https://deadhidden.org --since 10m --level error`
- Result: no error logs found.

## Boundaries Kept

- No Stripe keys touched.
- No buyer emails sent.
- No test charges or purchases fired.
- Existing dirty local checkout state was not changed.

