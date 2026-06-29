# 2026-06-16 18:57 CDT - Codex - Cursor CRO Homepage Sampler PR

## Request

Adam asked whether Cursor could improve the website, then said to go for it.

## Action

Codex made a small mobile-first CRO pass in clean worktree:

`/tmp/deadhidden-cursor-cro`

Branch:

`codex/cursor-cro-pass`

Commit:

`25682f24f8a098100aeaab470ee97eb988500038`

PR:

`https://github.com/bib1611/deadhidden/pull/52`

Changed files:

- `src/components/cro/HomepageBody.tsx`
- `src/components/cro/StickyBottomBar.tsx`
- `src/app/store/[slug]/page.tsx`

Changes:

- Homepage starter card now lists the four paid sampler files instead of hiding the manifest.
- Homepage sampler copy now matches fulfillment: `Warrior's Bible Blueprint`, not `Wind-Watcher Checklist`.
- Mobile sticky bar now matches the homepage primary offer: `Starter Pack`, `$7`, `GET THE FOUR`, linking to `/store/vault-sampler`.
- Vault Sampler page `Who this is for` copy now says `reader` and `household`, not male-only copy.

## Verification

Commands passed:

```text
npx tsc --noEmit
npm run lint -- src/components/cro/HomepageBody.tsx src/components/cro/StickyBottomBar.tsx 'src/app/store/[slug]/page.tsx'
npm run build
```

Build note:

- `npm run build` passed.
- `audit-slugs` still reports existing warn-only stale references in `src/hooks/useCategoryIntent.ts`.

Browser mobile QA:

- URL: `http://127.0.0.1:3021/?cursor_cro_final=2`
- Viewport: `390x844`
- Homepage rendered with no framework overlay.
- Sampler manifest visible on mobile.
- Sticky CTA showed `Starter Pack`, `$7`, and `GET THE FOUR`.
- Sticky CTA navigated to `http://127.0.0.1:3021/store/vault-sampler`.
- Sampler page loaded and showed `THE VAULT SAMPLER`.
- Sampler page showed `This is for the reader...`.
- Sampler page no longer showed `This is for the man...`.
- Sampler page showed `THE WARRIOR'S BIBLE BLUEPRINT`.
- Only console warning observed: existing Next smooth-scroll warning.

Screenshot proof:

- `/tmp/deadhidden-cursor-cro-final-mobile.png`
- `/tmp/deadhidden-cursor-cro-final-sampler-mobile.png`

PR status:

- PR #52 is open, non-draft, mergeable.
- Vercel preview checks passed for `deadhidden`, `deadhidden-site-live`, and `thebiblicalmantruth`.

## Side Effects

No merge, no production deploy, no checkout session, no Stripe change, no charge, no buyer email, no Substack/X publish.
