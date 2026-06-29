# 2026-06-10 11:53 CDT - Codex - Hermes Update

Adam asked Codex to update Hermes after seeing an available update.

## Actions

- Booted from `/Users/adamjohnsson/.deadhidden-os/ops/` and refreshed `TEAM_CONTEXT.md`.
- Verified Hermes was behind upstream: repo was on `72154ad879e2`, `hermes version` reported update available, and git showed `main...origin/main [behind 87]`.
- Ran the official updater:
  - `/Users/adamjohnsson/.local/bin/hermes update --backup --yes`
  - Pre-update backup: `/Users/adamjohnsson/.hermes/backups/pre-update-2026-06-10-114341.zip`
  - Pre-update snapshot: `20260610-164442-pre-update`
- Update fast-forwarded Hermes Agent to `d986bb0c6de6bcffda4981e83652284d481a90f4`.
- A final update check then found 3 fresh upstream commits, so Codex ran a second official update pass:
  - `/Users/adamjohnsson/.local/bin/hermes update --yes`
  - Pre-update snapshot: `20260610-165400-pre-update`
  - Final Hermes Agent commit: `3acf73161fe224a3dcdb985547966dc7fd9f78b6`
- The updater restored Adam's local Photon changes on top of upstream; the working tree intentionally still shows:
  - `plugins/platforms/photon/adapter.py`
  - `plugins/platforms/photon/sidecar/index.mjs`
- Rebuilt the Hermes desktop bundle during the first update pass. The second pass reported the packaged app was already up to date because the content stamp still matched. Final desktop stamp:
  - commit: `d986bb0c6de6bcffda4981e83652284d481a90f4`
  - built at: `2026-06-10T16:46:05.351Z`
  - bundle version: `0.15.1`
- Repaired the stale launchd service definition and restarted the gateway. The first restart briefly created a duplicate/stale gateway during launchd handoff; Codex collapsed it to one supervised gateway.
- Relaunched the packaged Hermes desktop app from:
  - `/Users/adamjohnsson/.hermes/hermes-agent/apps/desktop/release/mac-arm64/Hermes.app`

## Verification

- `hermes version`:
  - `Hermes Agent v0.16.0 (2026.6.5) · upstream 3acf7316`
  - `Up to date`
- `hermes update --check`:
  - `Already up to date`
- `hermes gateway status`:
  - service definition matches current install
  - loaded under launchd
  - PID `68916`
  - program: `/Users/adamjohnsson/.hermes/hermes-agent/venv/bin/python -m hermes_cli.main gateway run --replace`
- `hermes status`:
  - gateway running
  - Telegram configured
  - model/provider still `claude-fable-5` / `claude-max-opus`
- API health:
  - `http://127.0.0.1:8642/health` returned `{"status":"ok","platform":"hermes-agent","version":"0.16.0"}`
- Final process check showed one gateway process, one Photon sidecar, and the desktop app/dashboard.

## Notes

- Gateway restart logs show Telegram, Photon, and API server reconnected after the update.
- The update ran its bundled Cua Driver refresh. Final `cua-driver --version` reported `cua-driver 0.5.1`.
- No public post, customer action, money action, production deploy, webhook cutover, API key change, or credential print was performed.
- Internal Hermes restart/shutdown notifications may have been sent to Adam's configured home channels as part of the gateway restart.
