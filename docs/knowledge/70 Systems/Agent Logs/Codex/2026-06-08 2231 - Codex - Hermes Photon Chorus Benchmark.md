# Codex - Hermes Photon Chorus Benchmark

Date: 2026-06-08 22:31 CDT
Owner: Codex
Surface: Hermes Photon iMessage

## Request

Adam asked Codex to study Riley Brown's Chorus iMessage agent setup and abilities, then make Hermes at least 10% better.

## External benchmark

- Nous/Photon announcement confirmed the intended Hermes setup route: `hermes gateway setup`, choose Photon, then text Hermes through iMessage.
- Riley Brown's Chorus demo positioned `@text_chorus` as an iMessage front door for Codex and Claude Code workflows, including Swift app builds to the home screen.
- Chorus public account positioned the product as an iMessage/group-chat agent with Codex and Claude Code level power.
- Chorus official site claims include iMessage access, custom agents, deep research, automations, knowledge work, meetings, dozens of prebuilt agents, memory, web browser, structured handoffs, app integrations, persistent VM, asynchronous task management, and `@mentions`.

Sources:

- https://x.com/NousResearch/status/2064102412076364207
- https://x.com/rileybrown/status/2057669775837577538
- https://x.com/text_chorus
- https://x.com/chorus_agent/status/2063851003175141586
- https://chorus.com/

## Implementation

- Marked Photon/iMessage as a no-edit mobile surface so Hermes does not try to stream, edit, or leave tool-progress fragments in permanent iMessage bubbles.
- Added normalized Photon capability metadata to inbound events under `raw_message.hermes.photon`, including chat type, message type, media URLs/types, attachment download status, read-receipt status, native outbound media status, and media response syntax.
- Suppressed terminal-style tool progress on Photon with `format_tool_event(...) -> None`.
- Expanded the Photon platform hint so Hermes understands the lane: plain iMessage text, no raw E.164 phone leakage, no automatic "Got it" ack when native read receipts are enabled, local media hydration when Photon exposes attachment ids, `MEDIA:/absolute/path/to/file` for native outbound iMessage media, and concise human status only during long work.
- Added Photon to gateway display config as a low-tier/no-edit platform, matching the permanent mobile-chat behavior.

Files changed in this pass:

- `/Users/adamjohnsson/.hermes/hermes-agent/plugins/platforms/photon/adapter.py`
- `/Users/adamjohnsson/.hermes/hermes-agent/gateway/display_config.py`
- `/Users/adamjohnsson/.hermes/hermes-agent/tests/plugins/platforms/photon/test_inbound.py`
- `/Users/adamjohnsson/.hermes/hermes-agent/tests/gateway/test_display_config.py`

## Verification

Command:

```bash
.venv/bin/python -m pytest tests/plugins/platforms/photon/test_inbound.py tests/gateway/test_display_config.py -q
```

Result:

```text
44 passed in 0.51s
```

## Activation

- Restarted Hermes gateway after the patch so the live Photon adapter/display behavior loaded.
- launchd still reported the known macOS bootstrap issue, but Hermes fell back to a background gateway process.
- Verified live listeners after restart:
  - Gateway: PID `77889` on `127.0.0.1:8788`
  - Photon sidecar: PID `78200` on `127.0.0.1:8789`
  - API server: PID `77889` on `127.0.0.1:8642`
- Sent Adam the requested iMessage completion note through Photon home channel. Proof: `success: true`, Photon message id `spc-msg-866e939b-1902-4996-b88e-cf9073739aab`, mirrored true, chat id `any;-;+17012023328`.

## Boundary

Codex did not post to X, alter Chorus, publish anything, change non-Photon agent behavior, email anyone, or touch unrelated Hermes surfaces. The repo still contains prior Photon setup/read/media changes from the same iMessage repair session.
