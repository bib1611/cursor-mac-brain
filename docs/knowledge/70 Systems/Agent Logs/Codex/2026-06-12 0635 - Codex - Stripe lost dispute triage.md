# 2026-06-12 06:35 CDT - Codex - Stripe lost dispute triage

Adam pasted Stripe's lost-dispute email for dispute `du_1TcEWvJtGSEkhpBKlnzqTRSC` on account `acct_1P9nFWJtGSEkhpBK` and called it highly irritating.

Codex performed read-only Stripe verification using the local key that matched the emailed account. The Stripe connector token was expired, so no connector action was available.

Verified:

- Dispute `du_1TcEWvJtGSEkhpBKlnzqTRSC` is `lost`, reason `subscription_canceled`, amount 60.00 USD.
- Balance impact was 60.00 USD plus 15.00 USD dispute fee, net -75.00 USD.
- Charge `ch_3TWnTPJtGSEkhpBK0hIKSRmg` was the paid yearly subscription renewal charge.
- Invoice `in_1TWmWKJtGSEkhpBKE2jtPH41` was a subscription-cycle invoice for `1 x $60 a year`.
- Subscription `sub_1PDbGfJtGSEkhpBKeRwEIRjV` had existed since 2024, had paid 2024 and 2025 yearly invoices, renewed on 2026-05-13, and was canceled / ended on 2026-05-28 at 20:54:06 CDT.
- Dispute was created on 2026-05-28 at 19:44:05 CDT, roughly 70 minutes before the Stripe subscription cancellation timestamp.

Practical conclusion:

Stripe's records show the cancellation after the renewal charge and after the dispute creation, not before the charge. The issuer still decided for the customer. Per Stripe docs, that issuer decision is final from Stripe's side, but the customer can still withdraw the dispute through the bank.

Artifact:

`/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-12-stripe-dispute-du-1TcEWv/TIMELINE.md`

Boundary:

No refund, cancellation, customer message, subscription change, product change, Stripe object mutation, email, post, deploy, or public action was performed.
