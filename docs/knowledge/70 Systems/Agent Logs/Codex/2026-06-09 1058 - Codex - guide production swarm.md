# Codex - Guide Production Swarm

Date: 2026-06-09 10:58 CDT

Adam asked Codex to spin up agents and build professional guide/product launch infrastructure for the unfinished guide lane, using Codex, Hermes/Claude Opus 4.8, Grok, and subagents.

## Boundary

Local production work only.

No deploy, public publish, X post, Substack edit, Stripe mutation, customer email send, checkout-link creation, refund, account change, or customer-data print was performed.

## Agents And Model Passes

- Spawned subagent auditors for fulfillment/source inventory, CRO/email, and visual/PDF production.
- The first two initial agents were blocked because the old thread cwd no longer existed. Codex corrected the workdir to `/Users/adamjohnsson/code/deadhidden`.
- Visual/PDF auditor confirmed the right production spine is 6x9 guide PDFs, preferably Markdown to HTML/CSS to PDF.
- Source auditor confirmed `familiar-spirits` is the closest high-leverage finish and `loneliness-lie` is already a multi-part fulfillable product.
- CRO/email auditor confirmed Familiar and Plain Bible were bypassing unified checkout through static Stripe links and that abandoned-cart email needed an approval gate.
- Hermes/Claude Opus 4.8 generated launch copy and follow-up drafts, but hallucinated `$5`; Codex corrected the packet to the verified `$25` price.
- Grok Build confirmed `$25`, warned against overclaiming spiritual outcomes, and recommended keeping the page in text-backed "names the doors" language.

## Local Product Assets Added

Copied verified PDFs into the main repo:

- `/Users/adamjohnsson/code/deadhidden/public/product-files/familiar-spirits.pdf`
- `/Users/adamjohnsson/code/deadhidden/public/product-files/loneliness-lie-part-1.pdf`
- `/Users/adamjohnsson/code/deadhidden/public/product-files/loneliness-lie-part-2.pdf`
- `/Users/adamjohnsson/code/deadhidden/public/product-files/loneliness-lie-part-3.pdf`
- `/Users/adamjohnsson/code/deadhidden/public/product-files/loneliness-lie-part-4.pdf`

Checks:

- Familiar Spirits source PDF was 55 pages, 6x9, WeasyPrint 68.1.
- Familiar Spirits SHA-256 matched source and repo copy: `1b202d62fb177a4782a5c7821a3dfa1f1b50dd1d5c1ded1056da4f97eb49c578`.
- All four Loneliness Lie static backup PDFs matched their Downloads source copies by SHA-256.

## Code Changes

Patched local website code in `/Users/adamjohnsson/code/deadhidden`:

- Added static fulfillment paths for `familiar-spirits` and `loneliness-lie-part-1..4`.
- Removed Familiar Spirits from preorder behavior in success/download/resend/webhook paths while preserving preorder behavior for not-ready products.
- Updated Familiar Spirits product/page copy from preorder to instant PDF.
- Converted Familiar Spirits from hardcoded Stripe Payment Link to unified `/api/checkout` via `BuyButton`.
- Added Familiar Spirits product view tracking and mobile sticky CTA.
- Converted Plain Bible Manual static CTAs and floating CTA away from hardcoded Stripe Payment Links to `/api/checkout`.
- Added checkout cancel URLs with `checkout_abandoned=true&product=<slug>` so client recovery can identify the product.
- Updated browser-side checkout recovery to read the product slug from abandoned checkout state.
- Added `ABANDONED_CART_EMAILS_ENABLED=true` gate; default behavior suppresses server-side abandoned-cart emails.
- Added Familiar Spirits post-purchase follow-up email sequence in `src/lib/email.ts`, gated by `FAMILIAR_SPIRITS_FOLLOWUP_ENABLED=true`.
- Expanded `scripts/audit-store-routing.mjs` to scan static store pages for hardcoded `buy.stripe.com` links.

## Artifacts

- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-guide-production-swarm/GUIDE-STATUS.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-guide-production-swarm/FAMILIAR-SPIRITS-LAUNCH-PACK.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-guide-production-swarm/GO-LIVE-GATES.md`

## Verification

Passed:

- `npm run audit:store-routing`
- `npx tsc --noEmit`
- `npm run build`

Build note: Next.js warned about multiple lockfiles and root inference. Existing `audit-slugs` warn-only stale references remained, but `audit-slugs` passed.

## Not Ready Yet

Do not attach or promote yet:

- `where-the-bible-came-from`: local 26-page PDF says "Review Draft" and explicitly needs cleanup.
- `writers-mechanism`: found Gumroad sales/admin HTML, not the actual seven-day deliverable.
- `uncomfortable-christ`: no exact source/PDF found; do not confuse it with `60_Uncomfortable_Truths_Christian_Women.pdf`.
- `thanksgiving-marriage-vault`: product copy and delivery semantics conflict.
- `the-vault`: needs price/completeness pass before hard promotion.

## Dirty Worktree Note

The Dead Hidden repo was already dirty before this work. Codex did not revert unrelated changes. Existing untracked PDFs `feminine-needs-wants-flaws.pdf` and `five-weapons-attention.pdf` were already present before this lane and are not claimed as new guide-swarm outputs.

