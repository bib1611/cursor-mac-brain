# Codex Receipt - PBM2 funnel live deploy

Time: 2026-06-19 06:24 CDT

Adam asked Codex to make the Plain Bible Manual 2.0 funnel live so people route into it.

Changed and shipped:

- Updated `/Users/adamjohnsson/code/deadhidden/next.config.ts` so `/store/the-vault`, `/vault`, and `/vault-start` redirect to `/store/plain-bible-2.0`.
- Kept redirect status temporary/non-permanent and verified UTM query strings are preserved.
- Shipped the Plain Bible Manual 2.0 landing-page refresh and preview images already prepared under `/store/plain-bible-2.0`.
- Committed and pushed `7006328` (`Launch Plain Bible 2 funnel`) to `origin/main`.
- Deployed production with Vercel.

Production proof:

- Vercel deployment: `https://deadhidden-f8e59t1tn-bib1611s-projects.vercel.app`
- Vercel inspect: `https://vercel.com/bib1611s-projects/deadhidden/AS1MSPS63KvYDcxfNMk7M29rBTUS`
- Production alias: `https://deadhidden.org`
- `https://deadhidden.org/store/plain-bible-2.0` returned `200`.
- `https://deadhidden.org/vault-start?utm_source=substack&utm_medium=email&utm_campaign=vault_followup` returned `307` to `/store/plain-bible-2.0?utm_source=substack&utm_medium=email&utm_campaign=vault_followup`, then `200`.
- `/store/the-vault` and `/vault` also returned `307` to `/store/plain-bible-2.0` while preserving the test UTM query.
- `https://deadhidden.org/images/products/plain-bible-2/system-preview.png` returned `200`.

Verification:

- `npm run lint -- next.config.ts src/app/store/plain-bible-2.0/page.tsx src/app/store/plain-bible-2.0/Pbm2CheckoutForm.tsx` passed.
- `npm run audit:store-routing` passed.
- `npm run build` passed locally.
- Vercel production build passed and aliased to `deadhidden.org`.

Boundary:

No Substack article edit, email send, X/social post, Stripe/customer/money mutation, checkout-session creation, refund, discount, Linear/Notion write, credential change, DNS change, or unrelated local-file cleanup performed.
