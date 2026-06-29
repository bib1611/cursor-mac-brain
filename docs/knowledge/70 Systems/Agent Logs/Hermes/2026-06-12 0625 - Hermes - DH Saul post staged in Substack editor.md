---
type: agent-log
date: 2026-06-12
agent: Hermes
topic: DH morning free post staged with CTA buttons
tags: [hermes, dead-hidden, substack, draft]
---

# DH Saul Post Staged in Substack Editor

## Goal

Stage the approved free morning post ("The Philistines Didn't Kill Saul") as a formatted Dead Hidden Substack draft with CTA buttons. Stage only — no publish.

## What I Checked

- Comet running with CDP on localhost:9223, profile `.comet-deadhidden`, logged into deadhidden.substack.com publisher dashboard.
- Pulled existing DH draft 201607195 via authenticated API to confirm editor JSON schema: paragraph, heading, blockquote, horizontal_rule, button (attrs url/text/action/class). House button style: ALL CAPS + UTM-tagged links.
- Publication users: Dead Hidden admin id 218038831.

## What I Did

- Patched `~/.hermes/scripts/cdp_eval.py` to accept `CDP_PORT` env var (was hardcoded 9222).
- Built full ProseMirror doc: 38 paragraphs, 2 H2s, 5 KJV blockquotes, 5 dividers, 4 buttons.
- POST /api/v1/drafts via Comet authenticated session → draft id **201731804**, status 200, audience `everyone` (free).
- Buttons: UPGRADE BEFORE THIS AFTERNOON (subscribe), GET FAMILIAR SPIRITS, START WITH THE DEAD HIDDEN OS, UNLOCK THE VAULT - $297. Store links carry utm_campaign=philistines_saul.
- Navigated Comet tab to the editor; verified render: title, 2 H2s, 5 blockquotes, all buttons present.

## Proof

- Draft URL: https://deadhidden.substack.com/publish/post/201731804
- API verify: counts {paragraph:38, blockquote:5, horizontal_rule:5, heading:2, button:4}, audience "everyone".

## Follow-Up

- NOT published. Adam reviews and publishes manually.
- Byline field returned empty via API despite PUT; confirm the author chip in the editor before sending.
- Afternoon paid post (Endor / 1 Samuel 28) is promised in the body — needs drafting today.
