# GRADE — the dynamic content grader (RUN.md step 5)

PART 1 is the FLOOR: does it avoid slop and sound like Adam. Pass or fail. This file is the CEILING: will it actually win. And it tunes itself on real numbers, so the grade gets sharper every week instead of staying a stranger's guess.

Two scores. One calibration loop. The grader is wrong until the market corrects it, and this file is how it learns.

---

## TIER 1 — THE FLOOR (binary, from WRITING-BRAIN.md PART 1)

Run PART 1 first. 7+ on every dimension, 60+ total, zero instant-kill words.

- FAIL = dead. No Tier 2. A slop draft with a brilliant hook is still slop.
- PASS = go to Tier 2.

## TIER 2 — THE WIN GRADE (0 to 100, predicts the result)

Seven dimensions, each scored 0 to 10. The weights are not fixed. They shift by what the post is FOR, and they retune over time (Tier 3).

| # | Dimension | The test (a grader can check it) |
|---|---|---|
| 1 | Scroll-Kill | Cover everything but line 1. Would a stranger still stop? |
| 2 | Zero-Resolution | Can they get the payoff WITHOUT reading on? If yes, it leaks. |
| 3 | Paradigm Voltage | Does it overturn a venerated thing or surface buried truth? How big is the flip? |
| 4 | Concrete Receipt | Point at the floating claim. There should be none. Numbers, scenes, verses. |
| 5 | Emotional Voltage | Does it hit a wound, a fear, a conviction. Or is it dry information? |
| 6 | Debate Pull | Would a sincere believer want to argue it? Defensible AND divisive (Confrontation Governor, PART 2). |
| 7 | SKU Pull | Which one SKU does it ladder to, and does the CTA feel inevitable or stapled on? |

### Declare the goal first. The weights follow it.

A father tribute and a reply-bait tweet do not win on the same axis. State the goal, then use its profile (PART 15 maps the style).

| Dimension | REPLIES / reach (Ed) | FREE-SUB (Dakota) | SALE / SKU (post) |
|---|---|---|---|
| Scroll-Kill | ×3 | ×3 | ×2 |
| Zero-Resolution | ×1 | ×3 | ×2 |
| Paradigm Voltage | ×3 | ×2 | ×1 |
| Concrete Receipt | ×2 | ×2 | ×2 |
| Emotional Voltage | ×1 | ×3 | ×3 |
| Debate Pull | ×3 | ×1 | ×1 |
| SKU Pull | ×1 | ×1 | ×3 |

Score = sum(dim × weight), normalized to 100 by dividing by that profile's max and ×100.

**Verdict bands (calibrated against winners.md):**
- 85 to 100 → BANGER candidate. Ship first-thing, strongest slot.
- 70 to 84 → SHIP. Solid daily.
- 55 to 69 → FLOOR. Publishable, will not move numbers. Raise the highest-weighted weak dim or hold.
- under 55 → KILL or rebuild the hook. A perfect body cannot save a dead hook.

**Every grade returns this, not just a number:**
- Tier 1: PASS or FAIL (name the killing dim if fail)
- Goal declared + Tier 2 score /100 + the seven raw dim scores
- The single weakest high-weight dimension + the one fix that raises it most
- Closest row in winners.md + does this BEAT its mechanic or only echo it
- Predicted band + the SKU it ladders to

## TIER 3 — THE CALIBRATION LOOP (this is "improve on dynamics")

The starting weights above are a hypothesis, not scripture. The market grades the grader.

1. **Tag every winner.** When a post earns a row in winners.md (~1k likes / 20k impressions / a sale), tag the 2 or 3 Tier-2 dimensions it MAXED. ("Noah's Father Died at 777" = Scroll-Kill + Zero-Resolution + Concrete Receipt.)
2. **Reweight monthly.** Recount the tags across all wins, per goal profile. Dimensions that keep showing up in YOUR wins get their weight raised. Ones that never predict a win get cut.
3. **Track the calibration miss (the sharpest signal of all):**
   - Graded BANGER, flopped → a blind spot. The grader is missing a dimension. Log it to losers.md WITH the diagnosis, then add or sharpen a dimension.
   - Graded FLOOR, went viral → an underrated pattern. Study it. It is handing you a new win-driver.
4. **Version the rubric.** Stamp every reweight (date + what changed) in the changelog below. In ~90 days the grade predicts your numbers inside a band. That is the day the brain can draft AND pick the winner without you in the loop.

RUN.md step 6 already logs winners and losers. This file reads those rows back into the weights.

---

## QUICK GRADE PROMPT

"Grade this against GRADE.md. State the goal, Tier 1 pass/fail, Tier 2 /100 with the seven dim scores, the one fix that raises it most, the closest winner, predicted band, and SKU. Be a hostile grader, not a friend."

## CHANGELOG (every reweight gets a dated line)

- 2026-06-21 — created. Starting weights are a hypothesis. Zero calibration data logged yet. First reweight due after winners.md carries 20+ rows with dimension tags.
- 2026-06-21 (first read) — tagged all 20 seeded winners. Frequency: Scroll-Kill 18/20, Zero-Resolution 12, Paradigm Voltage 10, Debate Pull 7, Emotional Voltage 6, SKU Pull 5, Concrete Receipt 2. Read: Scroll-Kill is near-universal, treat it as a near-gate not a differentiator. Zero-Resolution + Paradigm Voltage are the true win-drivers, hold their weights. Debate Pull clusters in the comment-monsters and SKU Pull in the top click-drivers, which confirms the goal-split is real, not assumed. Concrete Receipt reads low because at the hook level it lives in the body, not the title; keep it a floor item on short-form, weight it only on long-form SALE. NO numeric reweight applied: 20 hook-tags is signal, not enough predicted-vs-actual calibration to move the math. Reweight when 10+ shipped posts have a logged predicted grade vs real numbers.
