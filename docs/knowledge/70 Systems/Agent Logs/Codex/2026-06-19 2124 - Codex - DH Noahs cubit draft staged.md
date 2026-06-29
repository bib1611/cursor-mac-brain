# 2026-06-19 21:24 CDT - Codex - DH Noah's cubit draft staged

Adam asked Codex to add a CTA button for the new landing page and stage the Kent Hovind / Noah's cubit Dead Hidden post in the Dead Hidden editor on Comet.

## Draft

- Editor URL: `https://deadhidden.substack.com/publish/post/202795677`
- Draft ID: `202795677`
- Title: `They Made Noah's Ark Small`
- Subtitle: `The question was never only how big the ark was. It was what kind of world built it.`
- Audience: `everyone`
- Type: `newsletter`
- Status: `Saved`, not published

## CTA

Native Substack button added:

- Text: `GET PLAIN BIBLE 2.0`
- URL: `https://deadhidden.org/store/plain-bible-2.0?utm_source=dead_hidden_substack&utm_medium=post&utm_campaign=noahs_cubit_20260619&utm_content=plain_bible_2_cta`

CTA body line added above it:

`That is the whole reason I built Plain Bible 2.0.`

## Artifacts

- Local packet: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-19-tiktok-dh-post/DEAD-HIDDEN-POST-PACKET.md`
- Stage script: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-19-tiktok-dh-post/stage_deadhidden_noahs_cubit_comet.mjs`
- Stage result: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-19-tiktok-dh-post/stage-result.json`
- Top editor screenshot: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-19-tiktok-dh-post/deadhidden-noahs-cubit-editor-staged.png`
- Button screenshot: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-19-tiktok-dh-post/deadhidden-noahs-cubit-button-staged.png`

## Verification

- Comet Dead Hidden profile launched on CDP `9223`.
- Landing page returned HTTP `200` before staging.
- Stage result showed `savedVisible: true`, `savingVisible: false`, `audience: everyone`, `type: newsletter`, and `isPublished: false`.
- Native button node was verified in editor JSON with exact text and exact UTM URL.
- Raw URL was not visible in editor body text.
- Screenshots show `Saved` and the rendered gold button.

## Boundary

Staged/saved draft only. Codex did not click Continue, Preview, publish, schedule, send email, upload the TikTok/video, post to X/Threads/Substack Notes, mutate Stripe/customer/payment state, deploy code, change credentials, or change account settings.
