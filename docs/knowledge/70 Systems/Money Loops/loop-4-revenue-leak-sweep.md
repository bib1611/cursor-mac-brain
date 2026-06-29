# Loop 4 — Revenue-Leak Sweep
**Money lever:** Protects the entire ~$96K ARR paid catalog (~70 paid products, ~1,465 paid subs) by guaranteeing no paid PDF is free-downloadable at a guessable URL. Today's run proved the leak is LIVE: 18 paid PDFs return 200 + real PDF on both deadhidden.org and www — including the-strong-delusion, familiar-spirits, the loneliness-lie 4-parter. Every dollar the other loops earn leaks here if one file slips back to public. Read-only. The cheapest loop to run.
**Use when:** On a schedule (daily, plus after every store deploy / new-product launch / file move). Any time a PDF is added, moved, or a product file path changes.

## The loop (copy-ready prompt)
> Run `python3 revenue-leak-sweep.py` (read-only; `--json` for machine output). It probes the 18 paid product-file slugs across deadhidden.org and www.deadhidden.org on two paths: `/product-files/<slug>.pdf` must be 403/404, and `/api/serve/<slug>` with no session_id must deny (400/403). A check is a LEAK only if it returns 200 with a real PDF body. Pass gate is binary: leak count MUST be 0. If leaks is 0 and errors is 0, record PASS and stop. On any LEAK, do NOT edit anything — print the leaking URLs, alert Adam, and hand to Codex. On probe errors (timeout), re-run once before trusting a PASS. Stop after one clean pass or one alert.

## Feedback cycle
- **Observe:** Trigger fires (cron or post-deploy). Read the slug list and the two hosts from the script.
- **Choose:** Probe both paths for all 18 slugs x 2 hosts = 72 checks. No selection logic — every paid slug, every run.
- **Act:** GET each URL, follow redirects, sniff the body for `%PDF`. One bounded, reversible step — it only reads.
- **Verify:** Success gate = leak count is 0. The metric: number of paid assets reachable without payment. A check fails only on `200 + PDF body`; 400/403/404/410 all pass.
- **Record:** Append the run timestamp, leak count, error count to the sweep log. On a leak, capture the exact URLs and status codes.
- **Stop:** Terminal states — (1) PASS: leaks=0, errors=0, exit 0, stop. (2) LEAK: leaks>0, exit 1, alert Adam, STOP without changing anything. (3) ERROR: probe timeouts, exit 2, re-run once; if still erroring, flag the run inconclusive and stop. Never loops past one verdict per run.

## Success metric & target
**Metric:** count of paid assets reachable without payment (200 + PDF body).
**Baseline (live today, 2026-06-21):** 36 leaks — all 18 PDFs on the `/product-files/<slug>.pdf` static path, on both hosts. The gated `/api/serve/<slug>` path passes 36/36 (returns 400 "Missing session_id"). So the serve gate is sound; the public static copies are the live hole.
**Target:** 0. Binary. The repo already moved these files to `private/product-files`, but production still serves the public copies — VERIFY a deploy actually ships the removal, then this loop must read 0 on every run.

## Supporting artifact
Runnable read-only checker (built and tested live on 2026-06-21) at `70 Systems/Money Loops/revenue-leak-sweep.py`. Run with `python3 revenue-leak-sweep.py` (stdlib only, no deps; `--json` flag for machine output). Spec it encodes:

**The 18 slugs:** `count-the-number`, `evil-five-question-card`, `evil-kjv-passage-map`, `familiar-spirits`, `feminine-needs-wants-flaws`, `five-weapons-attention`, `if`, `loneliness-lie-part-1`, `loneliness-lie-part-2`, `loneliness-lie-part-3`, `loneliness-lie-part-4`, `north-the-empty-place`, `the-dog-at-the-kings-table`, `the-honest-algorithm`, `the-strong-delusion-print`, `the-strong-delusion`, `the-torment-triage`, `wars-and-rumors-of-wars`.

**Two hosts:** `https://deadhidden.org` and `https://www.deadhidden.org`. Both every run.

**URL patterns (2 per slug per host):** (1) Static `<host>/product-files/<slug>.pdf` MUST be 403/404 (real expected once private: 404). (2) Gated `<host>/api/serve/<slug>` with NO `session_id` MUST deny — verified live: 400 "Missing session_id" (route also gives 403 unpaid/wrong-product, 410 link >7 days, 500 fake session — all denies).

**Pass/fail rule:** A check is a LEAK only when it returns **200 AND a real PDF body** (Content-Type `application/pdf` or first bytes `%PDF`). Redirects followed; a 301/302 to a marketing/404 page is not a leak. Run passes when **leak count == 0**. Exit codes: 0 clean, 1 leak, 2 checker error.

**On a 200 (leak):** ALERT ADAM. Print the exact URL(s). Do NOT auto-change anything — no moves, no commits, no deploys. Fix is a separate approved Codex action.

**Slug-maintenance rule:** new paid product → add its slug to `PAID_FILE_SLUGS` in the script. Source of truth is the keys of `PRIVATE_PRODUCT_FILES` in `src/lib/private-product-files.ts`; VERIFY the script's list matches after any launch. Intentional free samples are listed in `KNOWN_PUBLIC_OK` so the sweep never false-alarms on them.

## Hand-off (what needs Codex / live systems)
- **Reads only:** production HTTP on `deadhidden.org` + `www.deadhidden.org` (store on Vercel). No Stripe/Resend/Gmail, no writes. Safe unattended.
- **Codex / approval (when a leak fires):** Confirmed today — production serves all 18 PDFs publicly while the repo has them in `private/product-files`. Codex must (a) VERIFY the private-files commit is merged and deployed, (b) if a PDF is genuinely back in `public/product-files`, move to `private/` and redeploy, (c) confirm the Vercel build excludes `public/product-files/*.pdf` for paid slugs. Any change to what the public can reach needs Adam's explicit approval before it ships.
- **Scheduling:** wire `python3 revenue-leak-sweep.py` into a daily cron + a post-deploy hook (it exits non-zero on any leak, so it slots into the existing watch harness). Use existing runner — no new infra.
- **One question:** is the private-files fix already deployed, or pending? If pending, this loop's first job after deploy is to flip the baseline from 36 to 0.
