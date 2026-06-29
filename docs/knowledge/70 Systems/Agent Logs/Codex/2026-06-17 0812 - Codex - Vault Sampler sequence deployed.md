# 2026-06-17 0812 - Codex - Vault Sampler sequence deployed

Adam passed Okara's recommendation to deploy a paid-only `$7` Vault Sampler to Vault sequence.

Shipped:

- PR: https://github.com/bib1611/deadhidden/pull/54
- Branch: `codex/vault-sampler-sequence-ship`
- Commit: `37d26f6ede7b1e9c18eb128926d4a0826061f683`
- Merge commit: `db59261538208b85c332d900c1facdae2edccdb4`

Changes:

- Added `sendVaultSamplerUpgradeSequence` in `src/lib/email.ts`.
- Added three emails for paid Vault Sampler buyers:
  - day 1: deploy the four guides, zero Vault sell
  - day 3: name the wider Vault shelf, no price/CTA
  - day 5: direct `$365` Vault offer with one CTA
- Wired only `productSlug === 'vault-sampler'` purchases in `src/app/api/webhook/route.ts`.
- Did not touch `/api/email-signup`, lead magnet delivery, or free opt-in paths.

Production deploy checks:

- `Vercel - deadhidden`: success, https://vercel.com/bib1611s-projects/deadhidden/Fp5ecEEm16h2Va1AvPFekqRGWs25
- `Vercel - deadhidden-site-live`: success, https://vercel.com/bib1611s-projects/deadhidden-site-live/3Zzgo8XZtXy27oczdkZBKnMNsr4c
- `Vercel - thebiblicalmantruth`: success, https://vercel.com/bib1611s-projects/thebiblicalmantruth/CgMQYk9WR8M3heZn1QcGgUPb9RRZ

Verification:

- Clean ship worktree from current `origin/main`.
- `npm run lint -- src/lib/email.ts src/app/api/webhook/route.ts src/app/api/email-signup/route.ts` passed.
- `npm run build` passed with existing warn-only stale slug audit warnings.
- `origin/main` contains `VAULT_SAMPLER_SLUGS`, `sendVaultSamplerUpgradeSequence`, `vaultSamplerUpgradePromise`, and `flow: vault_sampler_to_vault`.
- Live `https://deadhidden.org/store/vault-sampler?deploy_check=db59261` returned sampler-page content.

Boundary:

- No Stripe price/product change.
- No checkout session created.
- No buyer email sent manually.
- No Resend broadcast/manual send.
- No free opt-in automation change.
- No Substack/X publish.
