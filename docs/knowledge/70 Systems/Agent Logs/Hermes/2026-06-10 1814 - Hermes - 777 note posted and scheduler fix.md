# 777 Note posted + notes-scheduler rescue — 2026-06-10 18:14 CDT

- Posted fresh DH Note (Jude 1:14 "counts out loud" angle) for the 777 paid post via fixed pipeline.
- Note id 274147548 — https://substack.com/@deadhidden/note/c-274147548 — verified live (200, body renders, post card attached).
- Scheduler had been crashing every minute since ~16:45: `KeyError: slice(None,300,None)` in runner.py page_fetch fallback masked the real failure, `TypeError: Failed to fetch` — all Comet tabs were on deadhidden.substack.com, Notes API requires substack.com origin (CORS).
- Fixes in `~/.deadhidden-os/notes-scheduler/runner.py`: exceptionDetails surfaced, dict-safe fallback, alive-checked tab selection, auto-create background substack.com tab via CDP /json/new.
- Queue repairs: missed 16:45 wallpaper note → 2026-06-11 06:00; Option A image note 18:30 → 18:55 (anti-stacking with the 18:10 note).
- Remaining fires: 18:55 (image), 19:30, 20:45, 21:20, 02:00, 06:00 — launchd cron runs the fixed code every minute.
