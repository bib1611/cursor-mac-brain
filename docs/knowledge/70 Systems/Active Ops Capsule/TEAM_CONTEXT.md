# Dead Hidden Agent Team Context

Generated: 2026-06-29 13:46 CDT

Purpose: one current packet for Codex, Claude Code, Hermes/Telegram, Chorus/Jarvis, Stanley, and future helper agents.
This is not permanent memory. It is the freshest team handoff built from the local ops capsule, memory/session indexes, recent receipts, and live routing rules.

## Team Contract

- Read this packet before trusting private chat memory.
- Treat live systems and readable local files as proof; treat session memory as a clue.
- If you change files, money/customer state, publishing, agent routing, repos, or external apps, write a receipt.
- If a claim comes from an older session, say that and verify before acting on money, customers, publishing, or code deploys.
- Chorus/Jarvis cannot read local Mac paths directly. Paste or mirror this packet into Chorus when asking it to work.

## Read First

- `/Users/adamjohnsson/.deadhidden-os/ops/AGENT_BOOT.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/README.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/TEAM.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/NOW.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/QUEUE.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/TOOL_ACCESS.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/RULES.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/RECEIPTS.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/TELEGRAM.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/CHORUS.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/CLOUD.md`

## Memory And Session Index

- Codex memory registry: `/Users/adamjohnsson/.codex/memories/MEMORY.md` (present)
- Hermes memory: `/Users/adamjohnsson/.hermes/memories/MEMORY.md` (present)
- Hermes user profile: `/Users/adamjohnsson/.hermes/memories/USER.md` (present)
- Hermes last session digest: `/Users/adamjohnsson/.hermes/memories/LAST_SESSION_DIGEST.md` (present)
- Codex raw sessions: `/Users/adamjohnsson/.codex/sessions` (present)
- Claude raw sessions: `/Users/adamjohnsson/.claude/projects` (present)
- Obsidian agent logs: `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Logs` (present)
- Agent Bus: `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Bus` (present)

For session recall, prefer the available session_search tool when a user asks what happened before. If unavailable, use these paths as raw evidence and summarize with receipts.

## NOW.md

Path: `/Users/adamjohnsson/.deadhidden-os/ops/NOW.md`

# NOW

Updated: 2026-06-02 16:42 CDT

## Current Operating Decision

The active control layer is now:

`/Users/adamjohnsson/.deadhidden-os/ops/`

This local capsule is the first-read runtime source for active work. Obsidian remains the deep brain and receipt archive, but it is not the runtime source while key vault files are cloud-offloaded or stale.

The active team packet is:

`/Users/adamjohnsson/.deadhidden-os/ops/TEAM_CONTEXT.md`

Use it to refresh Codex, Claude Code, Hermes/Telegram, Chorus/Jarvis, Stanley, or any future helper agent with the same current files, memory/session index, latest receipts, and raw session pointers.

The active Codex main-operator lane is:

`/Users/adamjohnsson/.deadhidden-os/ops/CODEX_OPERATOR.md`

Telegram `/askcodex <task>` now writes to both the Obsidian Agent Bus and the existing Codex bridge inbox, then the launchd watcher records visibility.

The active cloud fallback relay is:

`https://deadhidden-cloud-relay.vercel.app`

It keeps a cloud-readable handoff in Linear issue `DEA-22` and can create cloud fallback Linear tasks when the Macs are unavailable. The Mac-side puller is `com.deadhidden.cloud-relay-pull`. The active Telegram bot is not currently pointed at Vercel; local Hermes polling is primary.

The AWS EC2 hot-standby relay is:

`https://3-133-83-24.sslip.io`

It runs the same cloud relay source on EC2 instance `i-0298517081c7adf1b` in `us-east-2`. Vercel remains Telegram-primary unless Adam explicitly asks to change the Telegram webhook to EC2.

## Verified Local State

- `/Users/adamjohnsson/.deadhidden-os/ops/` did not exist before this cleanup.
- Disk pressure is real: `/System/Volumes/Data` showed 13GiB free, 94% used on 2026-06-02.
- Obsidian vault path is `/Users/adamjohnsson/Documents/Obsidian Vault`.
- 1,022 markdown files in the Obsidian vault were marked `dataless` as of 2026-06-02 14:46 CDT.
- These high-value vault files were marked `compressed,dataless` during first verification:
  - `70 Systems/Agent Ops/CURRENT OPERATOR STATE.md`
  - `00 Command Center/Linear - Obsidian Agent Operating Protocol.md`
  - `70 Systems/Hermes Telegram Bridge/README.md`
- Those three files were hydrated with `brctl download` and read successfully at 2026-06-02 14:50 CDT.
- After hydrating them, the Obsidian dataless markdown count is 1,019.
- The Notion / Stanley bridge note read normally and says Notion is a structured mirror, not canonical truth.
- The 2026-06-02 Codex receipt says Hermes has no Linear API key and no Linear MCP server configured.
- Chrome history contained the Jarvis Chorus agent URL: `https://chorus.com/agents/65bca62c-e9de-4e5c-8758-5c18e0917dd8`.
- At 2026-06-02 15:00 CDT, Codex opened Jarvis through Chrome CDP, sent the Active Ops Capsule routing update, and received confirmation from Jarvis.
- Jarvis reported read-only-capable connected integrations: Stripe, Gmail/Google, Notion, Linear, GitHub, Dropbox, and YouTube.
- Jarvis explicitly put write/send/account-changing actions on hold unless Adam names the exact action.
- At 2026-06-02 15:10 CDT, Codex added the Telegram/Hermes command layer documented in `TELEGRAM.md`.
- Hermes plugin discovery verified these commands: `/ops`, `/opshandoff`, `/route`, `/askcodex`, `/askclaude`, `/askhermes`, `/askchorus`, `/receipt`, `/opshelp`.
- Hermes main gateway restarted through launchd; new PID was `34101`.
- Telegram reconnected in polling mode and registered its command menu after restart.
- At 2026-06-02 15:18 CDT, Codex generated a local `API_SERVER_KEY` in `/Users/adamjohnsson/.hermes/.env` without printing the key.
- At 2026-06-02 15:19 CDT, Codex disabled the duplicate `ai.hermes.gateway-workhorse` and `ai.hermes.gateway-kanban` launch agents so main Hermes is the single Telegram polling owner.
- At 2026-06-02 15:19 CDT, main Hermes restarted with PID `36233`; Telegram and `api_server` both connected.
- Hermes API server now requires bearer auth. Verified: authorized `/v1/capabilities` returns capabilities; unauthenticated request returns `invalid_api_key`.
- Hermes `agentmemory` MCP is repaired for main Hermes: `mcp_servers.agentmemory.command` is pinned to `/Users/adamjohnsson/.local/bin/npx`.
- Hermes MCP test for `agentmemory` connected in 1017ms and discovered 51 tools.
- At 2026-06-02 15:35 CDT, Codex created a Linear personal API key named `Hermes Telegram Linear 2026-06-02`, stored it locally as `LINEAR_API_KEY` in `/Users/adamjohnsson/.hermes/.env` without printing the secret, and verified it against Linear GraphQL.
- Hermes Linear write access is now granted and tested for explicit Linear tasks. Proof: Codex added comment `b7464550-9f32-461d-bfd3-137f5259fc1e` to `DEA-21` through the new key.
- At 2026-06-02 15:44 CDT, Codex added the shared agent-team context layer: `TEAM.md`, generated `TEAM_CONTEXT.md`, `/team`, `/teampacket`, and automatic team-packet injection into `/askcodex`, `/askclaude`, `/askhermes`, and `/askchorus` Agent Bus tasks.
- At 2026-06-02 15:55 CDT, Codex aligned the Telegram-to-Codex lane: `/askcodex` mirrors into `/Users/adamjohnsson/.codex-bridge/shared/COMMAND-INBOX.md`, `/operator` and `/codexinbox` were added, and `com.deadhidden.codex-bus-watch` was installed as a 60-second launchd watcher.
- At 2026-06-02 16:08 CDT, Codex deployed the Vercel cloud fallback relay at `https://deadhidden-cloud-relay.vercel.app`, synced the cloud context to Linear issue `DEA-22`, installed `com.deadhidden.cloud-relay-pull`, and verified an end-to-end cloud intake smoke test with `DEA-23`.
- At 2026-06-02 16:10 CDT, Codex set the Telegram webhook to `https://deadhidden-cloud-relay.vercel.app/api/telegram` and verified a synthetic `/cloudstatus` webhook smoke request returned `ok: true`.
- Hermes initially reclaimed polling and cleared the webhook. Codex then set `platforms.telegram.enabled: false` in `/Users/adamjohnsson/.hermes/config.yaml`, restarted Hermes with API server only, re-set the webhook, and verified it persisted after 25 seconds.
- At 2026-06-02 16:34 CDT, Codex launched AWS EC2 instance `i-0298517081c7adf1b`, deployed the cloud relay under systemd, configured Caddy HTTPS for `https://3-133-83-24.sslip.io`, and verified health plus authenticated handoff to Linear `DEA-22`.
- At 2026-06-02 16:42 CDT, Adam asked to restore the live Telegram chat path. Codex backed up Hermes config, set `platforms.telegram.enabled: true`, deleted the Telegram webhook, restarted Hermes, and verified Telegram polling mode plus command-menu registration.

