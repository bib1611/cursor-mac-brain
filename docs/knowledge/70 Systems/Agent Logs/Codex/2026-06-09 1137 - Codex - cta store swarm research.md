# Codex Receipt - CTA Store Swarm Research

Time: 2026-06-09 11:37 CDT  
Thread: `/Users/adamjohnsson/Documents/Codex/2026-06-09/i-need-you-to-launch-a`  
Boundary: research and local artifact creation only.

## Adam Request

Launch a swarm to study the best CTA writers on Substack and X, specifically Kristina God and Tim Denning, map the store, research best converting buttons to use in the editor, and make every workflow optimize CTA.

## Actions

- Spawned five research agents:
  - Kristina God CTA teardown: `019ead37-e25c-73a0-acf6-3b0f90979de3`
  - Tim Denning CTA teardown: `019ead37-f1dd-79c1-8690-979669ec0727`
  - Broader creator CTA survey: `019ead38-03ba-7851-92c1-ea044e904b65`
  - Dead Hidden store map: `019ead38-1448-78a1-a645-b33b0a4ed3b0`
  - Button/editor CRO lane: `019ead38-242b-7df3-8f7e-2185d5136d8d`
- Researched public Substack/X/editor CTA patterns.
- Audited local Dead Hidden store code read-only.
- Ran read-only local audits:
  - `node scripts/audit-slugs.mjs`
  - `node scripts/audit-store-routing.mjs`
- Wrote ops packet and user-facing output.

## Key Findings

- CTA architecture should be: public argument -> earned CTA -> verified offer -> fallback -> reply prompt -> X self-reply link.
- Strong local offers: Plain Bible Manual, How To Study, Strong Delusion, Familiar Spirits, Vault Sampler, Essential Arsenal, Torment Triage, FaithWall, Dead Hidden Pro.
- Vault should not be hard-promoted with price language until price/copy/completeness cleanup.
- IF CTA should avoid confusing PWYW language until checkout behavior is aligned.
- Store has 95 slugs, 87 paid, 8 free; store routing passed through `/api/checkout`.
- Slug audit passed, with 15 warn-only stale refs in `src/hooks/useCategoryIntent.ts`.
- Many products still lack product-specific `ctaText`, causing generic button fallback.

## Artifacts

- Ops packet: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-cta-store-swarm/CTA-STORE-SWARM-PACKET.md`
- User output: `/Users/adamjohnsson/Documents/Codex/2026-06-09/i-need-you-to-launch-a/outputs/cta-store-swarm-research.md`

## No Live Actions

No Substack publish, schedule, email send, X post, Stripe/customer action, deploy, product edit, account setting change, or live workflow mutation was performed.

