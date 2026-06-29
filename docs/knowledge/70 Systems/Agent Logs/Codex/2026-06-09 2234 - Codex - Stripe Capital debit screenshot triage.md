# 2026-06-09 2234 CDT - Codex - Stripe Capital Debit Screenshot Triage

Adam shared a Proton mobile screenshot of an email from `Stripe Capital <capital@stripe.com>` with subject preview `$1,066.95 debit initiated for your...`.

Screenshot details visible:

- Recipient: `biblicalman@proton.me`
- Claimed product: Stripe Capital
- Claimed business/merchant label: `The Adam Johnson substack`
- Claimed linked bank: BRAVERA BANK ending in `1332`
- Claimed debit: `$1,066.95`
- Claimed payment period: April 11, 2026 through June 10, 2026
- Claimed purpose: minimum payment requirement for loan obligations
- Footer text visible: on behalf of Celtic Bank / Stripe Servicing, Inc.

Read-only checks performed:

- Checked official Stripe Capital docs and support pages. Stripe documents that if sales withholdings do not meet the required minimum for a loan payment period, Stripe automatically debits the shortfall from the linked bank account or account balance.
- Used the Stripe connector in read-only mode to confirm the connected Stripe app can see an Adam Johnson Stripe account and balance data. The connector did not expose Stripe Capital loan/payment details, so it did not confirm or deny this specific debit.

Recommendation given:

- Treat the email as plausible but unverified from screenshot alone.
- Do not click the email button.
- Open Stripe directly and check `https://dashboard.stripe.com/capital` or Dashboard > Capital for the active loan, payment period, bank ending `1332`, and `$1,066.95` debit.
- If the Capital dashboard does not show the same debit, contact Stripe from the dashboard or the documented Capital support address.

Boundary:

- No email links clicked.
- No Stripe payment, refund, checkout, payout, customer, subscription, Capital, bank, or account setting changes were made.
- No external messages sent.
