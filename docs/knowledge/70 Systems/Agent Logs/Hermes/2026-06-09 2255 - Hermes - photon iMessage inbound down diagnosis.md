# Photon iMessage inbound down — diagnosed + gateway kickstart

- Date: 2026-06-09 ~22:55 CDT
- Reported by: Adam ("Is Hermes iMessage off again")
- Finding: photon webhook receiver (127.0.0.1:8788, inside ai.hermes.gateway photon adapter) died ~19:36 CDT, right after the 19:35 inbound message. lsof showed nothing bound on 8788 or 8789. Cloudflared tunnel healthy the whole time, returning "connection refused" from origin since 00:36Z.
- Impact: inbound iMessages after ~19:37 CDT never reached Hermes. Outbound unaffected (silent failure mode).
- Fix: `launchctl kickstart -k gui/501/ai.hermes.gateway` scheduled detached +20s after Telegram reply delivered.
- Pattern note: 8788 receiver can die inside a live gateway with no error in errors.log; tunnel log at ~/.deadhidden-os/ops/cloud/photon-tunnel.cloudflared.log shows "connection refused" = receiver dead, tunnel fine. Check `lsof -nP -iTCP:8788` first.
