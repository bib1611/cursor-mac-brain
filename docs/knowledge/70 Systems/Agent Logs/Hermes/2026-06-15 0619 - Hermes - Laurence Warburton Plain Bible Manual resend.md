# Customer Resend — Laurence Warburton — The Plain Bible Manual

Date: 2026-06-15 06:19 CDT
Agent: Hermes (Telegram, Adam-directed "fix it")
Channel: Proton watcher alert -> Gmail thread

## Issue
Laurence Warburton (laurencewarburton@gmail.com) replied to "THE PLAIN BIBLE MANUAL — Your Download Is Ready" (orig 23 May 2026 from adam@deadhidden.org): "Can you resend the link please mine has expired."

## Verification
- Buyer proof: received automated fulfillment email 23 May (fires only post-purchase).
- Gmail thread id 19eca4fb1ed04b59 (unread in inbox).
- Stripe (Dead Hidden acct): 0 customers/charges for his email. Plain Bible Manual is a Biblical Man product (prod_UUyKXzC53I3ec2), so purchase sits on the BM Stripe account, not DH. /api/resend-downloads returned not_found for that reason (no productSlug on the BM Payment Link session).
- Permanent blob link verified live (HTTP 200, PDF): https://vpfbq42gh0ucnfvw.public.blob.vercel-storage.com/the-plain-bible-manual.pdf

## Action
- Sent fresh permanent download link via Resend production rail.
- From: Dead Hidden <noreply@thebiblicalmantruth.com>, reply-to support@deadhidden.org
- Subject: Re: THE PLAIN BIBLE MANUAL — Your Download Is Ready
- Resend message id: 65c435c6-2e41-43f2-99f3-a9e01b13b719 (accepted)
- No refund, no money action. Single targeted resend, Adam-approved.

## Loose end
- A Gmail draft reply (id r4852651877151700414) was created in thebiblicalman1611@gmail.com before falling back to Resend. Harmless but unsent; delete if you want it tidy (Gmail MCP has no delete-draft tool).
