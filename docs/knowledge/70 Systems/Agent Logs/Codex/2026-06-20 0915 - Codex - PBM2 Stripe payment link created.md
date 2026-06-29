# 2026-06-20 0915 - Codex - PBM2 Stripe Payment Link Created

Adam asked Codex to recover the PBM2 / CNVS / Dino / Dakota phone-session context and finish the Stripe link setup because the phone lane was hitting permissions.

Recovered context:

- CNVS memory and Agent Bus receipt showed the PBM2 `14-Day Plain Bible Reset` build brief with Dino / Art of Purpose and Dakota / Growth Writing mechanics.
- Local artifact read: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-19-pbm2-cnvs-study-and-prompt.md`.
- The prior scope had explicitly avoided Stripe mutation.

Stripe action performed:

- Created live Stripe Payment Link for Plain Bible Manual 2.0 complete system.
- Payment Link ID: `plink_1TkPgALN6IypHVMVUMyZHKsP`.
- URL: `https://buy.stripe.com/8x2aEYco46MQeoCcZFc3m0m`.
- Account verified: `acct_1PeIdjLN6IypHVMV`.
- Total: `$37.00`.
- Line items:
  - Manual: `price_1TihuvLN6IypHVMV2l8njwlU`, `$19.00`.
  - Worksheets: `price_1TihuwLN6IypHVMVX3K1zcXk`, `$9.00`.
  - Scripture-Safe AI Prompts: `price_1TihuxLN6IypHVMVDQLuDHSX`, `$9.00`.

Metadata attached to the Payment Link:

```text
productSlug=plain-bible-manual-2
slug=plain-bible-manual-2
productName=Plain Bible Manual 2.0
checkoutFlow=pbm2-payment-link
offerLabel=Complete System
lineItemIds=manual,worksheets,prompts
amountCents=3700
fulfillment=pbm2_checkout
sourceComponent=stripe_payment_link
```

Verification:

- Pre-scan found no existing active PBM2 Payment Link using the four live PBM2 price IDs.
- `npx tsx scripts/assert-pbm2-delivery-fallback.ts` passed before and after link creation.
- Public Payment Link load check returned `200 https://buy.stripe.com/8x2aEYco46MQeoCcZFc3m0m`.
- Stripe read-back confirmed active link, total `3700` cents, and the three expected live PBM2 prices.

Caveat:

- `https://deadhidden.org/store/plain-bible-2.0` currently serves the older PBM2 hero copy from production. The repo branch `audit/store-seo-pricing-fixes` has the Dino/Dakota hero as uncommitted local changes, but the tree also contains unrelated dirty work including `package-lock.json` churn and Father's Day checkout work. Codex did not deploy from that dirty branch.

Boundary:

Live Stripe Payment Link creation only. No purchase, charge, refund, subscription change, customer lookup, customer edit, email, Substack/X/Notes publish, repo commit, push, production deploy, credential change, or account-setting change happened.
