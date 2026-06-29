# 2026-06-17 0754 - Codex - Plain Bible Vault sequence wiring

Adam attached Okara's Plain Bible Manual CRO audit. Codex treated it as a second-opinion prompt, verified the relevant local repo paths, and implemented the smallest local fixes.

Modified:

- `/Users/adamjohnsson/code/deadhidden/src/app/store/the-plain-bible-manual/page.tsx`
- `/Users/adamjohnsson/code/deadhidden/src/app/api/webhook/route.ts`
- `/Users/adamjohnsson/code/deadhidden/src/lib/email.ts`

Changes:

- Removed the bottom Field Files bundle cross-sell from the Plain Bible Manual page so the page closes on the $10 Manual CTA and P.S. instead of a $39 detour.
- Wired `sendPlainBibleVaultUpgradeSequence` into the Stripe webhook for non-presale `the-plain-bible-manual` purchases.
- Added a third day-5 Plain Bible-to-Vault email with direct $365 / 83-resource / lifetime-access math.

Verification:

- `npm run lint -- src/app/api/webhook/route.ts src/lib/email.ts src/app/store/the-plain-bible-manual/page.tsx` passed.

Addendum - 2026-06-17 07:57 CDT:

- Tightened the Plain Bible Manual post-purchase sequence copy after the Okara review.
- Email 1 is now confirmation/deployment only with no Vault mention.
- Email 2 now plants the Vault by naming related resources without price or checkout CTA.
- Email 3 now carries the direct Vault offer with the $10-to-$365 math and a single CTA.
- Updated the email HTML helper so CTAs are optional for the first two emails.
- `npm run lint -- src/lib/email.ts src/app/api/webhook/route.ts src/app/store/the-plain-bible-manual/page.tsx` passed.

Addendum - 2026-06-17 07:57 CDT, Okara line edit pass:

- Removed the `Friend,` salutation from day 1/day 3 copy and HTML.
- Replaced `first win` language with direct action framing.
- Flattened day 3 doorway/behind-it wording into direct shelf/resource language.
- Replaced `break in one place` with `confusion rarely sits in one place`.
- Removed `their shame` from the concrete problem list.
- Changed day 5 subject to `The Vault. $365. Lifetime.`
- `npm run lint -- src/lib/email.ts src/app/api/webhook/route.ts src/app/store/the-plain-bible-manual/page.tsx` passed.

Boundary:

- No deploy, commit, Stripe/customer/money action, Resend send/broadcast/manual email, Substack/X publish, credential change, or live account mutation performed.
