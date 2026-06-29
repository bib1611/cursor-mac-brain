# 2026-06-19 06:28 CDT - Codex - Robb dispute and Lisa Substack delivery

## Robb Foote dispute

- Screenshot dispute: `du_1TjsTh2ssWnFQsRYi918O5M2`, customer Robb Foote, `$47`, reason `Product unacceptable`, evidence due `2026-07-29`.
- Gmail purchase/support trail identifies the `$47` item as the legacy SamCart recurring subscription for **The Biblical Man Blueprint**, not a physical/damaged product.
- Key proof found in Gmail:
  - SamCart sale email for Robb: Order `#21407503`, original order date `2025-06-07`, product `The Biblical Man Blueprint`, initial `$27.00`, then `$47.00 monthly starting in 1 week`.
  - Subscription charge reminder: Subscription `#4268464`, next `$47` charge due `2025-10-14`, The Biblical Man.
  - Robb support thread from `2025-11-20`: he said he was still charged `$47 every month` for the Blueprint while a Vault member.
  - Robb forwarded SamCart support on `2025-11-21`: SamCart could not locate the subscription under his name/email and told him seller/card issuer routes were needed; Robb said he disputed through MasterCard and received a `$47` credit.
- Local Stripe API checks against available local keys (`STRIPE_KEY_DH`, `STRIPE_KEY_BM`, `STRIPE_SECRET_KEY`) all returned `404 No such dispute` for `du_1TjsTh2ssWnFQsRYi918O5M2`, so the dispute is not visible to the current local Stripe keys. It likely belongs to another Stripe account/dashboard path or legacy rail.

## Lisa Napolitano Substack delivery

- Screenshot email: Lisa says she is a `$5 monthly` Biblical Man subscriber, changed from the old Outlook email to the new Outlook email, and stopped receiving posts.
- Substack publisher record for the new email:
  - `membership_state`: `subscribed`
  - Stripe subscription: `active`
  - Plan: `$5/month`
  - Amount paid: `$75.00`
  - Expiry: `2026-07-29`
  - `unsubscribed_at`: `null`
  - `paused`: `false`
  - `email_disabled`: `true`
  - `email_disabled_at`: `2026-06-09T12:31:06.844Z`
  - `num_emails_received_last_7d`: `0`
  - `num_emails_received_last_30d`: `26`
- Old email lookup returned `404 User not found` in the current Substack subscriber endpoint; the new email is the active paid record.
- Event log shows she received `The Signs of a Christian Cult` on `2026-06-09T12:12:26Z`, opened it, then Substack logged `Disabled emails` at `2026-06-09T12:31:06Z`. Later opens/clicks came from that same delivered email, but no delivery has occurred since.
- Attempted the non-billing publisher re-add path with `sendEmail:false`; Substack returned `200`, but the subscriber record still showed `email_disabled: true`. No welcome email was sent and no billing state changed.
- Conclusion: she is still an active paid subscriber, but Substack has her email delivery disabled as a reader notification setting. Publisher-side re-add did not override it; she likely needs to re-enable emails from her own Substack email/preferences/account page, or Adam can send her a direct support reply with that instruction.

## Boundary

- No refund accepted or issued.
- No dispute evidence submitted.
- No Stripe/SamCart billing mutation performed.
- Customer email later sent to Lisa from `thebiblicalman1611@gmail.com` at `2026-06-19 06:32 CDT`; Gmail send id `19edfa71e5d8a4fc`.
- One Substack publisher `subscriber/add` call was attempted with `sendEmail:false`; verification showed no billing change and `email_disabled` remained true.
