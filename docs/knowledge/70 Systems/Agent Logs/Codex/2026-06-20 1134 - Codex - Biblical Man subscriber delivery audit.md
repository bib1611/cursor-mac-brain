# 2026-06-20 11:34 CDT - Codex - Biblical Man subscriber delivery audit

## Summary

Exported and analyzed the live Biblical Man subscriber table from the authenticated Substack publisher dashboard.

- Source: `https://biblicalman.substack.com/publish/subscribers`
- Endpoint used: `POST /api/v1/subscriber-stats`
- Exported rows: `25,823`
- Email delivery enabled: `25,659`
- Email delivery disabled: `164` (`0.64%`)
- Paid-access rows (`is_subscribed=true`): `1,244`
- Paid-access rows with email off: `164` (`13.18%` of paid-access)
- Paying rows excluding comp/gift/free-trial: `1,216`
- Paying rows with email off: `158` (`12.99%` of paying)
- Dormant-but-enabled re-engagement segment: `3,703`

Email-off definition: Substack returned `root_enabled=false` and no section emails in `sections_enabled` for the subscriber row. The table endpoint rejects the literal detail-only fields `email_disabled` and `email_disabled_at`, so the full-list audit uses Substack's exposed delivery-enable flags.

## Files

- Report: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-20-bm-subscriber-delivery-audit/REPORT.md`
- Raw JSONL export: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-20-bm-subscriber-delivery-audit/biblicalman_subscribers_live_2026-06-20.jsonl`
- Raw CSV export: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-20-bm-subscriber-delivery-audit/biblicalman_subscribers_live_2026-06-20.csv`
- Email-disabled list: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-20-bm-subscriber-delivery-audit/list_a_email_delivery_disabled.csv`
- Dormant-but-enabled re-engagement list: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-20-bm-subscriber-delivery-audit/list_b_dormant_but_enabled_reengagement.csv`
- Paid-access email-off list: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-20-bm-subscriber-delivery-audit/list_c_paid_access_email_off.csv`
- Paying-only email-off list: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-20-bm-subscriber-delivery-audit/list_c_paying_only_email_off_excluding_comp_gift_trial.csv`
- Cohort breakdown: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-20-bm-subscriber-delivery-audit/cohort_delivery_breakdown.csv`
- Summary JSON: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-20-bm-subscriber-delivery-audit/analysis_summary.json`

## Findings

The measurable hard suppression pocket is small in the full list, but concentrated in the dangerous place: all `164` email-off rows are paid-access rows, and `158` are paying rows after excluding comp/gift/free-trial.

The larger fatigue/re-engagement pocket is separate: `3,703` free, email-enabled readers are older than 60 days, have received more than five emails, and show zero opens, clicks, web post views, and activity rating under the conservative dormant filter.

Signup cohorts do not show a disabled-email spike after the FaithWall public/beta launch copy window (`2026-06-10`) or the active FaithWall positioning/app-recovery window (`2026-06-18`): rows on/after `2026-06-10` show `0/281` disabled; rows on/after `2026-06-18` show `0/70` disabled.

## Boundary

Read/export/analyze only. No Substack publish/send, subscriber setting change, tag mutation, import, email, Stripe/customer action, Linear/Notion write, deploy, credential change, or account-setting change was performed.
