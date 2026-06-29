# Codex - Biblical Man Gumroad clone

Scope: local implementation only. No deploy, no publish, no Gumroad mutation, no Stripe/customer change.

Changed:
- Added `/gumroad` route in `/Users/adamjohnsson/code/deadhidden/src/app/gumroad/page.tsx`.
- The page is a Gumroad-style storefront clone using existing Dead Hidden/Biblical Man product data and owned `/store/<slug>` links.
- Reused existing email signup endpoint through `EmailCaptureForm` with `source="gumroad_clone"`.

Reference:
- User supplied `https://biblicalman.gumroad.com` as the visual/content reference.
- Public search/open checks showed the Biblical Man Gumroad surface and product shelf.

Verification:
- `npm run lint -- src/app/gumroad/page.tsx` passed.
- `npm run build` passed.
- Build output includes static route `/gumroad`.

Boundary:
- Did not replace `/store`.
- Did not wire nav.
- Did not deploy.

## Follow-up verification 2026-06-27

Changed after retry:
- Matched the live Gumroad hero wording more closely: `Make the Bible Great Again.` and the 4 AM garbage-truck bio line.
- Removed `next/font/google` from `src/app/layout.tsx` so local builds do not depend on live Google Fonts access.
- Switched `package.json` build script to `next build --webpack` because Turbopack panicked in this sandbox while trying to bind a local port.
- Cleared generated `.next` cache after a webpack cache crash, then reran the normal build.

Verification:
- `npm run lint -- src/app/gumroad/page.tsx src/app/layout.tsx` passed.
- `npm run build` passed and includes static route `/gumroad`.
- Build still logs expected Substack feed DNS failures in the offline sandbox; those are caught and do not fail the build.

Boundary remains: local code only. No deploy, no Gumroad/Stripe/customer mutation, no public publish.
