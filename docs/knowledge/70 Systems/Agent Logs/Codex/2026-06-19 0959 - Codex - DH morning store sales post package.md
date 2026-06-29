# Codex - DH Morning Store Sales Post Package

Date: 2026-06-19 09:59 CDT

Adam reported no store sales for a while and asked Codex to investigate, use MarketingSecrets thinking, and come up with a Dead Hidden Substack post idea for this morning. Christie suggested deeper Bible-study guide ideas such as baptism and kingdom topics.

## What Was Checked

- Read the current ops capsule and offer-brain skill instructions.
- Used MarketingSecrets Brain through local `ms-brain recent 10`.
- Read prior Dead Hidden morning-post memory and the June 15 rollout summary as routing context only.
- Pulled live read-only Stripe checkout-session totals for account `acct_1PeIdjLN6IypHVMV`.
- Checked live product pages with `curl`.
- Checked repo product truth for `counterfeit-kingdom-starter-guide`, `plain-bible-2.0`, and checkout routing.

## Findings

- Store sales were not zero: last 24h had 20 checkout sessions, 7 paid sessions, and `$91.00` paid checkout gross.
- Last paid checkout seen was 2026-06-19 05:24 CDT for `WHEN EVIL COMES TO THE DOOR - HOUSEHOLD PACK`, `$12`.
- Most recent open unpaid checkout seen was 2026-06-19 06:44 CDT for `The Plain Bible Manual`, `$10`.
- Last 14d paid checkout leaders included `Plain Bible Manual 2.0` complete-system bundle at 12 orders / `$444`, `How to Count Your Bible` at 16 / `$304`, and `THE PLAIN BIBLE MANUAL` at 9 / `$90`.
- Live pages returned `200`: store, Counterfeit Kingdom Starter Guide, Plain Bible 2.0, Plain Bible Manual, Strong Delusion, How to Count, Count the Number, and `/evil`.

## Decision

Recommended a same-morning Dead Hidden Substack post around the kingdom/dispensational framework, using Christie's deeper-study idea as validation, but selling the already-live `$17` `The Counterfeit Kingdom Starter Guide` instead of pausing to build a new baptism guide.

Saved package:

`/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-19-dh-morning-store-sales/COUNTERFEIT-KINGDOM-POST-PACKAGE.md`

Verification:

- Draft package ASCII check passed.
- Em dash count: `0`.
- Both CTA URLs returned HTTP `200`.

## Boundary

Draft and read-only investigation only. No Substack publish, no Substack schedule, no email send, no Stripe/customer/payment mutation, no deploy, no X post, no Linear/Notion write, no credential/account setting change.
