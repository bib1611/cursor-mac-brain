# Codex Receipt - When Evil Comes Launch Deployed

Date: 2026-06-17 18:28 CDT
Agent: Codex
Task: Launch the When Evil Comes To The Door PDF funnel with Stripe checkout, site pages, delivery assets, and Omni prompt.

## Summary

Adam explicitly asked Codex to launch the self-defense PDF sequence, do Stripe and the website, and provide Omni a prompt for the Biblical Man post with CTA buttons.

Codex built from a clean worktree at `/tmp/deadhidden-evil-launch` because `/Users/adamjohnsson/code/deadhidden` was dirty and behind `origin/main`.

## Production Changes

PR:

- `https://github.com/bib1611/deadhidden/pull/59`

Merged commit:

- `d6b4d2f9bb0e62399e0e060f1133bb051053d351`

Live pages:

- `https://deadhidden.org/evil`
- `https://deadhidden.org/evil/waitlist`
- `https://deadhidden.org/store/evil-household-pack`
- `https://deadhidden.org/store/evil-five-question-card`
- `https://deadhidden.org/store/evil-kjv-passage-map`

Live product files:

- `https://deadhidden.org/product-files/evil-five-question-card.pdf`
- `https://deadhidden.org/product-files/evil-kjv-passage-map.pdf`
- `https://deadhidden.org/product-files/evil-five-question-card-sample-v1.pdf`

Omni prompt:

- Repo: `/tmp/deadhidden-evil-launch/ops/OMNI-BIBLICAL-MAN-POST-PROMPT.md`
- Artifact copy: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-17-self-defense-guide/OMNI-BIBLICAL-MAN-POST-PROMPT.md`

## Stripe / Fulfillment

Added catalog products:

- `evil-household-pack` - $12
- `evil-five-question-card` - $7
- `evil-kjv-passage-map` - $7

The launch uses the existing Dead Hidden checkout path:

- `/api/checkout` creates Stripe Checkout Sessions with dynamic product data.
- `/api/webhook` sends the standard purchase email.
- `/success` and `/api/success` return authorized downloads.
- `/api/serve/[slug]` serves the two static PDFs.
- `/api/resend-downloads` can recover the new paid files.

The household pack delivers the two PDFs separately through the existing success page rather than a zip. This avoids adding zip response handling to `/api/serve`.

## Verification

Local checks:

- `npm run lint -- src/app/evil/page.tsx src/app/evil/waitlist/page.tsx src/app/evil/WaitlistForm.tsx src/data/products.ts src/app/api/success/route.ts 'src/app/api/serve/[slug]/route.ts' src/app/api/resend-downloads/route.ts src/lib/email.ts` passed.
- `npm run audit:slugs` passed with existing warn-only stale references.
- `npm run build` passed.
- Local smoke returned 200 for `/evil`, `/evil/waitlist`, all three product pages, and all three static PDF files.
- Local Stripe checkout smoke returned a valid `checkout.stripe.com` URL and `cs_` session id.

GitHub / Vercel:

- Vercel preview checks passed for `deadhidden`, `deadhidden-site-live`, and `thebiblicalmantruth`.
- Production checks passed for `deadhidden`, `deadhidden-site-live`, and `thebiblicalmantruth`.

Live checks:

- Live 200 checks passed for all live pages and static PDF files listed above.
- Live Stripe checkout smoke for `evil-household-pack` returned a valid Checkout URL/session.
- Live Stripe session retrieval confirmed `metadata.productSlug=evil-household-pack`, `amount_total=1200`, and `mode=payment`.

## Boundaries

No Substack post was published.
No Resend broadcast or sequence was sent.
No refunds, customer records, DNS, credentials, or webhook settings were changed.

