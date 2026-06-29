# Loop 2 — Churn & Failed-Payment Save Loop
**Money lever:** 1,465 paid subs are already-won money. Three leaks bleed it: involuntary churn (failed cards), voluntary cancels, and silent pre-churn (164 PAID subs with Biblical Man email OFF = ~13% of 1,301 paid you can't even reach). At Biblical Man's ~$63/yr blended rate (VERIFY exact paid price in Stripe/Substack), saving even 10 paid/month from these three leaks holds ~$630/yr each touch and compounds. The 5 who already replied "ON" are the cheapest dollars in the business — paying readers asking to be let back in.
**Use when:** A Stripe payment fails on a renewal; a subscriber clicks cancel; or the email-off audit flags a paid sub not receiving sends. Run on a fixed cadence against the existing queues, never as a standing always-on process.

## The loop (copy-ready prompt)
> Pull today's three queues: (1) failed-payment renewals from Stripe, (2) new cancels, (3) paid-but-email-off subs from the bm-email-off audit. For each, send the ONE matching pre-approved message (dunning touch 1/2/3, single save note, or restore-delivery nudge) — never more than one touch per person per day, never a second save offer. Verify by checking Stripe for payment recovered, Substack for plan still active, and the reply/ON flag for delivery restored. Record saved vs lost per message variant. STOP a person when recovered, when they say "stop"/cancel-confirmed, or after the touch cap (dunning = 3 touches; save = 1; restore = 1). STOP the whole loop at plateau (2 consecutive batches with no net saves) or at Adam's batch-size limit. Approval boundary: Adam approves any discount/refund/free-month offer and any new send template before it goes out. Nothing charges, refunds, or sends without that.

## Feedback cycle
- **Observe:** Today's three queues — Stripe failed renewals (count + amount), new cancels (with exit reason if Substack captured one), and the paid-email-off list. Note the running ON/OFF/OTHER/BOUNCE reply tallies already seen.
- **Choose:** Pick the one message that matches each person's exact state. Failed card → dunning touch N. Cancel → single save note. Paid + email off → restore nudge. No cross-sends, no stacking.
- **Act:** Send exactly one pre-approved message to each person (one bounded, reversible step). Dunning advances one touch per day max. Bounced addresses get flagged for hygiene, not re-sent.
- **Verify:** Observable gates — Stripe shows the failed charge now succeeded (involuntary save); Substack shows the cancel reversed or plan still active 7 days post-save-note (voluntary save); the email-off sub flips to ON / replies / re-engages (delivery save). Metric: net paid subs saved per variant per batch.
- **Record:** Per variant: sent, saved, lost, bounced. Keep the reason codes from cancels (fatigue, path complexity, price, too many emails) feeding the Loop-1 path-simplification work. Log a dated receipt.
- **Stop:** Terminal states per person — RECOVERED (paid, charge succeeded, or email back ON), LOST (cancel confirmed / explicit "stop" / dunning cap hit with no payment), BOUNCED (bad address, route to hygiene). Loop-level stop: 2 consecutive batches with zero net saves (plateau) OR Adam's stated batch cap reached. Kill any variant that saves nobody across 2 batches.

## Success metric & target
**One metric: net paid subscribers saved per batch (involuntary + voluntary + delivery-restored).**
Live baselines that must be measured, not guessed: current Stripe failed-payment count/recovery rate (VERIFY in Stripe dunning settings — Substack/Stripe may already auto-retry, so measure incremental saves on top of that), and current monthly voluntary cancel count (VERIFY in Substack). Known starting signal from the email-off audit: 164 paid unreachable, 5 already self-identified as "want it back" — that's a concrete 5-sub floor and a 164-sub ceiling on the restore arm. Honest target for first 30 days: restore delivery to the 5 confirmed + win back 15-25 of the remaining 159 contacted, and convert the failed-payment + cancel arms into a measured recovery rate (target ≥30% of involuntary failures recovered once a clean dunning sequence runs — VERIFY against current rate before claiming lift).

## Supporting artifact

### (a) Failed-payment dunning sequence — 3 touches

**SEND MECHANISM — VERIFY:** Substack auto-retries failed cards and emails its own dunning notices for Substack-billed subs. Do NOT double-send into that. Confirm in Substack/Stripe whether these readers are Substack-billed (Substack owns the dunning) or store/Stripe-billed (Resend owns it). If Substack already dunns, use these as ONE warm human follow-up from Adam, not a parallel system. Sender for any store/Stripe-billed case: Adam at Dead Hidden <adam@deadhidden.org>.

---

**Touch 1 — Day 0. Subject: Your card didn't go through.**

Your renewal didn't clear.

Happens. Bank flags it, card expires, nothing dramatic.

Nothing's lost yet. Your subscription is still here.

One tap fixes it:

[UPDATE PAYMENT — VERIFY exact Substack/Stripe billing link]

That's it. No pitch.

Adam

---

**Touch 2 — Day 3. Subject: Still here when you're ready.**

The card still hasn't cleared.

I'm not writing to chase you.

I'm writing because you paid to be here once. That meant something.

"A friend loveth at all times." Proverbs 17:17.

If you want back in, one tap:

[UPDATE PAYMENT — VERIFY link]

If now's not the season, no hard feelings. The door stays open.

Adam

---

**Touch 3 — Day 7. Subject: Last note about your subscription.**

This is the last one I'll send.

Your subscription lapses soon if the card doesn't clear.

No guilt. No countdown timer.

Just the truth: the writing's still here when you come back.

Fix the card and nothing changes:

[UPDATE PAYMENT — VERIFY link]

Or let it lapse. You're still welcome on the free list.

Adam

---

### (b) Cancel-flow save message — single send

**SEND MECHANISM — VERIFY:** If the cancel happens inside Substack, Substack may not let you inject a custom save step in the cancel flow. Likely delivery = ONE email triggered after a detected cancel (Resend for store/Stripe; manual/Substack export for Substack-billed). Confirm where cancels are observable before automating.

---

**Subject: You're free to go. One honest thing first.**

You canceled. That's done. I'm not clawing it back.

One honest question before you go.

Was it the writing? Or was it the noise?

Because I've heard it from others. Too many emails. Too many layers. The Vault, the site, the inbox, all of it loud.

If that was it, tell me. One word back. I'm cutting the noise, not the gospel.

If the writing itself stopped feeding you, that's fair too. Say so. I'd rather know than guess.

Either way you keep every download you bought. All sales final, but yours stay yours.

"Let your communication be, Yea, yea; Nay, nay." Matthew 5:37.

Yea or nay. I read every reply.

Adam

---

### (c) Email-off restore note — for the 164 paid subs

**SEND MECHANISM — VERIFY:** This is the same audit Codex already ran (subject "Quick check on your Biblical Man emails," logged in bm-email-off-reply-watch.sqlite3). This copy is the follow-up for the 159 who haven't answered, and a confirmation for the 5 who said ON. Toggling Substack email-on for a sub may require the sub's own action or a Substack setting — VERIFY whether Adam can flip delivery server-side or whether the reader must do it. If reader-side, the "one tap" must point to their Substack subscription settings, not a phantom button.

---

**Subject: You're paying. You're not getting the emails.**

Quick one.

You pay for Biblical Man. But your emails are switched off.

So you're funding writing you never see in your inbox.

That's not right.

Turn delivery back on here — one tap:
[MANAGE EMAIL DELIVERY — VERIFY: link to reader's Substack subscription settings]

Or reply "on" and I'll sort it from my end where I can.

No new pitch. You already bought in. I just want the words reaching you.

"Faith cometh by hearing." Romans 10:17.

Hard to hear what never arrives.

Adam

---

## Hand-off (what needs Codex / live systems)
- **Stripe:** Source the failed-payment queue and verify charge recovery. VERIFY current auto-retry/dunning config so this loop measures *incremental* saves, not Stripe's existing recoveries. Any discount/refund/free-month offer needs Adam's explicit approval (per CLAUDE.md, refunds and discounts require it).
- **Substack:** Confirm which paid subs are Substack-billed vs store/Stripe-billed (decides who owns dunning). Source the cancel queue and the email-off audit list. VERIFY whether email-delivery and cancel-save steps can be triggered server-side or require the reader's own click — this changes every "one tap" link above.
- **Resend (Adam at Dead Hidden <adam@deadhidden.org>):** The likely sender for any store/Stripe-billed dunning and the cancel/restore follow-ups. Bounce handling feeds list hygiene (the audit already showed address-not-found / inbox-full / hop-count bounces).
- **Codex / bm-email-off-reply-watch.sqlite3:** Already holds the email-off queue and reply tallies (ON/OFF/OTHER/BOUNCE). Extend it as the per-variant ledger (sent/saved/lost/bounced) instead of building a new store.
- **Approval boundary before anything sends/charges:** Adam signs off on (1) every send template above, (2) any offer beyond "fix your card / turn delivery on" — i.e., any discount, free month, or refund, and (3) the batch size per run. No charge, refund, or send fires without that approval. All copy above is reversible (email only); nothing here touches a card or cancels/reinstates a plan automatically.

VERIFY items to close before first send: exact paid price for the dollar math, exact Substack/Stripe payment-update link, whether email-on can be flipped server-side, and current Stripe failed-payment recovery rate as the true baseline.