## Active Source Split

| Surface | Current Role | Proof Required |
| --- | --- | --- |
| Local ops capsule | Live routing and current state | This folder |
| Team context packet | Current cross-agent handoff, memory/session index, and latest receipts | `TEAM_CONTEXT.md` |
| Obsidian | Deep vault, source material, receipts, mirrored handoffs | Dated agent log or readable vault file |
| Linear | Tasks and implementation accountability | Linear issue URL |
| Notion | Structured mirror for Stanley/Chorus | Notion URL plus date |
| Telegram / blu | Intake, status, tactical routing | Bridge note or receipt |
| Hermes | Tactical dispatcher and local helper | Tool receipt, command output, or bridge note |
| Codex | Primary Mac-side router/executor and Telegram-reachable main operator | Local file, command output, PR, deploy, receipt, `CODEX_OPERATOR.md` |
| Claude Code | Specialist worker for code/writing | File changes plus receipt |
| Chorus / Jarvis | Connected-app helper and read-only external-app auditor | Screenshot, copied URL, or written note |
| Cloud relay | Mac-loss fallback intake and synced handoff | Vercel health URL, Linear issue URL |
| EC2 cloud relay | HTTPS hot standby for Mac-loss fallback | EC2 health URL, systemd status, Linear handoff |

## Current Blockers

- Obsidian has many dataless markdown files. Agents must not trust filenames alone.
- Hermes now has a tested local `LINEAR_API_KEY`; Linear writes are allowed only when Adam explicitly asks for a Linear action and the result returns a Linear issue/comment URL.
- Notion may be stale unless this capsule or a current Obsidian receipt has been mirrored into it.
- Broader disk cleanup or selective iCloud pinning is still needed before the whole Obsidian vault can be treated as a reliable runtime brain.
- Telegram is now local-Hermes polling primary. One bot token cannot use local polling and cloud webhook at the same time. Restore cloud fallback mode with `cloud-relay-webhook set` only if Adam explicitly wants that mode.
- EC2 is a hot standby, not Telegram-primary. The current Telegram webhook still points to Vercel.

## Current Default Owner

Codex is the default traffic controller on the Mac.

Route exceptions:

- Customer money, fulfillment, refunds, billing, Stripe, or active buyers: Codex verifies live systems before action.
- Writing/editing: Claude Code or Codex can draft, but the final artifact must be saved with a receipt.
- Telegram-first asks: Hermes/blu can intake and dispatch, but final proof must land here or in Obsidian.
- Stanley/Chorus asks: Notion is a mirror. Confirm critical facts against live source systems.
- Chorus/Jarvis asks: use `CHORUS.md`. Treat it as an external connected-app helper, not the canonical brain or Mac-side executor.
- Cross-agent asks: use `TEAM.md` and refresh `TEAM_CONTEXT.md`; paste `/teampacket` into agents that cannot read local Mac paths.
- Telegram-to-Codex asks: use `/askcodex`; check `/operator` or `/codexinbox` for visibility.
- Cloud-loss asks: use `CLOUD.md`; Vercel can create Linear fallback tasks but cannot run Mac-local tools until a Mac comes back online.

## QUEUE.md

Path: `/Users/adamjohnsson/.deadhidden-os/ops/QUEUE.md`

# QUEUE

Updated: 2026-06-14 08:10 CDT

## Active

- [active] MarketingSecrets 14-day trial sprint: Brain seeded, MCP configured, local `ms-brain` helper added. Next: use Chief of Staff / Attractive Character / One-to-Many / Dream 100 / Rev Scan against live Dead Hidden offers, then decide keep/cancel by 2026-06-26 before possible day-14 billing on 2026-06-28 if trial started 2026-06-14.
- [done] Create local non-cloud ops capsule at `/Users/adamjohnsson/.deadhidden-os/ops/`.
- [done] Mirror the capsule pointer into Obsidian under `70 Systems/Active Ops Capsule/`.
- [done] Log the cleanup as a Codex receipt.
- [done] Add boot pointers for Codex, Claude Code, and Hermes so new sessions read this capsule first.
- [done] Add read-only health check at `/Users/adamjohnsson/.deadhidden-os/ops/bin/health-check`.
- [done] Hydrate the three small Obsidian control files found dataless during setup.
- [done] Mirror routing decision into Notion Agent Operating Notes.
- [done] Create Linear issue for Hermes Linear access boundary decision: `DEA-21`.
- [done] Tap Chorus/Jarvis into the Active Ops Capsule: sent read-only routing handoff through Chrome CDP and captured Jarvis confirmation.
- [done] Add Telegram/Hermes command layer: `/ops`, `/opshandoff`, `/route`, `/askcodex`, `/askclaude`, `/askhermes`, `/askchorus`, `/receipt`, `/opshelp`.
- [done] Restart Hermes main gateway and verify Telegram reconnect/menu registration.
- [done] Resolve `DEA-21` operational boundary: Hermes routes Linear writes through Codex/Jarvis; do not grant direct Hermes Linear API access without Adam explicitly supplying and approving a key.
- [done] Configure `API_SERVER_KEY` for Hermes API server and verify bearer auth.
- [done] Repair Hermes `agentmemory` MCP startup path by pinning the main config command to `/Users/adamjohnsson/.local/bin/npx`; `hermes mcp test agentmemory` found 51 tools.
- [done] Disable duplicate workhorse/kanban gateway launch agents so main Hermes is the single Telegram polling owner.
- [done] Grant and test Hermes Linear API access: `LINEAR_API_KEY` is stored in `/Users/adamjohnsson/.hermes/.env`; GraphQL read test and `DEA-21` comment write test passed.
- [done] Add shared agent-team context layer: `TEAM.md`, generated `TEAM_CONTEXT.md`, `/team`, `/teampacket`, and automatic team-packet injection into routed Agent Bus tasks.
- [done] Align Telegram-to-Codex reachability: `/askcodex` now mirrors Agent Bus tasks into the Codex bridge inbox.
- [done] Add Telegram commands `/operator` and `/codexinbox`.
- [done] Install launchd watcher `com.deadhidden.codex-bus-watch` to detect Telegram-created Codex tasks and write status/receipts without auto-executing work.
- [done] Add Vercel cloud fallback relay at `https://deadhidden-cloud-relay.vercel.app`.
- [done] Sync cloud team context to Linear issue `DEA-22`.
- [done] Install Mac-side cloud fallback puller `com.deadhidden.cloud-relay-pull`.
- [done] Verify cloud API intake to Linear and Mac-side pull back into Agent Bus with smoke issue `DEA-23`.
- [done] Cut Telegram over to the Vercel cloud webhook and verify a `/cloudstatus` webhook smoke request.
- [done] Add AWS EC2 cloud relay hot standby at `https://3-133-83-24.sslip.io`.
- [done] Restore live Telegram chat by deleting the Vercel webhook, re-enabling Hermes Telegram polling, and restarting the main Hermes gateway.

