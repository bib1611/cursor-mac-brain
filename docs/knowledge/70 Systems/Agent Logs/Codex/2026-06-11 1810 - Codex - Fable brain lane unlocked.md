# 2026-06-11 18:10 CDT - Codex - Fable Brain Lane Unlocked

Adam explicitly asked to unlock Fable because he pays for it and wants to use it.

Codex re-enabled only the Fable/Claude Max brain lane and kept the public/customer outbound locks in place.

Actions:

- Loaded launchd service `com.biblicalman.claude-max-proxy` from `/Users/adamjohnsson/Library/LaunchAgents/com.biblicalman.claude-max-proxy.plist`.
- Confirmed proxy is running on port `3458`.
- Updated `/Users/adamjohnsson/.deadhidden-os/ops/OUTBOUND_LOCKDOWN.md` so it marks the Fable lane unlocked while keeping public Substack/X/Notes, Resend/customer-email, and Disclosure/Spielberg one-shot publish scripts locked.
- Updated Dead Hidden Computer so Fable lock status is parsed from the file content instead of treating the mere existence of `OUTBOUND_LOCKDOWN.md` as a Fable lock.
- Updated `dhc chat` to use Hermes/Fable first when unlocked, with Kimi/Moonshot fallback.

Proof:

- Direct proxy health returned `status: ok`, account `thebiblicalman2`, queue `active:0 queued:0`.
- Direct Fable proxy smoke returned `FABLE_DIRECT_OK`.
- Hermes route smoke returned `HERMES_FABLE_OK`, session `20260611_180836_4ca73d`.
- `dhc status` returned `Fable lock: unlocked` and `Public outbound lock: active`.
- `dhc chat 'Reply exactly: DHC_FABLE_OK'` returned `DHC_FABLE_OK`.
- `python3 -m py_compile /Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer/script/dhc` passed.
- `swift build` passed in `/Users/adamjohnsson/Hermes-Workspace/dead-hidden-computer`.
- `./script/build_and_run.sh --verify` passed.

Boundary:

No Substack post, X post, Note, email, Resend action, Stripe/customer action, deploy, credential change, SMS/code send, public launch-agent restart, Disclosure/Spielberg script re-enable, or external-account mutation was performed.

