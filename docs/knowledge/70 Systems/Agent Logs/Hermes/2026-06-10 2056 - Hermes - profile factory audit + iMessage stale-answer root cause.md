# Profile Factory Audit + iMessage Stale-Answer Root Cause
Date: 2026-06-10 evening. Agent: Hermes (Telegram).

## iMessage bot "old answer" root cause
- Photon session 20260610_113112_8999eede (state.db): Adam's ~20:30 voice memo stored as bare "(attachment)" — Photon path does NOT transcribe audio (Telegram path does).
- No assistant reply logged after that message; model had 59K tokens of day-long context, so the reply Adam received re-served earlier context (BM note thread). Bot never heard the question.
- gateway.error.log: photon adapter still flapping (inbound stream dropped / reconnect loop) — same instability as the 6:10 AM outage.
- Earlier richlinks also dropped: "[Photon content type not handled: richlink]".

## Profile factory findings
- Local Hermes v0.16.0 has commit d986bb0c6 "feat(dashboard): full-featured profile builder (model + skills + MCPs)".
- CLI: hermes profile {list,use,create,delete,describe,show,alias,rename,export,import,install,update,info}.
- 17 commits behind upstream; pending update includes fix(web): profiles page modal (#43858) + telegram/gateway delivery fixes.
- State snapshot 20260610-165400-pre-update exists (desktop updated; gateway repo still behind).
- 14 existing profiles; swarm1/4/5/8/12 have no model bound (dead shells). Active-value: kanban, librarian, openclaw, writer, workhorse, tactical.

## Recommendation given to Adam
Lean lineup mapped to lanes (writer/support/store-analyst), prune dead swarm profiles, fix Photon voice transcription before trusting iMessage with voice memos, run hermes update (with cron-loss caveat: session-bound support sweep cron dies on gateway restart).
