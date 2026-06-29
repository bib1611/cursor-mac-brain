---
type: agent-log
date: 2026-06-08
agent: Codex
topic: Hermes Photon iMessage setup partial
tags: [codex, operator, hermes, photon, imessage]
---

# Hermes Photon iMessage Setup Partial

## Goal

Set up the new Nous Research Hermes Photon iMessage bridge from:

`https://x.com/nousresearch/status/2064102412076364207?s=46`

## What I Checked

- X post read through local `xurl`: Nous Research announced Photon iMessage support for Hermes and instructed users to run `hermes gateway setup` and choose Photon.
- Official docs checked: `https://hermes-agent.nousresearch.com/docs/user-guide/messaging/photon`
- Current Hermes state checked before update: `Hermes Agent v0.16.0 (2026.6.5)`, 84 commits behind, no `hermes photon` command available.
- Node checked: `v22.22.3`, which satisfies the Photon requirement of Node 18.17 or newer.
- Photon ports checked: `8788` and `8789` were free.

## What I Did

- Stopped the Hermes gateway for update.
- Ran `hermes update --backup --yes`.
- Hermes created pre-update backup:
  - `/Users/adamjohnsson/.hermes/backups/pre-update-2026-06-08-210411.zip`
  - restore command printed by updater: `hermes import /Users/adamjohnsson/.hermes/backups/pre-update-2026-06-08-210411.zip`
- Updated Hermes to current `origin/main`.
- Repaired the launchd gateway state after update:
  - `hermes gateway start` refreshed the stale service definition.
  - A short-lived duplicate background gateway exited; final state had one launchd-managed gateway process.
- Installed Photon sidecar dependencies with `hermes photon install-sidecar`.

## Proof

- `hermes --version` after update:
  - `Hermes Agent v0.16.0 (2026.6.5) - upstream b5f8996c`
  - `Up to date`
- `hermes photon --help` now shows:
  - `setup`
  - `status`
  - `install-sidecar`
  - `webhook`
- `hermes photon status` after sidecar install:
  - device token missing
  - project id missing
  - project key missing
  - webhook key unset
  - sidecar deps installed
- `hermes gateway status` after service repair:
  - service definition matches current Hermes install
  - gateway service loaded
  - launchd PID `39419`
- Gateway logs confirmed:
  - Telegram connected in polling mode
  - API server listening on `http://127.0.0.1:8642`

## Blocker

Photon account binding requires Adam's iMessage-capable phone number in E.164 format and browser/device approval through Photon. Codex did not guess or scrape a phone number.

## Next Step

Run:

```bash
hermes photon setup --phone '+1XXXXXXXXXX'
```

Then approve the Photon login in browser, create/register a public webhook URL for `http://127.0.0.1:8788/photon/webhook`, save `PHOTON_WEBHOOK_SECRET`, restart the gateway with Photon enabled, and approve/pair Adam's number if needed.

## Boundary

No posting, public messaging, email sending, Stripe/customer/money changes, deploys, credential printing, or Photon account binding were completed.
