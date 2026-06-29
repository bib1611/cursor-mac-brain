# 2026-06-10 0720 - Codex - Bravera Stripe Count Number Launch Prep

Adam re-opened the Stripe/Bravera issue and clarified that the new guide should be a Bible-numbers/numerology guide from the Ruckman source lane in Google Drive. Adam also asked Codex to use Hermes / Claude Fable 5 as support while Codex stayed the harness.

## Live Verification

- Chrome showed Adam logged into Bravera Bank and Biblical Man/Adam Stripe surfaces.
- Stripe Capital dashboard showed a pending `$1,066.95` debit to meet the loan minimum, with the financing marked in progress and past due.
- Bravera dashboard showed the relevant business/free checking accounts by last four; no money movement or account settings were changed.
- Official Stripe Capital docs confirm that loan minimum shortfalls can be automatically debited from a linked bank account or account balance.
- Official Bravera contact page was refreshed for the phone/support path.
- Nacha unauthorized-return guidance was refreshed for ACH-block/return wording.

## Fable Use

Codex used Hermes Fable 5 as a bounded advisor and audit lane. Fable recommended:

- Treat the Stripe debit as likely Capital minimum-shortfall mechanics until Stripe says otherwise.
- Do not ask Bravera to return the Stripe Capital ACH before getting a written Stripe answer on consequences.
- Handle the unknown recurring CFG debit separately by asking Bravera for originator/company ID, trace details, ACH block options, fee/expiration terms, and return eligibility.
- Position the guide as original Biblical Man work, not a Ruckman reprint or transcript.
- Use `Count the Number` as the launch title, `$10` launch price, slug `count-the-number`.

## Artifacts

- `/Users/adamjohnsson/Documents/Codex/2026-06-10/i-was-working-on-having-you/outputs/bravera-stripe-ach-action-packet.md`
- `/Users/adamjohnsson/Documents/Codex/2026-06-10/i-was-working-on-having-you/outputs/numerology-guide-launch-packet.md`
- `/Users/adamjohnsson/Documents/Codex/2026-06-10/i-was-working-on-having-you/outputs/count-the-number-manuscript.md`
- `/Users/adamjohnsson/Documents/Codex/2026-06-10/i-was-working-on-having-you/outputs/count-the-number.pdf`
- `/Users/adamjohnsson/Documents/Codex/2026-06-10/i-was-working-on-having-you/work/render_count_the_number_pdf.py`

## Repo Changes Staged Locally

Repo: `/Users/adamjohnsson/code/deadhidden`

- Added local product PDF: `public/product-files/count-the-number.pdf`
- Added static download mapping for `count-the-number` in `src/app/api/serve/[slug]/route.ts`
- Added product catalog entry in `src/data/products.ts`

Verification:

- `npm run audit:store-routing` passed.
- `npm run audit:slugs` passed with existing warn-only stale-reference warnings.
- `npm run build` passed.
- Local dev server running at `http://localhost:3020`.
- Local product page `http://localhost:3020/store/count-the-number` returned 200 and visually rendered the title, price, CTA, launch price, and FAQ.
- Static PDF URL `http://localhost:3020/product-files/count-the-number.pdf` returned 200.

## Boundary

No Bravera transfer, ACH return, ACH block, Stripe setting change, Stripe checkout-session creation, customer email/message, Substack/X publish, production deploy, or external send was performed. The guide launch is prepared locally only and still requires Adam's explicit approval before any live public or money-connected action.
