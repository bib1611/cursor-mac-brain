# 2026-06-11 12:00 CDT - Codex - Hermes update and X bookmark review

## Request

Adam said Hermes had more updates and that he had bookmarked interesting X posts related to Hermes. He asked Codex to update Hermes Agent again and check whether the bookmarks help.

## Hermes Update

- Refreshed the local ops packet before acting.
- Ran:
  - `/Users/adamjohnsson/.local/bin/hermes update --backup --yes`
- Backup created:
  - `/Users/adamjohnsson/.hermes/backups/pre-update-2026-06-11-114941.zip`
- Result:
  - Hermes was already current at upstream `c7bfc938d54538d960a7e09c0db3c13139723951`.
  - Updater autostashed/restored local changes.
  - `hermes update --check` after the run still reports `Already up to date`.
- Expected local Hermes repo changes remain:
  - `plugins/platforms/photon/adapter.py`
  - `plugins/platforms/photon/sidecar/index.mjs`

## Desktop / Gateway Verification

- Hermes version:
  - `Hermes Agent v0.16.0 (2026.6.5) · upstream c7bfc938`
- Desktop install stamp:
  - commit `c7bfc938d54538d960a7e09c0db3c13139723951`
  - built at `2026-06-11T16:49:22.541Z`
  - `dirty: true` because local Photon edits are present
- Gateway:
  - launchd label `ai.hermes.gateway`
  - PID `64955`
  - `http://127.0.0.1:8642/health` returned OK
  - Telegram, Photon, and API server connected in the gateway log
- Desktop:
  - running from `/Users/adamjohnsson/.hermes/hermes-agent/apps/desktop/release/mac-arm64/Hermes.app`
  - dashboard backend running on `127.0.0.1:9120`

## Fable / Proxy Work

- After the update, a non-streaming Fable-high smoke test hung and left the local proxy queue occupied.
- Root cause found in `/Users/adamjohnsson/claude-max-proxy.js`:
  - streaming Claude requests killed the child on client disconnect
  - blocking Claude requests did not, so a timed-out caller could leave `claude --print` occupying the only proxy slot
- Patched the blocking Claude path to:
  - listen for `res.close`
  - send `SIGTERM`, then `SIGKILL` if needed
  - avoid writing a response after the client is gone
- Restarted `com.biblicalman.claude-max-proxy`.
- Verification:
  - `node --check /Users/adamjohnsson/claude-max-proxy.js` passed
  - short 20s Fable timeout killed PID `67961`
  - proxy queue returned to `active:0 queued:0`
  - direct `claude-fable-5` returned `DIRECT_FABLE_OK`
  - direct `claude-opus-4-7` returned `DIRECT_OPUS_OK`
  - proxy `claude-opus-4-7` returned `OPUS_PROXY_OK`
  - proxy `claude-fable-5` returned `FABLE_PROXY_RETRY_OK`
  - Hermes CLI returned `HERMES_AFTER_UPDATE_OK`

## X Bookmarks Reviewed

Pulled the 30 most recent bookmarks with:

- `/Users/adamjohnsson/.agents/bin/dh-with-env xurl bookmarks -n 30`

Useful Hermes-related bookmarks:

- Teknium, 2026-06-11: Hermes Desktop can access files from a remote instance machine, read-only for now.
  - Local code confirms this landed: recent commits include `feat(desktop): add read-only remote filesystem API`, `wire remote filesystem browsing`, and follow-up fixes.
- Teknium, 2026-06-11: profile management is being unified in the dashboard.
  - Full note text says the dashboard can switch management to any agent profile on the machine, avoiding multiple dashboards.
  - It also says one gateway for all agents is upcoming, not necessarily fully live yet.
  - Local code confirms profile switcher/hotkey/profile-scope work is present.
- Nous Research, 2026-06-10: Hermes Agent Profile Builder.
  - This is relevant to Adam's writer/support/storeanalyst lanes.
  - Existing local route/code already reflects Profile Builder work.
- Nous Research, 2026-06-08: Hermes via iMessage through Photon.
  - Already relevant to the existing local Photon lane.
  - Treat phone/read-status proof as separate from the tweet.
- Nous Research, 2026-06-03 and 2026-06-02: Web Dashboard overhaul and Hermes Desktop public preview.
  - Already installed locally; useful mostly as feature awareness.
- Alex Finn, 2026-06-06: “7 things that made my Hermes Agent 100x better.”
  - Direct API read only exposed the first item: run Hermes on the main computer, not a side machine with separate accounts.
  - This matches Adam's current Mac-side operator setup.
- Ole Lehmann, 2026-06-02: turn X bookmarks into a second brain.
  - Practical takeaway: Adam does not need an extension first because `xurl bookmarks` already works locally. A recurring bookmark review/ingest job would be useful if Adam wants it.
- Matt Van Horn, 2026-06-01: Agent Cookie for Mac mini/OpenClaw/Hermes login persistence.
  - Potentially useful if Adam keeps seeing logged-out browser-agent workflows, but no local install/change was made.
- Mixroute / model switching and Step 3.7 Flash / Gemma 4 26B bookmarks:
  - Potential future provider/local-model options.
  - Not adopted now because Hermes is already current and the local Fable/Opus proxy path is verified again.

## End State

- Hermes Agent is current.
- Desktop app is current to commit `c7bfc938`.
- Gateway is healthy.
- Telegram polling is connected.
- Photon is connected.
- Fable/Opus local proxy is running and queue is idle.
- Blocking proxy requests are hardened against client timeouts.
- No public posts, follows, X notifications, provider switches, or credentials were changed.

