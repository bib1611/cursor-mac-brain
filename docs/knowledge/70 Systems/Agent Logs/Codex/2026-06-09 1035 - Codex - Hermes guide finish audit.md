# 2026-06-09 10:35 CDT - Codex - Hermes Guide Finish Audit

Adam asked Codex to prompt Hermes to audit the website and identify which guides need to be finished.

Codex treated `https://deadhidden.org` as the target site, verified the live sitemap and selected product pages, inspected the local Dead Hidden repo at `/Users/adamjohnsson/code/deadhidden`, checked product catalog state, store routing, static PDF files, and Vercel Blob PDF slug inventory, then prompted Hermes / Claude Opus 4.8 with a read-only audit packet.

Artifacts:

- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-guide-finish-audit/HERMES-PROMPT.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-guide-finish-audit/HERMES-AUDIT-OUTPUT.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-guide-finish-audit/CODEX-SUMMARY.md`

Verified evidence:

- Live sitemap returned `95` store URLs.
- Local `src/data/products.ts` has `95` products.
- Store routing audit passed: `95` slugs, `87` paid, `8` free, checkout via `/api/checkout`, webhook event `checkout.session.completed`.
- Vercel Blob inventory by slug only showed `159` blobs, `140` PDFs, and `95` unique PDF slugs.
- Product slugs with a direct matching blob/static PDF: `77` of `95`.
- Local-only live-404 products: `dead-hidden-study-desk`, `where-the-bible-came-from`.
- Live sitemap product absent from local products: `joel-tillis-church-college-bundle`.
- Selected live product checks returned `200` for `familiar-spirits`, `the-plain-bible-manual`, `christian-soldiers-battle-notes`, `the-vault`, `vault-sampler`, and `feminine-needs-wants-flaws`.
- `the-vault` live title still says `$1,855.81 Inventory for $285`.

Hermes conclusion:

- Do not treat this as a 60-guide writing backlog.
- First priority is `familiar-spirits`: live preorder, no matching PDF, content-vs-fulfillment must be verified.
- Second priority is `loneliness-lie`: multi-part blob/mapping risk.
- Third priority is `the-vault`: stale flagship price/inventory title.
- Then decide on `where-the-bible-came-from`, `thanksgiving-marriage-vault`, `uncomfortable-christ`, and `writers-mechanism`.
- Paid products without `extendedContent` are conversion-copy backlog, not proof the guides are unfinished.

Boundary:

- Read-only audit only.
- No website edits, file edits in the repo, deploys, posts, publishes, sends, Stripe changes, checkout links, customer actions, account changes, or public actions were performed.
