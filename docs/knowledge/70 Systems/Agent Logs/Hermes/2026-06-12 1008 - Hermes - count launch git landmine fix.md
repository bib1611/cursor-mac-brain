# 2026-06-12 10:08 CDT — Hermes — Count launch git landmine fix

## Problem
Production (How to Count Your Bible launch) was deployed from an uncommitted worktree. `origin/main` had diverged the other way (Adam-to-Noah chart + 666 CTA fix + SEO twins). Any push to main would have auto-deployed a tree WITHOUT the count product. Worse: the count-launch deploy had already knocked `/store/the-adam-to-noah-chart` offline (404 verified 09:5x CDT).

## Actions
1. **Insurance branch** — committed exact live-prod source from worktree `~/Documents/Codex/2026-06-12/.../deadhidden-count-launch` and pushed `origin/count-launch-live` (commit on top of 00c88b3).
2. **Resolved stalled merge** in `~/code/deadhidden` (snapshot e3eb4ef × origin/main 1914ab9, 27 conflicts) taking the snapshot side. Verified merged tree contains: count product (products.ts), chart product, 666 CTA fix (no `:::cta` literal), Theuderic testimonial.
3. **Removed dead code** `src/components/cro/DeadHiddenArchiveScene.tsx` (imported nowhere, @react-three/fiber never installed, blocked build).
4. **Build passed** locally. Pushed `dea-phase4-instrumentation` and fast-forwarded `main` 1914ab9 → **f54c4fa**.
5. Push auto-triggered Vercel production deploy `deadhidden-h9lropqj5` — status Ready.

## Verified live (this session)
- /store/how-to-count-your-bible → 200, testimonials present
- /store/the-adam-to-noah-chart → 200 (RESTORED, was 404)
- POST /api/checkout productSlug=how-to-count-your-bible → live cs_live session
- POST /api/checkout productSlug=the-adam-to-noah-chart → live cs_live session

## Traffic posts
- X post 2065442257562485078 live, 254 impressions @ ~10:00, store link confirmed in long-post body (entities: deadhidden.org/store/how-to-count-your-bible)
- Substack "The Chapter Hides a Countdown" is **SCHEDULED for 11:44am CDT today, not live**. Body/CTA link unverifiable pre-publish from Chrome (DH authorship is in Comet). Adam should confirm the post body links to the store page before 11:44.

## Outstanding
- No real $19 test purchase has confirmed email→download end to end.
- Prod now deploys from git/main — stop deploying from loose worktrees.
