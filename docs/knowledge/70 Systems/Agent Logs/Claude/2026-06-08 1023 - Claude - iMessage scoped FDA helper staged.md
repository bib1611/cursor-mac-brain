# Claude - iMessage Scoped FDA Helper Staged (Local-Only)

Date: 2026-06-08 10:23 CDT
Operator: Claude Code (specialist worker)
Surface: `~/.deadhidden-os/imessage-brain`, `com.adam.imessage-sync` LaunchAgent

## Request

Adam asked Claude to help Hermes pull/sync iMessages into a searchable "brain" to know him better, and to help understand Chorus/Stanley. Adam chose: **(1)** scoped FDA helper, **(a)** LOCAL-ONLY — nothing leaves the Mac. Thread-scope question (everything vs exclude family/financial) still open; will confirm at index time.

## Root cause found

The existing pipeline `~/.hermes/scripts/imessage_to_vault.py` + LaunchAgent `com.adam.imessage-sync` has failed every morning since 2026-05-13 with `sqlite3.DatabaseError: authorization denied`. Not a code bug — `/usr/bin/python3` lacks Full Disk Access to `~/Library/Messages/chat.db` (138 MB, live, updated today). No `inbox/imessage` vault dir was ever produced. Same wall blocked Claude's own sqlite3 read this session.

## Changes (all local, reversible)

- Built scoped interpreter: `~/.deadhidden-os/imessage-brain/venv` via `python@3.13 -m venv --copies`. Real **copied** arm64 Mach-O at `~/.deadhidden-os/imessage-brain/venv/bin/python3` (Python 3.13.12) — a distinct binary so Full Disk Access scopes to this one interpreter, not to all of system python. `--copies` means brew upgrades won't disturb the grant.
- Repointed LaunchAgent `com.adam.imessage-sync` ProgramArguments to the scoped interpreter. Backup: `~/Library/LaunchAgents/com.adam.imessage-sync.plist.bak-prescope-20260608`. Reloaded via `launchctl bootout`/`bootstrap`; verified `program = .../imessage-brain/venv/bin/python3`.
- Added manual wrapper `~/.deadhidden-os/bin/imessage-sync` (yesterday / `YYYY-MM-DD` / `--backfill N`).

## Verification

- venv python is a copied Mach-O arm64, runs (3.13.12).
- Scoped interpreter currently DENIED `chat.db` (expected) — confirms it is the correct FDA target.
- LaunchAgent reloaded and bootstrapped; points at the scoped interpreter; `state = not running` (correct, `RunAtLoad=false`, 5:30 already passed).

## BLOCKED ON ADAM (only he can do this)

Grant Full Disk Access to:

`/Users/adamjohnsson/.deadhidden-os/imessage-brain/venv/bin/python3`

System Settings → Privacy & Security → Full Disk Access → **+** → Cmd-Shift-G that path → enable. If the ad-hoc-signed venv binary won't hold the grant, fallback is granting FDA to `/usr/bin/python3` (Apple-signed, broader surface).

## Next after FDA (not yet done)

- Backfill history into `inbox/imessage` (local) via the wrapper.
- Index into existing Qdrant (`writing-brain`/`bm_memory` or a new `imessage` collection) with a local embedding model — Ollama currently only has `qwen3:4b` (a chat model), so a proper embedder will be pulled.
- Distill durable "who Adam is" facts into Claude curated memory.
- Confirm thread-scope (include/exclude Christie/kids/financial) before indexing.

## Boundary

Local-only per Adam's choice (a). Nothing sent to Chorus/Stanley or any external service. No iMessage content has been read or exported yet (FDA not granted). No external messages, posts, publishes, deploys, credential/webhook/API-key changes.
