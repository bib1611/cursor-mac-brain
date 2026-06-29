# Codex - Facebook FaithWall Competitive Check

Date: 2026-06-08 18:25 CDT
Agent: Codex

## Request

Adam flagged a Facebook share as a possible app-concept copycat threat and asked what they are doing.

Original share:

`https://www.facebook.com/share/1KraWZM5UK/?mibextid=wwXIfr`

## What Was Checked

Codex resolved the share through a public Facebook redirect:

`https://www.facebook.com/61579130018040/posts/122159604704971000/?mibextid=wwXIfr`

Public Facebook metadata identified the page/post as `Bible Word Study`.

Codex checked Apple's official lookup metadata for:

- `Bible Word Study`, App Store ID `6747986444`
- `Scripture First: Bible Lock`, App Store ID `6762501494`

Codex also checked local FaithWall evidence in:

- `/Users/adamjohnsson/code/deadhidden/src/data/products.ts`
- `/Users/adamjohnsson/code/deadhidden/public/polsia/faithwall-waitlist.html`
- `/Users/adamjohnsson/code/deadhidden/public/polsia/faithwall-beta.html`
- `/Users/adamjohnsson/code/deadhidden` git history for FaithWall commits

## Finding

The Facebook post itself is for `Bible Word Study`, a Bible-language and AI study app by Gabriel Jacobson / JCBSN LLC.

The same developer's `Scripture First: Bible Lock` is the closer FaithWall overlap. Apple's lookup metadata says it was released 2026-05-15 and uses the basic promise: pick distracting apps, pick or build a Bible reading plan, read first, then apps unlock.

FaithWall evidence predates that release in public repo history:

- 2026-05-02: FaithWall landing/homepage/nav/sitemap commits
- 2026-05-07: FaithWall iOS waitlist, dashboard, onboarding sequence, Polsia pages, and extension commits
- 2026-05-08: FaithWall products wired to Stripe
- 2026-06-01: FaithWall beta funnel page commit

Timeline boundary: FaithWall existed publicly before `Scripture First` released, but the exact FaithWall beta copy around a morning wall gating the phone until Scripture was read was committed after their App Store release. The safe current claim is direct competitor / same lane / adjacent positioning, not proven theft.

## Durable Local Brief

`/Users/adamjohnsson/Documents/Codex/2026-06-08/these-guys-are-trying-to-steal/2026-06-08-facebook-faithwall-competitive-check.md`

## Boundary

Read-only investigation only.

No posting, messaging, account changes, payments, refunds, deployments, credential changes, or public claims were made.

