# 2026-06-10 12:30 CDT — Hermes — 777 launch push + Count the Number link cleanup

## Context
"Noah's Father Died at 777" published 12:15 PM CDT (post id 201483631, paid-only).
Live: https://deadhidden.substack.com/p/noahs-father-died-at-777
Morning post "God Told You to Count" (id 201446721) had buttons pointing at deadhidden.org/store/count-the-number, which 404'd until the store hotfix shipped earlier today.

## Actions (all verified this session)

### 1. Morning post links verified + post updated
- Store button: 200. Checkout button: 303 into live Stripe checkout session. Both work — fix was server-side, post URLs were already correct.
- Added italic note after the first buy button: "(If the button above gave you an error this morning, that was on my end. It is fixed. Same button works now.)"
- Updated via PUT /api/v1/drafts/201446721 + POST .../publish {send:false} through logged-in Comet session (CDP 9223). No email resend (post_date unchanged: 2026-06-10T12:40Z).
- Verified note in published body_html and on cache-busted public page.

### 2. Reader DM answered (Adam approved send)
- Reader: Adrian Bagayas (@abaggy, user 2226434, paid subscriber). Thread: substack.com/chat/75545fe4-f747-4fab-8d59-aba9eaa5abc1
- His message matched the broken-link report verbatim.
- Sent approved reply (link fixed / Count the Number is separate from Vault, $10 / sign-off "Adam"). Verified posted in thread, composer cleared.

### 3. Promo Note published
- Note: https://substack.com/@deadhidden/note/c-273977940
- Copy: broken-button correction + 777 open loop. Link attachment card to the 777 post (open.substack r=2t2o3r).
- Verified rendered on @deadhidden profile.

### 4. X funnel posted (@Biblicalman via xurl)
- Open-loop tweet id 2064761812306850037: Genesis 5 / Lamech 777 / "That is not even the strange part."
- Self-reply id 2064761847392112864 with open.substack.com link (r=2t2o3r). No link in tweet body.

## Tooling notes
- Substack DM endpoints: list = GET substack.com/api/v1/messages/inbox?tab=all; thread UI = substack.com/chat/{uuid}; send done via UI composer (contenteditable + submit button) over CDP.
- Notes publish: POST /api/v1/comment/attachment {type:link,url} then POST /api/v1/comment/feed {bodyJson, attachmentIds, tabId:for-you, surface:feed}.
- Generic authed fetch helper: /tmp/cdp_req.py (port, domain, method, path, body-file).
