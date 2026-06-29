# 2026-06-14 0935 - Codex - MarketingSecrets in-app audit and support blockers

Adam signed into MarketingSecrets in the Codex in-app browser at the `deadhiddenos` chat URL. Codex used the in-app browser session to prompt MarketingSecrets with the read-only Sunday Vault sprint audit and then read the finished memo.

MarketingSecrets agreed the Vault upsell lane is the correct revenue move, but flagged two blockers before any broadcast:

- Open support queue around cancellation, downloads, and Vault access.
- A duplicate-broadcast bug reported by a customer receiving multiple copies of store emails.

New local artifacts:

- `/Users/adamjohnsson/Downloads/reports/marketingsecrets-sunday-audit.md`
- `/Users/adamjohnsson/Downloads/reports/sunday-support-revenue-blockers.md`
- `/Users/adamjohnsson/Downloads/reports/duplicate-send-guard.md`

Support work performed:

- Created a Gmail draft for the Sheila cancellation/subscription reply; not sent.
- Created a Gmail draft for the Lila Familiar Spirits download reply with a fresh verified link; not sent.
- Verified Susie and Lila Count-the-Number were not as open as MarketingSecrets first reported.
- Identified Luke, Lora, Douglas/Gene, and Justin as open/support-risk lanes that need real fulfillment or access repair before a broadcast.
- Read-only Resend inspection confirmed repeated welcome emails to the same address within minutes today.
- Staged a local duplicate-send guard in `/Users/adamjohnsson/code/deadhidden` by adding Resend idempotency keys to welcome, lead magnet, purchase delivery, scheduled follow-up, and cron sequence send paths.
- Verification passed: `git diff --check`, targeted ESLint, and `npm run build`.
- Saved the duplicate-send finding and local patch status back to MarketingSecrets Brain under `projects`.

No email sent. No Resend broadcast created. No Substack/X post published or scheduled. No deploy. No Stripe customer, subscription, refund, price, or payment-link mutation. No live automation paused.

Next approval gates:

- `Approve deploying the Vault funnel fix to production.`
- `Approve deploying the Vault funnel and duplicate-send guard to production.`
- Approve exact Gmail support sends after reviewing drafts.
- Approve creating a manual legacy Vault migration path for old Gumroad/Vault access issues.
- Approve any Resend broadcast only after duplicate-send source is checked and open-support contacts are suppressed.
