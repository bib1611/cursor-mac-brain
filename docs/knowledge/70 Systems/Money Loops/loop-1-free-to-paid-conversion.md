# Loop 1 — Free-to-Paid Conversion Engine
**Money lever:** 97% of the ~50K combined list rides free; only ~2.9% pays (1,465 paid). Moving the paying share from 2.9% to 4% across the list is ~+550 paid subs. At Biblical Man's blended rate (~$82K ARR / 1,301 paid ≈ ~$63/paid/yr) that is roughly **+$30-40K ARR** with zero new audience. This loop finds which free pieces actually produced upgrades, repeats that vein, places ONE simple CTA, and keeps only what beats baseline.

**Use when:** Weekly. Run every Monday on the prior 7 days of posts/Notes. Trigger early if a single free post drives an unusual upgrade spike worth repeating fast.

## The loop (copy-ready prompt)
> Each Monday, pull the prior 7 days of free posts/Notes and the list of new paid upgrades (Substack dashboard) for both publications. Attribute each upgrade to the last free piece that subscriber opened before upgrading; log every post in the tracker (title, upgrades, CTA used, conversion rate, keep/kill). Identify the single highest-converting vein. Write ONE new free piece in that vein with ONE single-step upgrade CTA (no Vault/sites/layers maze). Draft only — do not publish or send. Stop when no post beats the trailing 4-week baseline rate twice in a row, or after the weekly run. Adam approves before anything publishes.

## Feedback cycle
- **Observe:** Last 7 days of free posts/Notes + new paid upgrades pulled from each Substack dashboard. Which pieces preceded upgrades, which CTA each carried, which path the upgrade used.
- **Choose:** Pick the one vein (topic + hook shape) with the highest attributed upgrade rate, not the highest open rate. Opens are not money.
- **Act:** Draft one new free piece in that proven vein with ONE single-step CTA (one clear next action). Reversible: it is a draft, nothing sends.
- **Verify:** After publish, the piece's attributed free-to-paid rate beats the trailing 4-week baseline. Metric: attributed upgrades ÷ unique openers of that piece.
- **Record:** Append the row to the tracker. Mark keep (beat baseline) or kill (missed). Note which CTA wording won.
- **Stop:** Terminal states — (1) NO-PROGRESS: two consecutive published pieces fail to beat baseline, pause the vein and re-pick. (2) LIMIT: the weekly run is one cycle; do not auto-loop into a second draft without Adam. (3) STALL: list-wide paid share flat for 4 weeks, stop and escalate to Adam for a new angle.

## Success metric & target
**One metric: attributed free-to-paid conversion rate per published free piece** (attributed upgrades ÷ unique openers).

Baseline that must be measured live: there is no clean per-post upgrade rate today — Substack shows upgrades but not which post caused them, so week 1 of this loop IS the baseline-building week. The list-level anchor is known: ~2.9% of ~50K pays now. Target: move list-level paid share toward 4% over the run (~+550 paid, ~+$30-40K ARR). Per-post working target once baseline exists: each kept piece beats the trailing 4-week median upgrade rate. VERIFY: whether Substack's dashboard exposes upgrade timestamps and the last-opened post per upgrading subscriber — if not, attribution falls back to the proxy method in the artifact.

## Supporting artifact

### A. Weekly conversion tracker — exact fields (one row per published free piece)

| Field | What goes in it | Source |
|---|---|---|
| `week_of` | Monday date of the run | manual |
| `publication` | Biblical Man or Dead Hidden | manual |
| `post_title` | exact title | Substack |
| `post_url` | open.substack.com link, `r=2t2o3r` | Substack |
| `type` | post or Note | manual |
| `publish_date` | date live | Substack |
| `unique_openers` | unique opens (the conversion denominator) | Substack stats |
| `vein` | topic + hook shape (e.g. "confessional / male spiritual sloth") | manual |
| `cta_used` | which of the 3 CTAs below (A/B/C) or "none" | manual |
| `cta_placement` | top, mid, or end | manual |
| `upgrades_attributed` | new paid upgrades tied to this piece (see B) | Substack + method B |
| `conversion_rate` | upgrades_attributed ÷ unique_openers | calculated |
| `baseline_rate` | trailing 4-week median of conversion_rate | calculated |
| `beat_baseline` | yes / no | calculated |
| `keep_kill` | KEEP if beat 2x in vein, KILL if missed | decision |
| `path_steps` | count of clicks from CTA to checkout (target = 1) | manual |
| `notes` | reader reply signal, fatigue mentions, bounce flags | manual |

