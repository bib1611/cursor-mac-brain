# Count the Number — Download Break, Root Cause, Buyer Rescue

Date: 2026-06-10 ~20:45 CDT
Agent: Hermes (iMessage session)
Trigger: Adam forwarded ProtonMail screenshots (IMG_3123–3125, Downloads) — buyers Steve Burkholder (steveohg@gmail.com) and lilahammett@gmail.com reporting failed downloads. Adam also saved the raw error body at ~/Downloads/count-the-number.txt: "File not available yet. Contact thebiblicalman1611@gmail.com for help."

## Root cause
- 12:05 hotfix (91fff8d) added the count-the-number product page + PDF but did NOT register the slug in `STATIC_PRODUCT_FILES` in `src/app/api/serve/[slug]/route.ts`. Blob lookup also missed (PDF lives in /public, not Vercel Blob) → serve route returned 503 "File not available yet."
- Broken window: 12:05–~16:10. Email DOWNLOAD NOW (→ /success) and success-page DOWNLOAD PDF (→ /api/serve) both dead end at the same 503.
- 16:10 — commit 843d80f ("Register count-the-number in serve route static file map") fixed it. Adam's 16:17 error was deploy propagation.

## Verification (this session, live production)
- `/product-files/count-the-number.pdf` → 200
- `/api/serve/count-the-number?session_id=<Steve's real paid session>` → 200, valid 9-page PDF, identical to repo file, correct branding ("Dead Hidden", byline "Adam Johnson")
- `/api/download?session_id=<same>` → correct JSON with serve URL
- Both delivery paths confirmed working end to end.

## Affected buyers (Stripe live, paid, 06-10)
9 paid sessions, 8 unique buyers in/near broken window (paintdry4u@aol.com handled earlier today — double charge, sent Plain Bible Manual free):
jhotchkin@sbcglobal.net (12:11), lilahammett@gmail.com (13:19), steveohg@gmail.com (13:37), lbdk@earthlink.net (13:45), dknighton0627@att.net (13:52), bagayasa001@gmail.com (13:59, Adrian Bagayas — hit BOTH bugs today), mzura1@gmail.com (14:50), calmanza1@gmail.com (15:46).

## Rescue
Sent each buyer the PDF attached via Resend from "Adam at Dead Hidden <adam@deadhidden.org>", reply-to thebiblicalman1611@gmail.com, subject "Your Count the Number download is fixed". All 8 accepted:
4c6efa06, d3a2fcdc, 86259b72, 37ec1e5f, ea3a7b51, e4c8f621, d13882a8, 5126a42c

## Lessons
1. Hermes's 12:05 hotfix shipped the page + PDF but missed serve-route registration. New-product checklist on this codebase = product entry + PDF in /public/product-files + STATIC_PRODUCT_FILES entry in serve route + live download test WITH A REAL PAID SESSION, not just page/PDF 200s.
2. Local repo .env.local Resend key is stale → pull prod env via `npx vercel env pull`. EMAIL_FROM in prod env is empty string; code falls back to 'Adam at Dead Hidden <adam@deadhidden.org>' — scripts must replicate that fallback.
3. Resend API behind Cloudflare blocks python-urllib UA (error 1010); send with a curl UA.
