# 2026-06-16 09:54 CDT - Codex - Architecture of Heaven CTA landing-page fix

## Action

Edited the published Dead Hidden Substack post `The Architecture of Heaven` through authenticated Comet CDP on `127.0.0.1:9223`.

Changed only the two native button link targets:

- `Get NORTH: The Empty Place — $14`
  - before: `https://deadhidden.org/checkout?slug=north-the-empty-place&utm_source=deadhidden_substack&utm_medium=post&utm_campaign=architecture_of_heaven&utm_content=primary_cta`
  - after: `https://deadhidden.org/store/north-the-empty-place?utm_source=deadhidden_substack&utm_medium=post&utm_campaign=architecture_of_heaven&utm_content=primary_cta`
- `Get the NORTH + Strong Delusion bundle — $19`
  - before: `https://deadhidden.org/checkout?slug=north-strong-delusion-bundle&utm_source=deadhidden_substack&utm_medium=post&utm_campaign=architecture_of_heaven&utm_content=bundle_cta`
  - after: `https://deadhidden.org/store/north-strong-delusion-bundle?utm_source=deadhidden_substack&utm_medium=post&utm_campaign=architecture_of_heaven&utm_content=bundle_cta`

## Method

- Opened editor: `https://deadhidden.substack.com/publish/post/202289154`
- Verified exactly two `button` nodes in both `body` and `draft_body`.
- Saved via `PUT /api/v1/drafts/202289154` with updated `draft_body`.
- Updated the published post via `POST /api/v1/drafts/202289154/publish` with `{ "send": false }`.

## Verification

- Authenticated live reader page found both buttons with the new `/store/...` hrefs.
- Screenshot: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-16-architecture-cta-fix/architecture-of-heaven-store-ctas.png`
- Landing page checks:
  - `/store/north-the-empty-place?...primary_cta` returned HTTP 200 with `x-matched-path: /store/north-the-empty-place`.
  - `/store/north-strong-delusion-bundle?...bundle_cta` returned HTTP 200 with `x-matched-path: /store/north-strong-delusion-bundle`.
- Checkout checks:
  - `/checkout?slug=north-the-empty-place...` returned HTTP 303 to `checkout.stripe.com`.
  - `/checkout?slug=north-strong-delusion-bundle...` returned HTTP 303 to `checkout.stripe.com`.
- Landing-page button click checks in Comet:
  - `GET NORTH — $14` on the NORTH landing page reached `checkout.stripe.com` with title `Stripe Checkout`.
  - `GET THE BUNDLE — $19` on the bundle landing page reached `checkout.stripe.com` with title `Stripe Checkout`.

## Safety

No price changes. No test charge. No buyer email. No unpublish. No resend or subscriber re-notify.

Substack `email_sent_at` remained `2026-06-16T14:16:15.716Z` before and after the update. Publish/update response used `send:false`.
