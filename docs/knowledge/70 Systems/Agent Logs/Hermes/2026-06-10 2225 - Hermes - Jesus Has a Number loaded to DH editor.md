# 2026-06-10 22:25 CDT — Hermes — "Jesus Has a Number" loaded to DH Substack editor

## What
Loaded the paid-only draft "Jesus Has a Number" into the Dead Hidden Substack editor via the authenticated Comet session (CDP port 9223, profile `.comet-deadhidden`), per Adam's Telegram instruction.

## Draft
- Editor URL: https://deadhidden.substack.com/publish/post/201544405
- Title: Jesus Has a Number
- Subtitle: It is not 666. And the people selling you angel numbers do not want you to count it.
- Audience: only_paid
- Body: 62 paragraphs, 920 words, paywall divider after "But the Bible got there first."
- Opening line corrected from "This morning" to "Yesterday" (post drops the day after the free teaser "God Told You to Count").

## CTA buttons (Halbert-style, verified rendering in editor)
1. Pre-paywall tease + button "UNLOCK THE OTHER NUMBER" → https://deadhidden.substack.com/subscribe
2. Closer block + button "GET COUNT THE NUMBER" → https://deadhidden.org/store/count-the-number (URL verified 200)

## Cover image
- Generated via Higgsfield (nano_banana_2), 1376x768: ΙΗΣΟΥΣ on candlelit parchment, 888 in cracked gold. No faces, no modern type.
- Local copy: /Users/adamjohnsson/Hermes-Workspace/drafts/jesus-has-a-number-cover.png
- Uploaded to Substack S3 and set as draft cover_image (PUT 200): https://substack-post-media.s3.amazonaws.com/public/images/02d4cbc1-31fa-44fc-ab68-85423b55a046_1376x768.png

## Pre-publish guards run (substack-publishing-intelligence skill)
- Title rerun guard: clean — no "Jesus"/"number"/"888" titles in last 50 DH posts.
- Climbing-tail: "Noah's Father Died at 777" (paid, ~12:15 PM today) at 3.44 hearts/hr, 0.81 restacks/hr at ~10h — above DH ceiling. "God Told You to Count" (free, ~7:40 AM) 3.18/0.48 — also above ceiling.
- NOT scheduled, NOT published. Awaiting Adam's review and explicit approval per standing rules.

## Tooling
- New helpers: /Users/adamjohnsson/Hermes-Workspace/tools/cdp_eval.py (CDP JS eval), cdp_shot.py (screenshot; note: Comet /json/new ignores url param — navigate via Page.navigate; background tabs do not paint, use DOM verification).
- Substack draft API flow: POST /api/v1/drafts requires draft_bylines [{id: user_id}] up front; user id from window._preloads.user.id. Body is stringified ProseMirror doc; "button" and "paywall" node types accepted. Image upload: POST /api/v1/image with data URI.
