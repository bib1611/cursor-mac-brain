# Plain Bible ClickFunnels Live UI Audit

Date: 2026-06-15 09:58 CDT
Operator: Codex via Chrome extension

Adam asked Codex to finish wiring the Plain Bible Manual funnel in ClickFunnels Commerce using the live CF UI. Codex read the approved safe paste pack and implementation notes, then verified the live CF funnel before acting.

Live funnel: `Plain Bible Funnel`
Funnel ID/public id: `NAvVxd`
Workspace: `jwrDzb`
Site: `jkyMwd`

Live CF page state verified:

- Existing Sales: `Plain Bible Manual - Sales Page`; workflow step `RBkgEQ`; page-step `kRYWll`; page/edit id `xgWDao`; public URL `https://adamjohnsonsteamworb5124.myclickfunnels.com/plain-bible`; pageviews 0; attached products 0; canvas blank.
- Created Chart OTO: `Plain Bible Funnel - Adam to Noah Chart OTO`; workflow step `QlMgAm`; page-step `pyWxZB`; page/edit id `bLObPd`; public URL shown by CF `https://adamjohnsonsteamworb5124.myclickfunnels.com/oto-adam-to-noah-chart--cdc27`; pageviews 0. Requested slug `/oto-adam-to-noah-chart`; CF auto-appended `--cdc27`.
- Existing Vault OTO: `Plain Bible Funnel - Vault OTO`; workflow step `odMZkb`; page-step `roDRyw`; page/edit id `zEDBaZ`; public URL `https://adamjohnsonsteamworb5124.myclickfunnels.com/plain-bible/vault`; pageviews 0; attached products 0; canvas blank.
- Existing Thank You: `Plain Bible Funnel - Thank You`; workflow step `gAaZMA`; page-step `WdrLQq`; page/edit id `RRqzMQ`; public URL `https://adamjohnsonsteamworb5124.myclickfunnels.com/plain-bible/thanks`; pageviews 0; attached products 0; canvas blank.

Live change made:

- Added the missing Chart OTO page between Sales and Vault.

Live changes not made:

- No PML was pasted. The CF editor exposed native section/template insertion and custom header/footer/code settings, but no full-page PML import surface.
- No CF products were created. The CF Products app for workspace `jwrDzb` showed an empty product catalog; the new-product flow creates a new CF product record and did not show a first-step control to reuse existing Stripe products or Payment Links.
- No buy buttons were wired.
- No 1-click upsells were enabled.
- No decline routing was changed.
- No Stripe charge or test charge was run.

Stripe read-only findings from the logged-in dashboard:

- Existing Stripe product `The Plain Bible Manual`: `prod_UUyKXzC53I3ec2`; active product; customer-entered USD price product; Payment Links show active `$10.00 USD (Preset)` links `plink_1TVyOSLN6IypHVMVHwjFJkG3` and `plink_1TVyOILN6IypHVMVqKpJ5OO7`.
- Existing Stripe product `The Adam to Noah Chart`: `prod_UgWPbqTBeLfrcK`; active product; customer-entered USD price product; Payment Links show active `$5.00 USD (Preset)` link `plink_1Th9N8LN6IypHVMVuznc5GzG`.
- No active Stripe product or Payment Link for `The Vault` / `The Biblical Man Vault` was found after paging the active Stripe product catalog and Payment Links list.

Delivery and duplicate-send check:

- The Dead Hidden app path has Stripe webhook to Resend fulfillment and Vault sequence idempotency/session metadata guards in repo code.
- The CF workspace Apps page showed Payments AI as added and Stripe as available, but did not show a Resend-specific installed app or an attached product/email delivery flow for this funnel.
- Because no CF product/button wiring exists, CF-to-Resend PDF delivery and the CF-to-existing-post-purchase-Vault-sequence non-duplication path could not be confirmed as live.

Boundary:

No customer email was sent, no Resend broadcast/automation was created, no Stripe product/payment link/price/customer/charge was created or modified, no live test charge was fired, no public traffic was sent, and no hard-stop claims/testimonials/stale prices were published.
