# 2026-06-09 1506 - Codex - Fable 5 Workflow Swarm

Adam asked Codex to fully understand how to optimally use the new Claude Fable 5 drop and launch a swarm to investigate videos, walkthroughs, prompts, and workflows.

Codex booted from the local ops capsule, used the Fable/Hermes harness context, launched five research lanes, verified current official Anthropic docs, used web search plus local `yt-dlp` discovery for the video/walkthrough lane, and saved an operational packet.

Swarm lanes:

- Official facts: model ID, availability, limits, effort, refusal/fallback, tokenizer, retention, Claude Code access.
- Creator/walkthroughs: Every, Ethan Mollick, YouTube launch-day results, Addy Osmani, Reddit/HN signals.
- Harness architecture: role split, prompt envelope, context packet, validators.
- Dead Hidden workflow fit: Substack posts, Notes, X, CTA/store, Hermes editor staging.
- Eval/risk: scorecards, privacy gates, refusal handling, rollback criteria.

Key finding:

Fable 5 should be Adam's high-judgment closer, not the whole operator stack.

Working wrapper:

```text
Codex proves reality -> Fable judges/drafts/audits -> Codex validates mechanically -> Adam approves public action -> Hermes stages approved surfaces -> Codex writes receipts
```

Official facts verified:

- Canonical model ID: `claude-fable-5`.
- Launch date: 2026-06-09.
- 1M context and 128k max output.
- Price: $10 input / $50 output per million API tokens.
- Adaptive thinking always on.
- Use effort as the main control; default `high`, `xhigh` for capability-sensitive work.
- Refusals return HTTP 200 with `stop_reason: "refusal"`.
- Fable 5 is a Covered Model and not zero-data-retention eligible on Claude API.
- Claude Code v2.1.170 or later is required for Fable access.

Artifacts:

- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-fable5-workflow-swarm/FABLE5-WORKFLOW-SWARM-PACKET.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-fable5-workflow-swarm/WORKFLOW-CARDS.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-fable5-workflow-swarm/EVAL-PLAN.md`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-fable5-workflow-swarm/SOURCE-LEDGER.md`
- `/Users/adamjohnsson/Documents/Codex/2026-06-09/i-need-you-to-launch-a/outputs/fable5-workflow-swarm-research.md`

Boundary:

No public post, Substack publish, Substack schedule, X post, email send, Stripe/customer action, account setting change, credential change, deploy, or external send was performed.

