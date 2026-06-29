- Separate uncommitted workstream left untouched: how-we-got-our-bible series (sitemap.ts + new dirs).
- Upsell is prefilled-checkout tier (brief fallback option), not off-session one-click — checkout stack stores no PaymentMethod for reuse.

## 2026-06-12 1810 — Hermes/Fable — Brief 3: free-tool email capture (BUILT, NOT DEPLOYED)
- bible-source-code repo commit 2f4f0ff: /api/capture serverless fn (Resend, audience 853ea354, tag free_tool_5_numbers, idempotent dup, 400 junk), capture block replaces Substack CTA in #cta sheet (Substack demoted below), localStorage hides form after capture.
- Lead magnet "5 Numbers Your Reading Plan Skips" written (969/153/430/12+12/888, KJV, Johnson byline, $19 guide CTA), 7pp PDF rendered via headless Chrome, hosted on Vercel Blob: five-numbers-your-reading-plan-skips-xywaX1RuvG36zhrSOUJlmnaYK8phPi.pdf (HTTP 200).
- LIVE TEST: handler sent real email to thebiblicalman1611+freetool-test@gmail.com (200), duplicate idempotent (200), junk 400; contact verified in audience w/ tag then deleted. Audience size 694.
- RESEND_API_KEY added to bible-source-code Vercel project (Production).
- STOPPED before prod deploy per guardrail. Deploy = 'vercel --prod' in ~/code/bible-source-code on Adam's go.
