# 2026-06-19 08:51 CDT - Codex - TBM rollcall public replies and reader database

Adam asked that roll-call commenters receive short public replies as well as personal emails, using the Comment King training, with no long AI essays and no self replies. Adam clarified: no self replies.

Codex patched `/Users/adamjohnsson/.deadhidden-os/ops/bin/tbm-rollcall-watch` to add direct Substack public replies through `POST /api/v1/post/202711652/comment` with `parent_id` set to the reader comment id. The script now builds Substack `bodyJson` from the same ProseMirror shape returned by the comments endpoint, ignores Adam/Biblical Man author comments during fetch, and never creates a parentless anchor reply. The script also now stops public posting after a retryable `429` and defaults to one public reply per run so Substack is not hammered.

Codex created the new reader database `/Users/adamjohnsson/.deadhidden-os/ops/data/tbm-readers.sqlite3` with `readers`, `reader_events`, and `public_reply_queue`. It stores inbound Substack comments, outbound public replies, and outbound email interactions from the existing outreach queue. Future private emails are held until the public reply for that comment is `sent` or intentionally `coalesced`, preserving the requested order: public reply first, then email.

Codex patched `/Users/adamjohnsson/Library/LaunchAgents/com.biblicalman.tbm-rollcall-watch.plist` to keep `StartInterval=300` and add:

- `TBM_ROLLCALL_POST_PUBLIC_REPLIES=1`
- `TBM_ROLLCALL_MAX_PUBLIC_REPLIES_PER_RUN=1`
- `TBM_ROLLCALL_PUBLIC_REPLY_UNTIL=2026-06-20T01:08:16.999774+00:00`

Launchd was reloaded and verified with `run interval = 300 seconds`, public replies enabled, emails enabled, and last exit code `0`.

Live public child replies posted and verified under reader comments:

- Jordan Branscombe: `279076311`
- Craig: `279076696`
- Arty Gallegos: `279076701`
- marilyn: `279076704`
- Marilyn: `279077369`
- Brigette Langford: `279080675`
- Lila: `279084117`
- John W. Irwin: `279087723`
- Bambi Harding: `279091002`

As of 08:54 CDT, queue state in `/Users/adamjohnsson/.deadhidden-os/ops/data/tbm-readers.sqlite3` is `sent=9`, `queued=12`. Queued public replies include Nicky's access issue, Inogame, BenRoberts, Sara Anderson, Elizabeth Suess, Gloria I Long, JJ789, Scott Hinton, Leon, and Harry's prayer comment. Nicky's two simpler comments are planned to be covered by the one access-side public reply. Harry's comment uses the prayer-specific short reply rule: `Amen, Harry. That is the right spirit. Men praying for one another is not a side issue.`

Verification:

- `/Users/adamjohnsson/homebrew/bin/python3 /Users/adamjohnsson/.deadhidden-os/ops/bin/tbm-rollcall-watch --self-test` passed.
- `plutil -lint /Users/adamjohnsson/Library/LaunchAgents/com.biblicalman.tbm-rollcall-watch.plist` passed.
- Substack comment fetch verified posted replies as child comments with `ancestor_path` pointing to reader comment ids.
- LaunchAgent print verified `TBM_ROLLCALL_POST_PUBLIC_REPLIES=1`, `TBM_ROLLCALL_MAX_PUBLIC_REPLIES_PER_RUN=1`, `TBM_ROLLCALL_SEND_EMAILS=1`, and `run interval = 300 seconds`.

Boundary: Substack public child replies to actual commenters, local watcher/database changes, Resend/email queue ordering change, and receipts only. No parentless self replies, no Substack post/settings edit, no X post, no Stripe/customer/money mutation, no refund, no Vault file/access send, no deploy, no Linear write, and no Notion write were performed.
