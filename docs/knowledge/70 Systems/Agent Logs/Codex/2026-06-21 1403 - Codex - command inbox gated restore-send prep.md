# 2026-06-21 14:03 CDT - Codex - Command inbox gated restore-send prep

Task: pick up the Codex command inbox handoff covering the paid-PDF privacy fix, campaign ground-truth numbers, and the gated Biblical Man restore-send prep.

## PDF privacy fix

- Local commit: `b184063` (`Serve paid PDFs from private storage`) on branch `audit/store-seo-pricing-fixes`.
- Staged/committed only the privacy-fix paths; unrelated dirty files were left alone.
- Moved 18 paid PDFs from `/Users/adamjohnsson/code/deadhidden/public/product-files/` to `/Users/adamjohnsson/code/deadhidden/private/product-files/`.
- Updated `/api/serve/[slug]` to read private PDFs after Stripe session authorization.
- Updated `/api/resend-downloads` to send `/api/serve/<slug>?session_id=...` links.
- Added malformed slug guard and clean invalid-session `403`.
- Added `scripts/assert-private-product-files.mjs` and wired it into `prebuild`.

Verification:

- `node scripts/assert-private-product-files.mjs` passed.
- `npm run audit:store-routing` passed.
- `npx tsx scripts/assert-pbm2-delivery-fallback.ts` passed.
- `npm run build` passed.
- Local built server on `http://localhost:3021` returned paid static PDFs `404`, public sample PDF `200`, bad `session_id` `403`, malformed slug `400`.
- `.next` trace files included 18 private PDFs for `/api/serve/[slug]` and `/api/resend-downloads`.

Production note: no deploy or CDN purge happened, so production public PDF URLs remain live until this commit is shipped.

## Campaign ground truth

Sources:

- `/Users/adamjohnsson/Downloads/bm-email-off-reply-watch.sqlite3`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-20-bm-subscriber-delivery-audit/`

Results:

- Paid email-off segment: 164 paid-access subscribers.
- Live export paid denominator: 1,244 paid-access rows; 164 email off = 13.18%.
- Paying-only denominator excluding comp/gift/free-trial: 1,216 rows; 158 email off = 12.99%.
- SQLite paid reply outcomes: ON 5, OFF 4, OTHER 5, BOUNCE 3, HERE 0, QUIET 0.
- Dormant-free segment: 3,703; sent 300; pending 3,403; bounces 3/300 = 1.0%.
- Delivery audit list sizes: A 164, B 3,703, C paid-access 164, C paying-only 158, C paying-subscribers 158.

## Restore-send prep

Artifacts:

- Ready batch: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/bm-restore-send/2026-06-21-restore-send-ready-quiet-batches.csv`
- Holds/exclusions: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/bm-restore-send/2026-06-21-restore-send-holds-and-exclusions.csv`
- Rendered email: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/bm-restore-send/2026-06-21-restore-send-rendered-email.txt`
- Summary JSON: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/bm-restore-send/2026-06-21-restore-send-summary.json`

Prepared:

- 150 quiet paid-email-off recipients ready, capped as two 75-recipient batches.
- Held/excluded: 3 bounces, 4 OFF, 2 OTHER-only support/confusion replies, 5 ON readers held because they already received Sam help replies and another email would be a third touch inside 48h.
- Read-only Gmail lookup resolved the paid-campaign bounces as `jake.mcdowell@ipaper.com`, `brentv@usfamily.net`, and `vcserbia@gmail.com`.
- Billing/source resolution from the Substack export: 126 direct Substack annual, 29 direct Substack monthly, 3 iOS app monthly, 3 gift, 3 comp, 0 store/deadhidden.org Stripe-billed.
- Manage-delivery link resolved to `https://substack.com/settings`.
- Publication email test URL recorded as `https://biblicalman.substack.com/account/email-test`.
- Server-side flip resolution: no safe publisher-side flip path verified; treat restoration as reader-side through Substack settings unless Adam verifies a specific logged-in Substack subscriber action.

Bridge update:

- Appended the packet to `/Users/adamjohnsson/.codex-bridge/shared/OUTBOX.md`.

Boundary:

No email send, draft creation, label/archive/delete/spam/unsubscribe action, Substack/customer/list/account-setting mutation, Stripe/customer/money mutation, production deploy, Vercel purge, public post, Linear/Notion write, or credential change happened.
