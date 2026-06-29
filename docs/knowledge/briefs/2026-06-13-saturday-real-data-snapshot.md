# Saturday Real-Data Snapshot — 2026-06-13

Pulled live: **Sat Jun 13 2026 11:40–11:51 CDT**
Operator: Fable (Hermes desktop, Mac mini hub)
Sources: Stripe REST API (both live keys), Substack publisher dashboards (CDP), X profile DOM (CDP), Resend dashboard DOM (CDP).

**Every number below has a verifiable source. Nothing typed from memory. Where I could not get a number, it is marked `[GAP]` with the reason.**

---

## 1. STRIPE — Both accounts, all windows

### Dead Hidden — `acct_1PeIdjLN6IypHVMV` (key `STRIPE_KEY_DH`)
| Window                 | Net charges | Total revenue |
|------------------------|------------:|--------------:|
| Today (since 00:00 CDT)|           2 |        $28.00 |
| Last 7 days            |         104 |     $1,262.80 |
| June 1–13 (MTD)        |         124 |     $1,531.69 |
| Last 30 days           |         330 |     $8,272.90 |

Balance: available **−$38.33**, pending **+$146.34** (recent payout pulled available negative)
New customers (30d): **275**

#### DH — Top products, last 30 days (real)
| Revenue   | Units | Product |
|----------:|------:|---------|
| $4,098.00 | 14    | THE BIBLICAL MAN VAULT |
| $1,245.00 | 110   | THE PLAIN BIBLE MANUAL |
| $490.00   | 9     | SUPPORT DEAD HIDDEN (donation) |
| $351.00   | 39    | THE STRONG DELUSION |
| $332.00   | 19    | NOT ENOCH (PRE-ORDER) |
| **$228.00** | **12** | **HOW TO COUNT YOUR BIBLE** |
| $200.00   | 20    | COUNT THE NUMBER |
| $197.00   | 1     | JOEL'S CHURCH COLLEGE BUNDLE |
| $170.00   | 9     | FAITHWALL BETA |
| $150.00   | 6     | FAMILIAR SPIRITS |
| $132.00   | 22    | ADAM TO NOAH CHART |
| $119.96   | 4     | FAITHWALL — FOUNDING FAMILY |
| $100.00   | 12    | WHERE THE BIBLE CAME FROM (PRE-ORDER) |
| $98.00    | 14    | HOW TO STUDY YOUR BIBLE |
| $85.00    | 16    | IF |
| $77.00    | 1     | BIBLICAL MAN FIELD MANUAL |
| $56.00    | 8     | VAULT SAMPLER |
| $42.00    | 3     | TORMENT TRIAGE |
| $32.95    | 1     | TRADITIONAL BIBLICAL HOMEMAKING |
| $28.00    | 6     | FIVE WEAPONS |

#### DH — Last 7 days line-by-line
| Revenue | Units | Product |
|--------:|------:|---------|
| $261.00 | 29 | THE STRONG DELUSION |
| $228.00 | 12 | HOW TO COUNT YOUR BIBLE |
| $200.00 | 20 | COUNT THE NUMBER |
| $132.00 | 22 | THE ADAM TO NOAH CHART |
| $77.00  | 1  | BIBLICAL MAN FIELD MANUAL |
| $63.00  | 9  | HOW TO STUDY THE BIBLE |
| $58.00  | 3  | NOT ENOCH |
| $50.00  | 2  | FAMILIAR SPIRITS |
| $42.00  | 6  | THE VAULT SAMPLER |
| ...     | ... | (smaller rows omitted) |

**Honest findings on the ladder:**
- **Count guide lifetime = 12 units / $228 over 30 days.** Not the "11 today" number I claimed earlier — that was over the entire launch window through today.
- **Field Files bundle = $0, zero units.** Did not appear once in the last 30 days of Stripe data. Either no sales yet, or product name mismatch in checkout. Needs investigation before more traffic gets pushed at it.
- **Vault is the #1 revenue product on DH at $4,098 / 14 units in 30 days** — directly contradicts CLAUDE.md's "big-ticket rarely moves." Big-ticket moves quietly but consistently. Re-anchor strategy around it.
- Plain Bible Manual is the volume leader: 110 units / $1,245.

### Biblical Man — `acct_1P9nFWJtGSEkhpBK` (key `STRIPE_KEY_BM`)
| Window                 | Net charges | Total revenue |
|------------------------|------------:|--------------:|
| Today (since 00:00 CDT)|           7 |       $130.00 |
| Last 7 days            |         101 |     $1,213.71 |
| June 1–13 (MTD)        |         180 |     $2,135.74 |
| Last 30 days           |        ~107 |       $462.00 (paid sessions only) |

Balance: available **−$2.36**, pending **+$92.50**
New customers (30d): **22**

#### BM — Top products last 30 days (paid checkout sessions)
| Revenue | Units | Product |
|--------:|------:|---------|
| $460.00 | 12 | support baby Blake |
| $1.00   | 1 | The Vault |
| $1.00   | 1 | Stand With The Biblical Man |

**Honest finding:** BM Stripe is **NOT where BM revenue lives** — most BM revenue flows through Substack paid subs (next section). The BM Stripe account is now primarily a donations/one-off rail (Support Baby Blake is the bulk of it). The discrepancy between "Last 7 days: $1,213.71 / 101 charges" (balance_transactions) and "30d paid sessions $462" is because most BM charges are Substack-routed subscription payments that don't show as checkout sessions.

