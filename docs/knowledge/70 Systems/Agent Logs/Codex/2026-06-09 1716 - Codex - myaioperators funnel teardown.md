# Codex Receipt - MyAIOperators Funnel Teardown

Time: 2026-06-09 17:16 CDT
Owner: Codex + Fable
Task: Reverse engineer `https://myaioperators.com/` with Fable help.

## What Happened

Adam provided a paid-Facebook URL for `myaioperators.com` and asked to reverse engineer it with Fable's help.

Codex booted from the local ops capsule, used competitor-profiling/CRO framing, fetched the live page, downloaded the public HTML/client chunks, opened the page in Playwright, mapped the buy path, inspected checkout network requests, and saved the source packet. Fable 5 high then audited the evidence packet and produced a funnel/offer judgment.

## Findings

- The page is a Next.js/Turbopack app on Vercel.
- It uses Meta Pixel `984375987720293`, Vercel Analytics, Vercel Speed Insights, and embedded Stripe checkout.
- The visible offer is a `$27` Claude skill called `The Operator's Council`.
- The CTA first opens a `$97` one-time-offer modal before checkout.
- Declining the OTO opens embedded Stripe checkout for `$27`.
- The client bundle exposes a broader ladder: `$27`, `$97`, `$70` upgrade, `$12/mo`, `$19/mo`, and `$297` products.
- Exit-intent captures non-buyers through `POST /api/subscribe` with `source:"exit-intent"`.
- Fable's core recommendation: copy the funnel architecture, not the borrowed-celebrity-authority product concept.

## Artifacts

- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-myaioperators-teardown/SOURCE-PACKET.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-myaioperators-teardown/FABLE-AUDIT.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-myaioperators-teardown/TEARDOWN.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-myaioperators-teardown/raw/home.html`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-myaioperators-teardown/raw/chunks/`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-myaioperators-teardown/raw/checkout-drawer-viewport.png`

## Boundary

No purchase, email signup, account creation, public post, deploy, customer action, Stripe mutation owned by Adam, or external send was performed. One public Stripe checkout session was created on the target site by following the visible buy path to inspect the funnel.
