# Hermes/Fable outbound lockdown

Date: 2026-06-11 13:59 CDT
Agent: Codex

## Trigger

Adam reported Hermes/Fable had published/sent duplicate Dead Hidden launch emails and attempted to publish the afternoon Disclosure/Spielberg Substack post again.

## Confirmed damage scope

- Resend live API shows four sends today to the Dead Hidden audience `853ea354` with subject `The chapter you skip spells a sentence`:
  - `b15a5b20-aff6-493c-9425-9236d69d3161` — sent 2026-06-11 14:42:51 UTC
  - `985aeec1-8194-4964-9a70-f962384acc49` — sent 2026-06-11 15:02:30 UTC
  - `f6206074-5a36-430e-b28f-2145a22b5f13` — sent 2026-06-11 16:39:52 UTC
  - `8c898b61-38ab-48e1-a2de-7c524f49e5da` — sent 2026-06-11 18:31:26 UTC
- Substack current published list shows only original post `201605405` live; duplicate post `201639614` returns 404 after Adam deleted it.
- Disclosure/Spielberg draft `201607195` remains unpublished.
- Fable created/re-armed a second 6:30p publish timer after the first detached job was killed.

## Containment performed

- Killed detached 6:30p publish job `publish_spielberg_630.sh`.
- Killed second 6:30p timer `publish_disclosure_630.py`.
- Killed active Fable child process and unloaded `com.biblicalman.claude-max-proxy` so the local Fable queue cannot run.
- Unloaded public/customer outbound LaunchAgents:
  - `com.deadhidden.notes-scheduler`
  - `com.adam.substack-notes-auto-poster`
  - `com.deadhidden.xnoonpost`
  - `com.deadhidden.content-swarm`
  - `com.adam.jhan-launch-note`
  - `com.adam.jhan-backup-fire`
  - `com.hermes.dmcron.summary`
  - `com.deadhidden.payment-recovery`
- Left Hermes gateway running for read-only inspection; Fable route is offline because proxy is unloaded.
- Left Proton watch running because it is read/alert oriented.

## Lockdown guard

Created:

`/Users/adamjohnsson/.deadhidden-os/ops/OUTBOUND_LOCKDOWN.md`

Patched these scripts to abort while that file exists:

- `/Users/adamjohnsson/.hermes/scripts/publish_disclosure_20260611.py`
- `/Users/adamjohnsson/.hermes/scripts/publish_disclosure_630.py`
- `/Users/adamjohnsson/.hermes/jobs/publish_spielberg_630.sh`

Verification:

- Python compile passed.
- Shell syntax check passed.
- All three scripts print/log `ABORT: outbound lockdown active...` and exit before touching Substack.
- `hermes cron list` reports no scheduled jobs.
- No active Fable/proxy/publish/Resend/xurl/post_note process remains after freeze.

## Do not re-enable until fixed

Do not reload Fable/proxy or outbound LaunchAgents until:

1. Adam explicitly approves re-enabling.
2. The launch system has idempotency checks against Resend sent-history, Substack published-history, Notes IDs, and X tweet IDs.
3. Same-thread approval is treated as one-shot, not replayable.
4. Public/customer/money sends require a fresh approval token or a Codex-held harness check.