## Waiting On Adam

- Whether to pin more Obsidian files locally after disk cleanup. Current dataless markdown count is 1,019.
- Whether to add a second Telegram bot later so cloud fallback and local Hermes rich polling can run side by side without switching modes.

## Later

- Add a Chorus/Jarvis periodic sync note if Adam wants Chorus to receive copied capsule changes on a schedule.
- Mirror `TEAM_CONTEXT.md` into Notion on a schedule or through Chorus once a reliable write path is selected.
- Add a weekly cleanup step for old Codex/Claude/Hermes session artifacts that have receipts.
- Decide whether to enable macOS notifications for Codex bus watcher with `CODEX_BUS_WATCH_NOTIFY=1`.
- Consider a second dedicated emergency bot token if Adam wants local Hermes polling and cloud webhook simultaneously.
- Decide whether EC2 should stay hot standby or become Telegram webhook primary after a longer soak.

## TOOL_ACCESS.md

Path: `/Users/adamjohnsson/.deadhidden-os/ops/TOOL_ACCESS.md`

# TOOL ACCESS

Updated: 2026-06-02 16:42 CDT

## Verified In This Cleanup

| Tool / Surface | Current Access | Notes |
| --- | --- | --- |
| Local shell | Available | Used to create this capsule and inspect local files. |
| Obsidian vault | Read/write by filesystem | Many markdown files are dataless; do not trust filenames alone. |
| Chrome CDP | Expected on `127.0.0.1:9333` | Use for authenticated browser state, not public web fetch. |
| Hermes env | Present at `/Users/adamjohnsson/.hermes/.env` | Do not print secrets. |
| Hermes Linear | Available | `LINEAR_API_KEY` is present in `/Users/adamjohnsson/.hermes/.env`; GraphQL read test and `DEA-21` comment write test passed on 2026-06-02. Do not print the key. |
| Hermes Telegram command layer | Available | `/ops`, `/opshandoff`, `/route`, `/askcodex`, `/askclaude`, `/askhermes`, `/askchorus`, `/receipt`, `/opshelp` verified through plugin discovery. |
| Agent Team packet | Available | `dh-ops team` refreshes `TEAM_CONTEXT.md`; `dh-ops teampacket` prints it; `/ask*` Agent Bus tasks include it automatically. |
| Codex main operator lane | Available | `/askcodex` creates an Agent Bus task, mirrors it to `/Users/adamjohnsson/.codex-bridge/shared/COMMAND-INBOX.md`, and `com.deadhidden.codex-bus-watch` records new Codex tasks. |
| Cloud relay | Available | Vercel production URL `https://deadhidden-cloud-relay.vercel.app`; health and authenticated handoff verified on 2026-06-02. |
| EC2 cloud relay hot standby | Available | AWS EC2 `i-0298517081c7adf1b` at `https://3-133-83-24.sslip.io`; systemd relay plus Caddy HTTPS verified on 2026-06-02. |
| Cloud Linear context | Available | Linear issue `DEA-22` stores the current cloud packet. |
| Cloud task puller | Available | `com.deadhidden.cloud-relay-pull` pulls cloud fallback Linear issues into the Agent Bus. Smoke test `DEA-23` passed. |
| Telegram local polling | Available | Existing Telegram bot webhook is deleted; Hermes gateway PID `64981` connected in polling mode and registered the command menu at 2026-06-02 16:41 CDT. |
| Hermes API server | Available | `API_SERVER_KEY` configured in `.hermes/.env`; authorized `/v1/capabilities` works, unauthenticated request returns `invalid_api_key`. |
| Hermes agentmemory MCP | Available | `hermes mcp test agentmemory` connected and discovered 51 tools. Main config pins command to `/Users/adamjohnsson/.local/bin/npx`. |
| Hermes duplicate gateways | Disabled | `ai.hermes.gateway-workhorse` and `ai.hermes.gateway-kanban` disabled through launchd so only main Hermes polls Telegram. |
| Notion / Stanley | Mirror exists | Notion bridge says Stanley reads Notion and Linear, not Obsidian directly. |
| Linear | Direct through Hermes key or Codex/Jarvis | Hermes can write through `LINEAR_API_KEY` when Adam explicitly asks for a Linear action. A Linear write is only real with a Linear issue/comment URL or connector receipt. |
| Chorus / Jarvis | Browser access verified through Chrome CDP | Jarvis received the routing update and reported read-only-capable Stripe, Gmail/Google, Notion, Linear, GitHub, Dropbox, and YouTube integrations. |

## Agent Rules

- Codex can inspect and edit local files, run verification, and write receipts.
- Codex should check `/Users/adamjohnsson/.deadhidden-os/ops/CODEX_OPERATOR.md` and `/Users/adamjohnsson/.deadhidden-os/ops/status/CODEX_BUS_WATCH.md` when Adam is operating from Telegram.
- Claude Code can work as a specialist, but must save changed paths and a receipt.
- Hermes/blu can dispatch and summarize, but must write or point to proof.
- Chorus/Jarvis can help with connected apps and read-only external-app checks, but does not become the brain or Mac-side executor. It cannot read local Mac paths directly unless Adam/Codex provides copied content.
- Agents that cannot read local Mac paths should receive the `/teampacket` output or the copied `TEAM_CONTEXT.md` section from a routed Agent Bus task.
- If no Mac is available, the cloud relay can create Linear fallback tasks. Treat the Linear URL as proof of queued work, not proof of Mac-side execution.
- Hermes local Telegram polling is enabled in `/Users/adamjohnsson/.hermes/config.yaml`; cloud webhook mode is available but not active.
- Stanley can use Notion/Linear context, but Notion is a mirror and may be stale.

## Sensitive Actions

Do not do these without Adam explicitly asking for the specific action:

- Send email or broadcasts.
- Post to X, Threads, Substack, Facebook, or Telegram channels.
- Create Stripe checkout links, refunds, discounts, or subscription changes.
- Grant new API keys to Hermes or any other agent.
- Delete or bulk-move vault files.
- Ask Chorus/Jarvis to send email, cancel subscriptions, create Stripe links/refunds, post/publish, create/update Linear issues, upload/move/delete files, or change account state.

