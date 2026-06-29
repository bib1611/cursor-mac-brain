# 2026-06-09 17:36 CDT — Claude — Hermes agent + desktop app updated

Adam asked Claude Code to update Hermes, especially the desktop app.

## What happened

The update ran through the official Hermes Setup flow; Claude verified every stage against live state and confirmed the final result.

- `hermes update` pull at 17:10 CDT moved `~/.hermes/hermes-agent` to `57c67149` (Hermes Agent v0.16.0, release 2026.6.5).
- Hermes Setup.app (launched 17:23 CDT) ran `install-main.sh` non-interactive: repository stage re-pulled to `72154ad879e2` (newest upstream, CI-only change), then rebuilt the desktop app.
- Desktop app packaged at 17:31:41 CDT from commit `72154ad879e2`: `apps/desktop/release/mac-arm64/Hermes.app`, bundle `com.nousresearch.hermes` v0.15.1 (desktop versions itself separately from the agent), Electron 40.9.3.
- Installer launched the desktop app at 17:32:02 CDT — PID 20084, desktop log shows "Hermes backend is ready. Finalizing desktop startup."
- Gateway `ai.hermes.gateway` healthy after restart: PID 77903 (started 17:26:22 CDT), `/health` returns v0.16.0, Telegram polling (@blu1611_bot, 30 commands), Photon sidecar, and API server all connected.

## Notes

- Gateway process started before the final 17:30 pull, but the only delta between `57c67149` and `72154ad879e2` is `.github/workflows` CI caching — zero runtime difference. No extra restart needed.
- Local working-tree mods preserved through the update via autostash restore: `package-lock.json`, `plugins/platforms/photon/adapter.py`, `plugins/platforms/photon/sidecar/index.mjs`. Backup copy still in `git stash` as `hermes-update-autostash-20260609-221053`.
- `hermes update --check` confirms no newer upstream after the flow.
- MacBook Air (100.91.48.107) was unreachable over Tailscale SSH — if a Hermes copy lives there, it still needs its own update when awake.
- Claude's one intervention attempt (`hermes desktop --skip-build` at 17:24) failed harmlessly because the installer had just wiped the bundle to rebuild it; no side effects.

## Boundary

No money, customer, publishing, or external-send actions. No config edits. Repo state changed only by the official Hermes update/installer flow.
