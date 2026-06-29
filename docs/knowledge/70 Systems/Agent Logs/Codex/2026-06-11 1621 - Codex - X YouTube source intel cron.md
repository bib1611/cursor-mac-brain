# Codex - X YouTube Source Intel Cron

Date: 2026-06-11 16:21 CDT
Agent: Codex

## Trigger

Adam asked Codex to implement a cron that pulls saved/source intelligence at least three times per day from X, YouTube, and saved videos.

## Implementation

Created combined read-only local runner:

`/Users/adamjohnsson/.deadhidden-os/ops/bin/source-intel-cron`

The runner:

- Pulls X bookmarks through authenticated `xurl` via `/Users/adamjohnsson/.agents/bin/dh-with-env`.
- Pulls YouTube Watch Later / saved videos through `yt-dlp --flat-playlist` using local browser cookies from `chrome:/Users/adamjohnsson/.chrome-debug`.
- Writes Markdown packets under `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/source-intel/`.
- Tracks seen IDs in `/Users/adamjohnsson/.deadhidden-os/ops/state/source-intel-seen.json`.
- Appends run summaries to `/Users/adamjohnsson/.deadhidden-os/ops/logs/source-intel-cron.log`.
- Does not post, like, reply, repost, unbookmark, publish, email, download media, change providers, or mutate external account state.

Existing helper retained:

`/Users/adamjohnsson/.deadhidden-os/ops/bin/x-bookmark-intel`

## Scheduler

Created Codex app cron automation:

- Automation ID: `x-and-youtube-source-intel`
- Name: `X and YouTube Source Intel`
- Status: `ACTIVE`
- Cadence: every 8 hours, giving at least 3 runs per day
- CWD: `/Users/adamjohnsson/.deadhidden-os/ops`
- Model: `gpt-5`
- Reasoning effort: `low`
- Config file: `/Users/adamjohnsson/.codex/automations/x-and-youtube-source-intel/automation.toml`

## Verification

- `python3 -m py_compile /Users/adamjohnsson/.deadhidden-os/ops/bin/source-intel-cron` passed.
- Dry run pulled 5 X bookmarks and 5 YouTube Watch Later videos with zero errors.
- Real baseline run pulled 50 X bookmarks and 14 YouTube saved videos with zero errors.
- Baseline artifact:
  `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/source-intel/2026-06-11-1621-source-intel.md`
- State after baseline:
  50 X IDs and 14 YouTube IDs saved.
- Log confirmed:
  `x=50 youtube=14 new_x=50 new_youtube=14 errors=0`
- Automation config was verified on disk.

## Boundary

No X write, YouTube write, media download, Substack action, email/customer action, provider change, Hermes re-enable, launch-agent restart, or public/account-changing action was performed.

Fable was not used. The implementation was deterministic, and the current outbound lockdown keeps Fable/Claude Max routes locked until Adam approves re-enabling.
