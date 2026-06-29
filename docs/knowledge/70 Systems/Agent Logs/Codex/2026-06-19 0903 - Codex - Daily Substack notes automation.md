# Codex - Daily Substack Notes Automation

Date: 2026-06-19 09:03 CDT

Adam asked whether Codex can make the demonstrated Substack Notes workflow repeatable every day for Biblical Man and Dead Hidden: find Pinterest/image/quote ideas, use Claude/Writing-Brain style where useful, preserve image-only notes when the image is already strong, tune timing from Adam's own data, and keep a max of about 7-8 Notes per day.

What changed:

- Expanded `/Users/adamjohnsson/.codex/skills/deadhidden-substack-notes-timing/SKILL.md` with a daily cadence:
  - max `7-8` Notes total across both brands
  - mix text Notes and image/quote-card Notes
  - use Pinterest/image prompts, comments, recent posts, and revenue priorities
  - use Adam's own timing/engagement first, platform-wide Orel/WriteStack-style data as fallback
  - keep Notes spaced about 2 hours apart
  - treat `2:00 AM` as valid only when Adam's own data keeps proving it
- Created active Codex cron automation `daily-substack-notes-slate`:
  - schedule: every day at 6:00 AM local time
  - workspace: `/Users/adamjohnsson/Downloads`
  - model: `gpt-5`
  - reasoning effort: `high`
  - task: produce an approval-ready 24-hour slate, not blind publish
- Patched legacy WriteStack/Pinterest scripts so they fail loudly instead of logging false success:
  - `/Users/adamjohnsson/.hermes/bin/pinterest-notes-factory-check`
  - `/Users/adamjohnsson/.hermes/bin/substack-notes-auto-poster-runner`

Findings:

- Existing LaunchAgents `com.adam.pinterest-notes-factory-check` and `com.adam.substack-notes-auto-poster` were still loaded.
- The old Pinterest Factory path is exhausted/broken for current use: today's check reports `Only 0 unused sources remain` and the dated pack is missing.
- Before the patch, the checker logged `pack ready` even after `FAIL: missing pack`.
- After the patch, the checker exits nonzero and logs `FATAL: dry-run failed`.
- Existing `/Users/adamjohnsson/.deadhidden-os/notes-scheduler/runner.py` can post queued Dead Hidden Notes through Comet/CDP, but it is not the full two-brand creative workflow and should be treated as execution infrastructure after approval.

Validation:

- `zsh -n` passed for both patched shell scripts.
- `SKILL.md` frontmatter YAML parse passed.
- ASCII scan passed for the updated skill and patched scripts.
- `/Users/adamjohnsson/.codex/automations/daily-substack-notes-slate/automation.toml` exists and is `ACTIVE`.
- Manual legacy checker test for `2026-06-19` exited with code `3`, which is the intended fail-loud behavior when no pack can be generated.

Boundary:

- Codex created a planning automation and patched local script failure handling only.
- Codex did not publish, schedule, upload, edit, delete, or post any Substack Note.
- Codex did not buy, renew, or use WriteStack.
- No Stripe/customer/money mutation, email send, X post, Linear write, Notion write, deploy, credential change, or external-account mutation was performed.
- Full automatic Substack scheduling remains blocked until Adam explicitly approves the exact standing policy or exact daily slate.
