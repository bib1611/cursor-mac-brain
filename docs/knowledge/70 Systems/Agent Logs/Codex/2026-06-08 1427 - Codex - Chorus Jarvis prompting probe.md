# 2026-06-08 14:27 CDT - Codex - Chorus Jarvis Prompting Probe

## Request

Adam had the Chorus/Jarvis agent open and asked Codex to learn how to help prompt it for best use.

## Actions

- Loaded the Codex operator role and the Chorus/Jarvis boundary from the local ops capsule.
- Used fresh screen capture to inspect the open Chorus surface.
- Sent one read-only meta-prompt to Jarvis:
  - no changes, sends, creates, deletes, publishing, refunds, cancellations, uploads, or updates
  - ask for current readable sources, off-limits actions, prompt structure, routing split, proof types, and failure modes
- Did not request any state-changing operation.

## Observed Jarvis Guidance

- Confirmed/read in session: Notion reads, public web/WebFetch, SerpAPI/Google, individual X post URLs, Chorus gateway logs, memory, and past sessions.
- Connected but not exercised in that session: Dropbox, GitHub, Google Drive/Docs/Sheets/Calendar, Linear, and YouTube.
- Strong boundary: Jarvis cannot read local Mac paths such as `/Users/adamjohnsson/.deadhidden-os/` unless Codex or Adam copies the relevant text into Chorus.
- Jarvis is best for connected-app reads, cross-source research, Stripe/Gmail/Notion-style audits, drafting/refining copy in Adam's voice, gateway/messaging diagnosis, and long parallel sweeps.
- Codex/Hermes remain the right lane for local Mac files, canonical ops state, publishing, deploying, and changing account state.
- Jarvis can be slow or overproduce; prompts should force scope, proof, and cut lines.

## Practical Prompt Shape

Use this structure:

```text
Read-only unless I explicitly approve a specific action.

Goal:
[one sentence]

Sources to check:
[apps, URLs, docs, accounts, date range]

Do not:
[send, publish, refund, deploy, edit, upload, delete, create issues, or change state]

Return:
1. Answer first.
2. Evidence: copied snippets, links, counts, filenames, timestamps.
3. Confidence labels: confirmed / inferred / unsure.
4. Gaps and what Codex or Hermes must verify locally.
5. Next action recommendation.
```

## Boundary

No publishing, email, Stripe, Linear write, repo change, deploy, file upload/move/delete, or customer/account-state change was performed.
