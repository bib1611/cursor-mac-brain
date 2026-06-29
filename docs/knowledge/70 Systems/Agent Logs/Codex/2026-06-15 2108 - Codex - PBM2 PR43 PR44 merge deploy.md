# PBM2 PR43 PR44 Merge Deploy

Date: 2026-06-15 21:08 CDT
Operator: Codex
Repo: `/Users/adamjohnsson/code/deadhidden`

## Adam Instruction

Merge #43 and #44 now. Do not merge #45 yet; hold it until Adam confirms.

## Result

- PR #43 `polly/pbm2-throttle` merged.
  - Merge commit: `15e79bd3c9600f2f7921cdffa67c99b3cab9a6ad`
  - GitHub: `https://github.com/bib1611/deadhidden/pull/43`
- PR #44 `polly/pbm2-conversion` merged.
  - Merge commit: `b4a62ffb4064e4e3fd3d5cfd6ee3440fc4737ad6`
  - GitHub: `https://github.com/bib1611/deadhidden/pull/44`
- PR #45 `polly/pbm2-delivery-harden` not merged.
  - Status at handoff: open and mergeable.
  - Reason: Adam explicitly put it on hold.

## Verification

- Vercel commit status for `b4a62ffb4064e4e3fd3d5cfd6ee3440fc4737ad6`: success.
- Production target: `deadhidden-site-live`.
- Vercel deployment: `https://vercel.com/bib1611s-projects/deadhidden-site-live/95tB7UyXB656YrUKT8pJEPyDK8nf`
- Production URL checked: `https://deadhidden.org/store/plain-bible-2.0`

Read-only smoke checks:

- `GET https://deadhidden.org/store/plain-bible-2.0` returned 200.
- Cold page server HTML shows:
  - Already-own-the-manual bar with `?upgrade=1` link.
  - Two order-bump checkboxes pre-checked.
  - Running total `$37`.
  - Button text `Get the Complete System - $37`.
- `GET https://deadhidden.org/store/plain-bible-2.0?upgrade=1` returned 200.
- Upgrade page server HTML shows:
  - Zero order-bump checkboxes pre-checked.
  - `$15` bundle copy: `Add one for $9. Add both for $15. Save $3.`
  - Button starts disabled as `Choose an add-on`.

## Boundaries Kept

- No Stripe keys touched.
- No buyer email sent.
- No live purchase or test charge fired.
- Existing dirty local file `scripts/pbm2-existing-buyer-email.ts` was left untouched.

