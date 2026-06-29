# Codex - BM paid conversion timeline

Time: 2026-06-22 12:45 CDT

Built the Biblical Man paid-conversion timing series from the live BM Stripe account `acct_1P9nFWJtGSEkhpBK`.

Outputs:

- Daily CSV: `/Users/adamjohnsson/Library/CloudStorage/GoogleDrive-thebiblicalman1611@gmail.com/My Drive/Biblical Man Analytics/bm_paid_daily.csv`
- Event audit CSV: `/Users/adamjohnsson/Library/CloudStorage/GoogleDrive-thebiblicalman1611@gmail.com/My Drive/Biblical Man Analytics/bm_paid_events.csv`
- Ops artifact: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-22-bm-paid-conversion-timeline.md`

Result:

- Pulled 10,945 paid/succeeded Stripe charges.
- Daily output covers 2024-05-02 through 2026-06-22 in America/Chicago.
- Gross successful-charge revenue from Stripe USD balance transactions: $274,812.78.
- Verified CSV row counts: 777 lines in daily CSV, 10,946 lines in event audit CSV.

Honesty note:

New-vs-renewal could not be cleanly separated across the full history. Stripe returned subscription-looking Substack charges, but 153 of those payments lacked a customer id, so first-time payer status cannot be proven for the whole series. Per Adam's instruction, `bm_paid_daily.csv` falls back to total successful payments per day. The requested split columns are present but blank.

Boundary:

Read-only Stripe pull and local/Google Drive file writes only. No Stripe customer, subscription, checkout, refund, payment link, product, price, Radar, payout, email, public post, deploy, DNS/security, Linear, or Notion mutation happened.
