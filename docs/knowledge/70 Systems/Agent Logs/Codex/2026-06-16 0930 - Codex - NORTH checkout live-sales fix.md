# 2026-06-16 09:30 CDT - Codex - NORTH checkout live-sales fix

## Scope

Urgent live-sales fix for Dead Hidden Substack post:

`https://deadhidden.substack.com/p/the-architecture-of-heaven`

## Diagnosis

Root cause: the published Substack buttons were already pointing at the correct checkout URLs, but the NORTH store commit was not deployed to production, so `/checkout?slug=north-*` fell back to `/store`.

Before deploy:

- Production deployment: `dpl_CVUv8rA1kQucnaqUBRFm9oThQMYE`, created 2026-06-15 21:38 CDT.
- `https://deadhidden.org/checkout?slug=north-the-empty-place` returned 307 to `https://deadhidden.org/store`.
- `https://deadhidden.org/checkout?slug=north-strong-delusion-bundle` returned 307 to `https://deadhidden.org/store`.
- Live post DOM via Chrome CDP confirmed buttons:
  - `Get NORTH: The Empty Place — $14` -> `https://deadhidden.org/checkout?slug=north-the-empty-place&utm_source=deadhidden_substack&utm_medium=post&utm_campaign=architecture_of_heaven&utm_content=primary_cta`
  - `Get the NORTH + Strong Delusion bundle — $19` -> `https://deadhidden.org/checkout?slug=north-strong-delusion-bundle&utm_source=deadhidden_substack&utm_medium=post&utm_campaign=architecture_of_heaven&utm_content=bundle_cta`

## Change

Pushed the clean NORTH commit from branch `codex/north-empty-place-stage` to `origin/main`:

`ab209f52afea9cc7fd08c2be4b20d839895e8b28` - `Stage NORTH field file checkout`

Diff verified as only:

- `public/product-files/north-the-empty-place.pdf`
- `src/data/products.ts`
- `src/app/api/download/route.ts`
- `src/app/api/resend-downloads/route.ts`
- `src/app/api/serve/[slug]/route.ts`
- `src/app/api/success/route.ts`

Local build passed before push: `npm run build`.

Production deployment after push:

- `dpl_5GhXNrtQRgF63rMNcrgrvMGP6pnL`
- `https://deadhidden.org`
- Vercel status: Ready

## Verification

After deploy:

- Exact live-post $14 URL returns 303 to Stripe Checkout.
- Exact live-post $19 URL returns 303 to Stripe Checkout.
- Read-only Stripe session lookup confirmed:
  - `north-the-empty-place`: open/unpaid checkout, `amount_total=1400`, product `NORTH: THE EMPTY PLACE`.
  - `north-strong-delusion-bundle`: open/unpaid checkout, `amount_total=1900`, product `NORTH + THE STRONG DELUSION`.
- Existing checkout smoke checks still reach Stripe:
  - `the-strong-delusion`: `amount_total=900`.
  - `the-plain-bible-manual`: `amount_total=1000`.
  - `the-vault`: `amount_total=36500`.
- Unpaid `/api/success` checks for NORTH sessions return `403 Payment not completed`.
- Delivery mapping verified in deployed code:
  - standalone NORTH maps to `north-the-empty-place`.
  - NORTH bundle maps to `north-the-empty-place` + `the-strong-delusion`.
- Live PDF assets respond:
  - `/product-files/north-the-empty-place.pdf`: 200 PDF, 57,887 bytes.
  - `/product-files/the-strong-delusion.pdf`: 200 PDF, 136,018 bytes.

## Boundaries

No price changes. No test charge. No buyer email. No Stripe customer/payment mutation beyond opening unpaid checkout sessions for verification.
