# Codex Receipt - DH Homepage Mobile CRO PR

Date: 2026-06-16 16:58 CDT

Worktree: `/tmp/deadhidden-homepage-cro`

Branch: `codex/homepage-mobile-cro`

Commit: `ca5bf6d Improve mobile homepage conversion copy`

PR: https://github.com/bib1611/deadhidden/pull/51

Changed file:

- `src/components/cro/HomepageBody.tsx`

What changed:

- Reworked the mobile hero around the concrete $7 four-PDF starter offer.
- Added a mobile-only four-PDF manifest before the buy button.
- Demoted the quiz from a competing bordered button to a secondary text link.
- Replaced front-door male-coded/armed phrasing with household and reader language.
- Changed "One man at a time" to "One household at a time."
- Reframed the free email offer as a preview pack.
- Removed the unverified "LIMITED: 100 THIS WEEK" badge.

Verification:

- `npx tsc --noEmit` passed.
- `npm run lint -- src/components/cro/HomepageBody.tsx` passed.
- `npm run build` passed. Build retained existing warn-only stale slug warnings in `src/hooks/useCategoryIntent.ts`.
- Local smoke `http://localhost:3017/?audit=homepage-cro-local` returned 200.
- Mobile screenshot saved at `/tmp/deadhidden-homepage-cro-mobile.png`.

Boundaries:

- No merge.
- No production deploy.
- No checkout session.
- No Stripe change.
- No buyer email.
- No price change.
