# BRIEF — Marketing Ops Reporting Agent (Vercel-deployed)

**Owner:** Adam Johnson / Dead Hidden + Biblical Man
**For:** Codex (Mac-side executor)
**Drafted:** 2026-06-13 11:51 CDT by Fable
**Source pain:** every morning Adam pieces together Stripe (×2), Substack (×2), X, Resend, and Vercel across two browsers to know how the business is performing. This brief replaces that 30-minute manual scavenger hunt with one bookmarkable URL: `ops.deadhidden.org`.

---

## Files to read before you touch code
1. `/Users/adamjohnsson/Documents/Obsidian Vault/briefs/2026-06-13-saturday-real-data-snapshot.md` — the data shape this agent must reproduce, verified live today. Every metric in §1–§5 of that file is a cell on the dashboard. Match its structure.
2. `/Users/adamjohnsson/code/deadhidden/.env.local` — pattern for Stripe key naming and existing `RESEND_API_KEY` usage. Do NOT inline secrets in this brief or in code.
3. `/Users/adamjohnsson/.hermes/.env` — already contains `STRIPE_KEY_DH` and `STRIPE_KEY_BM` (live keys, verified working). Reuse via Vercel env vars, not by reading the file at runtime.
4. `/Users/adamjohnsson/code/deadhidden/` — for code conventions (Next.js App Router, Tailwind, oxblood/parchment theme). The agent UI matches the store visually.
5. `~/Documents/Obsidian Vault/CLAUDE.md` — for voice if any copy is needed.

---

## Build target

A new Vercel-hosted Next.js project at `~/code/marketing-ops-agent/`, deployed to a custom subdomain `ops.deadhidden.org` (Cloudflare/IONOS DNS — Adam already manages DNS via Hermes). One bookmarkable URL, mobile-friendly, server-side data pulls cached for ~5 minutes, no auth wall on the dashboard itself (Vercel deploy protection is the gate — Adam adds his Google email to the project).

### One screen, three rows of cards

**Row 1 — Today / Week / Month** (six cards: DH + BM × today/week/MTD revenue with charge counts).
**Row 2 — Audience truth** (combined Substack ARR, paid subs, total subs, X followers, Resend list — five cards).
**Row 3 — Live ladder** (top 10 products by revenue last 30 days across both Stripe accounts — one card with a table).

Each card shows the **pulled-at timestamp** (UTC + CDT) so Adam knows freshness at a glance.

Below the cards: **last-7-days line chart** (combined Stripe revenue, one line, oxblood).

---

## Data sources — what to wire, and how

### 1. Stripe (BOTH accounts — already proven working)
- Env vars in Vercel: `STRIPE_KEY_DH`, `STRIPE_KEY_BM` (Adam pastes from `~/.hermes/.env`).
- Endpoints: `/v1/balance`, `/v1/balance_transactions` (windowed sum, type=charge), `/v1/checkout/sessions` (line_items expand for product breakdown).
- Cache server-side in Vercel's edge runtime, 5-minute TTL via `unstable_cache`.
- Pattern verified working in today's snapshot — the Python script at the bottom of this brief is the canonical reference for the windowing.

### 2. Substack (BOTH publications) — the hardest one
- No official Substack API. Two viable paths:
  - **(a)** Extract `substack.sid` cookie from Adam's logged-in browser session (one-time), store as Vercel env var, use it to call `https://{publication}.substack.com/api/v1/publication_stats` server-side. Cookie expires periodically — needs a "session expired" warning on the dashboard with one-tap re-paste flow.
  - **(b)** Use a headless browser (Browserbase or Playwright on Vercel Fluid Compute) to load the publisher dashboard and scrape the same DOM I scraped today. More fragile but no cookie management.
- **Recommended: (a)** — simpler, faster, ~2 weeks between cookie refreshes per Adam's manual observation.
- Pull URL pattern: `/publish/home` returns the entire stats panel. Specific endpoints to test: `/api/v1/subscriber_counts`, `/api/v1/publication/stats`.
- Metrics needed: annual revenue, paid subs, free subs, today's post performance (likes, comments, opens, new paid).

### 3. X / Twitter (@Biblicalman)
- X API v2: requires bearer token from Adam's X developer account. If he doesn't have one, the agent can fall back to scraping the public profile page (the snapshot got 52.8K from `https://x.com/Biblicalman` DOM today).
- Metric needed for v1: **follower count only**. Posts analytics (impressions, replies, quotes) is v2 — needs paid X API tier or `xurl` automated against logged-in session.

