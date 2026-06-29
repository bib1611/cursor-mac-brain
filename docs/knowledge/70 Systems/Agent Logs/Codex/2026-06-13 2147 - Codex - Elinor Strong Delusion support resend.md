# Codex Receipt - Elinor Strong Delusion Support Resend

Date: 2026-06-13 2147 CDT
Owner: Codex
Lane: Dead Hidden customer care / digital delivery

## Customer

- Name: Elinor Fischer
- Email: elinfischer@icloud.com
- Gmail thread: `19eb04b68868f8cf`
- Customer message: asked whether "part 2" had been sent because she did not receive it.
- Subject: `Re: Your Field File. Read it tonight.`

## Verification

- Product in original receipt: `THE STRONG DELUSION`
- Amount: `$9.00`
- Checkout session: `cs_live_a1uUMCms6KadzUUK0qBqlKkVuK0YbEfvWL8tKZf8fcWUebMEePT7Kr2ATY`
- Live success page: `https://deadhidden.org/success?session_id=cs_live_a1uUMCms6KadzUUK0qBqlKkVuK0YbEfvWL8tKZf8fcWUebMEePT7Kr2ATY` returned HTTP 200.
- Live success API resolved the session to:
  - product: `THE STRONG DELUSION`
  - slug: `the-strong-delusion`
  - customerEmail: `elinfischer@icloud.com`
  - amountTotal: `900`
  - file URL: `/api/serve/the-strong-delusion?session_id=cs_live_a1uUMCms6KadzUUK0qBqlKkVuK0YbEfvWL8tKZf8fcWUebMEePT7Kr2ATY`

## Files Sent

- `/Users/adamjohnsson/code/deadhidden/public/product-files/the-strong-delusion.pdf`
  - sha256: `fbe550db36c4afdff76625ce9f8a89e8b3008dd31b1f7cf23bc944f7b9077943`
- `/Users/adamjohnsson/code/deadhidden/public/product-files/the-strong-delusion-print.pdf`
  - sha256: `26c1a25778fddef065e23a3a9dbc55c7d0cbf328f2d0eab192f8f0bf0ef37eb2`

## Action Taken

- Replied in the existing Gmail thread as Sarah from Dead Hidden customer care.
- Sent from authenticated Gmail account shown by connector as `Biblical Man <thebiblicalman1611@gmail.com>`.
- To: `elinfischer@icloud.com`
- Gmail sent message ID: `19ec40620a08780d`
- Gmail sent message labels: `SENT`
- Gmail verification confirmed `has_attachment=true` with both PDF attachments present:
  - `the-strong-delusion.pdf`
  - `the-strong-delusion-print.pdf`

## Sent Body

```text
Hi Elinor,

Sarah here from Dead Hidden customer care.

I'm sorry this did not land cleanly for you. I checked the thread and the safest fix is to put the file directly in your hands here.

Your Field File download link is still active:

https://deadhidden.org/success?session_id=cs_live_a1uUMCms6KadzUUK0qBqlKkVuK0YbEfvWL8tKZf8fcWUebMEePT7Kr2ATY

I also attached both copies for you:

- The Strong Delusion Field File
- The printer-friendly copy

If that link expires before you need it again, use this page and it will resend the download to your email:

https://deadhidden.org/resend-downloads

If you were looking for the next update/section and it still does not show up, reply here and I'll refresh it for you.

Sarah
Customer Care
Dead Hidden
```

## Boundaries

- No refund issued.
- No Stripe mutation performed.
- No customer/account/product mutation performed.
- This was a delivery/access fix only.
