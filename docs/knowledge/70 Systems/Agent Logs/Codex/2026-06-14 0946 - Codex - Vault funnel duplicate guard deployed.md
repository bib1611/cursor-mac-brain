# Codex - Vault funnel duplicate guard deployed

Date: 2026-06-14 09:46 CDT

## What changed

- Deployed the approved Vault funnel cleanup and duplicate-send guard to production.
- Commit `e12bbf7` (`Fix Vault funnel and email idempotency`) pushed to `origin/main`.
- Follow-up commit `5a7fea0` (`Align Vault resource count`) pushed to `origin/main`.
- Vault public offer copy is aligned to `$365` and 83 resources.
- Removed stale/fake-looking Vault proof and old campaign remnants from the checked funnel copy.
- Added Resend idempotency keys across welcome, lead magnet, purchase delivery, scheduled follow-up, and cron sequence send paths.

## Production deployment

- Vercel deployment: `dpl_8wJ8PLomxNknTz1ww769dfiu3Nyd`
- Deployment URL: `https://deadhidden-ourmxtctl-bib1611s-projects.vercel.app`
- Aliases confirmed:
  - `https://deadhidden.org`
  - `https://www.deadhidden.org`
  - `https://deadhidden.vercel.app`
  - `https://deadhidden-bib1611s-projects.vercel.app`
  - `https://deadhidden-git-main-bib1611s-projects.vercel.app`

## Verification

- `git diff --check`: passed.
- Targeted ESLint: passed with only pre-existing warnings in `src/app/store/category/[category]/page.tsx` for unused `products` and `relSeo`.
- `npm run build`: passed. Existing warn-only slug audit warnings remain in `src/hooks/useCategoryIntent.ts`; existing Next root lockfile warning remains.
- Live smoke tested public domain pages:
  - `https://deadhidden.org/store/the-vault?smoke=5a7fea0`
  - `https://deadhidden.org/?smoke=5a7fea0`
  - `https://deadhidden.org/store/essential-arsenal?smoke=5a7fea0`
- Smoke results showed the live HTML served deployment `dpl_8wJ8PLomxNknTz1ww769dfiu3Nyd`, visible `$365`, and visible `83 resources`.
- The checked live pages did not show the stale scanned terms: `$297`, `$285`, `76+ resources`, `ALL 76`, `4.9/5`, `247 buyers`, `SAVE $68`, `May Wedding`, `May 31`, `Marcus T.`, `David R.`, or `Sarah M.`

## Boundaries

- No email was sent.
- No Resend broadcast or automation schedule was started.
- No Substack or X publish/schedule action was performed.
- No Stripe customer, subscription, refund, price, payment link, or dashboard setting mutation was performed.
- The only irreversible action performed was the approved production deploy through `origin/main` and Vercel.
