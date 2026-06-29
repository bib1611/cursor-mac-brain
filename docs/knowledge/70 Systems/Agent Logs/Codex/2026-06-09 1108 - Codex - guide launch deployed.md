# 2026-06-09 11:08 CDT - Codex - Guide Launch Deployed

Adam approved the guide launch with "lunch these" after the local guide production swarm finished and identified deploy/env gates.

## Action Taken

Codex deployed a clean Vercel production snapshot for the guide launch rather than the full dirty local worktree.

Snapshot source:

- Base: `00c88b3` on repo `/Users/adamjohnsson/code/deadhidden`
- Clean deploy folder: `/tmp/deadhidden-guide-launch-snapshot`
- Included the guide/checkout/download/webhook/email/product files and verified PDF assets.
- Excluded unrelated dirty local admin, assistant, FaithWall beta, Gmail loop, and other pending work.

## Production Deploy

- Production deploy ID: `dpl_DHE7GmjxA715bx27hfwkNTL8TG9q`
- Production URL: `https://deadhidden-dt6eiw0s0-bib1611s-projects.vercel.app`
- Aliased domain: `https://deadhidden.org`
- Vercel inspector: `https://vercel.com/bib1611s-projects/deadhidden/DHE7GmjxA715bx27hfwkNTL8TG9q`
- Ready state: `READY`

## Environment Gates Enabled

Production Vercel env vars added:

- `FAMILIAR_SPIRITS_FOLLOWUP_ENABLED=true`
- `ABANDONED_CART_EMAILS_ENABLED=true`

These gates affect the newly deployed production build.

## Verification

Clean snapshot verification:

- `node scripts/audit-store-routing.mjs` passed.
- `npm run audit:slugs` passed with the known warn-only stale references in `src/hooks/useCategoryIntent.ts`.
- `npm run build` passed locally in `/tmp/deadhidden-guide-launch-snapshot`.
- Vercel remote production build passed.

Live smoke checks:

- `https://deadhidden.org/store/familiar-spirits` returned `HTTP/2 200`.
- Live page HTML contains the launch copy: `Finished field manual`, `Instant PDF`, `55-page`, and `GET THE FIELD MANUAL - $25`.
- `https://deadhidden.org/product-files/familiar-spirits.pdf` returned `HTTP/2 200`, `content-type: application/pdf`, `content-length: 92022`.
- `https://deadhidden.org/product-files/loneliness-lie-part-1.pdf` returned `HTTP/2 200`, `content-type: application/pdf`, `content-length: 290288`.
- `https://deadhidden.org/api/serve/familiar-spirits` returned `HTTP/2 400` without `session_id`, confirming the gated serve route rejects unauthenticated direct calls.
- `https://deadhidden.org/api/checkout` created a live Stripe Checkout Session for `familiar-spirits` through the site checkout pipe in a no-email smoke test.

## Boundary

No manual customer emails, broadcasts, X posts, Substack edits, refunds, checkout payment links, customer account changes, or manual customer sends were performed.

One no-email Stripe Checkout Session was created only as a smoke test for `/api/checkout`.
