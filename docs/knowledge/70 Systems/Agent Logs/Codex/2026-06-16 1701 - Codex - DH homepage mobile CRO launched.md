# Codex Receipt - DH Homepage Mobile CRO Launched

Date: 2026-06-16 17:01 CDT

PR: https://github.com/bib1611/deadhidden/pull/51

Merge commit: `d8d98173672e68909ab5fc1b8ec772dd8c499adb`

Production URL: `https://deadhidden.org/`

Production deployment:

- `Vercel - deadhidden`: `https://vercel.com/bib1611s-projects/deadhidden/ETGmM9oFi3YBinhgNZD2P576GwfL`
- `Vercel - deadhidden-site-live`: `https://vercel.com/bib1611s-projects/deadhidden-site-live/6HMV3zZgDrXVg9RyP6m2UgYQyF3n`
- `Vercel - thebiblicalmantruth`: `https://vercel.com/bib1611s-projects/thebiblicalmantruth/G1TmFTE13gyj7isYS9QZnXjqNJR6`

What launched:

- Mobile homepage hero now leads with `READ YOUR BIBLE STRAIGHT. NO CHURCH GAMES.`
- Hero names the $7 four-PDF offer.
- Mobile first screen shows the four PDFs before the CTA.
- Primary CTA reads `GET THE FOUR FOR $7`.
- Quiz is demoted to secondary text.
- "One man at a time" is replaced with "One household at a time."
- "Armed" front-door language is replaced with reader/Bibles-open language.
- Free offer is reframed as a preview pack.
- Unverified `LIMITED: 100 THIS WEEK` badge is removed.

Verification:

- PR #51 was open, non-draft, mergeable, and Vercel preview checks were green before merge.
- GitHub API merge succeeded.
- All post-merge Vercel contexts passed on `d8d9817`.
- Live `https://deadhidden.org/?deploy_check=d8d9817` returned HTTP 200.
- Live HTML contains:
  - `READ YOUR BIBLE`
  - `GET THE FOUR FOR $7`
  - `One household at a time`
  - `GET THE FREE PREVIEW PACK`
  - `131K+ readers. Bibles open.`
- Live HTML no longer contains:
  - `LIMITED: 100 THIS WEEK`
  - `One man at a time`
  - `GET 4 RESOURCES`
  - `TAKE THE 60-SECOND`
- Live deployment id in HTML: `dpl_ETGmM9oFi3YBinhgNZD2P576GwfL`.
- Live mobile screenshot: `/tmp/deadhidden-homepage-live-d8d9817-mobile.png`.
- `/store/vault-sampler?deploy_check=d8d9817` returned HTTP 200.

Boundaries:

- No checkout session created.
- No charge fired.
- No Stripe key, price, product, or webhook changes.
- No buyer email sent.
- No Substack/X publish.
