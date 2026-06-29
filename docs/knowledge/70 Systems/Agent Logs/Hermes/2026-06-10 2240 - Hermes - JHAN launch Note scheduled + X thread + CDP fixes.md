# 2026-06-10 22:40 CT — Hermes — JHAN launch: 7 AM Note scheduled, X thread drafted, CDP breakage patched

## Launch package for "Jesus Has a Number" (DH, post 201544405, publishes 2026-06-11 07:00 CT)

**Substack Note — fires 7:00 AM CT 2026-06-11**
- Poster script: `/Users/adamjohnsson/Hermes-Workspace/bin/post-jhan-launch-note.py`
- Posts via Substack native API (`/api/v1/comment/feed`) through Comet CDP (port 9223), as user **Dead Hidden (@deadhidden, id 218038831)** — probe verified 22:36 CT.
- Includes link-card attachment for the post URL (r=3ltbu7 share link Adam supplied).
- Idempotent: marker at `~/.hermes/state/jhan-launch-note-posted.json` blocks double-posts.
- Two triggers, either can fire safely:
  1. Hermes one-shot cron `98b0e0e5` (session-bound)
  2. launchd backstop `com.adam.jhan-launch-note` (self-removes after success) — loaded, verified in `launchctl list`
- Log: `~/.hermes/logs/jhan-launch-note.log`

**X thread** — drafted (3 posts + link self-reply), modeled on the Genesis 5 / 777 tweet (2064761812306850037: 71.5K impressions, 155 bookmarks vs 160 likes in ~5h; anatomy = skipped-thing hook → number shock → open loop; link isolated in a near-bare self-reply). Delivered to Adam on Telegram for approval/paste. NOT posted.

## Infrastructure faults found and fixed
1. **Chrome 149 rejects CDP over `127.0.0.1`** — only answers `Host: localhost`. Patched `~/.hermes/bin/substack-notes-auto-poster` DEFAULT_CDP → `http://localhost:9222` (backup: `substack-notes-auto-poster.bak-20260610`).
2. **Chromium now requires PUT for `/json/new`** — poster's tab-open used GET (405). Patched `urlopen_json` to support method, tab-open now PUT.
3. **WriteStack path dead for DH**: Chrome's WriteStack account only proves handle `biblicalman`; Comet's WriteStack session is logged out entirely. DH Note scheduling via WriteStack is currently impossible — hence the native-API route above.

## Faults flagged, NOT fixed
- **Pinterest Notes Factory is silently dead since Jun 9.** Pack dir (`50 Outputs/Substack Notes/Pinterest Factory/`) is empty (recreated 2026-06-09 05:50). The 6 AM checker logs "pack ready" but no file exists; poster then errors "Pack does not exist." No factory Notes have posted for 2 days. Needs checker diagnosis + WriteStack DH re-login (or migration to the native-API method proven tonight).

— Hermes
