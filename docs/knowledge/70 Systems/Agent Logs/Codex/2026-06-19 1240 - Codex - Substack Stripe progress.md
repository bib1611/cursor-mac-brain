# Codex Receipt - Substack Stripe Progress

Created: 2026-06-19 12:40 CDT
Agent: Codex
Task: Check how Dead Hidden and Biblical Man Substacks are doing today and pull Stripe numbers.

## Summary

Ran a read-only revenue/engagement sweep.

Saved report:

`/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-19-1239-substack-stripe-progress.md`

## Verification

- Biblical Man private publisher stats loaded through authenticated Substack `post_management/published`.
- Biblical Man roll-call post currently shows `25,314` delivered, `2,776` unique openers, `26` clickers, `79` publisher-stat comments, `2` paid upgrades, and `$60` estimated Substack value.
- Dead Hidden public post JSON for `The Kingdom They Flattened` showed the post live with `10` reactions, `3` comments, and `3` restacks.
- Live Stripe aggregate read through `/Users/adamjohnsson/.agents/bin/dh-with-env` using `STRIPE_KEY_DH` and `STRIPE_KEY_BM` showed combined today gross `$233.00`, `15` successful charges, `$0.00` refunds, and `$201.67` sales net before financing/payout ledger effects.

## Boundary

Read-only only. No Substack edit/send/post, no Stripe/customer/money mutation, no checkout/session creation, no email, no deploy, no Linear/Notion write, no credential/account setting change, and no customer/payment private data printed.
