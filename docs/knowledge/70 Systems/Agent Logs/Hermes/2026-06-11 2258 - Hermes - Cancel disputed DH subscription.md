# Cancel disputed DH subscription

- Date: 2026-06-11 22:58 CDT
- Action: Canceled Stripe subscription `sub_1TUEitLN6IypHVMVoJ606qlL` on the Dead Hidden Stripe account.
- Customer: `cus_UTB5Ye7cD7JMnA` (gwhohmann)
- Why: Subscription was past_due with a dead card; its $8 charge is under chargeback (dispute `du_1ThLBKLN6IypHVMVH7QeBZfz`, evidence submitted 2026-06-11, status under_review). Canceling stops retry attempts and prevents a second dispute.
- Approval: Adam, same Telegram thread — "Cancel it".
- Proof: Stripe API DELETE returned `status: canceled`, `canceled_at: 1781236718`.
- Open loop: dispute ruling from Capital One expected in 60–75 days. No action needed until Stripe emails a result.
