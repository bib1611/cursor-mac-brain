---
type: agent-log
date: 2026-06-12
agent: Hermes
topic: DH afternoon paid post (Endor) staged in Substack editor
tags: [hermes, dead-hidden, substack, draft, paid]
---

# DH Endor Paid Post Staged

## Goal

Write and stage the paid afternoon post promised in the morning free post ("The Philistines Didn't Kill Saul", draft 201731804). Stage only — no publish.

## What I Did

- Loaded voice-DNA.md, reused proven staging method from morning receipt (Comet CDP 9223 + POST /api/v1/drafts).
- Verified all 14 KJV quotes verse-exact via bible-api.com (KJV translation) before staging.
- Wrote "The Seance Worked" — 1 Samuel 28 verse by verse (~1,070 words of prose + 15 blockquoted verses).
- Free preview cuts at the scream (1 Sam 28:12); paywall node placed there. Zero links above paywall.
- POST via authenticated Comet session → draft **201733279**, audience **only_paid**.
- First CDP call timed out (backgrounded tab throttled); verified no duplicate draft created, activated tab, re-fired clean.
- Navigated Comet tab to editor, DOM-verified: 7 H2s, 15 blockquotes, paywall-editor divider, 3 CTA buttons (GET FAMILIAR SPIRITS / START WITH THE DEAD HIDDEN OS / UNLOCK THE VAULT - $297), utm_campaign=endor_seance.

## Proof

- Draft URL: https://deadhidden.substack.com/publish/post/201733279
- API round-trip counts: {paragraph: 97, blockquote: 15, paywall: 1, heading: 7, horizontal_rule: 8, button: 3}, audience "only_paid".
- Builder + payload: /Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-12-endor-paid-post/

## Follow-Up

- NOT published. Adam reviews and publishes this afternoon.
- Byline returned empty via API (same as morning draft) — confirm author chip reads Dead Hidden / Adam Johnson before sending.
- Morning free post 201731804 still unpublished as of staging; it carries the tease that makes this one due "this afternoon."
