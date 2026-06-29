# 2026-06-21 1301 - Codex - private paid PDF delivery repair

Task: Move paid PDFs out of public static paths and update `/api/serve/[slug]` to deliver them privately.

Changed:
- Moved 18 paid/static PDFs from `/Users/adamjohnsson/code/deadhidden/public/product-files/` to `/Users/adamjohnsson/code/deadhidden/private/product-files/`.
- Left public non-paid/support files in place:
  - `evil-five-question-card-sample-v1.pdf`
  - `familiar-spirits-manuscript.md`
  - `household-drift-audit.pdf`
  - `product-cover-the-dog-at-the-kings-table.jpg`
- Added `/Users/adamjohnsson/code/deadhidden/src/lib/private-product-files.ts`.
- Updated `/Users/adamjohnsson/code/deadhidden/src/app/api/serve/[slug]/route.ts` to read private PDFs only after Stripe session authorization.
- Updated `/Users/adamjohnsson/code/deadhidden/src/app/api/resend-downloads/route.ts` to send secure `/api/serve/<slug>?session_id=...` links instead of direct static/blob links.
- Updated `/Users/adamjohnsson/code/deadhidden/next.config.ts` with `outputFileTracingIncludes` for `/api/serve/[slug]` and `/api/resend-downloads`.
- Added `/Users/adamjohnsson/code/deadhidden/scripts/assert-private-product-files.ts`.
- Updated the store goal-loop ledger/report under `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/store-goal-loop/`.

Verification:
- `npm run audit:store-routing` passed.
- `npx tsx scripts/assert-pbm2-delivery-fallback.ts` passed.
- `npm run build` passed.
- `.next` trace files include all 18 private PDFs for `/api/serve/[slug]` and `/api/resend-downloads`.
- `npx tsx scripts/assert-private-product-files.ts` passed.
- Local built server on `http://localhost:3021` verified:
  - `/product-files/count-the-number.pdf` returned 404.
  - `/product-files/evil-five-question-card.pdf` returned 404.
  - `/product-files/the-strong-delusion.pdf` returned 404.
  - `/product-files/evil-five-question-card-sample-v1.pdf` still returned 200.
  - `/api/serve/count-the-number` without a session returned 400 `Missing session_id`.
  - `/store/the-vault` and `/vault` returned the Vault page.

Boundary:
- No deploy, live Stripe checkout/session creation, live charge, refund, customer mutation, webhook replay, email send, DNS change, public post, Linear/Notion write, or account-setting change happened.

Remaining gap:
- Production `https://www.deadhidden.org/product-files/*.pdf` will stay public until this repo change is deployed.
- A valid paid-session download test still needs an approved existing session ID or an approved live test purchase.
