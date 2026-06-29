# Codex - Checkout Card-Testing Controls

Date: 2026-06-22 10:18 CDT

Completed the approved Step 2 security control changes for card-testing abuse.

## Live Changes

Biblical Man Stripe Radar live account `acct_1P9nFWJtGSEkhpBK`:

- Confirmed existing enabled block rule: `:risk_level: = 'highest'`.
- Added enabled block rule: `:total_transactions_per_payment_instrument_fingerprint_hourly: > 2`.
- Added enabled block rule: `:declined_transactions_per_payment_instrument_fingerprint_hourly: > 1`.
- Added enabled block rule: `:cvc_check: = 'fail' or :address_zip_check: = 'fail'`.
- Confirmed global "Request 3DS if supported" rule remains disabled.

Dead Hidden Vercel Firewall:

- Published rule `DH checkout edge rate limit`.
- Rule ID: `rule_dh_checkout_edge_rate_limit_fOTbh6`.
- Paths: `/api/checkout` OR `/api/pbm2-checkout`.
- Limit: 8 requests per 60 seconds, fixed window, keyed by IP, deny on exceed.

## Verification

Vercel:

- `vercel firewall overview` showed Firewall enabled with 1 active custom rule.
- `vercel firewall rules inspect "DH checkout edge rate limit"` showed the exact live settings.
- `vercel firewall diff` showed no pending changes after publish.
- Live probe: 8 invalid `/api/checkout` POSTs reached app validation with 400; the 9th returned Vercel 403.
- After cooldown, invalid `/api/pbm2-checkout` POST reached app validation with expected 400.

Stripe:

- Radar Dashboard readback showed 13 total rules, 11 block rules, and the three new custom rules enabled.
- Fresh seven-day counts after controls went live:
  - Dead Hidden: 106 charges, 7 failed, 99 succeeded, 6.6% failed-charge rate.
  - Biblical Man: 129 charges, 18 failed, 111 succeeded, 14.0% failed-charge rate.

## Still Pending

A real paid end-to-end purchase was not completed because Codex cannot enter a real live payment method. Live Stripe checkouts cannot be completed with test cards. Radar live-block confirmation also needs either the next real bot wave or a user-approved live-card test pattern.

## Boundary

No checkout UX, product/store pages, code files, deploy, Turnstile/hCaptcha, global 3DS, refunds, customer records, payment links, products, prices, credentials, DNS, email, public posts, Linear, or Notion records were changed.

Detailed artifact: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-22-checkout-card-testing-step2.md`
