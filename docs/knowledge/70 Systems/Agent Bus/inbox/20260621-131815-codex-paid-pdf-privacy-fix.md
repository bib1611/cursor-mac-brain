---
type: agent-bus-task
id: 20260621-131815-codex-paid-pdf-privacy-fix
created: 2026-06-21 13:18:15
source: claude-code
requested_agent: codex
priority: high
status: inbox
---

# Ship the paid-PDF privacy fix (independent audit punch-list)

## Context

This is a hand-off from Claude Code after an independent, read-only security
audit of YOUR in-progress change on branch `audit/store-seo-pricing-fixes` in
`/Users/adamjohnsson/code/deadhidden` (moving 18 paid PDFs from
`public/product-files/` to `private/product-files/` + gated `/api/serve`).

**Your code design is correct and was credited.** The audit confirmed: the
entitlement gate is verified server-side against Stripe (paid + 7-day + slug
match), no path traversal is possible (fixed-dictionary map), every fulfillment
path (webhook, success, resend, download, emails) emits only gated
`/api/serve/<slug>?session_id=<id>` links, the helper is a true single source of
truth (18 slugs ↔ 18 files ↔ resend gate), and `outputFileTracingIncludes` is
valid and build-verified (the `.nft.json` traces all 18 PDFs into both
functions). **Do NOT re-derive or re-copy the migration — it is internally
complete.**

The problem is that the fix is **half-shipped** and has an exposure tail the
code cannot touch. Execute the steps below in order. This task is NOT a request
to re-architect anything.

## Boundary

Allowed: stage/commit on `audit/store-seo-pricing-fixes`, wire the existing
guard script into prebuild, the 500→403 + slug-validation edits, run the build
locally, open/merge the PR, trigger the Vercel deploy, purge the Vercel CDN
cache, and re-verify with read-only curl. **Get Adam's explicit OK before:**
merging to the production branch, the production deploy itself, and any git
history rewrite/force-push. Do not change Stripe, customer, or payment state.
Do not touch the GitHub repo visibility (owner-only; Adam is handling that
separately — see step 0).

## Steps (in order)

0. **[OWNER-ONLY — Adam] Repo visibility.** `bib1611/deadhidden` is PUBLIC and
   the 18 paid PDFs are recoverable from git history across 18 commits. The
   `biblicalman1611` collaborator account has push but NOT admin, so it cannot
   flip visibility. Adam is making it private from the `bib1611` owner account.
   Do not block your steps on this, but do NOT consider the history exposure
   closed until it is private (or history is scrubbed).

1. **Commit `private/` — this is the deploy trap.** `private/product-files/` is
   currently untracked (`?? private/`). Vercel builds only the committed tree;
   if it is not committed, `outputFileTracingIncludes` traces zero PDFs and
   EVERY paid download 503s in production — a full fulfillment outage.
   Run `git add private/product-files/` and confirm
   `git ls-files private/product-files/ | wc -l` prints **18** before any deploy.

2. **Wire your guard into prebuild.** You already wrote
   `scripts/assert-private-product-files.ts` (asserts all 18 slugs have a private
   file AND no public copy) and `scripts/verify-local.sh` — exactly the right
   regression guard — but `package.json` prebuild only runs `audit-slugs.mjs`, so
   it never fires. Add `assert-private-product-files.ts` to prebuild (or CI) so a
   missing private file or a re-leaked public copy FAILS THE BUILD instead of
   503-ing a paying buyer.

3. **Harden the gated endpoint (small, do now):**
   - `src/app/api/serve/[slug]/route.ts`: invalid/unknown/unpaid `session_id`
     currently throws into the catch (~line 184) and returns **500**; make it a
     deterministic **403**. Wrap the `stripe.checkout.sessions.retrieve` lookup.
   - Add slug validation at route entry (~line 45):
     `if (!/^[a-z0-9-]+$/.test(slug)) return 400` — kills the raw-slug
     Content-Disposition header-injection surface (line 19) a Vault buyer could
     probe. Not exploitable for file read today; defense-in-depth.

4. **Commit, build, get Adam's OK, deploy.** `npm run build` must pass with the
   new prebuild guard. Then (with Adam's approval) merge to the production branch
   and let Vercel build + deploy. Only the deploy changes live bytes.

5. **Purge CDN + verify — the fix is NOT done until this is green.** A redeploy
   alone does not evict edge/browser cache (responses showed
   `x-vercel-cache: HIT`) and old immutable `*.vercel.app` deployments still
   contain the bytes. After deploy: explicitly purge the Vercel CDN cache, then
   re-curl EVERY paid slug on BOTH hosts and require 404/403:
   - `for s in count-the-number evil-five-question-card evil-kjv-passage-map familiar-spirits feminine-needs-wants-flaws five-weapons-attention if loneliness-lie-part-1 loneliness-lie-part-2 loneliness-lie-part-3 loneliness-lie-part-4 north-the-empty-place the-dog-at-the-kings-table the-honest-algorithm the-strong-delusion-print the-strong-delusion the-torment-triage wars-and-rumors-of-wars; do for h in deadhidden.org www.deadhidden.org; do echo "$h/$s -> $(curl -sI https://$h/product-files/$s.pdf -o /dev/null -w '%{http_code}')"; done; done`
   - Also confirm `https://www.deadhidden.org/private/product-files/familiar-spirits.pdf` returns 404 (private dir not publicly served) AND that a real gated buy-flow download still works (regression check that you didn't break fulfillment).

6. **After live hole is closed — history.** Once private/CDN are clean, if Adam
   wants the bytes permanently gone, scrub history
   (`git filter-repo --path public/product-files --invert-paths` or BFG) and
   force-push (Adam approval required). Making the repo private (step 0) is the
   faster bleed-stop and may be sufficient.

## Open question for Adam (do not guess)

`public/kopher-breakdown.pdf` (153KB, "KOPHER — The Word Hidden in Your Bible")
sits at site root with ZERO code references and no fulfillment path. Filesystem
evidence says it is free/unwired, but confirm with Adam it was NEVER sold. If it
was sold, move it to `private/` + add to the catalog + the private map. The other
two leftover public PDFs are confirmed free (the `evil-five-question-card-sample`
must stay public — the lead-magnet email links it; `household-drift-audit.pdf` is
a free lead magnet, now orphaned).

## Report back

Write a Codex receipt with: the commit SHA, prebuild-guard wired (yes/no), the
500→403 + slug-validation diffs, the deploy URL, CDN purge confirmation, and the
full curl matrix output proving every slug is 404/403 on both hosts. The leak is
only closed when that matrix is green.
