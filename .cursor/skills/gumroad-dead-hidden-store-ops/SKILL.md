---
name: Gumroad / Dead Hidden Store Ops
description: "Use when working on Adam's Gumroad store (biblicalman.gumroad.com)
  or the deadhidden.org store: editing products, Discover categories/tags,
  pricing, storefront layout, email broadcasts, or workflow automations. Trigger
  on any Gumroad/Dead Hidden store, product, broadcast, or automation task."
autoInject:
  keywords:
    - Gumroad
    - biblicalman.gumroad.com
    - deadhidden.org store
    - broadcast
    - workflow automation
    - Discover
    - Vault
    - Vault Sampler
    - upsell
    - lead magnet
---
# Gumroad / Dead Hidden Store Ops

Operating playbook for Adam's store (biblicalman.gumroad.com, ~51 products, ~$48.7K lifetime). deadhidden.org is the warm-audience native store; Gumroad Discover is the cold-traffic net. Price identically on both to prevent arbitrage.

## Login
- No saved password in vault. Use the **X (@biblicalman) OAuth button** on gumroad.com/login. Gumroad emails a 2FA token to thebiblicalman1611@gmail.com; retrieve via `gmail.getInbox(0)` and enter at `gumroad.com/two-factor`.

## Skip-always products (never recategorize, publish, optimize, or re-add to grid)
- `eklgf` Penguin ($97 test placeholder, 0 sales)
- `lwahb` Support Blake's Fight (charity donation, no 30% fee)
- `zasak` Martyrdom Is Not Ancient History (unpublished, 0 sales)
- Also hidden from public grid: Dick Detox (`gbdtsl`).

## Key products / slugs
- Biblical Man Vault $365 (`huyrp`, `l/huyrp`) — top earner, requires intent.
- $7 Vault Sampler (`lkpzi`, `l/lkpzi`) — current featured product, cold-traffic entry.
- The Submission Fraud (`ozuoy`) — $0 PWYW lead magnet (tip default $7).
- The 5 Conversations workbook (`udech` / `5-conversations-workbook`, $9) — companion to "Before The World Does" ($49.99).
- Default funnel flagship: $27 Confusing Things in the Bible (deadhidden.org).

## Discover categorization (Gumroad has no "Religion" category)
- faith/Bible/men's titles -> **Self Improvement > Spirituality**
- marriage titles -> **Self Improvement > Dating & Relationships**
- writing titles -> **Writing & Publishing**
- Standard tags: `kjv`, `bible study`, `christian`, `christian men`, `biblical masculinity`, `spiritual warfare`, `devotional`, `scripture`, `biblical marriage`, `discipleship` (5 per product).
- High-ticket badge (e.g. $365 Vault) may lag ~24h after tagging.

## Title formula
- `[Specific metric or outcome]: [Benefit statement]` with a concrete number beats vague "Learn X."
- Thumbnails: covers 1280x720 (16:9, up to 8 carousel); square 600x600 min.

## OPEN ITEM to fix
- **Post-Purchase Upsell workflow:** 68.6% opens / 0 clicks. Same broken-link/plain-text-CTA pattern that was fixed elsewhere. Needs CTA buttons via Insert -> Button. Not yet done.

## Durable UI quirks (Gumroad)
- **Broadcast publish:** top-level Publish opens a dropdown that does NOT send. Send only after clicking **"Publish now"** inside it. Navigating away after the top-level click silently discards the draft.
- **CTA insertion (only reliable path):** position cursor at body end (`.click()` + `Meta+a` + `ArrowRight`), Insert toolbar -> Button menuitem -> fill "Enter text" + "Enter URL" -> "Add button." Do NOT use keyboard-selection + Insert link (lands mid-word). ProseMirror: `pressSequentially()` after `.click()`; `Meta+a`+`ArrowRight` to reach end.
- **Add-email body-ref hazard:** new email form opens collapsed; the last `textbox "Email message"` ref may resolve to an existing email's body. Always `innerText()` all body refs to confirm the empty new one before inserting.
- **Has-bought / Has-not-yet-bought comboboxes (workflows):** React-select; do NOT `locator.fill()`. Click to open, `pressSequentially()` to filter, clear prior text with 40+ Backspace, Enter selects top result. Remove a chip by clicking the chip button directly.
- **Membership tag combobox** (`cxnjbs`): re-renders DOM per tag; re-snapshot after each tag press, don't reuse a ref.
- **Profile editor:** "Update profile" stays disabled until a change is made. Featured-product combobox can show stale state; confirm via `currently selected` in snapshot, not regex (em dashes in titles break regex).
- **Discover batch-edit throughput:** ~18-22s/product. Batch **4-5** per REPL run; 6 times out with the last item aborted.
- **Price extraction:** use `page.evaluate()` reading anchor `.textContent` for the first dollar regex. On `/products`, each row shows revenue first then price/floor (second amount is the price).

## Guardrails
- Bio ("Make the Bible Great Again. I wrote my first devotionals at 4 AM in a frozen garbage truck...") is a genuine differentiator. Do not overwrite.
- Email subject lines that win: curiosity + KJV edge, personal hooks. List ~966 subs, elite 42-52% open rates.
- Sending broadcasts and publishing are externally visible: draft and confirm with Adam first.
