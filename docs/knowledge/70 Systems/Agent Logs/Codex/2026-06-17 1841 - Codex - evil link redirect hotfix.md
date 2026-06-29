# 2026-06-17 18:41 CDT - Codex - Evil Link Redirect Hotfix

Adam reported that clicking the new `/evil` links still produced the Dead Hidden 404 page. Codex treated this as launch-broken and shipped a production hotfix.

## Changed

- Repo: `bib1611/deadhidden`
- Worktree: `/tmp/deadhidden-evil-launch`
- Branch: `codex/evil-link-redirect`
- PR: https://github.com/bib1611/deadhidden/pull/60
- Merge commit: `28db9bc019f99bc251c9902d9f6861a749d05a6e`
- File changed: `middleware.ts`

The middleware now redirects malformed `evil` funnel URLs that end with a stray `]` or `)` back to the clean URL. This covers encoded variants such as `/evil%5D`, `/evil%29`, `/evil/waitlist%5D`, and `/evil/waitlist%29`. The existing `/store/if` referral cookie behavior remains fenced to `/store/if`.

## Verification

- `npm run lint -- middleware.ts` passed.
- `git diff --check` passed.
- `npm run build` passed.
- Local production smoke passed:
  - `/evil%5D` -> `308` to `/evil`
  - `/evil%29` -> `308` to `/evil`
  - `/evil/waitlist%5D` -> `308` to `/evil/waitlist`
  - `/evil/waitlist%29` -> `308` to `/evil/waitlist`
- Vercel production checks passed on merge commit `28db9bc019f99bc251c9902d9f6861a749d05a6e`:
  - `deadhidden`
  - `deadhidden-site-live`
  - `thebiblicalmantruth`
- Live public URL checks passed:
  - `https://deadhidden.org/evil` -> `200`
  - `https://deadhidden.org/evil/` -> `200`, final `https://deadhidden.org/evil`
  - `https://deadhidden.org/evil%5D` -> `308` to `https://deadhidden.org/evil`, final `200`
  - `https://deadhidden.org/evil%29` -> `308` to `https://deadhidden.org/evil`, final `200`
  - `https://deadhidden.org/evil/waitlist` -> `200`
  - `https://deadhidden.org/evil/waitlist%5D` -> `308` to `https://deadhidden.org/evil/waitlist`, final `200`
  - `https://deadhidden.org/evil/waitlist%29` -> `308` to `https://deadhidden.org/evil/waitlist`, final `200`
- Live funnel page checks passed:
  - `https://deadhidden.org/store/evil-household-pack` -> `200`
  - `https://deadhidden.org/store/evil-five-question-card` -> `200`
  - `https://deadhidden.org/store/evil-kjv-passage-map` -> `200`
- Live checkout smoke passed:
  - POST `https://deadhidden.org/api/checkout` with `productSlug=evil-household-pack` returned a live Stripe Checkout session ID beginning `cs_live_`.

## Boundary

No Substack publish, X post, Resend broadcast, manual customer email, refund, DNS change, credential change, webhook setting change, or Stripe product/price mutation was performed.
