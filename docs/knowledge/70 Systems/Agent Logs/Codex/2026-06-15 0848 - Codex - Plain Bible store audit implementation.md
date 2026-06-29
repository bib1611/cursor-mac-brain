# 2026-06-15 08:48 CDT - Codex - Plain Bible Store Audit Implementation

Adam said "do this" against an attached store-audit packet. Codex booted from the local ops capsule, read the current team packet, checked the Dead Hidden commerce skill, verified the live repo/source-of-truth files, and implemented the real high-leverage parts of the audit without trusting stale claims.

## Changed

- `/Users/adamjohnsson/code/deadhidden/src/components/cro/HomepageBody.tsx`
  - Homepage announcement, hero copy, primary CTA, and first-move card now point to The Plain Bible Manual instead of the `$7` sampler.
  - Homepage Plain Bible checkout uses the existing `/api/checkout` flow with `productSlug: the-plain-bible-manual`.
- `/Users/adamjohnsson/code/deadhidden/src/components/Navbar.tsx`
  - Global nav primary CTA now says `BUY $10 MANUAL` and points to The Plain Bible Manual.
  - Mobile drawer close behavior moved from route-change effect to link clicks, cleaning the touched-file lint rule.
- `/Users/adamjohnsson/code/deadhidden/src/data/campaign.ts`
  - Active campaign switched from The Vault to The Plain Bible Manual.
- `/Users/adamjohnsson/code/deadhidden/src/components/StoreContent.tsx`
  - Store campaign hero now features The Plain Bible Manual.
  - Store top `START HERE` card now makes Plain Bible the first buy.
  - Removed hard-coded `NEW` label from the generic active-campaign hero.
- `/Users/adamjohnsson/code/deadhidden/src/app/store/the-plain-bible-manual/page.tsx`
  - Added a `Look inside` preview section.
  - Reframed the Field Files block as `Frequently bought with`.
- `/Users/adamjohnsson/code/deadhidden/src/data/products.ts`
  - Widened Plain Bible catalog copy from men-only language to believers/families/households.
- `/Users/adamjohnsson/code/deadhidden/src/lib/funnel-events.ts`
  - Added `plain_bible` CTA/start-here analytics values.
- `/Users/adamjohnsson/code/deadhidden/docs/funnel-events.md`
  - Documented the new `plain_bible` funnel values.

## Verification

- `npx eslint src/data/campaign.ts src/data/products.ts src/components/Navbar.tsx src/lib/funnel-events.ts src/components/cro/HomepageBody.tsx src/components/StoreContent.tsx src/app/store/the-plain-bible-manual/page.tsx` passed.
- `npm run audit:store-routing` passed: 100 slugs, 92 paid, 8 free, checkout pipe `/api/checkout`.
- `npm run build` passed. Existing prebuild slug audit still reports 15 warn-only stale references in `src/hooks/useCategoryIntent.ts`; audit passed.
- Full `npm run lint` was attempted earlier and failed on pre-existing repo/worktree lint debt, including `.claude/worktrees`, `src/app/about/page.tsx`, `src/app/store/[slug]/success/page.tsx`, `src/components/Navbar.tsx` before this patch, `src/components/ShareButtons.tsx`, `src/components/SmartNudge.tsx`, `src/components/SupportButtons.tsx`, and `src/lib/markdown.ts`.
- Local visual verification used Chrome via Playwright against `http://localhost:3020`.

## Screenshots

- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-15-store-audit-implementation/homepage-desktop-final.png`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-15-store-audit-implementation/store-desktop-final2.png`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-15-store-audit-implementation/plain-bible-mobile-final.png`

## Boundary

No deploy, commit, Stripe/customer/money action, refund, email, X/Substack post, ClickFunnels action, DNS/credential change, or public account mutation was performed.
