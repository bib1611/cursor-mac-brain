# 2026-06-17 0825 - Codex - Quiz direct checkout deployed

Adam passed Okara's recommendation to stop routing quiz and homepage battle cards into category browse pages.

Shipped:

- PR: https://github.com/bib1611/deadhidden/pull/55
- Branch: `codex/quiz-direct-product-ship`
- Commit: `6dedfdc9ad57c489207fea5c0b8a19ea3d6af381`
- Merge commit: `2d8994771801456964e8d3c1e7357d79b9250a80`

Changes:

- Quiz results now show one matched product, one price, and one CTA to `/checkout?slug=...`.
- Removed quiz-result email capture, secondary campaign card, and browse-store detours.
- Homepage `FIND YOUR FIGHT IN 60 SECONDS` cards now route to direct checkout URLs instead of `/store/category/...`.
- Removed the `VIEW ALL CATEGORIES` browse link from that homepage section.

Mappings:

- Marriage -> `vault-sampler` (`$7`)
- Spiritual Warfare -> `the-torment-triage` (`$14`)
- Bible Study -> `the-plain-bible-manual` (`$10`)
- Parenting -> `vault-sampler` (`$7`)
- General Discipleship -> `the-plain-bible-manual` (`$10`)
- Homepage Biblical Masculinity -> `the-plain-bible-manual` (`$10`)

Production deploy checks:

- `Vercel - deadhidden`: success, https://vercel.com/bib1611s-projects/deadhidden/2W2TW57KLsivZWz9hZMosbLHLf31
- `Vercel - deadhidden-site-live`: success, https://vercel.com/bib1611s-projects/deadhidden-site-live/8zxPfSL5L4VmenBiRs2TggG6mCct
- `Vercel - thebiblicalmantruth`: success, https://vercel.com/bib1611s-projects/thebiblicalmantruth/Cf2yZX11XMFbui58DBV1XDV1Fhio

Verification:

- Clean ship worktree from current `origin/main`.
- `npm run lint -- src/components/cro/QuizFunnel.tsx src/components/cro/HomepageBody.tsx` passed.
- `npm run build` passed with existing warn-only stale slug audit warnings.
- Local browser QA: Spiritual Warfare quiz result CTA pointed to `/checkout?slug=the-torment-triage`, browse/secondary result count was `0`, homepage battle cards pointed to checkout URLs.
- Live browser QA against `https://deadhidden.org/find-your-fight?deploy_check=2d89947` confirmed Spiritual Warfare result CTA `/checkout?slug=the-torment-triage` and no browse/secondary result cards.
- Live browser QA against `https://deadhidden.org/?deploy_check=2d89947` confirmed homepage battle cards point to checkout URLs for Plain Bible Manual, Vault Sampler, and Torment Triage.

Boundary:

- No Stripe price/product change.
- No checkout session created.
- No buyer email sent manually.
- No Resend broadcast/manual send.
- No free opt-in automation change.
- No Substack/X publish.
