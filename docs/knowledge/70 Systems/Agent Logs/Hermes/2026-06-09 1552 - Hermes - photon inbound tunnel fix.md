# Photon iMessage inbound — root cause and permanent fix

Date: 2026-06-09 15:52 CDT

## Symptom
Adam's texts stuck on "Delivered" — no read receipt, no replies. Last real inbound 06:28; dead all day.

## Root cause
Photon delivers inbound via webhook to a registered public URL. The registered URL was an ephemeral cloudflared quick tunnel (`trials-hiring-specially-update.trycloudflare.com`, registered 2026-06-08 21:23 CDT) with NO supervising process — when cloudflared died midday, Photon kept POSTing into a dead URL. Nothing local restarts it; nothing re-registers. Outbound (sidecar) kept working, masking the break. The sidecar "drained inbound" log lines (15:32, 15:41) were Adam's messages arriving on the spectrum-ts stream and being intentionally discarded — webhook is the canonical inbound path.

## Fix (permanent, self-healing)
- New: `~/.deadhidden-os/ops/bin/photon-tunnel-supervisor` — runs cloudflared quick tunnel → parses fresh URL → rotates Photon webhook registration → persists new signing secret to ~/.hermes/.env → kicks gateway to load it. Exits when cloudflared dies.
- New: `~/.deadhidden-os/ops/bin/photon-webhook-rotate.py` — deletes stale webhooks, registers new URL, persists signing secret (exit 3 = already current, no gateway kick).
- New launchd job: `com.deadhidden.photon-tunnel` (KeepAlive=true, throttle 15s) — tunnel death now auto-heals end to end.

## Proof
- 15:49:11 tunnel up at approximate-gabriel-analyze-diversity.trycloudflare.com
- 15:49:15 stale webhook f4651e70 deleted; new webhook 28d4629a registered; signing secret saved
- 15:49:21 gateway kicked; 15:49:29 photon reconnected clean (stale-sidecar eviction fired)
- 15:51:33 signed test POST through the PUBLIC tunnel URL → inbound dispatched → mark-read ok (2.7s)

## Remaining
- Photon-cloud→new-URL leg unproven until Adam sends a real text (test bypassed Photon's sender).
- Note: quick-tunnel URL changes on every cloudflared restart; rotation handles it but each rotation restarts the gateway. A named CF tunnel or Tailscale funnel (needs tailnet ACL) would remove restarts — only worth it if rotations get frequent.
- Side finding: ~/.hermes/.env lines 444–445 (PHOTON_HOME_CHANNEL/_NAME) break naive bash `source` in dh-with-env (semicolons/spaces) — harmless to gateway, noisy in cloud-relay-pull logs.
