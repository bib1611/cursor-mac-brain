# 2026-06-16 18:30 CDT - Codex - Cursor Dead Hidden Setup

## Request

Adam asked Codex to set up Cursor so the new Cursor improvements would be useful for Dead Hidden work.

## Research

Checked current Cursor documentation and launch notes. Relevant useful features:

- Project rules in `.cursor/rules/`.
- MCP support exists, but this local Cursor install has no connected MCP catalog yet.
- Bugbot / review flow is useful before PRs and merges.
- Design Mode improvements are useful for frontend CRO work because Cursor can use selected UI elements and screenshots as edit context.

## Action

Created Dead Hidden project rule:

`/Users/adamjohnsson/code/deadhidden/.cursor/rules/deadhidden.mdc`

The rule tells Cursor agents to:

- Read `AGENTS.md` first and `CLAUDE.md` for spawned agents.
- Treat Stripe, delivery, email, publishing, and live deploy behavior as customer-facing.
- Avoid checkout sessions, charges, buyer emails, refunds, fake urgency/testimonials, price changes, and publish/deploy actions unless Adam explicitly asks.
- Preserve user changes and run `git status` before edits.
- Keep current commerce facts in view, including Vault `$365`, PBM2 cold `$37`, and PBM2 existing-owner upgrade `$15`.
- Use mobile-first CRO defaults with the 60% women audience note.
- Use `/review-bugbot` or `/review-security` before risky PR/merge work.
- Write receipts for customer-facing or agent/tooling changes.

Created project slash command:

`/Users/adamjohnsson/code/deadhidden/.cursor/commands/dh-ship-check.md`

The command gives Cursor a repeatable Dead Hidden pre-ship flow: dirty-state check, touched-file summary, money-path classification, typecheck, lint, build, Bugbot/Security Review, and final report.

Created workspace launcher:

`/Users/adamjohnsson/DeadHidden.cursor.code-workspace`

The workspace opens `/Users/adamjohnsson/code/deadhidden`, ignores `.next`, `.worktrees`, `node_modules`, and `tsconfig.tsbuildinfo`, and points Cursor at the repo TypeScript SDK.

Installed Cursor extensions:

- `dbaeumer.vscode-eslint`
- `bradlc.vscode-tailwindcss`
- `github.vscode-pull-request-github`

Opened Cursor to `DeadHidden.cursor (Workspace)`.

## Verification

- Workspace JSON validated with `jq empty`.
- Cursor window title shows `DeadHidden.cursor (Workspace)`.
- `cursor --list-extensions` includes ESLint, Tailwind CSS IntelliSense, and GitHub Pull Requests.
- `git status --short` shows new `.cursor/` setup files plus pre-existing unrelated local changes:
  - `M scripts/pbm2-existing-buyer-email.ts`
  - `?? .worktrees/`
  - `?? .cursor/`

## Not Done

No Cursor MCP servers were connected. This local Cursor install has no `~/.cursor/mcps` catalog yet, so MCP should be connected from Cursor Settings after Adam signs in.

No repo commit, PR, deploy, Stripe change, checkout session, buyer email, or publishing action was performed.