### B. How to attribute an upgrade to a post (no new tools)
Substack does not natively say "post X caused this upgrade." Use this two-tier proxy, simplest first:

1. **Primary (single-CTA isolation):** Each week, only ONE free piece carries an upgrade CTA. Every new paid upgrade in the 72 hours after that piece goes out is attributed to it. One CTA live at a time = clean attribution. This is the whole reason the loop ships only one CTA per cycle.
2. **Fallback (last-open):** For upgrades outside that window, in the Substack subscriber view check the upgrading subscriber's last-opened free post before their upgrade date; credit that post. VERIFY this field is visible per-subscriber on the current plan.

Log denominator = `unique_openers` of the CTA-carrying piece. This makes rate, not raw count, the unit of truth — a small post that converts hot beats a big post that converts cold.

### C. Three single-CTA upgrade asks (Adam's voice, one clear step, no maze)

**CTA A — the plain ask (confessional)**
> You have read free for months.
>
> The free posts are the door.
>
> The paid posts are the room.
>
> "Buy the truth, and sell it not." Proverbs 23:23.
>
> One button. No maze. Become a paid subscriber and read the rest.
>
> [Upgrade here → open.substack.com/... ?r=2t2o3r]
>
> Adam

**CTA B — the path-complexity killer (names the friction, removes it)**
> I made this too hard.
>
> Vault. Sites. Layers. Too many doors.
>
> Forget all of it.
>
> One step now. Paid subscription. That is the whole path.
>
> "Let your communication be, Yea, yea." Matthew 5:37.
>
> [Become a paid subscriber → open.substack.com/... ?r=2t2o3r]
>
> Adam

**CTA C — the stakes ask (cost of staying free)**
> Free keeps you fed.
>
> Paid keeps you trained.
>
> One is a meal. One is a sword.
>
> "Take... the sword of the Spirit." Ephesians 6:17.
>
> Pick up the sword. One click. Paid.
>
> [Upgrade now → open.substack.com/... ?r=2t2o3r]
>
> Adam

Each CTA: one ask, one button, KJV-grounded, no "go to the site then the Vault then." That single-step shape is the live test against the PATH COMPLEXITY finding (a paying reader disengaged because "sites, Vault, extra layers... felt confusing"). Rotate A/B/C across weeks; the tracker's `cta_used` column reveals the winner.

VERIFY before use: paste the exact `open.substack.com` upgrade URL for each publication with `r=2t2o3r` into the brackets. The bracketed link is the only placeholder and it is marked because the canonical upgrade URL must come from Adam's live Substack settings.

## Hand-off (what needs Codex / live systems)
- **Substack (both publications):** read-only pulls of post stats, unique opens, and the new-paid-upgrades list each Monday. Confirm whether per-subscriber "last opened post" and upgrade timestamps are visible on the current plan (drives method B fallback). Use the existing browser split — Dead Hidden = Comet, Biblical Man = Chrome; never restart either.
- **The tracker itself:** lives wherever Adam keeps live numbers (Obsidian vault sheet or a simple CSV). No new tool. Codex can scaffold the empty table with the columns above on request.
- **Approval boundary — Adam must approve before anything sends/publishes:** (1) publishing any drafted free piece, (2) the exact CTA wording and the live `open.substack.com` upgrade URL, (3) any change that touches the actual upgrade/checkout path. The loop drafts and measures autonomously; it does not publish, email, or alter the paid offer without Adam's explicit go.
- **No Stripe/Resend writes** in this loop — upgrades flow through Substack's own paid subscription, so no charge logic is touched here. If a CTA ever points to a deadhidden.org store product instead of a Substack upgrade, that crosses into Stripe/Resend and needs separate approval.
