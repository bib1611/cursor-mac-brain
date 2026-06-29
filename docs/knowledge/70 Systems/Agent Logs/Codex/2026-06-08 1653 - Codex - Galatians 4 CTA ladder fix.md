# 2026-06-08 16:53 CDT - Codex - Galatians 4 CTA Ladder Fix

## Summary

Adam correctly flagged that the Galatians 4 Biblical Man draft had pastoral prose but no engineered CTAs.

Codex corrected the workflow, built a store-backed offer map, created a replacement CTA draft, sent the follow-up through Hermes Desktop, and verified the saved Substack editor state through Chrome CDP.

## Editor

Publication:

Biblical Man

Editor URL:

`https://biblicalman.substack.com/publish/post/201212767`

Title:

`You Cannot Serve Your Way Into the Family`

## Changed Artifacts

- Workflow updated: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-08-substack-source-to-hermes-editor/WORKFLOW.md`
- Offer map added: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-08-substack-source-to-hermes-editor/OFFER-MAP-CTA.md`
- CTA draft added: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-08-substack-source-to-hermes-editor/DRAFT-galatians4-sonship-CTA.md`
- Hermes follow-up added: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-08-substack-source-to-hermes-editor/HERMES-FOLLOWUP-CTA-FIX.md`
- Original Hermes handoff marked superseded for the "No product CTA" instruction: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-08-substack-source-to-hermes-editor/HERMES-HANDOFF-GALATIANS4.md`
- Verification proof added: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-08-substack-source-to-hermes-editor/PROOF-CTA-UPDATE.md`

## CTA Stack

- Early share CTA: send the post to the exhausted believer serving from fear.
- Subscribe CTA: `Subscribe to The Biblical Man`
- Primary buy CTA: `Buy The Plain Bible Manual - $10`
- Secondary buy CTA: `Get How To Study The Bible Like Your Life Depends On It - starts at $7`
- Final share/action CTA: send the post to one tired Christian who keeps serving like God has a clipboard.

## Offer Logic

The Plain Bible Manual was selected as the primary product CTA because it was the strongest verified relevant low-ticket Bible-reading offer in the read-only Stripe summary used for this workflow.

How To Study The Bible Like Your Life Depends On It was selected as the secondary CTA because it fits the post's "open the Book and study it" next step.

The Vault was not used as the primary CTA because the live Vault page still had stale May 31 urgency copy on 2026-06-08.

## Verification

Chrome CDP verification at 2026-06-08 16:53 CDT:

- Editor page title: `(72) Editing "You Cannot Serve Your Way Into the Family" - Substack`
- URL: `https://biblicalman.substack.com/publish/post/201212767`
- `saved: true`
- `bodyLength: 4644`
- `blockquotes: 4`
- `hasBringThisHome: true`
- `hasFinalShare: true`

Verified CTA links:

- `https://biblicalman.substack.com/subscribe?utm_source=post&utm_medium=web&utm_campaign=galatians4_sonship`
- `https://deadhidden.org/store/the-plain-bible-manual?utm_source=biblicalman_substack&utm_medium=post&utm_campaign=galatians4_sonship&utm_content=primary_cta`
- `https://deadhidden.org/store/how-to-study-bible?utm_source=biblicalman_substack&utm_medium=post&utm_campaign=galatians4_sonship&utm_content=study_cta`

## Boundary

Draft/editor update only.

No publish, schedule, email send, X post, Notes post, media upload, Stripe change, product change, account setting change, refund, cancellation, deletion, GitHub/Linear write, or deployment was performed.
