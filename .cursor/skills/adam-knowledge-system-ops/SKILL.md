---
name: Adam Knowledge System Ops
description: "Use before any system, memory, routine, receipt, or revenue/list operation for Adam's businesses. The operational wrapper over Adam's knowledge stack: read order and source-of-truth routing across Obsidian, the Dead Hidden ops capsule, and Aside memory; routine safety rules; Obsidian receipt conventions; and revenue / email-list operating defaults. Trigger on Obsidian, memory, routines, source-of-truth, receipts, Daily Numbers, Dead Hidden ops, or revenue/ARR/churn/email-list tasks."
autoInject:
  keywords:
    - Obsidian
    - memory system
    - routine memory
    - active routines
    - source of truth
    - agent receipt
    - Daily Numbers
    - Dead Hidden ops
    - Agent Bus
    - revenue
    - ARR
    - Stripe
    - Gumroad
    - Substack paid
    - churn
    - email list
    - broadcast
    - dunning
    - winback
    - paid conversion
  url:
    - dashboard.stripe.com
    - app.gumroad.com
    - gumroad.com
    - substack.com
---
# Adam Knowledge System Ops

The operational wrapper over Adam's knowledge stack. Durable facts live in the Aside memory pages and Obsidian vault; this skill is the routing layer that tells you what to read first, which source wins on conflict, and the standing safety defaults for system, routine, receipt, and revenue/list work. When a core rule changes, update the relevant memory page, not just this skill.

## Read order before any system task
1. `memory/agent/current-systems.md` (source-of-truth map).
2. `memory/agent/outbound-approval-rules.md` (what needs Adam's approval).
3. `memory/agent/active-routines.md` (current cron/heartbeat registry, ids, safety modes).
4. The Dead Hidden ops capsule: `/Users/adamjohnsson/.deadhidden-os/ops/` (active routing + current state).
5. The active Obsidian vault: `/Users/adamjohnsson/Documents/Obsidian Vault` (deep brain, receipts, Agent Bus, Agent Logs, Daily Numbers, money loops).

## Source trust hierarchy (conflict resolution)
1. Live system state or a readable local file.
2. Active runtime capsule: `/Users/adamjohnsson/.deadhidden-os/ops/`.
3. Dated Obsidian receipt in `70 Systems/Agent Logs/`.
4. Aside memory under `memory/`.
5. Linear, Notion, cloud mirrors, archived Obsidian, or old session transcripts (mark freshness; treat as weakest).
- Generated dashboards (e.g. `Daily Numbers.md`) never override live Stripe / Gumroad / Substack / X data. If a source reports an impossible value (X followers ~3, Stripe latest scrape $0.00 while rolling sums show revenue), treat it as a scraper failure until verified live.
- `memory_search` can miss known files. For high-value recall use direct `find` + `read_file` on the memory dir, not search alone.

## Active agent / workflow surfaces
- **Codex** — Mac-side router/executor and receipt writer (`.deadhidden-os/ops/CODEX_OPERATOR.md`).
- **Hermes / Telegram** — intake and tactical routing (local polling primary).
- **Jarvis / Linq / Chorus** — connected-app helper + writing QC layer. Not the canonical brain; cannot read local Mac paths unless context is pasted/mirrored.
- **Cloud relay (Vercel / EC2)** — fallback intake and Linear task creation; does not prove Mac-side execution.
- **Aside** — browser operator + local memory/skills layer. For web actions follow current final-confirm rules even if an older ops file claims auto-fix authority.

## Routine safety rules
- Every recurring routine must have a `memory/routines/<routine-slug>/MEMORY.md` before activation.
- Default routine mode is **draft / report / read-only**. A routine may not auto-post, auto-send, auto-schedule, refund, block, buy, or change account state unless its prompt explicitly grants that permission AND Adam approved it.
- Routine prompts must state allowed and forbidden external actions. If a routine prompt conflicts with `outbound-approval-rules.md`, the rules page wins until Adam clarifies.
- Update `active-routines.md` whenever a routine is created, changed, paused, or deleted (id + safety mode).

## Obsidian receipt conventions
- Write dated receipts to `70 Systems/Agent Logs/` (Aside logs under the Aside subfolder). Use the templates in `70 Systems/Templates/`.
- A receipt records what changed, where, why, and the source confidence. Receipts are the trail; memory pages are the durable summary.

## Revenue and email / list operating defaults
- **Money loops (Obsidian `70 Systems/Money Loops/`):** Loop 1 free-to-paid (target paid share up, simplify the path), Loop 2 churn/dunning save, Loop 3 back-catalog cross-sell (one offer per send), Loop 4 revenue-leak sweep. Root cause of the conversion gap is **path complexity + email-volume fatigue**, not weak writing. Simplify before adding volume. Loop 4 can run; Loops 1-3 need per-action approval.
- **Email cadence:** reduce frequency; one ask per send. BM list opens are strong (~42-52% on the elite Gumroad segment) but over-sending fatigues the list.
- **Gumroad broadcast quirk:** the top-level Publish opens a dropdown that does NOT send. Send only via **"Publish now"** inside it; navigating away after the top-level click silently discards the draft. (Full store quirks: Gumroad / Dead Hidden Store Ops skill.)
- **No financial figures in any public/customer-facing copy** — no revenue, subscriber counts, or stats. Internal/ops tools are exempt.

## Safety
- In Aside final-confirm sessions, get Adam's approval on the exact final action before anything externally visible, paid, destructive, or customer/account-state-changing (send, post, publish, schedule, refund, dispute submission, discount, purchase, block, privacy/security change). Drafting, reading, analyzing, and local prep are safe.
- **Repentance / accountability messages from unknown parties:** do not draft or send a reply on your own. Read it to Adam, get clearance, then proceed as directed (2026 scandal context; genuine messages exist).
- If Adam appears in distress, prioritize wellbeing over the task; loop in Christie; 988/911 if needed. Handle discreetly.
- Never invent stories about Adam's family. Never imitate a living writer's voice or central metaphor.
