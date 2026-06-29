# 2026-06-22 0959 CDT - Codex - Checkout card-testing diagnosis

Adam asked for Step 1 diagnosis only before any blocking rule goes live.

Read-only actions:

- Read the Dead Hidden ops capsule and refreshed team context.
- Reviewed `/Users/adamjohnsson/code/deadhidden` checkout implementation.
- Verified live Vercel headers and DNS for `deadhidden.org` / `www.deadhidden.org`.
- Queried Vercel runtime logs read-only for checkout errors, `429`, and `400` records over seven days.
- Queried Stripe read-only using local keys loaded through `/Users/adamjohnsson/.agents/bin/dh-with-env`.
- Pulled seven days of Charges, PaymentIntents, Checkout Sessions, Events, and Payment Link metadata for Dead Hidden and Biblical Man.
- Checked official Stripe Radar and Vercel Firewall docs for current rule/control handles.

Diagnosis artifact:

`/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-22-checkout-card-testing-diagnosis.md`

Main findings:

- Dead Hidden store checkout is server-created Stripe Checkout Sessions through `POST https://www.deadhidden.org/api/checkout`; PBM2 uses `POST https://www.deadhidden.org/api/pbm2-checkout`.
- The live site is Vercel / Next.js, not Cloudflare-proxied.
- Dead Hidden had `106` charges in the seven-day window, `7` failed, `99` succeeded, `6.6%` decline rate, and `249` Checkout Sessions. It has bot-like unpaid session churn, but not a large current failed-charge storm.
- Biblical Man had `129` charges, `18` failed, `111` succeeded, `14.0%` decline rate, `188` PaymentIntents with `75` failed/canceled, and `100` Checkout Sessions, all Payment Links and unpaid/open/expired.
- The strongest card-testing signature is on Biblical Man direct Payment Links, especially variable-amount links:
  - `https://donate.stripe.com/dRmfZie3u1uh4E0fwicMM1a` - `57` sessions, `54` expired/unpaid.
  - `https://buy.stripe.com/3cIdRa2kM8WJgmIabYcMM1T` - `20` sessions, `16` expired/unpaid and `4` open/unpaid.
- Stripe API did not expose client IPs in the read objects; Vercel runtime logs did not provide access-log IP data for checkout routes.

Boundary:

No Stripe Radar rule, Payment Link setting, Vercel Firewall rule, code patch, deploy, checkout UX/page change, refund, customer/money mutation, DNS/security/account-setting change, email, public post, Linear/Notion write, or credential print happened.