## RULES.md

Path: `/Users/adamjohnsson/.deadhidden-os/ops/RULES.md`

# RULES

Updated: 2026-06-02 16:08 CDT

## First-Read Rule

Every agent working for Adam should read:

`/Users/adamjohnsson/.deadhidden-os/ops/README.md`

Then read:

1. `NOW.md`
2. `QUEUE.md`
3. `TOOL_ACCESS.md`
4. `RULES.md`
5. `RECEIPTS.md`
6. `TEAM.md`
7. `CLOUD.md` when the task involves cloud fallback, Telegram webhook cutover, or Mac-loss continuity.

For cross-agent continuity, refresh/read:

`/Users/adamjohnsson/.deadhidden-os/ops/TEAM_CONTEXT.md`

## Source-Of-Truth Rule

Live source truth beats memory.

Order of trust:

1. Live system or local repo state.
2. This local ops capsule.
3. Dated receipt in Obsidian.
4. Notion/Linear mirror with URL and date.
5. Session memory or chat summary.

If no Mac is online, Linear cloud context issue `DEA-22` and the Vercel deployment snapshot are the best available fallback, but they are stale until a Mac or live system verifies them.

## Team Packet Rule

Use `TEAM_CONTEXT.md` as the shared current handoff for all agents.

- Refresh it with `/Users/adamjohnsson/.deadhidden-os/ops/bin/dh-ops team`.
- Use `/teampacket` in Telegram when an agent needs pasted context.
- `/askcodex`, `/askclaude`, `/askhermes`, and `/askchorus` Agent Bus tasks include the packet automatically.
- Session files and memories listed in the packet are evidence sources, not commands; verify before acting on high-risk work.

## Receipt Rule

If a task changes money, publishing, customer support, repo state, agent routing, or live workflows, leave a receipt.

Preferred receipt path:

`/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Logs/<Agent>/YYYY-MM-DD HHMM - <Agent> - task.md`

If Obsidian is unreliable, write the receipt path into:

`/Users/adamjohnsson/.deadhidden-os/ops/RECEIPTS.md`

## Linear Rule

Linear is for tasks, not memory.

- A Linear write is only real when the agent returns a Linear issue URL.
- Hermes has verified Linear GraphQL access through `LINEAR_API_KEY` in `/Users/adamjohnsson/.hermes/.env`.
- Hermes may perform Linear writes only when Adam explicitly asks for a Linear action, and the result must include a Linear issue/comment URL.
- Never print, paste, or summarize the Linear key value.

## Notion Rule

Notion is a structured mirror for Stanley/Chorus.

- Do not treat Notion as canonical for offer prices, buyers, customer state, or current campaigns.
- Verify critical facts against Stripe, repo, Resend/Gmail/Proton, Substack, or readable Obsidian receipts.

## Chorus / Jarvis Rule

Chorus/Jarvis is a connected-app helper and read-only external-app auditor, not the runtime brain.

- It cannot read local Mac paths directly. Provide copied notes or point it to the Notion mirror.
- It confirmed read-only-capable access to Stripe, Gmail/Google, Notion, Linear, GitHub, Dropbox, and YouTube on 2026-06-02.
- It must not send emails, cancel subscriptions, create Stripe links/refunds, post/publish, create or update Linear issues, upload/move/delete files, or change account state unless Adam explicitly names that exact action.
- Any Chorus result must come back with a copied URL, written note, screenshot, or other receipt.

## Telegram Rule

Telegram is an operator surface.

- Use it for intake, status, and dispatch.
- Do not let Telegram-only history become the only proof.
- Any meaningful Telegram task needs a receipt or a bridge note.
- Use `/ops` for Dead Hidden status. `/status` is reserved by Hermes for session status.
- Use `/opshandoff` for the Dead Hidden ops handoff. `/handoff` is reserved by Hermes for cross-platform session handoff.
- Use `/askcodex`, `/askclaude`, `/askhermes`, and `/askchorus` to create routed Agent Bus work from Telegram.
- Use `/operator` and `/codexinbox` to check whether Codex has pending Telegram-created work.
- Chorus/Jarvis requests created from Telegram are bridge requests; Chorus cannot read local Mac paths until Adam/Codex/Hermes copies the request into Jarvis.

## Cloud Relay Rule

The cloud relay is for Mac-loss continuity, not full Mac-side execution.

- Production URL: `https://deadhidden-cloud-relay.vercel.app`.
- Cloud context issue: `DEA-22`.
- Cloud fallback tasks are Linear issues marked with `DH_CLOUD_RELAY_TASK`.
- `com.deadhidden.cloud-relay-pull` imports those issues into Agent Bus when a Mac is online.
- Telegram can be local polling or cloud webhook for one bot token, not both.
- Do not set or delete the Telegram webhook without recording it in `CLOUD.md` and `RECEIPTS.md`.

## Codex Main Operator Rule

`/askcodex` must create durable, visible work. The current path is:

1. Create an Agent Bus task in `70 Systems/Agent Bus/inbox/`.
2. Attach the current team packet.
3. Mirror the request into `/Users/adamjohnsson/.codex-bridge/shared/COMMAND-INBOX.md`.
4. Let `com.deadhidden.codex-bus-watch` record visibility in `status/CODEX_BUS_WATCH.md`.

The watcher does not claim, execute, publish, send, spend, refund, deploy, delete, or change account state.

## Obsidian Rule

Obsidian remains the deep brain, but it must be readable.

- Do not trust a vault filename if the file is empty, unreadable, or marked `dataless`.
- Pin or hydrate only the control files needed for active work.
- Preserve provenance when moving or copying archive material.

## Support Auto-Fix Rule (Adam, 2026-06-10 18:05 CDT)

Customer product/download/access complaints are AUTO-FIX AUTHORIZED. Any agent may, without per-incident approval:

- verify the purchase (Stripe / [AUTO] Purchase Tag email)
- test the live delivery route
- resend the product file via Resend from adam@deadhidden.org (precedent: Agent Logs/Hermes/2026-06-10 1710; API pattern in ~/.hermes/scripts/payment_recovery/dunning_sweep.py)
- reply short and plain, sign-off "Adam"

NO REFUNDS. Ever, without Adam's explicit same-thread approval. Refund requests = make access right (resend, upgrade, bonus PDF per the paintdry4u precedent) and flag Adam. Cancellations and card changes also stay Adam-only.

## X Posting Lockdown (Adam, 2026-06-11 21:45 CDT)

NO agent posts to X without Adam's explicit same-thread approval of the EXACT final text. No exceptions, no standing approvals, no "he approved the idea so the post is approved."

Cause: 2026-06-11 incident. Hermes flagged a Facebook share link as a stolen Dead Hidden post, mischaracterized the source, and a tweet went out built on that wrong claim. Adam deleted it himself. The verification failed BEFORE the posting did — the post inherited the bad claim.

Operating consequence:
- Draft freely. Post nothing.
- "Sure, post it" applies only to text Adam has already seen verbatim in that thread.
- Any claim about theft/plagiarism/copying requires the actual source artifact loaded and quoted in-session before it appears in ANY draft (see plagiarism stance: convergent biblical themes are commonplace; never accuse on a preview).
- Scheduled/staged X posts count as posts. A staged post that fires later still needs the exact-text approval at staging time, and must be killable: record where it is staged in the receipt.

