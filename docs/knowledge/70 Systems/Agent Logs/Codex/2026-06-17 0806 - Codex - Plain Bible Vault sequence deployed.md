# 2026-06-17 0806 - Codex - Plain Bible Vault sequence deployed

Adam asked for the Plain Bible Manual website and email-sequence changes to be deployed, not left local.

Shipped:

- PR: https://github.com/bib1611/deadhidden/pull/53
- Branch: `codex/pbm-vault-sequence-ship`
- Commit: `920d7c39b60f489bb7c46fba958fdad54aa4fe05`
- Merge commit: `4bb33411946900f87a94e6f59dddac9e7b93a9fd`

Production deploy checks:

- `Vercel - deadhidden`: success, https://vercel.com/bib1611s-projects/deadhidden/5gYYPjWAUk16YeJncfAH4Dhiczu1
- `Vercel - deadhidden-site-live`: success, https://vercel.com/bib1611s-projects/deadhidden-site-live/C36GidXUTUtq7b8c7XCBoURFeVax
- `Vercel - thebiblicalmantruth`: success, https://vercel.com/bib1611s-projects/thebiblicalmantruth/9PHaaSRfGkwRHXV1jvNS8Hj6p2WV

Verification:

- Clean ship worktree from current `origin/main`.
- `npm run lint -- src/lib/email.ts src/app/api/webhook/route.ts src/app/store/the-plain-bible-manual/page.tsx` passed.
- `npm run build` passed with existing warn-only stale slug audit warnings.
- Live `https://deadhidden.org/store/the-plain-bible-manual?deploy_check=4bb3341` contains `Buy the Plain Bible Manual`.
- Live page does not contain `Get The Field Files bundle`, `Want all four`, or the product-page Field Files cross-sell URL.

Boundary:

- No Stripe price/product change.
- No checkout session created.
- No buyer email sent manually.
- No Resend broadcast/manual send.
- No Substack/X publish.
