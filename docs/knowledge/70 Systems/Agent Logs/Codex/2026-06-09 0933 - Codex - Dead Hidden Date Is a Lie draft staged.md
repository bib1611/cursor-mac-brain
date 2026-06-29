# 2026-06-09 09:33 CDT - Codex - Dead Hidden Date Is a Lie draft staged

Adam asked Codex to have Hermes edit the Donovan date post in the Dead Hidden Substack editor with stronger conversion CTAs, and said this one should be free as part of a free-plus-paid daily cadence.

Codex used Hermes / Claude Opus 4.8 to generate the final free-post draft, verified the CTA targets, staged the draft in the authenticated Dead Hidden Substack editor through Comet CDP, then converted the four CTA blocks into native Substack button nodes.

Artifacts:

- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-donovan-next-ideas/HERMES-FREE-POST.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-donovan-next-ideas/STAGING-PROOF.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-donovan-next-ideas/DAILY-FREE-PAID-SUBSTACK-WORKFLOW.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-donovan-next-ideas/cdp_stage_deadhidden_date_lie_free_draft_comet.mjs`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-donovan-next-ideas/cdp_set_deadhidden_date_lie_buttons_comet.mjs`

Draft verification:

- Editor URL: `https://deadhidden.substack.com/publish/post/new`
- Document title: `Editing "The Date Is a Lie" - Substack`
- Title: `The Date Is a Lie`
- Subtitle: `The pyramid date only works if Genesis is false before the calculation begins.`
- Body length: `7966`
- Blockquotes: `5`
- Native Substack button nodes: `4`
- Raw URLs visible in body text: `false`
- Paywall markers detected: `false`
- Saved marker visible: `true`

CTA buttons staged:

- `Get the next Dead Hidden post free`
- `Get The Strong Delusion`
- `Start with the $7 Vault Sampler`
- `Stand with FaithWall`

Important routing note:

- Chrome CDP `127.0.0.1:9222` was logged in as `biblicalman@proton.me` and blocked from Dead Hidden publisher pages.
- Comet CDP `127.0.0.1:9223` had the authenticated Dead Hidden editor and should be used for Dead Hidden Substack drafting.

Boundary:

- Draft staged only.
- No publish, send, schedule, X post, email, Stripe mutation, checkout change, paywall insertion, or public action was performed.