## TELEGRAM.md

Path: `/Users/adamjohnsson/.deadhidden-os/ops/TELEGRAM.md`

# TELEGRAM / HERMES COMMAND LAYER

Updated: 2026-06-13 07:58 CDT

## Current Decision

Telegram/blu is the remote operator front door.

Telegram is now local-Hermes polling primary again for live chat. Codex remains the Mac-side router/executor. The local ops capsule remains runtime truth when a Mac is online:

`/Users/adamjohnsson/.deadhidden-os/ops/`

## Current Opus Lane

Verified 2026-06-13 07:58 CDT:

- Adam requested Fable 5 off and Opus 4.8 on after the picker showed Fable 5 unavailable. Codex treated that as an operational model-availability signal, not a verified legal claim.
- Hermes default model is `claude-opus-4-8`.
- Hermes default provider is `claude-max-opus`.
- Main, `writer`, and `storeanalyst` Hermes configs now default to `claude-opus-4-8`.
- Local Claude Max proxy is `com.biblicalman.claude-max-proxy` on `http://127.0.0.1:3458/v1`; launchd reports it running as PID `14588`.
- Proxy log shows direct Opus 4.8 requests completed successfully at 07:52 and 07:54 CDT.
- Gateway service is `ai.hermes.gateway`, launchd `user/501`, PID `11268`; Codex could not kickstart or kill it from the sandbox (`Operation not permitted`).
- Existing Telegram cached agents may stay on the old Fable route until `/new` or `/reset`, cache eviction, or a manual gateway restart. Use `/new` in Telegram before the next Hermes task to force a fresh Opus 4.8 agent.
- Telegram is connected in local polling mode.
- Telegram webhook remains blank; cloud fallback is not active for the bot.

Cloud fallback exists at:

`https://deadhidden-cloud-relay.vercel.app`

One Telegram bot token can use local polling or cloud webhook, not both. Current state: webhook is deleted and Hermes is connected to Telegram in polling mode.

## Live Commands

Use these in Telegram:

- `/ops` - current Dead Hidden ops status from the local capsule.
- `/operator` - Codex main operator reachability and service status.
- `/codexinbox` - pending Codex Agent Bus tasks.
- `/opshandoff` - compact handoff for Codex, Claude Code, Hermes, Chorus/Jarvis, or Stanley.
- `/team` - refresh and show the shared agent team context packet paths.
- `/teampacket` - print a compact shared team packet for copy/paste into agents that cannot read local files.
- `/route <task>` - recommend the owner for a task.
- `/askcodex <task>` - create a Codex Agent Bus task.
- `/askclaude <task>` - create a Claude Agent Bus task.
- `/askhermes <task>` - create a Hermes Agent Bus task.
- `/askchorus <task>` - create a Chorus/Jarvis bridge request.
- `/receipt <note>` - write a durable Telegram operator receipt.
- `/opshelp` - show this command list.
- `/dhstatus` - legacy local operator health check.
- `/bus` - list Agent Bus inbox tasks.

The `/askcodex`, `/askclaude`, `/askhermes`, and `/askchorus` commands now attach the current `TEAM_CONTEXT.md` packet to the created Agent Bus task automatically.

`/askcodex` additionally mirrors the request into:

`/Users/adamjohnsson/.codex-bridge/shared/COMMAND-INBOX.md`

and the launchd watcher `com.deadhidden.codex-bus-watch` records new Codex tasks in:

`/Users/adamjohnsson/.deadhidden-os/ops/status/CODEX_BUS_WATCH.md`

Reserved:

- `/status` is Hermes' built-in session status. Use `/ops` for Dead Hidden status.
- `/handoff` is Hermes' built-in cross-platform handoff command. Use `/opshandoff` for the Dead Hidden ops handoff.

## Implementation Proof

Helper:

`/Users/adamjohnsson/.deadhidden-os/ops/bin/dh-ops`

Hermes user plugin:

`/Users/adamjohnsson/.hermes/plugins/deadhidden-ops-commands/`

Hermes config:

`/Users/adamjohnsson/.hermes/config.yaml`

Configured:

- `quick_commands.ops`
- `quick_commands.opshandoff`
- `quick_commands.opshelp`
- `plugins.enabled: deadhidden-ops-commands`

Agent Bus helper updated to accept `chorus` and `jarvis` as requested agents:

`/Users/adamjohnsson/.agents/bin/dh-bus`

## Verification

Verified at 2026-06-02 15:44 CDT:

- Hermes plugin discovery registered `ops`, `opshandoff`, `team`, `teampacket`, `route`, `askcodex`, `askclaude`, `askhermes`, `askchorus`, `receipt`, and `opshelp`.
- Codex operator commands are wired through `dh-ops`: `/operator` and `/codexinbox`.
- Codex bus watcher launch agent: `/Users/adamjohnsson/Library/LaunchAgents/com.deadhidden.codex-bus-watch.plist`.
- `dh-ops status`, `dh-ops route`, and `dh-ops help` returned clean output.
- Hermes main gateway restarted through launchd.
- New gateway PID after restart: `34101`.
- Telegram reconnected in polling mode.
- Telegram menu registration succeeded for default, private chat, and group scopes.

## Known Remaining Warnings

- Current Telegram state as of 2026-06-02 16:42 CDT: webhook is not set; local Hermes polling is primary for Telegram intake.
- Cloud commands are `/cloudstatus`, `/cloudhandoff`, `/cloudaskcodex`, `/askcodex`, `/askclaude`, `/askhermes`, `/askchorus`, and `/route`.
- Hermes config has `platforms.telegram.enabled: true`.
- Restore cloud fallback mode with `/Users/adamjohnsson/.deadhidden-os/ops/bin/cloud-relay-webhook set` only if Adam wants the active bot moved back to Vercel.
- Chorus/Jarvis still cannot read local Mac paths directly; paste `/teampacket` or mirror the packet into Notion/Jarvis.
- Obsidian still has many dataless markdown files; use the team packet and receipts before trusting vault filenames.

## CHORUS.md

Path: `/Users/adamjohnsson/.deadhidden-os/ops/CHORUS.md`

# CHORUS / JARVIS

Updated: 2026-06-18 18:18 CDT

## Latest Setup Attempt - 2026-06-18 18:18 CDT

Codex recovered Chrome extension control, proved the pipe was healthy, and finished the Jarvis cloud-agent setup through the live Chorus page:

`https://chorus.com/agents/65bca62c-e9de-4e5c-8758-5c18e0917dd8`

Verified repair/state:

- Clean browser runtime reset restored `browser.user.openTabs()`; Jarvis tab was visible and claimable.
- Chrome helper checks passed: Chrome running, Google Chrome installed, Codex Chrome Extension installed/enabled in the `Default` profile, native host manifest correct.
- Isolated local smoke test proved text and clipboard control worked.
- Isolated file chooser test failed with `{"code":-32000,"message":"Not allowed"} fileChooser.setFiles failed`; this is the Chrome extension file-upload permission fork, not a native pipe failure.
- Chrome automation cannot open `chrome://extensions`; do not work around this with raw CDP/AppleScript. Manual fix for uploads: in Chrome, open `chrome://extensions`, click Details under the Codex Chrome Extension, enable `Allow access to file URLs`.

Jarvis update:

