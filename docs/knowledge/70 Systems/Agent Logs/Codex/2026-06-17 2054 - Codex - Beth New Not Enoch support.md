# Beth New Not Enoch Support

Date: 2026-06-17 20:54 CDT
Agent: Codex

Adam asked Codex to help Beth with a support email asking about a $14 preorder from May 20 and alternate email `bethnew@kc.rr.com`.

Verified live Stripe:

- Checkout Session: `cs_live_a1rmtuinX99NfNk7zvhf3NvkjdvX94JCvEHhiJoxRxAAWA4i6QbutWMyf0`
- Created: 2026-05-21 01:41:51 UTC, which is 2026-05-20 CDT
- Amount: $14.00 USD
- Status: complete / paid
- Customer: Beth New
- Checkout email: `bethnew.usa@gmail.com`
- Product: `Not Enoch: Seven Bible Proofs the Book Is Not Scripture (Pre-Order)`
- Product metadata: `booklet=not-enoch`, `product_type=presale`, `ship_target=2026-06-03`

Checked local repo and receipts:

- `not-enoch` remains in the preorder slug set in `src/app/api/download/route.ts`, `src/app/api/success/route.ts`, `src/app/api/resend-downloads/route.ts`, and `src/app/api/webhook/route.ts`.
- No final Not Enoch PDF/download file was found in the live delivery path during this support pass.
- Prior receipt in `RECEIPTS.md` already flagged Not Enoch as overdue/no final PDF found during Wallace Stuart support on 2026-06-11.

Sent support email through Resend:

- To: `bethnew.usa@gmail.com`, `bethnew@kc.rr.com`
- Subject: `Re: Not Enoch preorder`
- Resend ID: `70c969d2-0e61-4081-a209-5425d3e94fb4`

Email told Beth:

- Her $14 preorder was found.
- It was for Not Enoch.
- It is recorded under `bethnew.usa@gmail.com` from May 20.
- The booklet is still not finished and missed the early-June target.
- She does not need to buy it again.
- Both emails are now included on the support note.

Boundary:

- No refund.
- No Stripe/customer/money-state mutation.
- No product-page edit.
- No deploy.
- No public post.
- No Linear write.
