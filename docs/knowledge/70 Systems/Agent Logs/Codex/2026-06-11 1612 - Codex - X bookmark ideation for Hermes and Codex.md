# Codex - X Bookmark Ideation for Hermes and Codex

Date: 2026-06-11 16:12 CDT
Agent: Codex

## Trigger

Adam asked Codex to pull the X bookmarks he had just added and see whether there were useful ideas for Hermes or Codex.

## Actions

- Read the active Dead Hidden ops capsule and refreshed `TEAM_CONTEXT.md`.
- Used the `deadhidden-intelligence-loop` skill and its capture template.
- Verified `xurl whoami` as `@Biblicalman`.
- Pulled recent bookmarks with authenticated read-only `xurl bookmarks -n 60`.
- Opened wrapper/quoted posts where the bookmark text only pointed to another tweet or X Article title.
- Checked local state: the old bookmark scraper is still disabled, Hermes profile code includes `/profiles/new`, local profiles include `writer`, `support`, and `storeanalyst`, and `OUTBOUND_LOCKDOWN.md` is active.
- Saved the intelligence capture at:
  `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Intelligence/X Bookmarks/2026-06-11 - Hermes and Codex bookmark ideation.md`
- Implemented a manual read-only command:
  `/Users/adamjohnsson/.deadhidden-os/ops/bin/x-bookmark-intel`
- Verified the command with `python3 -m py_compile`, stdout-only mode, and a local packet write:
  `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/x-bookmark-intel/2026-06-11-1614-x-bookmark-intel.md`

## Findings

The strongest ideas were:

- Manual, read-only bookmark-to-Obsidian capture instead of rearming the old scraper.
- Treat Hermes profiles as a role roster with explicit allowed actions and receipts.
- Add SOUL lint/checks for Hermes profiles.
- Bridge Hermes/Codex source intelligence into Obsidian while keeping the ops capsule canonical.
- Use browser/CDP for full X Article body retrieval when `xurl` only exposes a title.
- Keep remote-instance file access read-only for now.
- Sandbox provider/cost routing experiments; do not add new providers to live public/support paths during lockdown.
- Use Mythos/video-generation ideas only for internal assets, not mass posting.

## Boundary

No X post, like, reply, DM, repost, unbookmark, Substack action, email, customer action, provider change, Hermes re-enable, launch-agent restart, or public/account-changing action was performed.

Fable was not used because it was not needed for this read-only classification and the current outbound lockdown explicitly keeps Fable/Claude Max routes locked until Adam approves re-enabling.
