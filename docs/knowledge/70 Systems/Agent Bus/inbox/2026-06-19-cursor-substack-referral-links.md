# Cursor → Codex: Substack referral-safe links

**Date:** 2026-06-19  
**Branch:** `cursor/substack-referral-links`  
**Risk:** Low (copy-only href changes, no auth/commerce)

## What changed

Updated outbound Substack links in:

- `src/components/Footer.tsx`
- `src/app/publications/page.tsx`

Bare `deadhidden.substack.com` / `biblicalman.substack.com` URLs replaced with `open.substack.com/pub/...?r=2t2o3r` plus site UTMs. Biblical Womanhood link already had `r=2t2o3r`; added matching UTMs.

## Why

Public endpoint review found site footer/publications links dropped Substack referral attribution. `open.substack.com` preserves `r=` and `utm_*` through Substack redirects.

## Checks run

- `read_lints` on both edited files — clean
- No build/test run (href-only diff)

## Codex verify

1. Merge PR after spot-checking live footer + `/publications` links
2. Optional follow-up: same pattern on `where-to-begin`, store pages, email templates (out of scope for this PR)
