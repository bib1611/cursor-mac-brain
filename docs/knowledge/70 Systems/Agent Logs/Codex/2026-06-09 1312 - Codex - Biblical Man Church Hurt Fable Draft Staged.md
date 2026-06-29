# Biblical Man Church Hurt Fable Draft Staged

Date: 2026-06-09 13:12 CDT
Operator: Codex with Hermes/Fable
Status: published by Adam, verified by Codex

## Request

Adam pointed to the Biblical Man X post and matching Substack Note about church hurt and losing faith in people instead of Christ. He asked to use the workflow, create a Biblical Man Substack post for this afternoon, use the CTA research on high-converting buttons, and have Hermes put it in the Biblical Man editor on Chrome as a first real Fable use.

## Result

Saved Biblical Man Substack draft:

`https://biblicalman.substack.com/publish/post/201340823`

Title:

`You Did Not Lose Faith in Christ`

Subtitle:

`You lost faith in people you mistook for Him. The Bible saw them coming.`

## Work Performed

- Verified the live X source with `xurl read`.
- Verified the public Substack Note text through Substack fetch.
- Built `SOURCE-PACKET.md`, `OFFER-MAP.md`, and `CTA-PLAN.md`.
- Verified `GIVE ME SOMETHING TO BELIEVE IN` live at 200 and starting at $5.
- Verified `HOW TO STUDY THE BIBLE LIKE YOUR LIFE DEPENDS ON IT` live at 200 and starting at $7.
- Verified the Biblical Man subscribe page returns 200.
- Ran Hermes using `macproxy/adam-writing-fable-5` to draft and audit the post.
- Staged the draft through authenticated Chrome CDP on `127.0.0.1:9222`.
- Used three Substack `button` nodes for subscribe, primary offer, and fallback offer.
- Repaired one subtitle parsing defect after Hermes caught it.

## Final Verification

- Editor state: `Saved`
- Browser title: `Editing "You Did Not Lose Faith in Christ" - Substack`
- Editor URL: `https://biblicalman.substack.com/publish/post/201340823`
- Body length: 5,824 chars
- Button count: 3
- Raw URLs visible in body: false
- Leftover markers visible: false
- Subtitle divider defect: false
- Paywall markers: false

CTA buttons:

1. `Subscribe free for the next Bible-first reset`
2. `Get Give Me Something To Believe In - $5`
3. `Start studying the Bible - $7`

Proof file:

`/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-biblicalman-church-hurt-christ/STAGING-PROOF.md`

Screenshots:

- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-biblicalman-church-hurt-christ/biblicalman-church-hurt-draft-fixed.png`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-biblicalman-church-hurt-christ/biblicalman-church-hurt-draft-top.png`

## Boundary

Codex and Hermes did not publish, schedule, email, post to X, post a Substack Note, click Preview, click Continue, upload media, change settings, touch Stripe/customer state, or alter unrelated editor surfaces.

## Publish Update

At 2026-06-09 13:34 CDT, after Adam said `Sent`, Codex verified the public Substack post:

`https://biblicalman.substack.com/p/you-did-not-lose-faith-in-christ`

Public page proof:

- HTTP 200
- Substack embedded post data: `is_published: true`
- Published: `2026-06-09T18:33:01+00:00`
- Post ID: `201340823`
- Slug: `you-did-not-lose-faith-in-christ`
- Title and subtitle match the staged draft.
- Public page includes the subscribe, primary product, and fallback product button HTML.
- Public word count: `1071`

Prepared-only promo packet:

`/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-biblicalman-church-hurt-christ/POST-PUBLISH-PROMO.md`

Codex did not post to X, post a Substack Note, schedule, email, upload media, change settings, or touch Stripe/customer state.
