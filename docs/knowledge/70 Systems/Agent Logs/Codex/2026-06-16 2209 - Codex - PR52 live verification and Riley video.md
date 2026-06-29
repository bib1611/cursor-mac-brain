# 2026-06-16 22:09 CDT - Codex - PR52 live verification and Riley video

Adam asked Codex to make sure the Dead Hidden homepage CRO work fully took and to watch Riley Brown's Cursor video.

Site action:

- Verified PR #52 `Improve homepage sampler conversion path` was open, non-draft, mergeable, and green.
- Merged PR #52 into `main`.
- Merge commit: `404ed81f4f289532118215282fb6c09f9a57796a`.
- Vercel production checks succeeded on the merge commit for `deadhidden`, `deadhidden-site-live`, and `thebiblicalmantruth`.
- Chrome production verification passed with cache-busting URLs.

Live proof:

- Homepage now shows the starter pack with `Warrior's Bible Conquest`, `King's Marriage Manual`, `Modern Demons in 7 Days`, and `Warrior's Bible Blueprint`.
- The stale paid-slot `Wind-Watcher Checklist` no longer appears in the paid starter pack. It still appears only in the free preview pack area.
- Homepage sticky/start CTA points to `/store/vault-sampler` and says `GET THE FOUR`.
- Vault Sampler page uses reader/household-safe copy and no longer uses the male-only line.
- Direct checkout route `https://deadhidden.org/checkout?slug=vault-sampler` returns HTTP 303 to Stripe Checkout.

Screenshots:

- `/tmp/deadhidden-pr52-chrome-after-merge-home.png`
- `/tmp/deadhidden-pr52-chrome-after-merge-sampler.png`

Riley video:

- Source: `https://www.youtube.com/watch?v=LSpEP9N_7iY`
- Title: `SpaceX Just Bought Cursor for $60B. It’s About to Take OVER.`
- Channel: Riley Brown.
- Transcript captured locally at `/tmp/riley-cursor-video/transcript.txt`.
- Practical takeaway: Cursor is moving toward a general agent platform with in-app browser, multi-model routing, design mode, automations/customizations, project chats, and portable memory/skills import. For Dead Hidden, use Cursor as an additional UI/design and agent-workbench surface, while keeping Codex as the canonical live-ops executor with receipts, checkout/email/deploy guardrails, and ops-capsule continuity.

No Stripe key change, price change, checkout test purchase, charge, buyer email, Substack/X publish, or refund-policy change was performed.
