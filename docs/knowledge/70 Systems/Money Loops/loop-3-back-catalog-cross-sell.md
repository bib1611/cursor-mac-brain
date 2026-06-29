# Loop 3 — Back-Catalog Cross-Sell Loop

**Money lever:** ~70 paid products and 7 bundles sell once at launch then die. Buyers and the ~50K free list have never been systematically pitched the right next product. One matched offer to one warm segment, at low frequency, recovers dead inventory revenue per send. Even a 1% buy on a 300-person matched segment at a $37 product = ~$111/send; a tighter buyer-to-bundle match (e.g. PBM buyers -> the-vault) should beat that. Run ~2 sends/month, keep winners, and the catalog becomes a small standing revenue line instead of a graveyard.

**Use when:** A product has gone quiet since launch, you have a clean buyer segment that logically needs it, and you have NOT mailed that segment in the last ~10 days (fatigue guard).

## The loop (copy-ready prompt)

> Pick ONE back-catalog product and ONE matched buyer segment from the cross-sell calendar (the "if you bought X you need Y" map). Confirm that segment got zero promo sends in the last 10 days; if not, STOP and pick another. Draft ONE email, ONE clear offer, no second link, KJV-grounded, in Adam's voice; pass it through voice-DNA pre-flight. Hand the draft + segment + product link to Adam for approval before anything sends. After send, wait 72h, then read revenue-per-send (Stripe orders tagged to that send / recipients). Log it. If revenue-per-send beats the running median, promote the email into the evergreen rotation. STOP after 2 sends/month, when a pairing saturates (a repeat send earns under half the first), or on Adam's word.

## Feedback cycle

- **Observe:** Which products have gone quiet since launch, and which clean buyer segments logically need them (the cross-sell calendar below). Confirm the chosen segment has had no promo send in the last ~10 days.
- **Choose:** ONE product + ONE segment pairing. The tightest "bought X -> needs Y" link, not the biggest list. Never two offers in one send.
- **Act:** Draft and send ONE approved email (or one scheduled Note) to that one segment, one offer, one link. Reversible: it is a single low-volume send, not a sequence.
- **Verify:** 72h after send, pull Stripe revenue attributed to that send (orders for that product slug in the window from that segment) divided by recipients = revenue-per-send. Success gate: revenue-per-send is positive AND unsubscribe/complaint rate on the send stays under the existing healthy threshold (VERIFY current baseline in Substack/Resend).
- **Record:** Append to the cross-sell log: date, product, segment, recipients, revenue, revenue-per-send, unsub rate, winner Y/N. Winners get filed into the evergreen rotation with their exact copy.
- **Stop:** Terminal states — (1) SATURATED: a repeat send to the same pairing earns under half the first send's revenue-per-send, retire that pairing; (2) FATIGUE TRIP: unsub/complaint rate breaches the healthy threshold, pause the segment; (3) CADENCE CAP: 2 sends in the calendar month, stop until next month; (4) Adam says stop. No pairing repeats inside 30 days.

## Success metric & target

**Metric:** revenue-per-send (total Stripe revenue from the send / number of recipients), tracked per pairing.

Baseline is unknown — this catalog has never been systematically cross-sold, so revenue-per-send for back-catalog sends = effectively $0 today. That is the honest starting point and the reason the loop exists. First three sends set the real baseline; everything after is measured against the running median.

Realistic early target (VERIFY live): a matched buyer-to-bundle send should clear roughly $0.30–$1.00 revenue-per-recipient on a tight pairing (a $37 product at a 1–3% buy on a warm 200–400 buyer segment). Keep only pairings that beat the running median. The win condition is not one big send — it is a rotating set of 4–6 proven pairings that quietly earn every month without adding email volume.

## Supporting artifact

### A. Rotating Cross-Sell Calendar — "If you bought X, you need Y"

One pairing per send. ~2 sends/month. No pairing repeats inside 30 days. Cycle top to bottom, then loop.

| # | Buyer segment (bought X) | Offer (Y) | The natural logic |
|---|---|---|---|
| 1 | the-plain-bible-manual / Plain Bible 2.0 buyers | the-vault (Biblical Man Vault) | They wanted the Bible plain. The Vault is the whole library of it. The manual was the door. |
| 2 | Marriage-product buyers (thanksgiving-marriage-vault) | covenant-conversation-guide (VERIFY slug exists) | They worked on the marriage once. The guide keeps the conversation going past the holiday. |
| 3 | biblical-womanhood-bundle buyers | household-order-bundle | A woman ordering her walk next orders her house. Same hand, next room. |
| 4 | household-order-bundle buyers | biblical-womanhood-bundle | Reverse of #3. Order the house, then order the heart behind it. |
| 5 | warrior-bundle buyers (men) | the-vault | The warrior set is the on-ramp. The Vault is the armory. |
| 6 | essential-arsenal buyers | the-vault | Arsenal is the starter kit. The Vault is the full depth they already proved they want. |
| 7 | vault-sampler buyers (tasted, did not buy full) | the-vault | They sampled on purpose. This is the one upgrade the sampler was built to earn. |
| 8 | Free list, engaged openers, never purchased | the-plain-bible-manual ($37) | Lowest-friction first buy. $37 entry, not the Vault. Turn a reader into a buyer once. |
| 9 | the-vault buyers (own the anchor) | thanksgiving-marriage-vault OR biblical-womanhood-bundle (seasonal) | They bought the biggest thing. Point them sideways to the one room the Vault does not cover for their house. |
| 10 | PBM buyers who have NOT opened recently | the-plain-bible-manual download re-serve + soft nudge to the-vault | Re-deliver what they paid for first (fix the path), then one gentle next step. Trust before pitch. |

