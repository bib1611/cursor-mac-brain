# 2026-06-10 16:21 — Hermes — Count the Number download fix + afternoon dispatch

## Download 500 — root cause and fix (CUSTOMER-FACING, RESOLVED)

- Buyers reported failed downloads of Count the Number (screenshots AirDropped to ~/Downloads: IMG_3123-3125). Lila Hammett (lilahammett@gmail.com, 2:38 PM support email) and Steve Burkholder (steveohg@gmail.com, 2:26 PM) both hit it.
- Root cause: morning hotfix 91fff8d shipped the PDF as a static file (`public/product-files/count-the-number.pdf`) but the serve route's `STATIC_PRODUCT_FILES` map in `src/app/api/serve/[slug]/route.ts` was never updated. Every download fell through to a Vercel Blob lookup that doesn't exist → 500 ("Download failed...") for ALL buyers since launch.
- Fix: commit `843d80f` "Register count-the-number in serve route static file map" pushed to origin/main from a clean worktree (dev branch untouched). Vercel deployed (deadhidden-dfmlzc16u, Ready).
- Verified live with a REAL paid session (calmanza1, 3:46 PM): `/api/serve/count-the-number?session_id=cs_live_a1nun...` → HTTP 200, 19,873 bytes, valid %PDF-1.4, 9 pages. Buyers' original DOWNLOAD NOW email buttons work again (session links valid 7 days).

## Affected buyers (Stripe, today, paid count-the-number — 9 purchases, $90)

paintdry4u@aol.com (12:34 AND 13:15 — DOUBLE PURCHASE, likely retried after failure; refund decision pending Adam), jhotchkin@sbcglobal.net (12:11), lilahammett@gmail.com (13:19), steveohg@gmail.com (13:37), lbdk@earthlink.net (13:45), dknighton0627@att.net (13:52), bagayasa001@gmail.com (13:59, Adrian — also the morning 404 reporter), mzura1@gmail.com (14:50), calmanza1@gmail.com (15:46).

- Reply emails to Lila + Steve drafted, NOT sent — awaiting Adam approval (hard line: no outbound email without explicit same-thread approval).

## Dispatched (in flight)

- ProtonMail triage watcher: Hermes cron d6bb3506, every 20 min (4,24,44), read-only triage → PROTON_TRIAGE.md + push alerts for customer issues, newsletter swipe file in Agent Bus. NOTE: session-bound, auto-expires in 7 days — needs a permanent launchd version if Adam wants it standing.
- SEO twins agent: building free question-framed twin articles for past-week DH posts in repo worktree, branch `seo-twins-2026-06-10`, PR-style review before merge (no direct main push).
- Footer/bio agent: appending deadhidden.org/store link to DH email footer (Comet), BM email footer (Chrome), and @Biblicalman X bio (xurl, only if it fits 160 chars).

— Hermes