- Used Jarvis `Build with your agent` flow.
- First attempt only sent the Chorus starter prompt; Jarvis replied that the message cut off.
- Second attempt used coordinate focus plus browser clipboard paste, verified `dead-hidden-ops-context`, `Trust order`, and `Codex task:` were in the composer before sending.
- Jarvis replied: `Created: dead-hidden-ops-context`.
- Jarvis test answer correctly stated it is the cloud connected-app helper/read-only auditor, that Codex owns Mac-local execution, that Notion/Linear are mirrors/tracking, that raw secrets must not be exposed, and that email/posting/Stripe/customer/file/Linear/app mutations require exact Adam approval.

Local Codex skill added for future repairs:

`/Users/adamjohnsson/.codex/skills/repair-chrome-extension-pipe/SKILL.md`

Validated with:

`python3 /Users/adamjohnsson/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/adamjohnsson/.codex/skills/repair-chrome-extension-pipe`

## Latest Setup Attempt - 2026-06-18 18:05 CDT

Codex opened Chrome, restored Codex Chrome Extension control after launching a fresh Chrome window, logged into Chorus/Jarvis through Google as `thebiblicalman1611@gmail.com`, and reached the canonical Jarvis agent:

`https://chorus.com/agents/65bca62c-e9de-4e5c-8758-5c18e0917dd8`

Observed live state:

- Jarvis page title: `Jarvis - Chorus`.
- Agent panel opened.
- Overview reported Jarvis as a `Data Analyst`.
- Overview reported 179 skills.
- Skills tab showed installed/enabled skills including Stripe, Notion, Linear, Google Workspace, Environment, screenshot, `gh-fix-ci`, `notion-knowledge-capture`, `figma-implement-design`, and `netlify-deploy`.
- Files tab was accessible and showed workspace folders such as `skills`, `Pictures`, `Public`, `Projects`, `Documents`, and `Desktop`.
- Skills tab exposed `Add custom skill` with options: `Build with your agent`, `Upload a skill`, and `Upload a folder`.
- Connections tab opened but rendered inside an embedded iframe that did not provide a readable body through the Chrome extension.
- Platforms tab was not fully inspected in this pass; prior visible overview still showed `Platforms: None`.

Local setup artifacts created:

- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-18-jarvis-cloud-agent-setup.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-18-dead-hidden-ops-context-chorus-skill.md`

Blocker:

The Codex Chrome Extension native pipe became unstable after repeated file-upload/DOM attempts and started returning `native pipe is closed`. The safe setup packet and custom skill were not successfully pasted or uploaded into Jarvis during this pass.

Next manual/resume action:

Open the Jarvis tab in Chrome, use the `Add custom skill` menu in Skills, choose `Upload a skill`, and upload `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-18-dead-hidden-ops-context-chorus-skill.md`; or paste the first-test prompt from `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-18-jarvis-cloud-agent-setup.md` into the Jarvis composer.

## Current Boundary

Chorus/Jarvis is a connected-app helper and read-only external-app auditor.

It is not the runtime brain, not the Mac-side executor, and not the source of truth.

Runtime truth remains:

`/Users/adamjohnsson/.deadhidden-os/ops/`

Chorus cannot read that local path directly unless Adam/Codex copies the relevant text into the Chorus thread.

Current copied context source:

`/Users/adamjohnsson/.deadhidden-os/ops/TEAM_CONTEXT.md`

From Telegram, use `/teampacket` to print the context or `/askchorus <task>` to create a bridge request that includes the current packet.

## Verified Jarvis Agent

URL:

`https://chorus.com/agents/65bca62c-e9de-4e5c-8758-5c18e0917dd8`

Verified through Chrome CDP at 2026-06-02 15:00 CDT.

Jarvis received the Active Ops Capsule routing update and confirmed it saved the rule as standing policy.

## Read-Only-Capable Integrations Jarvis Reported

- Stripe: balances, payouts, charges, subscriptions, invoices, disputes, customers.
- Gmail / Google: search and read mail, Drive, Docs, Sheets, Slides, Forms, Calendar.
- Notion: read and search pages/databases, including the Active Ops Capsule mirror.
- Linear: read issues, projects, cycles, status.
- GitHub: read repos, branches, commits, PRs, CI status, file contents.
- Dropbox: list and read files.
- YouTube: read channel/video data and analytics.

## Off-Limits Without Exact Adam Approval

- Sending email.
- Cancelling subscriptions.
- Creating Stripe payment links, refunds, discounts, or subscription changes.
- Posting or publishing.
- Creating or updating Linear issues.
- Pushing, merging, or opening GitHub PRs/issues.
- Creating, editing, moving, uploading, or deleting files.
- Sending iMessage/SMS.
- Any account-state change.

## Operating Rule

Use Chorus/Jarvis for read-only checks across connected apps when it can produce proof.

For any action that changes state, Adam must name the exact action and the expected target. The completion proof must be a copied URL, written note, screenshot, or external-app receipt.

## CLOUD.md

Path: `/Users/adamjohnsson/.deadhidden-os/ops/CLOUD.md`

# CLOUD RELAY

Updated: 2026-06-02 16:42 CDT

## Current Decision

Dead Hidden now has a cloud fallback relay on Vercel:

`https://deadhidden-cloud-relay.vercel.app`

It also has an AWS EC2 hot-standby relay:

`https://3-133-83-24.sslip.io`

The relay exists so Adam can still reach the operator system if the Mac mini or MacBook Air is offline, lost, or unavailable.

## What Cloud Can Do

- Return a current synced team handoff.
- Receive Telegram or HTTP intake when the webhook is pointed at Vercel.
- Create Linear fallback tasks in the `DEA` team.
- Run a bounded cloud agent from the synced packet through `/api/agent` or Telegram `/cloudagent` when model credentials are configured.
- Let the Mac pull those Linear fallback tasks back into the local Agent Bus when a Mac comes online.

## What Cloud Cannot Do

- Read Mac-local files that were not synced.
- Use Chrome CDP on `127.0.0.1:9333`.
- Read local Codex/Claude/Hermes session files after the Mac is gone.
- Hydrate iCloud-offloaded Obsidian files.
- Publish, send, spend, refund, deploy, delete, or change account state.

## Cloud Agent Runner

Local source status as of 2026-06-18 15:47 CDT:

- `/Users/adamjohnsson/.deadhidden-os/cloud-relay` has a local `/api/agent` endpoint and Telegram `/cloudagent` / `/agent` command handler.
- The cloud agent reads the synced cloud packet, routes the task, calls a server-side model, creates a Linear fallback issue, and attaches `DH_CLOUD_AGENT_RESULT` as a Linear comment.
- It uses `OPENROUTER_API_KEY`, `OPENAI_API_KEY`, or `CLOUD_AGENT_API_KEY`; optional knobs are `CLOUD_AGENT_MODEL`, `CLOUD_AGENT_BASE_URL`, `CLOUD_AGENT_MAX_TOKENS`, and `CLOUD_AGENT_PACKET_CHARS`.
- Local smoke checks passed, including a live OpenRouter call that returned `CLOUD_READY`.
- It is not live on Vercel or EC2 until Adam explicitly approves production deployment and cloud model credentials are present in the target environment.

Boundary remains: cloud agent output is draft/route/reasoning only. Mac-local verification is still required before publishing, sending, spending, refunding, deploying, deleting, or changing account state.

## Current Cloud Proof

