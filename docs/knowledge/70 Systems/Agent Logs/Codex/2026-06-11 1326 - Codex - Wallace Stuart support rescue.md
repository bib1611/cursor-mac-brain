# Wallace Stuart support rescue

Date: 2026-06-11 13:26 CDT
Agent: Codex
Trigger: Adam pasted a frustrated buyer email from Wallace Stuart / birdie6463@yahoo.com asking for The Plain Bible Manual download and saying an $18 payment was made on 2026-05-21.

## Boundary

- Support/download complaint is auto-fix authorized under ops `Support Auto-Fix Rule`.
- No refund, cancellation, card, subscription, or Stripe state change was made.
- External customer email was sent through Resend as a one-off fulfillment/support fix.

## Verification

- Refreshed local team packet at 2026-06-11 13:21 CDT.
- Used `deadhidden-commerce-ops` and `deadhidden-brain-mail` workflows.
- Live store page check: `https://deadhidden.org/store/the-plain-bible-manual` returned HTTP 200.
- Product file verified locally:
  - `/Users/adamjohnsson/openclaw/dh-store/blob/the-plain-bible-manual.pdf`
  - PDF, 137 pages, 1,929,255 bytes.
  - SHA-256: `1db98608200e1ba8ac28ac4ad709ff06fea48241ef34753ee2896813b43a24fa`
- Resend credentials and Stripe credentials were present in the Dead Hidden live-site env. Secret values were not printed.
- Recent Resend sent-history check for `birdie6463@yahoo.com` returned no recent matches before this send.
- Live Stripe customer/search evidence for `birdie6463@yahoo.com`:
  - `cus_UYShVjsaCNTUsI`, Wallace Stuart, created 2026-05-21.
  - `cus_URa1UXFphaPyCi`, Wallace Stuart, created 2026-05-02.
- Live Stripe checkout session matching Wallace's stated May 21 / $18 payment:
  - Session `cs_live_a1lTI2KgicDucZj8xZLxWYmRaRXAlNuTbFxPQajhvfS1X5XV1hNFPLhcSN`
  - Created `2026-05-21T01:49:07Z`
  - Amount `1800`, paid, email `birdie6463@yahoo.com`
  - Line item: `Not Enoch: Seven Bible Proofs the Book Is Not Scripture (Pre-Order)`
  - Metadata: `booklet=not-enoch`, `brand=deadhidden`, `product_type=presale`, `ship_target=2026-06-03`
- Additional live Stripe evidence:
  - 2026-05-22 $10 paid checkout under same email for `Where the Bible Came From (Pre-Order)`.
  - 2026-05-02 $29.99 paid checkout under same email for FaithWall Founding Family Individual.
- No live Stripe checkout/session evidence found that the May 21 $18 payment was The Plain Bible Manual.
- Targeted artifact search found no final Not Enoch PDF. It did find `Where the Bible Came From - Review Draft.pdf`, but `GUIDE-STATUS.md` says that draft must not be attached or fulfilled yet.

## Action

Sent Wallace a short plain support email through Resend:

- To: `birdie6463@yahoo.com`
- From: `Adam at Dead Hidden <adam@deadhidden.org>`
- Reply-to: `thebiblicalman1611@gmail.com`
- Subject: `Re: The Plain Bible Manual download`
- Resend ID: `57fdbcc8-8e02-4fc1-b7c6-b2ddce571c4a`
- Post-send Resend check: `last_event=delivered`
- Attachment: The Plain Bible Manual PDF from `/Users/adamjohnsson/openclaw/dh-store/blob/the-plain-bible-manual.pdf`

Customer-facing copy apologized for the silence, stated that the May 21 $18 checkout appears as the Not Enoch preorder rather than The Plain Bible Manual, attached The Plain Bible Manual anyway so he was not stuck, and said he did not need to pay again.

Draft/body artifact:

- `/Users/adamjohnsson/Documents/Codex/2026-06-11/there-is-a-new-update-for/work/wallace-stuart-plain-bible-rescue-email.txt`

## Follow-up Risk

Wallace's real May 21 purchase appears to be the Not Enoch preorder, with a stated ship target of 2026-06-03, and no final Not Enoch PDF was found in targeted local searches. Treat this as an overdue preorder fulfillment/support risk, separate from today's goodwill Plain Bible Manual attachment.