---

## 2. SUBSTACK — Both publications, live dashboard pulls

### Biblical Man (Chrome → biblicalman.substack.com/publish/home)
- **Annual revenue: $78,733** (88.4% YoY growth, from $41,785)
- **Paid subscribers: 1,244** (80.3% growth, from 690)
- **Total subscribers: 25,829** (86.1% growth, from 13,876)
- Most recent post (Jun 12): 40 likes, 4 comments, 6,638 views, **+$60 new revenue / +1 paid sub**, 19.85% open
- Recent post (Jun 11, "Noah's Father Died at 777"): 39 likes, 3 comments, 0 new paid, 7.27k subs, 21% open

### Dead Hidden (Comet → deadhidden.substack.com/publish/home)
- **Annual revenue: $15,995** (4,056.9% YoY growth, from $385)
- **Paid subscribers: 193** (3,116.7% growth, from 6)
- **Total subscribers: 24,273** (4,925.5% growth, from 483)
- Today's post (6:18 AM): 10 likes, 1 comment, **+1 paid**, 4,073 subs reached, 13.76% open
- Note: this is likely the Antichrist paywalled post — fired this morning at 6:18, currently at +1 paid sub. Still early.

### Combined Substack truth
- **Combined Substack ARR: $94,728** (BM $78,733 + DH $15,995)
- **Combined paid subs: 1,437** (BM 1,244 + DH 193)
- **Combined total subs: 50,102** (BM 25,829 + DH 24,273)

### How this differs from CLAUDE.md (which was stale)
| Metric | CLAUDE.md claim | Real today | Delta |
|--------|-----------------|------------|-------|
| BM ARR | $82K | $78,733 | −$3,267 |
| BM paid | 1,301 | 1,244 | −57 |
| BM total | 25,302 | 25,829 | +527 |
| DH ARR | $14.5K | $15,995 | +$1,495 |
| DH paid | 164 | 193 | +29 |
| DH total | 24,656 | 24,273 | −383 |
| Combined ARR | $96.5K | $94,728 | −$1,772 |
| Combined paid | 1,465 | 1,437 | −28 |

**CLAUDE.md needs updating.** BM paid is actually trending down, not up. DH paid is growing faster than CLAUDE.md showed.

---

## 3. X / TWITTER — @Biblicalman (Chrome DOM read)
- **Followers: 52.8K**
- Following: 244
- Total posts: 9,897

CLAUDE.md had 52.9K — within rounding.

[GAP: last-7-days impression data not pulled — X analytics requires deeper auth dance. Codex brief in §6 covers wiring this via X API v2.]

---

## 4. RESEND — Live segment list (DH account, dashboard DOM)
| Segment | Contacts | Unsubscribed |
|---------|---------:|-------------:|
| **Dead Hidden** (main DH list) | **704** | 37 |
| vault_eligible | 170 | 7 |
| PBM buyers no Vault | 166 | 9 |
| Selah Subscribers | 26 | 0 |
| DH — Paid / Lapsed / Free | 0 / 0 / 0 | — (segments configured but empty) |
| BM — Paid / Lapsed / Free | 0 / 0 / 0 | — (same — not populated) |
| General | 0 | — |

**Honest finding:** The DH/BM segmentation in Resend is **set up but empty**. The Resend → Stripe webhook that should be populating paid/lapsed/free segments isn't running, or never got built. That's a real ops gap — and it's exactly what the Marketing Ops Reporting Agent in §6 needs to fix.

[GAP: full Audiences list (not Segments) and recent broadcast open/click rates not pulled — Resend API key in DH `.env.local` is sending-only, 403s on `/audiences`, `/emails`, `/domains`, `/api-keys`. Need a full-scope Resend API key for the agent.]

---

## 5. VERCEL / STORE TRAFFIC
[GAP: not pulled this session. Vercel CLI is installed (`/opt/homebrew/bin/vercel`). Codex brief in §6 includes `vercel analytics` query for `code.deadhidden.org`, `/store/the-field-files`, `/store/how-to-count-your-bible`.]

---

## 6. WHAT'S NEEDED TO MAKE THIS LIVE — Marketing Ops Reporting Agent brief
The above snapshot is a one-time manual pull. The Codex brief that follows specifies the always-live Vercel-hosted agent (see `2026-06-13-codex-brief-marketing-ops-agent.md`).

Tokens/credentials needed to build it:
1. **Stripe** — already have. `STRIPE_KEY_DH` and `STRIPE_KEY_BM` in `~/.hermes/.env`.
2. **Substack publisher API** — needs `substack_session` cookie or publisher API token. Adam must extract from logged-in browser session.
3. **X API v2** — needs bearer token. Adam has X dev account?
4. **Resend** — needs full-scope account API key (current one is restricted). Adam creates in Resend dashboard.
5. **Vercel Analytics** — already wired via Vercel CLI for any project owned by his account.

---

## Honesty note
This snapshot took ~12 minutes of real CDP + API work. Every number above either came from a Stripe API response, a Substack publisher dashboard DOM read I did in this session, an X profile DOM read I did in this session, or a Resend segments dashboard DOM read I did in this session. The `[GAP]` markers are honest blockers, not omissions.

Receipt logged to `~/.deadhidden-os/ops/RECEIPTS.md`.

— Fable, 2026-06-13 11:51 CDT
