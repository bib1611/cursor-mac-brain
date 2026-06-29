# 2026-06-21 1254 - Codex - Dead Hidden store goal loop

Task: Run a bounded Codex goal loop against the Dead Hidden store, checkout guardrails, and fulfillment/delivery path.

Artifacts:
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/store-goal-loop/2026-06-21-store-checkout-fulfillment-user-stories.csv`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/store-goal-loop/2026-06-21-store-checkout-fulfillment-report.md`

Code change:
- `/Users/adamjohnsson/code/deadhidden/next.config.ts`
- Removed stale `/store/the-vault -> /store/plain-bible-2.0` redirect.
- Removed stale `/vault-start -> /store/plain-bible-2.0` redirect.
- Changed `/vault` to redirect to `/store/the-vault`.

Checks:
- Live route/API smoke: `/`, `/store`, `/store/plain-bible-2.0`, `/store/fathers-day-household-shelf`, `/api/checkout`, `/api/pbm2-checkout`, `/api/webhook`, `/api/success`, and `/api/serve/count-the-number`.
- `npm run audit:store-routing` passed: 105 slugs, 97 paid, 8 free, checkout pipe `/api/checkout`, webhook event `checkout.session.completed`.
- `npx tsx scripts/assert-pbm2-delivery-fallback.ts` passed.
- `npm run build` passed after patch.
- Local built server on `http://localhost:3021` confirmed `/store/the-vault`, `/vault`, `/vault-start`, and malformed API guards.

Open defect:
- `DH-DEF-001`: paid PDFs are directly reachable at public static `/product-files/*.pdf` URLs. Live HEAD returned 200 for `count-the-number.pdf`, `evil-five-question-card.pdf`, and `the-strong-delusion.pdf`; local built HEAD also returned 200 for `count-the-number.pdf`.
- Not patched in this loop because `/api/serve/[slug]` currently fetches those same public paths for authorized delivery. Safe repair needs private storage or private bundled assets plus a serve-route rewrite and paid-session retest.

Boundary:
- No deploy, Stripe checkout session creation, live charge, refund, customer mutation, webhook replay, email send, DNS change, public post, Linear/Notion write, or account-setting change happened.
