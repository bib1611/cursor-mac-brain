# 2026-06-14 08:10 CDT - Codex - MarketingSecrets trial research and brain seed

Adam asked Codex to research MarketingSecrets.ai and use the 14-day trial to the max for Dead Hidden / Biblical Man / FaithWall.

Research:

- Public research used live web sources for MarketingSecrets.ai/MarketingSecrets.AI, AI Secrets Challenge, Marketing Secrets archive, Google Play listing, and prior public review pages.
- Finding: public official MarketingSecrets.ai material is limited from the unauthenticated web; the strongest live proof is Adam's logged-in screenshots plus MCP discovery.
- Finding: the platform appears best used as a marketing memory + campaign workspace, not as a source of truth for money, customers, publishing, or deploys.
- Trial risk: if the trial started on 2026-06-14, day 14 is 2026-06-28. Billing date still must be verified in the MarketingSecrets / ClickFunnels Billing tab.

Created:

- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-14-marketingsecrets-trial/MARKETINGSECRETS-TRIAL-OPERATING-PLAN.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/bin/ms-brain`

MarketingSecrets Brain writes:

- Added 17 compact, non-secret memories across `business`, `preferences`, `projects`, `audience`, and `misc`.
- Seeded brand voice, audience, active offer/campaign facts, trial operating rule, X/Substack/public-copy guardrails, and live-verification boundaries.
- Verified `memory_search` for `Honest Algorithm` and `FaithWall`.
- Verified `memory_get_recent` returned the new trial and audience facts.

Ops update:

- Added an active MarketingSecrets 14-day trial sprint item to `/Users/adamjohnsson/.deadhidden-os/ops/QUEUE.md`.

Verification:

- `/Users/adamjohnsson/.deadhidden-os/ops/bin/ms-brain search 'Honest Algorithm' 3` returned the seeded Honest Algorithm project facts.
- `/Users/adamjohnsson/.deadhidden-os/ops/bin/ms-brain recent 4` returned recent MarketingSecrets memories.
- `ms-brain` is executable and reads the API key from Keychain service `MarketingSecretsMCP`.

Boundary:

- No public post, email, customer action, Stripe/billing mutation, deploy, Telegram webhook change, Linear/Notion mutation, or external send was performed.
- Hermes gateway was not restarted because `hermes status` showed two active sessions.
- MarketingSecrets memory was treated as context only, not canonical truth.
