# Field Files Bundle + Post-Purchase Upsell — Production Deploy

**Date:** 2026-06-12 18:25 CDT
**Agent:** Hermes
**Trigger:** Adam: "GO on field-files"

## What shipped
- Fast-forward push `f54c4fa..af4b906` (branch `field-files-upsell`) to origin/main on bib1611/deadhidden
- Commit: "Add Field Files bundle ($39, 4 PDFs) + post-purchase upsell on count-guide success page"
- Vercel auto-deploy; live ~45 seconds after push

## Pre-push safety
- origin/main was at f54c4fa (this morning's count-launch fast-forward) — field-files-upsell was exactly origin/main + 1 commit, so the push was a pure fast-forward. No merge commit, no conflicts.
- Local `main` ref was stale at 1697be9 (an older ancestor already contained via merge 810439f) — moved to af4b906 to match.
- Untracked how-we-got-our-bible WIP (3 paths + sitemap.ts mod) deliberately excluded, still in working tree.

## Live verification (all this session, on production)
1. `/store/the-field-files` → 200, "Get The Field Files — $39" x2, "$52 apart, $39 together"
2. OG image `/product-covers/the-field-files.png` → 200, 153KB; og:image meta correct
3. Live checkout POST → cs_live session; retrieved from Stripe: **amount_total 3900, productSlug=the-field-files, productCategory=bundles**
4. Bundle cross-sell CTA on all 4 component store pages: how-to-count-your-bible, the-strong-delusion, the-plain-bible-manual, **the-torment-triage** (correct slug has "the-"; /store/torment-triage 404 is the wrong slug, not a bug)
5. Fulfillment: serve route `fieldFilesSlugs` set matches catalog slugs exactly + grants the-strong-delusion-print to bundle buyers
6. Regression: how-to-count-your-bible checkout still returns cs_live OK

## Not yet money-tested
- Upsell block render on the count-guide success page (requires a real paid session_id)
- Bundle delivering all 4 PDFs to a real buyer
- First real purchase is the live test — same pattern that held 11x for the count guide today.
