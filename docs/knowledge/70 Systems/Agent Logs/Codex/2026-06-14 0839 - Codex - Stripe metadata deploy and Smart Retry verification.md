# 2026-06-14 0839 - Codex - Stripe metadata deploy and Smart Retry verification

Adam approved both pending Stripe actions: deploy the metadata patch and proceed with Smart Retries work.

Metadata deploy:

- Re-verified repo state had only two changed files: `src/app/checkout/route.ts` and `src/app/api/support/route.ts`.
- Ran `npm run lint -- src/app/checkout/route.ts src/app/api/support/route.ts`: passed.
- Ran `npm run audit:slugs`: passed with existing warn-only stale `src/hooks/useCategoryIntent.ts` references.
- Ran `npm run build`: passed.
- Committed `eba823b` with message `Fix Stripe metadata on legacy checkout`.
- Pushed `main` to `origin`.
- Vercel production deployment became ready: `https://deadhidden-80d0pdefm-bib1611s-projects.vercel.app`, deployment id `dpl_5hgzW994Edk1HAfKfEEHfnhgeGV4`.
- Vercel inspect confirmed aliases `https://deadhidden.org`, `https://www.deadhidden.org`, `https://deadhidden.vercel.app`, and git-main alias.
- Live `/support` returned 200.
- Live `/checkout?slug=the-strong-delusion` returned 303 to Stripe Checkout.
- Live unpaid smoke Checkout Session `cs_live_a1T3oYSAjAegKiV27Mm6UBttBdctbtQXKH3diQzX4Io2WsshttbZkQle7v` carried correct session metadata: productSlug/slug `the-strong-delusion`, product name `THE STRONG DELUSION`, category `spiritual-warfare`, amount `900`, fulfillment `standard`. No charge/customer/email. PaymentIntent was not created yet because the session is unpaid.

Smart Retries:

- Stripe official docs were checked and show Smart Retries configuration lives in Dashboard under Billing > Revenue recovery > Retries; automatic collection docs say Smart Retry policy controls retry count/window.
- Public Stripe API did not expose a normal account-level Smart Retries toggle.
- Read-only invoice API check showed 7 open auto-collection invoices, 3 with `next_payment_attempt` scheduled, total open auto-collection amount remaining `$143`, amount with next payment attempt `$23`, attempt counts up to 9. This suggests retries are already active on at least some invoices.
- Exact dashboard Smart Retries toggle, retry window, and customer failed-payment email settings were not dashboard-confirmed because Codex cannot currently attach to Adam's logged-in Chrome session. Chrome is running, but Codex Chrome Extension is missing/not enabled in selected profile.

MarketingSecrets Brain:

- Saved a note that patch `eba823b` is live and Smart Retries is API-verified but not dashboard-confirmed.

Artifacts:

- `/Users/adamjohnsson/Downloads/reports/stripe-metadata-deploy-and-smart-retries-status.md`

No refunds, subscription changes, price changes, emails, customer mutations, Payment Link edits, or Stripe dashboard setting changes were performed.
