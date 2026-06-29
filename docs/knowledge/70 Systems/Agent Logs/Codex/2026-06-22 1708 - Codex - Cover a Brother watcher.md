# 2026-06-22 1708 CDT - Codex - Cover a Brother Watcher

Adam asked Codex to build a read-only "Cover a Brother" campaign watcher that polls Substack post comments, Substack Notes replies, and X campaign tweet replies every 15 minutes, dedupes seen comment IDs, classifies new comments, and writes private ready-to-send drafts. Adam sends every reply himself.

Built:

- Script: `/Users/adamjohnsson/.deadhidden-os/ops/bin/cover-a-brother-watch`
- Config: `/Users/adamjohnsson/.deadhidden-os/ops/config/cover-a-brother-watch.json`
- LaunchAgent: `/Users/adamjohnsson/Library/LaunchAgents/com.deadhidden.cover-a-brother-watch.plist`
- Digest directory: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/cover-a-brother/`
- Seen file: `/Users/adamjohnsson/.deadhidden-os/ops/state/cover-a-brother-seen.json`
- Logs: `/Users/adamjohnsson/.deadhidden-os/ops/logs/cover-a-brother-watch.log`

Safety boundary:

- Read/classify/draft only.
- No DM, reply, email, post, checkout, Stripe, customer, deploy, or account-setting action exists in the script.
- The pocket assistance code is used only in private CANT_AFFORD digest drafts.
- INTERESTED drafts use the public campaign discount code and campaign shelf link.
- Source failures are logged and do not crash the run.
- X conversation replies page through `next_token`.
- Substack Notes uses Adam's profile reader feed `/api/v1/reader/feed/profile/169765767` and pages through `nextCursor`.

Current state:

- Launchd installed and loaded with `StartInterval` 900 seconds.
- The Biblical Man "Cover a Brother" launch post is enabled: post id `203161465`, `https://biblicalman.substack.com/p/cover-a-brother`.
- Dead Hidden post, Substack Note IDs, and X campaign tweet ID are still disabled because no matching source IDs were found in read-only discovery on 2026-06-22.
- X authenticated account verified as `@Biblicalman`; `@thebiblicalman1611` is not a valid X username.

Verification:

- `cover-a-brother-watch --self-check` passed.
- `python3 -m py_compile /Users/adamjohnsson/.deadhidden-os/ops/bin/cover-a-brother-watch` passed.
- `plutil -lint /Users/adamjohnsson/Library/LaunchAgents/com.deadhidden.cover-a-brother-watch.plist` passed.
- `launchctl print gui/501/com.deadhidden.cover-a-brother-watch` showed `run interval = 900 seconds`.
- `launchctl kickstart -k gui/501/com.deadhidden.cover-a-brother-watch` returned cleanly.
- `launchctl print` after the final kickstart showed `runs = 2`, `last exit code = 0`, and `run interval = 900 seconds`.
- Live BM-post dry run returned `new_total=0 errors=0 digest=not_written`.
- Final launchd kickstart wrote `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/cover-a-brother/cover_a_brother_digest_20260622.md`.
- Log proof: `2026-06-22T17:12:56.149156-05:00 new=0 cant_afford=0 errors=0 digest=/Users/adamjohnsson/.deadhidden-os/ops/artifacts/cover-a-brother/cover_a_brother_digest_20260622.md`

Activation:

Edit `/Users/adamjohnsson/.deadhidden-os/ops/config/cover-a-brother-watch.json`, fill the exact Dead Hidden post id, Substack Note root ids, and X campaign tweet id, then set those sources to `enabled: true`.
