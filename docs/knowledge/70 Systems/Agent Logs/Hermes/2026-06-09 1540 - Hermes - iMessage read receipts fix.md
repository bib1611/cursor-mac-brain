# iMessage read receipts — diagnosed and verified working (2026-06-09 15:40)

## Symptom
Adam's iMessages stopped showing "Read" after the midday gateway outage/fix session.

## Findings
- Mark-read feature shipped Jun 8 ~22:13–22:25 (adapter `_schedule_mark_read` + sidecar `/read` + `PHOTON_MARK_READ_ON_INBOUND=true` in `~/.hermes/.env`). Worked this morning.
- It ran SILENTLY on success — zero log lines, undiagnosable.
- Adam's 15:18–15:19 ping exchange ran during the restart-churn window (stale sidecar pair). No inbound at all arrived after the clean 15:25:48 restart, so mark-read never got a chance to fire on the fixed stack.
- Verified live: sidecar `/read` returns ok (spectrum-ts remote `chats.markRead`, supported in remote mode).

## Changes
- `plugins/platforms/photon/adapter.py`: INFO-level logging on mark-read scheduled / ok / skipped / disabled (was silent or debug-only).
- Gateway restarted via `launchctl kickstart -k gui/501/ai.hermes.gateway` at 15:35:26 — stale-sidecar eviction fired correctly, single clean sidecar.

## Proof
- 53/53 Photon tests pass.
- Signed test webhook injected at 15:37:28 → log shows `mark-read scheduled` → `mark-read ok` (2.8s, via sidecar /read → Photon remote markRead).
- Note: first injection failed silently because payload lacked `"event": "messages"` — handler ack-drops unknown events at adapter.py:496.

## Open
- Adam to confirm "Read" now shows on his phone for the test chat.
