# 2026-06-19 08:58 CDT - Codex - TBM support agent email identity

Adam clarified that deeper customer-service emails should not identify as Adam. Going forward, the roll-call watcher should identify as a team helper, using Sam or Sarah, and escalate money/Adam-specific issues for Adam's eyes.

Codex patched `/Users/adamjohnsson/.deadhidden-os/ops/bin/tbm-rollcall-watch` so future private follow-up emails draft as `Sam`, a Dead Hidden / Biblical Man support helper. The default Resend display name is now `Sam at Dead Hidden <adam@deadhidden.org>`. Donation/payment uncertainty now says Sam will get the details in front of Adam; access and missing-email cases stay with support unless they need Adam.

Already-sent Adam-signed messages were not changed or resent. Current unsent queue state before the next run: `ready_for_review=6`, `sent=15`; those future sends will be re-drafted at send time with Sam's identity after their public replies are sent or coalesced.

Verification: `/Users/adamjohnsson/homebrew/bin/python3 /Users/adamjohnsson/.deadhidden-os/ops/bin/tbm-rollcall-watch --self-test` passed.

Boundary: local watcher email-copy/default-from change and receipt only. No email was sent during this patch, no public reply was posted, no Stripe/customer/money mutation, no Substack post/settings edit, no X post, no deploy, no Linear write, and no Notion write were performed.
