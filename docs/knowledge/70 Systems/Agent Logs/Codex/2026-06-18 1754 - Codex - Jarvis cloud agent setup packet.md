# Codex Receipt - Jarvis Cloud Agent Setup Packet

Date: 2026-06-18 17:54 CDT

Adam clarified that Chorus/Jarvis is the cloud agent he wants to use, including from iMessage, and asked Codex to inspect what already exists and key in as much second-brain context as possible.

Actions:

- Read the live local ops capsule, `CHORUS.md`, `TEAM_CONTEXT.md`, `TOOL_ACCESS.md`, and `RULES.md`.
- Used the Chrome skill path. Chrome is running, the Codex Chrome Extension is installed/enabled in the selected Chrome profile, and the native messaging host manifest is correct, but the extension did not respond to control.
- Per Chrome recovery instructions, Codex asked Adam before opening a fresh Chrome window in the selected profile to retry browser control.
- Built a paste-ready Jarvis cloud-agent setup packet:
  - `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-18-jarvis-cloud-agent-setup.md`

The packet includes:

- Standing policy for Jarvis.
- Source-of-truth hierarchy.
- Connected-app read roles for Stripe, Gmail/Google, Notion, Linear, GitHub, Dropbox, YouTube, and public web.
- Mac-local paths Jarvis cannot read unless pasted.
- Secret/capability names only, no values.
- iMessage prompt shape and first test prompt.
- Chorus setup checklist.

Boundary:

- No raw secrets copied to Chorus or into the packet.
- No browser form submitted.
- No Chorus/Jarvis setting changed yet.
- No iMessage/SMS sent.
- No external app write, email, publishing, Stripe/customer/money action, Linear write, repo/deploy, credential/key/account setting change, upload, deletion, or permission change performed.
