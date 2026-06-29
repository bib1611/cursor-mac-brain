# Codex Receipt - DRACO OpenRouter Fusion Claude Desktop Setup

Date: 2026-06-14 19:28 CDT
Agent: Codex

Adam asked Codex to configure OpenRouter/Fusion, especially with Claude Desktop, then named the setup DRACO.

Codex created a dependency-free local MCP server for Claude Desktop that exposes DRACO/OpenRouter Fusion as tools `draco_fusion` and `draco_status`. Claude Desktop MCP config now includes server `draco`, preserving existing MCP servers. Hermes config now includes provider `draco-openrouter-fusion`, but Hermes default remains `claude-max-opus` / `claude-opus-4-8`.

Created:

- `/Users/adamjohnsson/.deadhidden-os/ops/bin/openrouter-fusion-mcp`
- `/Users/adamjohnsson/.deadhidden-os/ops/bin/draco-fusion-mcp`
- `/Users/adamjohnsson/.deadhidden-os/ops/bin/openrouter-store-key`
- `/Users/adamjohnsson/.deadhidden-os/ops/bin/openrouter-fusion-smoke`
- `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-14-openrouter-fusion-claude-desktop/DRACO-SETUP.md`

Modified:

- `/Users/adamjohnsson/Library/Application Support/Claude/claude_desktop_config.json`
- `/Users/adamjohnsson/.hermes/config.yaml`

Backups:

- `/Users/adamjohnsson/Library/Application Support/Claude/claude_desktop_config.json.bak-openrouter-fusion-20260614-191922`
- `/Users/adamjohnsson/Library/Application Support/Claude/claude_desktop_config.json.bak-draco-20260614-192426`

Verification:

- DRACO MCP server compiles.
- MCP initialize handshake passed.
- MCP tools/list returned `draco_fusion` and `draco_status`.
- Claude Desktop JSON validates and includes `draco`.
- Claude Desktop launched and loaded DRACO successfully; Claude's MCP log shows `tools/list` returned `draco_fusion` and `draco_status`.
- Hermes YAML validates and includes `draco-openrouter-fusion`.
- Hermes default provider/model stayed unchanged.
- OpenRouter key installed in Keychain service `OpenRouterAPI`.
- Hermes `.env` updated with `OPENROUTER_API_KEY`.
- OpenRouter key metadata check succeeded.
- DRACO MCP smoke returned `Fusion smoke test OK`; OpenRouter reported 3,075 tokens and cost `0.1309355`.
- Hermes status shows OpenRouter configured.
- Hermes DRACO smoke returned `DRACO_HERMES_OK` in session `20260614_193059_fd203a`.

Remaining caveats:

- Chrome extension control is unavailable because the Codex Chrome Extension is not installed/enabled in the active Chrome profile, though Chrome itself is running and the native host manifest is valid.
- Local Chrome CDP on `127.0.0.1:9222` did not return a debugger endpoint from this Codex process.
- The OpenRouter key was pasted into chat. DRACO is live with it now, but rotating the key later would be cleaner security.

Boundary:

No public post, customer/money action, deploy, external send, or Stripe/account mutation was performed. No key was intentionally printed by Codex; the first TTY helper echoed the pasted line, then Codex patched the helper to disable echo for future use.
