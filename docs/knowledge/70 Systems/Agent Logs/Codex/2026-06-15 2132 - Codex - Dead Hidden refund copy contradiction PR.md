# Dead Hidden Refund Copy Contradiction PR

Date: 2026-06-15 21:32 CDT
Operator: Codex
Repo: `/Users/adamjohnsson/code/deadhidden`

## Adam Instruction

Fix the trust contradiction where the Plain Bible Manual page promised refunds while the store and refund policy say all sales final. Do not change the refund policy. Open a PR. Do not merge.

## Read-Only Findings

Policy/store all-sales-final language confirmed:

- `src/app/refund-policy/page.tsx`: `All sales are final. No refunds. No exceptions.`
- `src/app/store/[slug]/page.tsx`: generic store copy says instant digital delivery, no refunds, all sales final.
- `src/components/StoreContent.tsx`: paid resources are digital products, instant downloads, no refunds.

Conflicting buyer-facing refund promises found:

- `src/app/store/the-plain-bible-manual/page.tsx`
  - `Personal refund guarantee`
  - `Refund anytime`
  - `My personal refund`
  - `If it does not give you the spine to teach the Word to your own house, email me and I will refund it. No form. No screening. You email me, I refund.`
  - `Instant download. Personal refund guarantee. Plain Bible reading.`
- `src/data/products.ts`
  - Dog at the King's Table FAQ: `Refund?`
  - `If you read it and got nothing, write me. I will send the seven dollars back. The work is the point. Not the receipt.`
- `src/app/os/page.tsx`
  - `Refund If It Misses`

## Changes

- `src/app/store/the-plain-bible-manual/page.tsx`
  - Removed refund guarantee language from metadata, trust strip, risk-reversal box, and final CTA note.
  - Replaced with all-sales-final-compatible owner copy:
    - `Read it. Use it. If it does not put Scripture back in your hands, write me. I answer my own mail.`
  - Swapped existing internal Field Files `<a>` to `next/link` so touched-file eslint passes.
- `src/data/products.ts`
  - Replaced the Dog product refund FAQ with `What if it misses?` and the owner-mail promise.
- `src/app/os/page.tsx`
  - Replaced `Refund If It Misses` with `I Answer My Own Mail`.

## Verification

- `rg -n -i "refund anytime|personal refund|refund guarantee|money[ -]?back|moneyback|refund if|will refund|i refund|send the seven dollars back" src`
  - Result: no matches.
- `npx tsc --noEmit`
  - Passed.
- `npm run lint -- src/app/os/page.tsx src/app/store/the-plain-bible-manual/page.tsx src/data/products.ts`
  - Passed.
- `npm run build`
  - Passed. Existing `audit-slugs` warn-only stale-reference warnings still printed, then build passed.

## PR

- PR: `https://github.com/bib1611/deadhidden/pull/46`
- Title: `Fix refund-policy contradiction: align product copy with all-sales-final`
- Branch: `codex/fix-refund-policy-copy`
- Commit: `0f838a2 Fix refund-policy contradiction in store copy`

## Boundaries Kept

- Did not change `src/app/refund-policy/page.tsx`.
- Did not change Stripe, checkout, refund, webhook, or delivery logic.
- Did not merge the PR.

