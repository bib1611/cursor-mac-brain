# Codex - Komand and MCP config check

Summary:
- Verified `/Applications/Komand.app` is installed as bundle id `ai.clonk.app`, version `1.0.6`.
- Verified Komand bridge launch agent exists at `/Users/adamjohnsson/Library/LaunchAgents/com.komand.bridge.plist`.
- Verified bridge status file reports `state=running`, `connectionStatus=connected`.
- Verified Komand sidecar logs show Codex surfaces are being queried (`codex_thread_list`, `codex_model_list`, `codex_skills_list`, `codex_account_rate_limits_read`).
- Tried to disable stale raw Codex MCP config blocks for `vercel`, `github`, `stripe`, `notion`, `firecrawl`, and `elevenlabs`.
- Direct write to `/Users/adamjohnsson/.codex/config.toml` was blocked by macOS/Codex sandbox permissions, so live config was not changed.
- Wrote patched config copy only: `/Users/adamjohnsson/Downloads/config.toml.patched-raw-mcp-disabled`.
- Wrote backups/copies in Downloads:
  - `/Users/adamjohnsson/Downloads/config.toml.bak-20260622-raw-mcp-disable`
  - `/Users/adamjohnsson/Downloads/config.toml.bak-before-filesystem-mcp-edit-20260622`

Boundary:
- No external app write, no secrets printed, no config successfully changed, no agent routing changed.