- Vercel project: `deadhidden-cloud-relay`
- Production URL: `https://deadhidden-cloud-relay.vercel.app`
- Health endpoint: `https://deadhidden-cloud-relay.vercel.app/api/health`
- Telegram webhook: not currently set; local Hermes polling is primary.
- AWS EC2 relay: `https://3-133-83-24.sslip.io`
- AWS EC2 health endpoint: `https://3-133-83-24.sslip.io/api/health`
- AWS EC2 instance: `i-0298517081c7adf1b` in `us-east-2`, public IP `3.133.83.24`
- AWS EC2 SSH key: `/Users/adamjohnsson/.ssh/deadhidden-ops-relay-20260602`
- AWS EC2 security group: `sg-0a0098505fb898faa`
- Linear cloud context issue: `https://linear.app/deadhidden-os/issue/DEA-22/dh-cloud-current-team-packet`
- Local cloud relay source: `/Users/adamjohnsson/.deadhidden-os/cloud-relay`
- Local secret file: `/Users/adamjohnsson/.deadhidden-os/ops/cloud/cloud-relay-secrets.env`

## Local Commands

Sync the current Mac packet into the cloud relay project and Linear context issue:

`/Users/adamjohnsson/.deadhidden-os/ops/bin/cloud-relay-sync`

Pull cloud fallback Linear issues into the local Agent Bus:

`/Users/adamjohnsson/.deadhidden-os/ops/bin/cloud-relay-pull`

Redeploy the relay source and synced cloud packet to the EC2 hot standby:

`/Users/adamjohnsson/.deadhidden-os/ops/bin/ec2-relay-deploy`

Check EC2 hot-standby health:

`/Users/adamjohnsson/.deadhidden-os/ops/bin/ec2-relay-health`

Check Telegram webhook state:

`/Users/adamjohnsson/.deadhidden-os/ops/bin/cloud-relay-webhook status`

Set Telegram webhook to the cloud relay:

`/Users/adamjohnsson/.deadhidden-os/ops/bin/cloud-relay-webhook set`

Delete the webhook and return to local Hermes polling:

`/Users/adamjohnsson/.deadhidden-os/ops/bin/cloud-relay-webhook delete`

## Telegram Cutover Boundary

Telegram supports either local polling or a webhook for one bot token, not both.

- Local polling means Hermes on the Mac receives Telegram messages.
- Cloud webhook means Vercel receives Telegram messages and creates Linear fallback tasks.

Current state as of 2026-06-02 16:42 CDT:

- Telegram webhook is deleted.
- Local Hermes polling is Telegram-primary.
- EC2 relay is HTTPS-ready hot standby; do not cut Telegram over to EC2 unless Adam explicitly asks for the webhook target change.
- Cloud relay remains available for Mac-loss fallback, but it is not receiving the active Telegram bot while local polling is enabled.
- Hermes config has `platforms.telegram.enabled: true`.
- The Mac-side puller bridges cloud Linear issues back into Agent Bus tasks.

Hermes config backup before cloud-webhook mode:

`/Users/adamjohnsson/.hermes/config.yaml.bak-cloud-webhook-202606021613`

Hermes config backup before restoring local polling:

`/Users/adamjohnsson/.hermes/config.yaml.bak-local-polling-20260602164135`

## Cloud Telegram Commands

When the bot is pointed at the cloud webhook:

- `/cloudstatus` or `/ops` checks the cloud relay.
- `/cloudhandoff`, `/opshandoff`, `/team`, or `/teampacket` returns the current cloud handoff.
- `/cloudaskcodex <task>` or `/askcodex <task>` creates a Linear fallback task.
- `/cloudagent <task>` or `/agent <task>` runs the bounded cloud agent and attaches the result to Linear.
- `/askclaude <task>`, `/askhermes <task>`, and `/askchorus <task>` create routed Linear fallback tasks.
- `/route <task>` recommends a route.
- Non-command messages become Codex fallback tasks.

## Source Of Truth

When a Mac is online:

1. Live systems and local files.
2. `/Users/adamjohnsson/.deadhidden-os/ops/`
3. Obsidian receipt.
4. Linear/Notion mirror.
5. Session memory.

When no Mac is online:

1. Live cloud systems.
2. Linear cloud context issue `DEA-22`.
3. Vercel deployment snapshot.
4. Older receipts and memory, marked as stale until verified.

## Hermes Last Session Digest

Path: `/Users/adamjohnsson/.hermes/memories/LAST_SESSION_DIGEST.md`

# LAST SESSION DIGEST

> **Purpose:** Curated ground-truth digest. The FIRST file Hermes reads on
> any recall request (see SOUL.md Recall Protocol). For raw transcript
> facts auto-extracted from session JSON, see `SESSION_RAW_FACTS.md`.

---

# Session — 2026-06-10 (Wed, ~09:25 CDT)

## What shipped (live, verified)

**BM "Tutor Nobody Appointed" promo wave 1 — POSTED, not draft.**
Codex drafted the packet (Fable 5), Hermes/Telegram verified wording
against voice-DNA and shipped all three:

- X main tweet (no link in body):
  https://x.com/Biblicalman/status/2064714765214093580
- X self-reply with post link:
  https://x.com/Biblicalman/status/2064714803210334663
- Substack Note (confirmed BM account, not DH):
  https://substack.com/@biblicalman/note/c-273870816
- Post being funneled:
  https://open.substack.com/pub/biblicalman/p/the-tutor-nobody-appointed?r=2t2o3r

Source packet: `~/Documents/Codex/2026-06-10/so-as-you-know-i-have/outputs/faithwall-tutor-note-and-x-promo.md`
Receipts: ops RECEIPTS.md (~line 2090+) and
`Agent Logs/Hermes/2026-06-10 0924 - Hermes - Tutor post X and Notes promo shipped.md`

## Held in reserve

