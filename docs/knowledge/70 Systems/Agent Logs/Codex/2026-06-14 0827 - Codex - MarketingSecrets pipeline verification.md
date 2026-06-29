# 2026-06-14 0827 - Codex - MarketingSecrets pipeline verification

Adam supplied MarketingSecrets screenshots claiming a Q2 2026 pipeline analysis. Codex treated the bot output as an intelligence lead and verified against live Stripe, Gmail, and local checkout code.

Live Stripe read-only verification:

- Q2 charges since 2026-04-01: 931 succeeded, $21,313.17 gross, $0 refunded in pull, $21,313.17 net after refunds; 87 failed, $2,544.96.
- Jun 10-14 charges: 109 succeeded, $1,147.39; 10 failed, $226.00.
- Jun 10-14 paid Checkout Sessions: 81, $917.99, all with product metadata.
- Live subscriptions returned: 171 active, 15 trialing, 3 past_due, 51 canceled; active MRR $1,406.50; active + trialing + past_due MRR $1,550.50.
- Q2 paid Checkout Sessions missing product metadata: 188, $5,254.67. 172 of those, $4,514.74, came from Stripe Payment Links.
- Biggest missing session line items: Wars and Rumors of Wars, Familiar Spirits, FaithWall founding offers, Support Dead Hidden, Not Enoch preorder.

Gmail verification:

- MarketingSecrets said the Elinor customer thread needed reply.
- Gmail showed the latest message in that thread was a sent reply at 2026-06-14 12:57 UTC, after the customer's 12:36 UTC inbound. No additional reply was sent.

Code changes made in `/Users/adamjohnsson/code/deadhidden`:

- `src/app/checkout/route.ts`: legacy `/checkout?slug=...` now reuses `checkoutMetadata` and attaches it to Checkout Session metadata plus PaymentIntent metadata for one-time payments or Subscription metadata for subscription checkouts.
- `src/app/api/support/route.ts`: support gifts now stamp support/product metadata on the Checkout Session and PaymentIntent.

Verification:

- `npm run lint -- src/app/checkout/route.ts src/app/api/support/route.ts` passed.
- `npm run audit:slugs` passed, with existing warn-only stale references in `src/hooks/useCategoryIntent.ts`.
- `npm run build` passed.

Artifact:

- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-14-marketingsecrets-pipeline-review/MARKETINGSECRETS-PIPELINE-VERIFY-ACTION-PACKET.md`

No Stripe settings changed. No refund, customer mutation, email send, Gmail label mutation, deploy, X/Substack post, or public publish action performed.
