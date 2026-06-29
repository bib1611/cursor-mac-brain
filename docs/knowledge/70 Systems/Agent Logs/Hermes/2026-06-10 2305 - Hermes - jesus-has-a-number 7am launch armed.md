# Jesus Has a Number — 7 AM launch fire armed

Date: 2026-06-10 23:05 CT
Agent: Hermes (Telegram operator)
Approved by: Adam, same-thread Telegram (note at post time + 4-post X thread via xurl)

## What fires at 7 AM CT on 2026-06-11

- Post: https://deadhidden.substack.com/p/jesus-has-a-number — scheduled in Substack by Adam for 7:00 AM.
- Substack Note (DH): posted via Substack API through Comet CDP 9223 (`post_note.py --live`). Link attached as card with Adam's share URL (r=3ltbu7). Auth probed OK tonight (/api/v1/settings = 200).
- X thread: 4 tweets via xurl from @Biblicalman (`post_thread.py`). Modeled on the Genesis 5 thread (2064761812306850037, 72K impressions, 157 bookmarks in 5h): curiosity hook, no link until final self-reply. Link only in tweet 4.

## Triggers

- Primary: Hermes session cron `8bbcbd5e` @ 7:01 — verifies post live (200), runs both scripts, messages Adam, writes receipts. Session-bound: dies if gateway restarts.
- Backup: launchd `com.adam.jhan-backup-fire` @ 7:05 — same scripts, idempotent guards (NOTE-RESULT.json / THREAD-RESULT.json) prevent double-posting. Self-disarms after run.

## Artifacts

`/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-11-jesus-has-a-number-launch/`
THREAD.json, post_thread.py, post_note.py, schedule_note.py (WriteStack path, blocked), backup_fire.sh.

## Infrastructure findings (needs follow-up)

1. `com.adam.substack-notes-auto-poster` (6 AM daily) has scheduled ZERO notes since at least 2026-06-04. The checker logs "pack ready" but the pack file (`50 Outputs/Substack Notes/Pinterest Factory/<date> - Pinterest Notes Pack.md`) never exists on disk — the entire Pinterest Factory directory is missing from the vault. Silent daily failure.
2. WriteStack in Chrome (9222) is single-author, byline `biblicalman` — Dead Hidden notes are blocked on that session.
3. Comet (CDP 9223, DH profile) has no authenticated WriteStack session, but its substack.com session is authenticated — direct Substack API is the working DH Notes path.
