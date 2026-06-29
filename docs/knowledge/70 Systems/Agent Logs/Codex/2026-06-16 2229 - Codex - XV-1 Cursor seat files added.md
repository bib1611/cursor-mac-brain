# 2026-06-16 22:29 CDT - Codex - XV-1 Cursor seat files added

Adam asked Codex to add the concrete XV-1 Cursor integration files:

- `SEATS.md`
- Cursor's own `SOUL.md`
- global Cursor rule
- repo `xv1-seat.mdc` rule
- Cursor memory digest
- Cursor memory inbox
- local-file hydration checker

Files added:

- `/Users/adamjohnsson/.deadhidden-os/ops/SEATS.md`
- `/Users/adamjohnsson/.cursor/SOUL.md`
- `/Users/adamjohnsson/.cursor/rules/dead-hidden-global.mdc`
- `/Users/adamjohnsson/code/deadhidden/.cursor/rules/xv1-seat.mdc`
- `/Users/adamjohnsson/.deadhidden-os/ops/state/cursor-memory-digest.md`
- `/Users/adamjohnsson/.cursor/memory-inbox.md`
- `/Users/adamjohnsson/code/deadhidden/scripts/verify-local.sh`

Also ensured these directories exist:

- `/Users/adamjohnsson/.cursor/rules`
- `/Users/adamjohnsson/.deadhidden-os/ops/state`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Logs/Cursor`
- `/Users/adamjohnsson/code/deadhidden/.cursor/rules`

Verification:

- `chmod +x /Users/adamjohnsson/code/deadhidden/scripts/verify-local.sh`
- `bash -n /Users/adamjohnsson/code/deadhidden/scripts/verify-local.sh`
- `/Users/adamjohnsson/code/deadhidden/scripts/verify-local.sh /Users/adamjohnsson/.deadhidden-os/ops/SEATS.md /Users/adamjohnsson/.cursor/SOUL.md /Users/adamjohnsson/.deadhidden-os/ops/state/cursor-memory-digest.md /Users/adamjohnsson/.cursor/memory-inbox.md /Users/adamjohnsson/code/deadhidden/.cursor/rules/xv1-seat.mdc`

The hydration checker returned `VERIFY_LOCAL_OK` for all checked new files.

Repo state note:

- `/Users/adamjohnsson/code/deadhidden` is on `main`, behind `origin/main` by 16 commits.
- Pre-existing unrelated state remains: modified `scripts/pbm2-existing-buyer-email.ts`, untracked `.worktrees/`, and untracked `.cursor/`.
- Codex did not pull, commit, merge, deploy, touch Stripe, email buyers, publish, or change live systems.

