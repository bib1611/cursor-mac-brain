# 2026-06-12 09:45 CDT — Claude — How to Count Your Bible: launch audit + Reader proof shipped

## Context
Adam pasted the landing copy + build brief + Stripe sequence for deadhidden.org/store/how-to-count-your-bible. Audit found Codex had already built and deployed the page earlier today from `~/Documents/Codex/2026-06-12/files-mentioned-by-the-user-20260612/work/deadhidden-count-launch/` via `vercel --prod` (uncommitted working tree).

## Verified (live, this session)
- Page live at https://deadhidden.org/store/how-to-count-your-bible — copy matches the brief (hero, empathy, "the line", Genesis 5 table, what's inside, footer line, CTA x2, oxblood #7f1416 / parchment).
- Stripe price `price_1ThVrRLN6IypHVMVUy71Dy9Q`: active, $19.00 USD, one_time, product `prod_UgteTUgtKNP7dy` (DH account).
- Live `POST /api/checkout {productSlug: how-to-count-your-bible}` returned a real `cs_live_...` Stripe session URL.
- Fulfillment PDF in Vercel Blob: `how-to-count-your-bible-8MV9KXbpEl0rBNczRxBOMW6AmNyop0.pdf` (388KB). Serve route resolves via `getBlobUrl(slug)`; Stripe-session-gated, 7-day expiry. Source PDF also at `~/Downloads/how-to-count-your-bible.pdf`.
- OG image https://deadhidden.org/og/how-to-count-your-bible.png → 200, 136KB, 1200x630 meta set.

## Changed (this session)
- Populated `countBibleTestimonials` in `src/app/store/[slug]/page.tsx` in BOTH trees (Codex launch workdir + `~/code/deadhidden`) with the only 2 real comments on the DH post "God Told You to Count" (post id 201446721, public API): Theuderic99 ("…a little less lonely now") and Tiny Notes from the Bible (jigsaw puzzle line). Labeled "Public comment on 'God Told You to Count'". No invented proof. "Jesus Has a Number" had 0 comments.
- Redeployed production: deployment `dpl_CajiWEefHE6gHAnEPjsSURHaHazL` (vercel --prod from launch workdir). Verified "Reader proof" section live.

## Open risks / next moves
1. GIT LANDMINE: production runs from UNCOMMITTED working trees. The product entry, custom page, OG/cover images exist in no git branch. Any push to `main` auto-deploys and TAKES THE PAGE DOWN + breaks buyer downloads. Needed: land the count-launch diff (products.ts entry, [slug]/page.tsx, checkout route, public/og + cover) on `main` via clean worktree/PR without dragging in the dirty Phase 4 branch (60 modified files on `dea-phase4-instrumentation`).
2. No live $19 end-to-end test purchase yet (store skill standard before a traffic push). Code + blob path verified; real purchase not.
3. v2 per brief (don't block): $7 order bump, post-purchase upsell (Strong Delusion $9 / Vault).
4. Brief asked for 3 testimonials; only 2 real comments exist. Slot auto-renders more when added to the array.
