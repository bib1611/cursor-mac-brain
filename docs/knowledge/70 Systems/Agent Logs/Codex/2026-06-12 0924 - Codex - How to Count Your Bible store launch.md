# Codex Receipt — How to Count Your Bible store launch

Time: 2026-06-12 09:24 CDT

## Outcome

Shipped the `How to Count Your Bible` sales page live at:

`https://deadhidden.org/store/how-to-count-your-bible`

The deployed page uses the existing Dead Hidden store route, product registry, `/api/checkout`, `/success`, `/api/success`, `/api/serve/[slug]`, Stripe webhook, and Blob-backed PDF fulfillment path.

## Live objects

- Vercel deployment: `dpl_EHHYAKF9UmYarCyCNDixhNxa9LWi`
- Production URL: `https://deadhidden-aiz2n2n4d-bib1611s-projects.vercel.app`
- Aliases verified on deployment: `https://deadhidden.org`, `https://www.deadhidden.org`
- Stripe product: `prod_UgteTUgtKNP7dy`
- Stripe one-time price: `price_1ThVrRLN6IypHVMVUy71Dy9Q`
- Amount: `1900` cents USD
- Vercel Blob PDF pathname: `how-to-count-your-bible-8MV9KXbpEl0rBNczRxBOMW6AmNyop0.pdf`

## Files changed in clean deploy copy

Clean deploy worktree:

`/Users/adamjohnsson/Documents/Codex/2026-06-12/files-mentioned-by-the-user-20260612/work/deadhidden-count-launch`

Changed:

- `src/data/products.ts`
- `src/app/api/checkout/route.ts`
- `src/app/store/[slug]/page.tsx`
- `public/product-covers/how-to-count-your-bible.png`
- `public/og/how-to-count-your-bible.png`

Note: the main repo worktree had many unrelated uncommitted changes, including some in overlapping files. To avoid shipping unrelated work, Codex deployed from a clean detached worktree based on commit `00c88b3cfb3139f49242fb4970ea3343cde498db` with only the guide-launch changes applied.

## Verification

- `npm run audit:store-routing` passed in the clean deploy copy.
- `npx tsc --noEmit` passed in the clean deploy copy.
- `npm run build` passed in the clean deploy copy. Existing warn-only stale slug warnings remained in `src/hooks/useCategoryIntent.ts`.
- Live route returned HTTP 200 for `https://deadhidden.org/store/how-to-count-your-bible`.
- Live HTML contained:
  - title `How to Count Your Bible | Dead Hidden`
  - `og:title` = `How to Count Your Bible`
  - OG image `/og/how-to-count-your-bible.png`
  - CTA `Send Me the Guide — $19`
  - Genesis 5 table content including `Methuselah` / `His death shall bring`
- Live checkout POST to `https://deadhidden.org/api/checkout` returned a `checkout.stripe.com` session.
- Live session line item verified:
  - price ID `price_1ThVrRLN6IypHVMVUy71Dy9Q`
  - subtotal `1900`
  - currency `usd`
- Live unauthenticated file endpoint `https://deadhidden.org/api/serve/how-to-count-your-bible` returned `400 Missing session_id`.
- Blob lookup found the uploaded PDF by slug prefix.
- Live mobile visual QA: no horizontal overflow; first CTA visible inside the first viewport.

## Boundary

No purchase was completed. No test charge was made. The created checkout sessions were unpaid smoke sessions only.

The pasted Anthropic key from the task was not written to this receipt.
