# 2026-06-19 06:34 - Codex - Mac mini disk cleanup

Adam said he was tempted to wipe the Mac mini because of recurring memory/storage pressure and asked Codex to help solve it, including possible app offload.

Codex audited disk usage and found apps were not the main problem. The largest actionable buckets were user Library/app support, developer caches, agent folders, model caches, update caches, and package-manager caches.

Cleanup performed:

- Removed failed Hugging Face incomplete downloads.
- Removed `~/.cache/whisper`.
- Removed `~/.cache/huggingface`.
- Removed OpenAI Codex Sparkle updater cache.
- Removed Claude Desktop ShipIt updater cache.
- Cleaned npm cache.
- Pruned pnpm store cache.
- Ran Homebrew cleanup.
- Removed Xcode iOS DeviceSupport for `iPhone18,2 27.0 (24A5355q)`.
- Removed `~/.codex/.tmp` temporary files.

Result:

- Initial observed free space before cleanup: about 2.2 GiB.
- Free space immediately before the first cleanup command: 1.1 GiB.
- Free space after first cleanup pass: 15 GiB on `/System/Volumes/Data`.
- Free space after approved Hermes backup ZIP removal: 20 GiB on `/System/Volumes/Data`.
- Free space after approved Claude Desktop VM bundle removal: 26 GiB on `/System/Volumes/Data`.
- Free space after performance trim: 35 GiB on `/System/Volumes/Data`.
- Net reclaimed during cleanup commands: about 24-25 GiB.

Saved report:

`/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-19-mac-mini-disk-cleanup.md`

Remaining large options:

- `~/.codex/sessions`: 3.6G
- `~/.hermes/profiles/openclaw`: 1.7G
- `~/.cache/codex-runtimes`: 1.4G

Follow-up:

- Adam approved Hermes backup cleanup.
- Codex deleted the five old `~/.hermes/backups/pre-update-*.zip` archives.
- `~/.hermes/backups` is now 348K; small config/profile backup folders remain.
- Claude VM bundles were inspected and identified as Claude Desktop local-agent sandbox images.
- Adam approved deleting the Claude Desktop VM bundle.
- Codex quit `/Applications/Claude.app`, deleted `~/Library/Application Support/Claude/vm_bundles`, verified it no longer exists, verified no Claude Desktop process remained, and verified the Claude CLI still resolves to `/Users/adamjohnsson/homebrew/bin/claude`.
- Adam asked for the Mac mini to be fast, not sluggish.
- Codex stopped orphaned Claude Desktop Telegram plugin `bun server.ts` workers, `CuaDriver`, stale Stagehand/headless Chrome sessions, Comet, Omnigent, Hermes desktop GUI, and the runaway Chrome debug profile.
- Codex kept `ai.hermes.gateway`, Codex, Tailscale, Google Drive, Telegram, and the Claude CLI intact.
- Added repeatable trim command: `/Users/adamjohnsson/.deadhidden-os/ops/bin/mac-mini-trim`.

Boundary:

- No apps were deleted.
- No projects were deleted.
- No small Hermes config/profile backup folders were deleted.
- Claude Desktop local-agent VM bundles were deleted after approval.
- Claude Desktop app and Claude CLI were not deleted.
- Stale optional processes were stopped, not uninstalled.
- No Codex session history was deleted.
- No credentials, configs, receipts, repo files, public posts, email, customer/money state, deploys, Linear, Notion, Telegram, or Stripe state were changed.
