# 2026-06-14 0915 - Codex - Sunday Vault conductor packet staged

Adam asked Codex to act as conductor for the MarketingSecrets Sunday revenue sprint while he was away from desktop.

## Actions

- Read current ops capsule and refreshed team packet.
- Queried MarketingSecrets MCP directly and saved corrected Brain facts:
  - Vault operating price is `$365` lifetime, not stale `$297`.
  - Live low-ticket non-Vault segment stats are now in Brain.
- Tried official Chrome bridge after Adam said he was signed in. Chrome is running, but the Codex Chrome Extension is still not installed/enabled in selected Chrome profile, so live tab claim is unavailable through the official Chrome tool. Continued through direct MarketingSecrets MCP.
- Dispatched read-only Agent Bus tasks to Hermes and Chorus/Jarvis:
  - Hermes: Sunday revenue blind-spot audit.
  - Chorus/Jarvis: Vault funnel offer/content pressure test.
- Created live low-ticket Vault upsell segment from Stripe/Resend with no sends or mutations:
  - 681 paid Checkout Sessions scanned.
  - 712 Resend contacts returned.
  - 293 candidate rows.
  - 279 active Resend rows.
  - 238 active rows in the primary `$7-$19` band.
  - 41 active rows in the expanded `$20-$25` band.
  - 14 missing/unsubscribed suppressed.
- Staged local Vault funnel patch in `/Users/adamjohnsson/code/deadhidden`:
  - Active Vault public copy back to `$365`.
  - Removed active fake-looking Vault testimonial block.
  - Removed active homepage fake scarcity countdown and social-proof toast render.
  - Corrected Vault analytics checkout values to `365`.
  - Updated success and purchase-delivery Vault bridge copy.
  - One-time Stripe Checkout no longer hard-codes payment methods, so dashboard dynamic methods can show; subscriptions remain card-only.

## Files

- `/Users/adamjohnsson/Downloads/reports/vault-funnel-fix-approval.md`
- `/Users/adamjohnsson/Downloads/reports/sunday-store-revenue-plan.md`
- `/Users/adamjohnsson/Downloads/drafts/sunday-vault-direct-email.md`
- `/Users/adamjohnsson/Downloads/drafts/post-purchase-upsell-sequence.md`
- `/Users/adamjohnsson/Downloads/content/sunday-afternoon-drafts.md`
- `/Users/adamjohnsson/Downloads/reports/chrome-marketingsecrets-status.md`
- `/Users/adamjohnsson/Downloads/scripts/export-low-ticket-vault-segment.mjs`
- `/Users/adamjohnsson/Downloads/data/low-ticket-vault-candidates.csv`
- `/Users/adamjohnsson/Downloads/data/low-ticket-vault-candidates-summary.json`
- `/Users/adamjohnsson/Downloads/segments/vault-upsell-low-ticket-active.csv`

## Verification

- Stale price/fake proof scan clean for `$285`, `$297`, May offer terms, old fake testimonial names, fake rating phrase, and old `47` Vault tracking values. The only remaining payment-method hit is the intentional subscription card-only branch.
- `npm run audit:slugs` passed with existing warn-only stale slug references.
- Targeted lint passed on touched files, with two pre-existing warnings in category route.
- `npm run build` passed.

## Boundaries

- No deploy.
- No email send.
- No Substack/X publish or schedule.
- No Stripe price, refund, charge, customer, subscription, Payment Link, or dashboard mutation.
- No Resend contact/segment mutation beyond read-only contact listing.

## Next Approval

Adam can approve these separately:

1. Deploy the Vault funnel fix to production.
2. Send the Sunday Vault direct email to the primary `$7-$19` segment.
3. Publish/schedule the Sunday Substack/X drafts.
4. Confirm or toggle Stripe Smart Retries in Dashboard.
