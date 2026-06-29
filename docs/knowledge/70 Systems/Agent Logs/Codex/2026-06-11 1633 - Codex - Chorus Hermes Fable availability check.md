# Codex - Chorus Hermes Fable Availability Check

Time: 2026-06-11 16:33 CDT

## Request

Adam asked Codex to test whether Chorus is still available for use with Hermes, with Codex acting as the harness/operator and Fable 5 as the intended brain/engine via Hermes and Chorus. Adam also pointed to the Riley Brown X post about `@text_chorus` / Fable 5.

## What Was Checked

- Refreshed the Dead Hidden ops/team packet.
- Read the Chorus/Jarvis boundary and Active Ops Capsule tool-access rules.
- Pulled the referenced X post with authenticated read-only `xurl`.
- Checked Hermes version, profile, gateway, proxy readiness, and launchd state.
- Opened the known Chorus/Jarvis agent URL through Chrome CDP in read-only mode and inspected page state without submitting anything.

## X Source Signal

The Riley Brown post quoted a `text_chorus` post saying Claude Mythos / Fable 5 can build Swift apps from iMessage, to use `@text_chorus`, and to use `/model` to switch to Chorus.

This was treated as an idea signal only, not proof that Adam's local stack is currently connected.

## Hermes / Fable Result

- Hermes Agent is installed and responding as `v0.16.0`.
- Hermes gateway health returned `{"status":"ok","platform":"hermes-agent","version":"0.16.0"}`.
- `hermes status` reports model `claude-fable-5`, provider `claude-max-opus`, Telegram configured, and gateway running under launchd.
- `hermes profile show default` reports model `claude-fable-5 (claude-max-opus)`, gateway running, 69 skills, `.env` present, and `SOUL.md` present.
- `hermes proxy status` reports Nous Portal upstream ready, but the managed Nous Tool Gateway says the Portal account has no usable paid credits for managed web/image/TTS/browser/Modal tools.
- `launchctl print gui/501/com.biblicalman.claude-max-proxy` reports the service is not loaded.

Important boundary: `/Users/adamjohnsson/.deadhidden-os/ops/OUTBOUND_LOCKDOWN.md` is active and explicitly locks Fable/Claude Max proxy until Adam re-enables it. Codex did not restart the proxy, did not run a Fable prompt, and did not bypass the lock.

## Chorus / Jarvis Result

- The canonical Jarvis URL is still `https://chorus.com/agents/65bca62c-e9de-4e5c-8758-5c18e0917dd8`.
- Chrome CDP was available over IPv6 at `http://[::1]:9222/json/version`.
- Opening the Jarvis URL redirected to `https://chorus.com/sign-in?redirect_url=%2Fagents%2F65bca62c-e9de-4e5c-8758-5c18e0917dd8`.
- The page title was `Log in - Chorus`.
- The visible state was phone verification with a prefilled phone input and buttons for `Send code` and `Sign out`.

Codex stopped before pressing `Send code` because that would transmit a verification request/SMS. Current verdict: Chorus web is reachable, but the current browser session is not usable as Jarvis until Adam completes or approves the phone-code verification step.

## Recommended Harness Shape

- Codex remains the harness/operator/verifier and writes receipts.
- Hermes remains the local gateway/Telegram dispatch and profile runner.
- Fable 5 can be the high-judgment brain only after Adam explicitly re-enables the Fable/Claude Max path or gives a narrow safe smoke-test approval.
- Chorus/Jarvis should be treated as a connected-app read-only auditor after login is restored. It cannot read local Mac paths directly, so Codex/Hermes must paste `/teampacket` or specific context into Chorus before asking it to judge anything.

## Boundary

No X write, Substack action, email/customer action, provider change, SMS/code send, Fable run, Hermes proxy restart, launch-agent change, or public/account-changing action was performed.