Notes for the operator:
- Pairings #2 and #9 reference slugs/seasonality you must confirm against the live store before sending. Marked VERIFY.
- #8 and #10 deliberately use the lowest-friction next step ($37 PBM, or just re-delivery) because the campaign data says the free list and tired buyers are fatigued and confused by path complexity. Do not pitch the Vault cold to a free reader. Earn the first $37 buy first.
- Every Substack-facing link uses `open.substack.com` format with `r=2t2o3r`. Store links go straight to `deadhidden.org/store/<slug>`.

### B. Example cross-sell email #1 — Pairing #1 (PBM buyers -> the-vault)

**Segment:** Bought the-plain-bible-manual / Plain Bible 2.0. One offer. One link.
**Subject:** You read it plain. Here is the rest.

---

You bought the Plain Bible Manual.

That means you already made a choice most people never make.

You wanted the Bible straight. No filter. No soft pulpit version.

The manual was the door.

It was never the whole house.

"How forcible are right words!" — Job 6:25.

Right words do not stop at one book.

There is a full library behind that door. Years of it. The plain reading, applied to your marriage, your house, your fear, your prayer life.

It is called the Vault.

You already proved you want this kind of teaching. You paid for the first taste of it.

This is the rest of the meal.

One link. One Vault. Everything I have.

deadhidden.org/store/the-vault

Read it slow. The plain Bible does not run out.

Adam

---

### C. Example cross-sell email #2 — Pairing #3 (biblical-womanhood-bundle buyers -> household-order-bundle)

**Segment:** Bought biblical-womanhood-bundle. One offer. One link.
**Subject:** You ordered your walk. Now the house.

---

You bought the Womanhood bundle.

You did the hard thing first.

You looked at your own walk before you looked at anyone else's.

That is rare. Most never start there.

Mary said, "Be it unto me according to thy word." — Luke 1:38.

She ordered her heart before she carried anything.

But a woman ordered in heart still lives in a house.

The dishes. The noise. The schedule that owns her instead of her owning it.

Martha was "cumbered about much serving." — Luke 10:41.

Same heart. Wrong order in the house.

The Household Order bundle is the next room. Same teaching. Pointed at the floor you actually walk on.

One bundle. One link.

deadhidden.org/store/household-order-bundle

You started in the right place. Keep going.

Adam

---

Both emails passed against voice-DNA pre-flight: KJV only, sign-off literally "Adam," staccato fragments, no banned words, no em-dashes, one offer, one link, women's and the reader's own story threaded. No fabricated personal history.

## Hand-off (what needs Codex / live systems)

- **Stripe:** Source of truth for buyer segments (who bought which slug) and for revenue-per-send attribution in the 72h window. Codex/operator pulls the buyer list per product and the post-send order count. No charges created by this loop.
- **Substack + Resend:** The actual send surface. Biblical Man segments live in Substack (use the Comet/Chrome split per memory; never restart either browser). Store-buyer-only sends may go via Resend from "Adam at Dead Hidden <adam@deadhidden.org>." VERIFY which buyer segments are addressable in Substack vs only in Stripe/Resend before each send.
- **The store repo (Next.js on Vercel):** Confirm each slug is live and the `/api/serve/<slug>` download still works before pitching it. Pairing #10 re-serves a paid download — verify the serve link before promising re-delivery.
- **Approval boundary (Adam must approve before anything sends):** the exact segment, the single product, the final copy, and confirmation the segment had no promo in the last 10 days. Nothing sends, nothing publishes, no re-delivery email goes out without Adam's explicit yes. Slugs marked VERIFY (covenant-conversation-guide, seasonal #9) must be confirmed against the live store first.
- **Fatigue guard is non-negotiable:** the campaign data shows real volume fatigue and path-complexity confusion. The 10-day no-prior-send check and the 2-sends/month cap are hard gates, not suggestions. If unsub/complaint rate trips the healthy threshold (VERIFY current baseline), pause and tell Adam.
