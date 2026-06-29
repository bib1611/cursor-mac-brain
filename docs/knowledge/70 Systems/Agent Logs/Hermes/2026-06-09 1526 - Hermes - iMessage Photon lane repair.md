# 2026-06-09 1526 CDT — Hermes — iMessage (Photon) lane repair

## Symptom
iMessage sessions dead. Last working inbound/reply loop: 06:13–06:42 this morning. Nothing after.

## Root causes found (with live proof)

### 1. `--replace` restart orphans the Photon sidecar (primary)
On every `hermes gateway restart` / `--replace`, the new gateway spawned its Node sidecar while the old gateway's sidecar still held port 8789. The new sidecar crashed `EADDRINUSE`, but the readiness health check passed against the doomed OLD sidecar (same token), so the adapter reported "✓ photon connected" anyway. When the old gateway exited it killed its sidecar — leaving NO sidecar, no respawn, outbound iMessage dead.
- Observed in gateway.log at 12:40, 12:50, and reproduced live at 15:20 (sidecar 43242 dead, port 8789 empty, gateway 43017 "connected").
- Today's churn: gateway restarts at 12:38–12:50, gateway down 14:42–14:59. Broken window ~12:40 → repair.

### 2. Cold sends blow the 30s timeout (secondary)
First spectrum-ts send after a sidecar restart takes 25–30s+ (measured: cold 25.4s, warm 6.5s). Adapter httpx timeouts were 30.0s → first reply after any restart failed ("Send failed … fallback also failed", seen 2026-06-08 21:47 and 22:09).

### Ruled out
- ENOSPC session-store errors: June 5, disk now has 49Gi free.
- Disk, gateway process, Telegram lane: all healthy.

## Fixes applied
File: `~/.hermes/hermes-agent/plugins/platforms/photon/adapter.py`
1. New `_evict_stale_sidecar()` called at top of `_start_sidecar()`: if a healthy sidecar already holds the port, POST `/shutdown` (token-authed) and wait up to 10s for the port to free before spawning ours.
2. Timeouts 30.0 → 120.0 in three places: adapter `_http_client`, `_sidecar_call`, standalone send client.

## Verification
- `py_compile` clean; Photon test suite: **53 passed**.
- Gateway restarted 15:25. Eviction fired live: "stale sidecar holds port 8789 — requesting shutdown" → "stale sidecar gone — port 8789 free" → clean bind → `✓ photon connected`.
- Single gateway process; sidecar PID 61080 owns 8789.
- Live outbound: `hermes send --to photon` → `success: true`, message id `spc-msg-ae48cb85-557f-4127-a665-95f7202e73fd`, 11.2s.
- Inbound leg: awaiting Adam's "ping" text for full-loop confirmation.

## Separate finding (not fixed — needs Adam's GUI action)
`com.adam.imessage-sync` launchd job (iMessage → Obsidian vault, daily 05:30) has NEVER run successfully: `sqlite3.DatabaseError: authorization denied` on `~/Library/Messages/chat.db`. On 2026-06-08 the plist interpreter was swapped to `/Library/Developer/CommandLineTools/usr/bin/python3` but that binary lacks Full Disk Access. Fix requires System Settings → Privacy & Security → Full Disk Access → add `/Library/Developer/CommandLineTools/usr/bin/python3`. Vault output dir `~/Documents/Obsidian Vault/inbox/imessage/` does not exist yet.

## Boundary
No public posts, no customer/money actions, no credential changes. One Hermes core file patched (Photon adapter), gateway restarted twice, three test iMessages sent to Adam's own number.
