# Codex - Resend Vault Buyer Broadcast Scheduled

Date: 2026-06-14 11:59 CDT

Adam approved:

`Approve creating the Resend segment from /Users/adamjohnsson/Downloads/segments/vault-upsell-first-send-primary-suppressed.csv and sending the V3 Vault email with subject "You bought one file. Here is the shelf." Monday 9:00 AM Chicago.`

## Outcome

- Resend segment created/reused: `Vault buyer shelf first send - 2026-06-15 0900 CDT`
- Segment ID: `d5563bf2-1e73-444b-85a7-241cda6a67bc`
- Verified segment contacts: `235`
- Active contacts: `235`
- Unsubscribed contacts in segment: `0`
- Broadcast created: `00728782-8d30-42ae-821d-26f3858c0638`
- Broadcast status: `scheduled`
- Subject: `You bought one file. Here is the shelf.`
- Scheduled time: `2026-06-15 09:00 CDT`
- Resend scheduled_at: `2026-06-15 14:00:00+00`

## Safeties

- Source CSV had `237` rows.
- Live Resend verification skipped `2` missing contacts.
- No unsubscribed contacts were included.
- Final Stripe recheck found `0` current Vault buyers in the CSV since generation.
- No same-campaign Resend broadcast existed before scheduling.
- First apply attempt failed before broadcast creation because `.env.local` had blank `EMAIL_FROM=""`; script was patched to fallback to `Adam at Dead Hidden <adam@deadhidden.org>`.

## Files

- Result JSON: `/Users/adamjohnsson/Downloads/reports/resend-vault-buyer-broadcast-2026-06-15.json`
- Human report: `/Users/adamjohnsson/Downloads/reports/resend-vault-buyer-broadcast-scheduled.md`
- Runner: `/Users/adamjohnsson/Downloads/scripts/schedule-vault-buyer-shelf-resend.py`
- Source CSV: `/Users/adamjohnsson/Downloads/segments/vault-upsell-first-send-primary-suppressed.csv`
- Draft: `/Users/adamjohnsson/Downloads/drafts/deadhidden-buyer-vault-email-v3.md`

## Not Done

- No Day 7 resend scheduled.
- No Substack/X schedule or publish action.
- No Stripe mutation.
- No repo changes.

## Next

Monitor Monday after send for delivery, clicks, replies, unsubscribes, and Vault sales. Review first-send metrics before scheduling any resend.
