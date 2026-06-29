---
generated: 2026-06-29T16:00:03
source: ~/code/vault-query/dashboard.py
tags: [dashboard, daily, auto]
---

# Daily Numbers — Monday, June 29, 2026

_Auto-generated. Edit `dashboard.py` to change layout._

## TODAY — 2026-06-27

| Source | Today | Δ vs yesterday |
|---|---|---|
| Stripe DH (24h) | $5.00 | (▼ -10) |
| Stripe BM (24h) | $0.00 | (—) |
| Stripe total (24h) | $5.00 | (▼ -10) |
| Stripe DH (30d rolling) | $4,693.80 | (▲ +1) |
| Stripe BM (30d rolling) | $7,461.72 | (▲ +56) |
| Substack ARR | $78,497.00 | (—) |
| Substack paid subs | 1,237 | (—) |

**Substack subs (cowork)**: total=25,790, paid=1,235, new_paid_today=0  (▲ +10)

> X scrape returning suspiciously low followers — recheck CDP session.

## THIS WEEK — last 7 days (TRUE daily sum)

- Stripe BM 7d: **$611.00**
- Stripe DH 7d: **$273.00**
- Stripe total 7d: **$884.00**
- Paid subs net Δ 7d: **-2**
- Days with daily data: **6/7**  (rest are pre-fix rows)
- For reference, Stripe rolling-30d (latest scrape): **$12,155.52**

## THIS MONTH — June 2026 (27 calendar days, 27 with real data)

- Stripe BM MTD: **$6,046.23**
- Stripe DH MTD: **$3,814.20**
- Stripe combined MTD: **$9,860.43**
- Run-rate (annualized): **$133,298.41** (extrapolating from 27 real-data days)
- Stripe rolling-30d (latest scrape, NOT summed): **$12,155.52**

## STRIPE BY ACCOUNT — latest scrape

| Account | Gross 30d | MRR | Disputes | Balance |
|---|---|---|---|---|
| Dead Hidden / deadhidden.org | $4,693.80 | $549.98 | 0 | $-0.82 |
| The Biblical Man | $7,461.72 | $825.66 | 2 | $-0.17 |

## TOP CONTENT — last 30 days by score

| Date | Platform | Title | Score | X imp | SS opens | SS clicks |
|---|---|---|---|---|---|---|
| 2026-04-28 | substack | If You Don't Hear From Me Again | 780.0 | 0 | 0 | 0 |
| 2026-05-08 | substack | The Bible Disclosed First | 688.0 | 0 | 0 | 0 |
| 2026-05-03 | substack | 18 Brutal Truths From Genesis About Depression, Porn, Marria | 680.0 | 0 | 0 | 0 |
| 2026-04-25 | substack | When God Shut the Door | 644.0 | 0 | 0 | 0 |
| 2026-04-23 | substack | Addressing Plagiarism | 632.0 | 0 | 0 | 0 |
| 2026-04-13 | substack | The Rulers You Can't Google | 624.0 | 0 | 0 | 0 |
| 2026-04-19 | substack | He died  | 620.0 | 0 | 0 | 0 |
| 2026-04-19 | substack | The Bible You're Reading Erased the Word for What's Eating Y | 572.0 | 0 | 0 | 0 |
| 2026-04-04 | substack | Your Funeral Already Happened. Now Get Up. | 556.0 | 0 | 0 | 0 |
| 2026-04-04 | substack | Your Funeral Already Happened. Now Get Up. | 556.0 | 0 | 0 | 0 |

## ALERTS

- ⚠️ **Stripe disputes open** on The Biblical Man: **2**
- ⚠️ Paid subs net -2 today (small churn)
- ⚠️ income_daily is 2 days stale (last=2026-06-27)
- ⚠️ X followers=4 (expected ~45.9K) — CDP session may be dead

---

## Query the brain

```
vault "what is working"
vault "subs churn this week"
vault "disputes" --source vault
```