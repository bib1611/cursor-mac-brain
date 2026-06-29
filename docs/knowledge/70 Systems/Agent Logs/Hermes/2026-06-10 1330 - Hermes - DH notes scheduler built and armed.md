# 2026-06-10 13:30 — Hermes — DH Notes scheduler built and armed

## What Adam asked
Schedule 7 Substack Notes today on Dead Hidden pushing the paid post "Noah's Father Died at 777" at WriteStack-suggested times: 2:05p, 6:20p, 6:30p (approved option A note + ark image), 7:30p, 8:45p, 9:20p, 2:00a. Check lapsed WriteStack for metrics if possible.

## What was built
- `/Users/adamjohnsson/.deadhidden-os/notes-scheduler/runner.py` — posts queued Notes at fire time through the logged-in Comet session (CDP 9223) via Substack internal API (`/api/v1/comment/feed`). Handles post-card link attachments and image attachments (base64 upload to `/api/v1/image`). Lock file prevents double-posts. Logs to `post.log`.
- `/Users/adamjohnsson/.deadhidden-os/notes-scheduler/queue.json` — 7 notes, 7 distinct angles (Methuselah clock, Genesis-5 wallpaper, option A w/ image, two Lamechs vs Matt 18:22, Luke 3's 77 names, angel-numbers counterfeit, "which list is your name on"). All attach the 777 post card. Voice-DNA pre-flight passed on each.
- `~/Library/LaunchAgents/com.deadhidden.notes-scheduler.plist` — launchd agent, StartInterval 60. Loaded via `launchctl bootstrap gui/501`, verified in `launchctl list`. (crontab installs were silently blocked by macOS TCC — launchd used instead.)

## Verified this session
- Authenticated POST to Substack from page context works: link attachment created (id 3c89652c-…), image attachment created (id a17a6aef-…) from `~/Desktop/777-note-option-A.jpg`.
- Live 777 post URL confirmed via archive API: https://deadhidden.substack.com/p/noahs-father-died-at-777 (only_paid).
- Runner live-ran as a clean no-op with nothing due; 7 pending in queue.
- Hermes one-shot crons: f7a26037 (2:12 PM — verify first fire, auto-repair + alert on failure), c844d594 (7:18 AM tomorrow — per-note engagement + Stripe conversion report).

## WriteStack check
writestack.io/dashboard → 404; app.writestack.io → dead Vercel deployment (DEPLOYMENT_NOT_FOUND). No metrics retrievable on the lapsed account. Adam's stated times used as given.

## Dependencies / risk
- Comet must stay running with a logged-in substack.com tab on port 9223 for fires (incl. 2:00 AM). Mac mini is always-on; Comet has been up since yesterday.
- 6:20p + 6:30p double-drop is 10 min apart per Adam's explicit times — flagged in report to him.
