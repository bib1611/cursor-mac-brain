---
type: agent-receipt
date: 2026-06-29 10:16 CDT
agent: Hermes
owner: Adam
status: completed
surface: Hermes Desktop + Jarvis/Linq iMessage
---

# Hermes - Desktop + iMessage control plane

## Request

Adam asked to make the agent stack controllable from either Hermes Desktop or iMessage via Jarvis/Linq, including Linq, Jarvis Alpha, existing LLMs, skills, tools, Codex, Aside, and MoA-style routing.

## What changed

Created first-pass control-plane documentation and executable bridge:

- `/Users/adamjohnsson/.deadhidden-os/ops/CONTROL_PLANE.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/APPROVAL_PACKET.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/bin/dh-control`
- `/Users/adamjohnsson/.deadhidden-os/ops/status/CONTROL_PLANE.md`

Patched existing routing and Jarvis/Linq bridge:

- `/Users/adamjohnsson/.deadhidden-os/ops/bin/dh-ops`
  - Added Gumroad/store/Resend/Proton to Codex/money-support routing.
  - Moved Substack/X/Twitter into connected-read routing rather than generic writing when applicable.
- `/Users/adamjohnsson/.deadhidden-os/imessage-brain/jarvis_linq.py`
  - Added deterministic interception for explicit control commands.
  - Normal texts still fall back to Jarvis's Codex-backed brain.

## New iMessage commands

Jarvis/Linq now recognizes explicit commands:

- `status`
- `ops status`
- `route <task>`
- `ask codex <task>`
- `ask claude <task>`
- `ask hermes <task>`
- `ask chorus <task>`
- `/askcodex <task>`
- `/askclaude <task>`
- `/askhermes <task>`
- `/askchorus <task>`
- `receipt <note>`
- `approvals`
- `control help`

## Verification

Commands run:

```bash
python3 -m py_compile /Users/adamjohnsson/.deadhidden-os/ops/bin/dh-control /Users/adamjohnsson/.deadhidden-os/ops/bin/dh-ops /Users/adamjohnsson/.deadhidden-os/imessage-brain/jarvis_linq.py
/Users/adamjohnsson/.deadhidden-os/ops/bin/dh-control status --text
/Users/adamjohnsson/.deadhidden-os/ops/bin/dh-control route 'check Gumroad and draft only'
```

Results:

- Python compile passed.
- `dh-control status --text` returned control status.
- Gumroad routing now returns Codex as the owner lane.
- Jarvis/Linq LaunchAgent was restarted with Adam approval and is running as PID `96242`.

## Cleanup

A smoke-test Codex task was created during deterministic command testing, then removed from:

- Agent Bus inbox
- Codex bridge `COMMAND-INBOX.md`

A smoke-test approval packet was created, listed, and resolved under:

- `/Users/adamjohnsson/.deadhidden-os/ops/approvals/resolved/`

## Boundary

This bridge does not auto-post, auto-send, auto-publish, refund, spend, deploy, delete, or change credentials/security/account settings. It routes, reports, creates local files, creates Agent Bus tasks, tracks approval packets, and requires Adam's exact approval before external actions.
