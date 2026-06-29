# Adam to Noah Chart — launch execution receipt

Date: 2026-06-11 11:32–11:42a CT
Agent: Hermes
Approval: Adam, same thread — "Let's get this launched live ASAP."

## Executed, with proof

1. **DH noon post PUBLISHED at 11:38a** (not scheduled — see note below)
   - "Ten Dead Men Spell a Sentence", draft 201605405, audience: everyone
   - POST /api/v1/drafts/201605405/publish → 200, send:true (email went to list)
   - Live: https://deadhidden.substack.com/p/ten-dead-men-spell-a-sentence (public 200 verified)
   - Why early: Substack removed the legacy schedule API (`/api/v1/drafts/{id}/schedule` → 404 on POST/PUT; `draft_scheduled_at` PUT silently ignored; `/api/v1/post_management/schedule` → 404). Adam said "ASAP"; 11:38 vs 12:00 judged equivalent. UI scheduling via editor remains the fallback for future scheduled posts.

2. **Spielberg post armed for 6:30p CT** — detached job, survives session close
   - "The Bible Already Had a Disclosure Day", draft 201607195, audience: everyone
   - Job: /Users/adamjohnsson/.hermes/jobs/publish_spielberg_630.sh (pid 94675, nohup)
   - Uses validated publish endpoint via Comet CDP tab 8C194599D4FE57EA1BFD6224B37B15C6; one retry fallback; logs to publish_spielberg_630.log

3. **Email blast SENT 11:39a**
   - Resend broadcast f6206074-5a36-430e-b28f-2145a22b5f13 → status: sent, sent_at 2026-06-11 16:39:52 UTC
   - Audience: 853ea354 "Dead Hidden" (deadhidden.org capture list)
   - Subject: "The chapter you skip spells a sentence" — store CTA button, PWYW $5 floor
   - NOTE: Resend card still failing per morning alert — Adam owns the fix, said rail works for now.

4. **DH Note posted** (Comet, user_id 218038831) — obituary-column angle + store link attachment (attachment 321933ed) → 200

5. **BM Note posted** (Chrome, user_id 169765767) — gospel-sentence angle + store link attachment (c16200bc) → 200

6. **Reply tweets posted** (@Biblicalman via xurl)
   - Under Genesis 5 thread (2064761812306850037): tweet 2065112592452837570
   - Under X article (2065055939732906200): tweet 2065112634672783786

## Store
- https://deadhidden.org/store/the-adam-to-noah-chart → 200, OG card renders ("10 names that spell out a sentence from God")
- Stripe PWYW $5 floor, fulfillment via existing webhook + Resend rail

## Open items
- Resend card fix (Adam, back burner)
- Watch-loop ticks continue (12:23p next); chart sales fold into deltas
- 6:23p tick double-checks the Spielberg job log before 6:30p fire
