# Loop 5 — Substack vs beehiiv Migration Decision

**Money lever:** Substack's ~10% cut is ~$8,200/yr on Biblical Man's ~$82K ARR. beehiiv takes 0% of subscriptions but costs ~$149/mo Scale (~$1,788/yr) or ~$249/mo Max (~$2,988/yr) at 25K subs, plus ad-network upside (~$1,800–6,000/yr, faith niche, soft ceiling). Net guaranteed prize from leaving: ~$5,200–6,400/yr. Against that sits the migration risk to 1,242 active paid subs and the loss of Substack's free discovery while paid acquisition is already collapsing (145→20/mo). This loop spends a small, reversible test to decide it on data, not vibes — and never moves the paid base on a hunch.

**Use when:** You are seriously weighing leaving Substack (throttle frustration, wanting sponsors, wanting ownership). Run it instead of either migrating on impulse or dismissing the idea. Trigger a re-run if Substack changes its sponsor/cut policy or your acquisition trend shifts hard.

## The loop (copy-ready prompt)
> Stand up beehiiv on the FREE tier and run a read-only content import (touches nothing on Substack). Pick the lower-risk publication as the test bed (Dead Hidden, ~$14.5K ARR, not the $82K Biblical Man). Migrate only its cleaned FREE list to a warmed custom domain, then run paired identical sends on both platforms for a set window. Each window, score the deciding metrics (deliverability, open rate, ad revenue per send, paid take-rate, monthly new paid, discovery/source mix) against the Substack baseline. Keep testing only while beehiiv wins the gate; stop into a named decision (MIGRATE / STAY / KEEP-BOTH / ABORT). The 1,242 active paid subs and the 25,822-person Biblical Man list never export, migrate, or get a live beehiiv send without Adam's explicit written go. A MIGRATE verdict is a tested recommendation, not permission.

## Feedback cycle
- **Observe:** Pull the real baseline from Substack (deliverability %, open rate, new-paid/mo, subscriber-source split) and the live beehiiv dashboard after warmup (CPM, ad fill, post-warmup open rate, paid attrition).
- **Choose:** Run the test on the lowest-exposure surface first — Dead Hidden's free list, and Substack-native sponsors on Biblical Man (the zero-risk sponsor test). Never the Biblical Man paid base.
- **Act:** One bounded, reversible step per window — a paired identical send on both platforms to a matched free slice. Nothing on the paid base moves.
- **Verify:** Score the window against the scorecard below. The gate is explicit (see Decision rule). Deliverability and real paid attrition are load-bearing; ad revenue and cut-savings are paper wins that cannot carry the decision alone.
- **Record:** Log each window's scorecard row, the running tally, and any deliverability/spam-folder events.
- **Stop:** Terminal states — **MIGRATE** (beehiiv clears the gate over 2 consecutive windows AND the paid-transfer path is verified), **STAY** (beehiiv loses the gate twice running, or warmup spam-folders the test), **KEEP-BOTH** (beehiiv wins on monetization but Substack still wins on discovery — keep Substack for growth, beehiiv for owned sends/sponsors), **ABORT** (deliverability or paid-attrition risk shows up real on the test bed). No "migrate anyway" branch exists.

## The deciding metrics (the scorecard)

| Metric | Substack baseline (real) | beehiiv after test | Load-bearing? |
|---|---|---|---|
| Deliverability (delivered ÷ list) | ~73% (~18,860 / 25,822) | measure post-warmup | **Yes** |
| Open rate (single clean send) | ~44% (collapses to 11% when blasted 6× in 48h) | measure | Yes |
| Ad revenue per send | $0 (no native ads featured) | measure real faith-niche fill | No (paper win) |
| Subscription take-rate | Substack 10% (~$8.2K/yr) | beehiiv 0% + platform fee | No (paper win) |
| New paid / month | 145 (Feb) → 20 (Jun), ~86% drop | measure on test bed | **Yes** |
| Discovery / source mix | VERIFY in Stats → subscriber sources (network vs X vs direct) | beehiiv has no app/feed/Notes | **Yes** |

## Decision rule
Migrate **only if** beehiiv wins **4 of 6** metrics AND **2 of the 3 load-bearing** ones (deliverability, new-paid, discovery), over **2 consecutive windows**, AND the paid-transfer path is verified first (709 yearly / 376 monthly / 3 lifetime / 22 ios_app / 13 gift / 11 comp / 1 quarterly — Stripe cards copy over, but the 22 Apple-billed and 13 gift / 11 comp need manual handling). If beehiiv wins monetization but loses discovery → **KEEP-BOTH**. If it loses the gate twice or spam-folders the warmup → **STAY**. Ad-revenue and cut-savings alone never justify a migrate. The cheap parallel test that needs no migration: **turn on Substack native sponsors on Biblical Man this month** — if faith brands won't pay you on Substack, they won't on beehiiv either, and you've answered the whole question for free.

## Hand-off (what needs Codex / live systems / Adam approval)
- **Read-only first:** beehiiv free-tier signup + content import; Substack Stats pull for the subscriber-source split (the single number that most decides this — VERIFY in dashboard). Use the existing browser split: Dead Hidden = Comet, Biblical Man = Chrome; never restart either.
- **Test-bed migration (Dead Hidden only):** clean the free list (drop dead addresses — the same hygiene the on/off campaign exposed), attach + warm a custom domain over 6–8 weeks to avoid spam-foldering.
- **Pre-work for any future Biblical Man move:** attach a custom domain on Substack now (~$50) so a later cutover keeps backlinks/SEO and auto-redirects.
- **Hard approval boundary:** the 1,242 active paid subs and the 25,822-person Biblical Man list never export, migrate, or receive a live beehiiv send without Adam's explicit written go. Codex/agents may set up, import read-only, and measure — never move the paid base or the prize list.
- **Source data:** 2026-06-20 Substack export (`email_list.biblicalman.csv`, `posts.csv`, per-post delivers/opens) + the email on/off campaign sqlite. Full beehiiv pricing/monetization/migration research in `substack-vs-beehiiv-research.md`; full reasoning in `substack-vs-beehiiv-decision-memo.md`.
