# Photon iMessage sidecar rescue — 2026-06-10 11:22 CDT

## Symptom
Adam's 11:07 AM voice memo (1:15, Dead Hidden Substack teaser/paywall idea) bounced with Photon's "agent on this number isn't online" auto-reply. Memo was never delivered or stored anywhere recoverable.

## Root cause
- Photon plugin runs a Node sidecar (`plugins/platforms/photon/sidecar/index.mjs`, port 8789) streaming inbound iMessages over gRPC from Photon's Spectrum cloud.
- 2026-06-10 06:10:22 — sidecar logged `inbound stream errored — restarting: [upstream] Authentication failed.` Upstream auth token died; sidecar then spun in a silent "inbound stream ended — re-subscribing" loop every ~30s without delivering. Photon cloud marked the agent offline → inbound messages bounced (window ~06:10–11:17).
- The gateway adapter only spawns the sidecar at adapter-connect time. Killing the dead sidecar left the adapter in an infinite "All connection attempts failed; reconnecting in 30s" loop — it never respawns.
- Red herring: the cloudflared tunnel → port 8788 webhook path is legacy (plugin migrated to gRPC sidecar streaming 2026-06-09 17:26). Cloudflared "connection refused" errors on 8788 are expected and harmless in gRPC mode. `com.deadhidden.photon-tunnel` launchd job + supervisor can probably be retired.

## Fix
1. Killed stale sidecar PID 26360 (up since 06-09 17:35, dead auth).
2. Created `/Users/adamjohnsson/.deadhidden-os/ops/bin/photon-sidecar-respawn.py` — respawns the sidecar with identical env (project creds via plugin `auth.py` + `~/.hermes/.env` sidecar token) so the still-running gateway adapter reconnects on its next 30s retry. Logs to `ops/cloud/photon-sidecar-manual.log`.
3. Ran it — new sidecar PID 14672, `Spectrum started`, listening 8789. Gateway adapter reconnected ~11:17:40 (failure warnings stopped).
4. Proof: direct `/send` POST delivered iMessage to Adam — messageId `spc-msg-650c49e1-8ef1-4330-9a18-cfbea327b189`.

## Residual / follow-ups
- Upstream bug: adapter has no sidecar health-respawn; sidecar doesn't exit on persistent upstream auth failure (so adapter supervision never triggers). Worth a watchdog (launchd or cron: if gateway log shows N consecutive "All connection attempts failed" or "Authentication failed", run respawn script) or an upstream hermes-agent patch.
- On next full gateway restart, adapter `_stop_sidecar` POSTs /shutdown to 8789 — cleanly stops the manually spawned sidecar. No port conflict expected.
- Voice memo content is unrecoverable; asked Adam to resend (iMessage + Telegram).
