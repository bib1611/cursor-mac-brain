# 2026-06-09 12:57 CDT - Codex - Fable 5 Hermes Harness

Adam asked Codex to figure out how to use the new Claude Fable 5 drop through Hermes/Codex, launch agents to research the best harness, and make it useful for Dead Hidden/Biblical Man Substack, X, Notes, CTA, and store-aware workflows.

Codex booted from the local ops capsule, refreshed `TEAM_CONTEXT.md`, used the Hermes/tool-access/content/social skills, verified current Anthropic docs, tested the actual local Claude CLI account, patched the local Mac proxy and Hermes config, launched five research agents, ran Fable itself against the current Mythos and CTA workflow packets, and saved the harness packet.

Changes made:

- Patched `/Users/adamjohnsson/claude-max-proxy.js` to route `claude-fable-5`, `fable-5`, `fable5`, and `mythos-class` through Claude CLI as `claude-fable-5`.
- Added `macproxy/adam-writing-fable-5`.
- Added both Fable IDs to proxy `/v1/models`.
- Added explicit effort handling with default `high`.
- Changed Claude proxy prompts from command-line argument to stdin.
- Raised proxy prompt cap from `40000` chars to `400000` chars, with env override `CLAUDE_MAX_PROXY_PROMPT_CHARS`.
- Patched `/Users/adamjohnsson/.hermes/config.yaml` so Hermes default is `claude-fable-5` under provider `claude-max-opus`.
- Added Fable and Adam-writing Fable catalog entries to Hermes.

Backups:

- `/Users/adamjohnsson/claude-max-proxy.js.bak-fable5-20260609-124840`
- `/Users/adamjohnsson/.hermes/config.yaml.bak-fable5-route-20260609-124840`

Verification:

- Direct Claude CLI with official ID `claude-fable-5` returned `FABLE5_REAL_ID_OK`.
- Raw proxy `/v1/models` advertised `claude-fable-5` and `macproxy/adam-writing-fable-5`.
- Raw proxy Fable smoke returned `FABLE_PROXY_READY`.
- Adam-writing Fable alias returned `ADAM_WRITING_FABLE_READY`.
- Long-context stdin smoke above the old 40k cap returned `FABLE_LONG_CONTEXT_READY`.
- Hermes status showed model `claude-fable-5` and provider `claude-max-opus`.
- Hermes default smoke returned `HERMES_FABLE5_READY` and later `HERMES_FABLE_STDIN_READY`.

Artifacts:

- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-09-fable5-harness/FABLE5-HARNESS-PACKET.md`
- `/Users/adamjohnsson/Documents/Codex/2026-06-09/i-need-you-to-launch-a/outputs/fable5-harness-research.md`

Key decision:

Fable is now the high-judgment drafting/audit layer. Codex remains the wrapper: source retrieval, mechanical validators, route proof, state transitions, approval boundaries, and receipts. Adam remains the final gate for public actions.

Known caveats:

- Fable is a Covered Model and has retention caveats; raw private customer/family/iMessage material should stay local or be distilled first.
- Proxy prompt cap is now `400000` chars, not the true 1M-token model ceiling.
- Hermes gateway still shows launchd stale-service/manageability warnings on restart.
- Gateway logs showed Photon sidecar duplicate bind attempts on `127.0.0.1:8789`; not blocking Fable.
- The existing Notes scheduler has a false-green/source-exhaustion bug and should be fixed before Fable-generated Notes feed any live scheduler.

Boundary:

No public post, Substack publish, Substack schedule, X post, email send, Stripe/customer action, deploy, account permission change, credential change, webhook cutover, or external send was performed.
