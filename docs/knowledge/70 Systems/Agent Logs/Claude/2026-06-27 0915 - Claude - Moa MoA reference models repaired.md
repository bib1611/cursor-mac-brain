# 2026-06-27 09:15 — Claude (Jarvis) — Moa / Hermes MoA reference models repaired

## Problem
Adam ran `/moa` in Hermes desktop on a 5-step content task. It sat silent ~20 min then died: `API call failed after 3 retries: HTTP 404: Not found`.

## Root cause
`moa.presets.orchestrator` is a Mixture-of-Agents that fans out to 3 reference models, then aggregates with Opus. All 3 reference legs were broken:
- `codex-gpt-5.5` → base_url `127.0.0.1:3458` (Claude Max proxy). That proxy only serves `claude-opus-4-8`, not `gpt-5.5` → 404 model-not-found.
- `kimi-moonshot` → `KIMI_API_KEY` commented out in `~/.hermes/.env`. No key on machine.
- `xai-grok` → key actually present (`XAI_API_KEY` line 429 of `.env`, also in Keychain `com.cnvs.canvas.grok_api_key`). This leg was fine.

MoA gathered zero reference responses, retried 3x, collapsed before the aggregator ever ran.

## Fix (config.yaml, backup: `config.yaml.bak-moa-fix-20260627`)
Routed gpt-5.5 + Kimi + fusion through OpenRouter (`OPENROUTER_API_KEY`, live), kept Grok native, Opus aggregator unchanged. Added two model slugs under `draco-openrouter-fusion` provider: `openai/gpt-5.5`, `moonshotai/kimi-k2.6`.

New `reference_models`:
- draco-openrouter-fusion / openai/gpt-5.5
- draco-openrouter-fusion / moonshotai/kimi-k2.6
- draco-openrouter-fusion / openrouter/fusion
- xai-grok / grok-4.3

aggregator: claude-max-opus / claude-opus-4-8 (unchanged)

## Verified
- All 4 legs smoke-tested green individually (grok native + gpt-5.5/kimi/fusion via OpenRouter).
- YAML loads, gateway restarted clean (`launchctl kickstart -k gui/501/ai.hermes.gateway`), `/health` 200 ok v0.17.0.
- NOT yet run end-to-end as a full MoA aggregation — Adam to fire the real test (racing it vs Aside).

## Boundary
Local config + gateway restart only. No secrets printed, no external send, no money/customer mutation.
