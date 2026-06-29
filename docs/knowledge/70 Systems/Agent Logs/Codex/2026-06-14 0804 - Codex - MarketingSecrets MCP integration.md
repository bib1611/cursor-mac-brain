# 2026-06-14 08:04 CDT - Codex - MarketingSecrets MCP integration

Adam supplied a MarketingSecrets.ai MCP endpoint and API key for the Dead Hidden / MarketingSecrets business brain integration.

Actions:

- Verified the endpoint with MCP `tools/list`; the server exposed `memory_search`, `memory_get_profile`, `memory_save`, and `memory_get_recent`.
- Checked `memory_get_profile` and `memory_get_recent`; the profile existed but was empty and there were no saved memory facts before this work.
- Stored the MarketingSecrets API key in the macOS login keychain under service `MarketingSecretsMCP`.
- Created no-secret wrapper script:
  - `/Users/adamjohnsson/.deadhidden-os/ops/bin/mcp-marketingsecrets`
- Added Codex global MCP config:
  - `/Users/adamjohnsson/.codex/config.toml`
- Added Hermes MCP config with a four-tool whitelist:
  - `/Users/adamjohnsson/.hermes/config.yaml`
- Backed up and updated Claude Desktop MCP config:
  - Backup: `/Users/adamjohnsson/Library/Application Support/Claude/claude_desktop_config.json.bak-marketingsecrets-20260614-0804`
  - Updated: `/Users/adamjohnsson/Library/Application Support/Claude/claude_desktop_config.json`
- Saved one non-secret starter memory to MarketingSecrets under `business`, capturing Adam's current agent routing boundary and live-verification rule.

Verification:

- Direct MCP `tools/list` returned four MarketingSecrets tools.
- `hermes mcp test marketingsecrets` connected in 3040ms and discovered four tools.
- `hermes mcp list` showed `marketingsecrets` enabled with `4 selected` tools.
- `codex mcp get marketingsecrets` showed the new global stdio server entry pointing at the wrapper.
- Node JSON parsing validated the updated Claude Desktop config and backup.
- `memory_get_recent` and `memory_search` confirmed the starter memory saved and read back.
- Keychain read check for `MarketingSecretsMCP` succeeded.

Boundary:

- No API key was written into Codex, Hermes, Claude Desktop, or the wrapper script configs.
- No public post, customer action, money action, deploy, Telegram webhook change, Stripe/Linear/Notion mutation, or email/send action was performed.
- Current Codex/Claude Desktop sessions may need restart/new session to load the new MCP server. Hermes has been config-tested, but the live gateway was not restarted in this pass.
