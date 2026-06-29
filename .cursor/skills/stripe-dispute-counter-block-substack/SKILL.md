---
name: Stripe Dispute Counter & Block (Substack)
description: Use when Adam gets a Stripe dispute/chargeback notification
  (especially "fraudulent" / reason code 10.x) on the Dead Hidden or Biblical
  Man Stripe account and wants to identify the transaction, counter it with
  evidence, and/or block the customer. Trigger on forwarded Stripe dispute
  emails, "dispute," "chargeback," "fraudulent transaction," or "block this
  person."
siteSpecific: true
autoInject:
  keywords:
    - stripe dispute
    - chargeback
    - fraudulent transaction
    - dispute
    - counter dispute
    - block this person
    - du_
    - wells fargo dispute
  url:
    - dashboard.stripe.com/disputes/**
    - dashboard.stripe.com/**/disputes/**
---
# Stripe Dispute Counter & Block (Substack subscriptions)

Workflow for handling a Stripe dispute on Adam's Substack-connected Stripe accounts (Dead Hidden / Biblical Man). Goal: identify what was bought, build a strong counter, submit it, and block the abuser.

## 0. Key context
- The Stripe account in the dispute email is named **"Adam Johnson"**. Dashboard: `https://dashboard.stripe.com/disputes/{dispute_id}`.
- Most disputes are **Substack annual subscriptions** (product literally named like "$96 a year", metadata `substack: yes`). Pattern: free signup -> 7-day trial -> auto-convert charge -> customer disputes as "fraudulent" = usually **friendly fraud / buyer's remorse**, not real card theft.
- Substack publications live under **different logins**:
  - The Biblical Man -> `biblicalman.substack.com`
  - irynx chvrch -> `irynxchvrch.substack.com`
  - **Dead Hidden -> `deadhidden.substack.com` (SEPARATE account login)**. If not logged in, ask Adam to log in via another tab, then `listBrowserTabs()` + `attachBrowserTab()`.

## 1. Open the dispute & read the facts
Open `dashboard.stripe.com/disputes/{dispute_id}` and snapshot. Capture:
- Disputed amount, total withdrawn (amount + dispute fee), customer email, card (last4 / fingerprint), **billing ZIP**, issuer, reason + network reason code, response due date.
- Related objects: subscription ID, invoice number (e.g. `MXRMU7N9-0002`, the `-000N` suffix = billing cycle).
- Open the subscription/invoice/product to confirm exactly what was purchased (name, price, trial, start/charge/cancel dates).

## 2. Gather evidence (strongest first)
Pull from Stripe (auto-available) and Substack:
- **Location match (biggest lever):** Stripe's "Device location" IP geolocation vs the card **billing ZIP**. If they match (e.g. IP Portland OR = ZIP 97201) and **ZIP/AVS check passed**, that's compelling.
- **Trial-then-convert** pattern = knowing signup.
- **Substack subscriber record** (search subscriber by email in the right publication, open profile + **Events tab**): customer real name, State/Country (should match billing region), first paid date (= charge date), cancel date (often = dispute date), and **post-purchase usage** (emails opened, posts seen, links clicked AFTER the charge). Screenshot the profile AND the Events log.
- Save screenshots to `./tmp/`.

## 3. Fill the counter form
Click **Counter dispute** -> Continue. Step 1:
- "Why should you win?" -> **The purchase was made by the rightful cardholder**.
- Product type -> **Digital product or service**. Next.

Step 2 (evidence):
- **Customer name** field: fill real name from Substack.
- **Access activity log** field: write a factual narrative covering location triple-match, prior relationship, post-purchase usage dates, and the same-day cancel/dispute (buyer's remorse). Keep it truthful, sourced only from Stripe + Substack data.
- **Upload exhibits:** use `page.locator('input[type="file"]').setInputFiles([absPath])`. After it appears under "Uploaded documents", set its category via `selectOption(...)` and verify with `page.evaluate(()=>document.querySelector('select').value)`. Categories: profile screenshot -> `serviceDocumentation`; email/activity events -> `customerCommunication` (satisfies Visa's "compelling evidence" requirement). Upload one file, categorize, then upload the next (re-grab refs; they go stale).
- Stripe shows "Evidence completion: ... ready to submit" when done.

### Form quirks
- Evidence auto-saves ("All changes saved"). If a tab closes, reopen `.../disputes/{id}/respond` — drafts persist.
- Refs go stale after uploads/selects; re-snapshot.
- The `page` global can slip to another tab after cross-tab actions; re-`attachBrowserTab()` the Stripe tab.

## 4. Submit decision (cost nuance — ALWAYS surface to Adam)
- **Submit now** = files immediately, **dispute-countered fee applies** (refunded if we win).
- **Leave auto-submit ON** = Stripe auto-submits our evidence by the due date; per Stripe's email the **countered fee is waived** (Smart Disputes). Same evidence either way.
- Clicking **Submit evidence now** -> a Visa compelling-evidence dialog lists included/omitted items (customer signature won't exist for online subs) -> **Submit anyway**.

## 5. Block the customer
On the dispute page click **Add to block list**. Default-checks card fingerprint + email + customer ID; set "Remove from list after" to **Do not remove**. Confirm -> "Added to block list."

## 6. Confirmation gate (required)
Submitting the counter (paid) and blocking are externally-visible actions: confirm with Adam before doing them. Offer the submit-now-vs-auto-submit choice. After submit, note the bank's decision window (~3 months) and offer a reminder near the due date.

## 7. Report
State: what was actually purchased, that it's friendly-fraud not theft, the evidence submitted, decision ETA, and that the customer is blocked. Attach the final "Evidence submitted" screenshot.