### 4. Resend
- Current `RESEND_API_KEY` in `~/code/deadhidden/.env.local` is **send-only** (403s on `/audiences`, `/emails`, `/domains`). Adam must create a **full-scope account API key** in resend.com → API keys, save as `RESEND_API_KEY_FULL` in Vercel env.
- Endpoints once unblocked: `/audiences` (list + contact counts per audience), `/emails` (last 30d sends with open/click rates), `/broadcasts` (last 10 broadcasts).
- Metric needed: total contacts per audience, last broadcast open rate, ANTI-4X check (count of broadcasts sent in last 24h — alert if >1 on the same subject).

### 5. Vercel Analytics
- Vercel CLI is installed and Adam is authenticated. Use `vercel analytics --json` for `deadhidden.org` and `code.deadhidden.org` projects, server-side from the agent via the Vercel REST API with `VERCEL_TOKEN` env var.
- Metrics: top 10 pages by views last 7 days, specific pageviews for `/store/the-field-files`, `/store/how-to-count-your-bible`, the lead-magnet capture endpoint hits on `code.deadhidden.org`.

---

## Specific findings the agent must surface — caught in today's snapshot
1. **The Field Files bundle has zero sales since launch.** The agent must alert when a launched product registers $0 over 72 hours of being live, since traffic IS hitting the page. Treat this as a probable broken funnel, not low demand.
2. **The Resend DH/BM segments are configured but empty** — Stripe webhook is not populating them. The agent must show a red badge on the Resend card if any named segment is configured but has zero contacts after 7 days of existence.
3. **The Vault is DH's #1 revenue product** ($4,098 / 14 units / 30d) — contradicts CLAUDE.md's "big-ticket rarely moves." The agent must auto-rank top products by revenue, not by CLAUDE.md's narrative.

---

## Acceptance tests (must pass before Adam sees `ops.deadhidden.org`)
1. Load `ops.deadhidden.org` on a phone. All three rows of cards render in under 3 seconds. No card shows `NaN`, `undefined`, or `0` when the underlying source has real data.
2. The Stripe DH "today" card matches what `~/.hermes/.env`-keyed curl returns for the same window — within $1.
3. The Substack BM paid sub count matches what the publisher dashboard shows when Adam opens it manually — within 5 subs.
4. The X follower card shows 52.8K (or whatever the real current count is, not a stale memory).
5. The Resend card shows real audience names and counts, OR a red banner saying "Resend full-scope key needed" if the key still has restricted scope.
6. The "Pulled at" timestamp on every card is a real time from this session, not a hardcoded value.
7. When Adam refreshes the page, the data refreshes within the 5-minute cache window — no manual `?refresh=true` query string required.

---

## What this agent must NEVER do (guardrails)
- Never write to Stripe (no charges, refunds, customer updates).
- Never send a Resend email or modify an audience.
- Never publish to Substack or X.
- Never log API keys to console or to any file.
- Never claim a number is real if the source was unreachable — show `[unreachable]` with the HTTP error code instead.
- Never roll up CLAUDE.md's stale numbers as truth. Pull live or label the cell `[stale: last verified YYYY-MM-DD]`.

---

## Stop-after-step-1 gate
Codex executes Step 1 (read all linked files, confirm env keys are accessible, draft the file structure for the Next.js project, list any blockers in plain English), then **STOPS and reports** before writing a single line of Next.js code. Adam reviews the plan before the build.

This is a hard gate. The previous deferred-build pattern (Codex finishes everything overnight, Adam wakes to surprises) is exactly the wreckage this whole project exists to stop. Step 1 is a 15-minute pass. Steps 2–5 happen only after Adam approves.

---

## Canonical reference — windowed Stripe pull pattern (proven this session)

```python
import os, json, urllib.request, urllib.parse, base64, time
from collections import defaultdict

def stripe_get(key, path, params=None):
    url = f"https://api.stripe.com{path}"
    if params: url += "?" + urllib.parse.urlencode(params, doseq=True)
    req = urllib.request.Request(url)
    req.add_header("Authorization", "Basic " + base64.b64encode(f"{key}:".encode()).decode())
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())

def sum_window(key, gte_ts):
    total_cents = count = 0
    starting_after = None
    while True:
        params = {"created[gte]": gte_ts, "limit": 100, "type": "charge"}
        if starting_after: params["starting_after"] = starting_after
        data = stripe_get(key, "/v1/balance_transactions", params)
        for tx in data["data"]:
            total_cents += tx["amount"]; count += 1
        if not data["has_more"]: break
        starting_after = data["data"][-1]["id"]
    return total_cents, count
```

Time anchors: `today_cdt = unix(2026-06-13 05:00 UTC)`, `week = now - 604800`, `month_mtd = unix(2026-06-01 05:00 UTC)`.

---

## Acceptance — final
When Adam types `ops.deadhidden.org` into his phone and sees real numbers he can trust, with timestamps that prove freshness, this agent is done. Until then, it isn't.

— Fable