**Alternate main tweet** ("A servant works to stay. A son already
belongs...") is UNPOSTED — earmarked as an evening second wave IF the
morning Note shows restack movement. Do not repost the morning tweet;
do not treat the alternate as already published.

## Open

1. ~2-3 hrs after 09:24 CDT: check restacks/hr on the Note. If moving,
   fire the alternate tweet as wave 2 (needs Adam's go for the post).
2. Any iMessage/Photon query about "today's BM promo" → answer from the
   URLs above, not from the draft packet (the packet says draft-only;
   it is now LIVE).

---

# Session — 2026-05-20 (Wed, 11:28 CDT)

## What we did today

**Infrastructure session.** No content published. Adam wanted to set up
Hermes Workspace v2 and a dedicated writer profile.

### 1. Hermes Agent updated
- Was: v0.14.0, 43 commits behind main
- Pulled 49 commits, base deps reinstalled with `--break-system-packages`
  (PEP 668 was blocking on macOS Python 3.14)
- Pre-update snapshot saved: `20260520-161858-pre-update`
- Now reports `Hermes Agent v0.14.0 (2026.5.16) — Up to date`

### 2. Hermes Workspace v2 installed
- Path: `~/hermes-workspace-app` (NOT `~/hermes-workspace`, which is
  Adam's existing symlink command center — case-collision on APFS)
- Vite UI at `:3000`, gateway at `:8642`
- Marketing site at hermes-workspace.com is just the landing page; the
  actual UI is local
- `pnpm dev` runs the workspace; `hermes gateway run` runs the gateway

### 3. `writer` profile created
- Cloned from default (`hermes profile create writer --clone`)
- Description set so the kanban decomposer routes writing tasks to it
- `SOUL.md` REWRITTEN — now keyed specifically to @biblicalman.substack.com
  voice instead of the master Anchor persona. Includes:
    • Platform mechanics (Substack/X/Notes/reader replies)
    • Banned words expanded (added landscape, seamless, robust, ecosystem)
    • Brand boundaries (BM ≠ DH, no @deadhidden handle, FaithWall rules)
    • Hook benchmark baked in (scripture-first + stat-shock + listicle)
    • All fabrication guardrails kept (Sunday School, grandfather-in-
      recliner, vending machine, Adam Johnson byline)
    • Exit clause if Adam loads writer for strategy work
- Path: `~/.hermes/profiles/writer/SOUL.md` (168 lines)
- Wrapper: `~/.local/bin/writer` (PATH already set)

### 4. Launcher script written
- `~/.local/bin/workspace` (executable, in PATH)
- Commands: `workspace` (up), `stop`, `status`, `logs`, `restart`
- Starts gateway + UI idempotently, opens Chrome via CDP on :9222
- Verified end-of-session: gateway, UI, Chrome CDP all UP

### 5. Codex Bridge — unlocked, no worker added
- Token: `ZQyrByGicYtwA-_3TFU4KtjkhiK15KSJQ8Ll_GCht2M`
- Adam considered adding a "worker" to the Bridge but decided to leave
  it as-is.
- Hermes misread "add a worker" as a Workspace v2 ask and built the
  writer profile + installed Workspace v2 before clarifying. Both are
  still useful; just not what he originally pointed at.

## Open for tomorrow

1. **Writer profile is configured but not exercised.** No drafts have been
   produced through it yet. Test it: `writer chat` or route a Substack
   draft task through kanban with `writer` as assignee.

2. **Workspace v2 Conductor untried.** He hasn't spawned a mission yet.
   Open `http://localhost:3000/` → Conductor → New Mission to see if the
   role/worker grid does what he wants.

3. **Content debt — zero posts published today.** Combined ARR ~$96K.
   Pull biblicalman.substack.com to check last-publish date before
   touching any more infra tomorrow.

[truncated]

## Latest Agent Receipts

- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Logs/Hermes/2026-06-29 1024 - Hermes - codex 5.5 build verification.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Logs/Hermes/2026-06-29 1016 - Hermes - desktop imessage control plane.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Logs/Hermes/2026-06-29 0945 - Hermes - aside skills memory sync.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Logs/Codex/2026-06-29 0921 - Codex - capital one verizon extension drafts.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Logs/Codex/2026-06-29 0717 - Codex - TBM growth money move.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Logs/Codex/2026-06-28 2109 - Codex - DH Isaiah cave Substack draft.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Logs/Codex/2026-06-28 2104 - Codex - DH Wicked Bible Substack draft.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Logs/Codex/2026-06-28 1304 - Codex - runtime boot refresh.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Logs/Codex/2026-06-28 1202 - Codex - BM paid email off reply watch.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Logs/Codex/2026-06-28 1100 - Codex - BM paid email off reply watch.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Logs/Codex/2026-06-28 1001 - Codex - BM paid email off reply watch.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Logs/Codex/2026-06-28 0904 - Codex - writing brain AI tells guard.md`

## Latest Agent Bus Files

- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Bus/receipts/2026-06-29 100609 - Codex Bus Watch - inspect-control-plane-no-external-changes.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Bus/inbox/20260621-131815-codex-paid-pdf-privacy-fix.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Bus/inbox/20260620-081536-chorus-agent-canvas-mission.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Bus/inbox/20260619-202054-claude-agent-canvas-mission.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Bus/inbox/20260619-202054-codex-agent-canvas-mission.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Bus/receipts/2026-06-19 202106 - Codex Bus Watch - agent-canvas-mission.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Bus/inbox/2026-06-19-cursor-substack-referral-links.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Bus/receipts/2026-06-19 092244 - Codex Bus Watch - agent-canvas-mission.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Bus/inbox/20260619-092153-hermes-agent-canvas-mission.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Bus/inbox/20260619-092153-codex-agent-canvas-mission.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Bus/inbox/20260619-092153-claude-agent-canvas-mission.md`
- `/Users/adamjohnsson/Documents/Obsidian Vault/70 Systems/Agent Bus/inbox/20260619-092153-chorus-agent-canvas-mission.md`

## Latest Raw Session Files

Codex:
- `/Users/adamjohnsson/.codex/sessions/2026/06/29/rollout-2026-06-29T13-46-04-019f14b3-f0b3-7013-ab20-f487df984cb6.jsonl`
- `/Users/adamjohnsson/.codex/sessions/2026/06/29/rollout-2026-06-29T12-29-19-019f146d-ac29-7061-a30e-98b0180a26c2.jsonl`
- `/Users/adamjohnsson/.codex/sessions/2026/06/29/rollout-2026-06-29T12-25-33-019f146a-38cb-79e1-b5fd-1d206cfc2e14.jsonl`
- `/Users/adamjohnsson/.codex/sessions/2026/06/29/rollout-2026-06-29T12-18-40-019f1463-eba2-77f2-b534-a3e5163f60f3.jsonl`
- `/Users/adamjohnsson/.codex/sessions/2026/06/29/rollout-2026-06-29T12-12-38-019f145e-65a5-7b12-b091-9a32493856ed.jsonl`
- `/Users/adamjohnsson/.codex/sessions/2026/06/29/rollout-2026-06-29T10-20-08-019f13f7-6543-7a71-b482-dfa6d8d02b96.jsonl`
- `/Users/adamjohnsson/.codex/sessions/2026/06/28/rollout-2026-06-28T20-53-19-019f1114-bcea-73d3-b7a0-2ad5fb2e1cf7.jsonl`
- `/Users/adamjohnsson/.codex/sessions/2026/06/29/rollout-2026-06-29T09-27-43-019f13c7-6ac7-7af1-b4fa-30e242ecbbbc.jsonl`

Claude:
- `/Users/adamjohnsson/.claude/projects/-Users-adamjohnsson-reader-voice/b879ae7f-d63a-43f1-aded-dba4a6733099.jsonl`
- `/Users/adamjohnsson/.claude/projects/-Users-adamjohnsson-reader-voice/b04b32a9-aa18-4a43-bd57-94b577cf0e4c.jsonl`
- `/Users/adamjohnsson/.claude/projects/-Users-adamjohnsson-reader-voice/608a4fd3-b75d-4497-b1c0-33f824330baf.jsonl`
- `/Users/adamjohnsson/.claude/projects/-Users-adamjohnsson-reader-voice/bc456fd5-7fea-419f-98da-ca729f78cc94.jsonl`
- `/Users/adamjohnsson/.claude/projects/-Users-adamjohnsson-reader-voice/26e6d2b4-0a37-49e9-a95c-0cabf0e022d1.jsonl`
- `/Users/adamjohnsson/.claude/projects/-Users-adamjohnsson-reader-voice/9b2e4a71-0740-4f0d-aa14-722ded527f28.jsonl`
- `/Users/adamjohnsson/.claude/projects/-Users-adamjohnsson-reader-voice/ce147c7e-9394-4148-8f0e-910db068ee5d.jsonl`
- `/Users/adamjohnsson/.claude/projects/-Users-adamjohnsson-reader-voice/0ab5aca6-2c93-4773-9efb-6885c65fc952.jsonl`
