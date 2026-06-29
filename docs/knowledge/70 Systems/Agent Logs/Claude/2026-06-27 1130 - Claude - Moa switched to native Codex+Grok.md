# 2026-06-27 11:30 — Claude (Jarvis) — Moa switched to native Codex + Grok

## Why
OpenRouter balance hit -$0.02 ($878 of $878 spent). All OpenRouter-routed MoA legs (gpt-5.5, kimi-k2.6, fusion) returned empty with HTTP 402 (can only afford ~1173 tokens/call). Grok kept working (native xAI key, separate billing). Adam: "Use our native codex and grok models forget Kimi."

## Discovery
The local proxy on `127.0.0.1:3458` (was Claude Max proxy) now also serves NATIVE models: `/v1/models` lists `gpt-5.5`, `codex`, `claude-fable-5`. Live chat test to `gpt-5.5` returned "NATIVE READY" — this is Adam's Codex / GPT Pro backend, no per-token OpenRouter cost.

## Change (config.yaml, backup: config.yaml.bak-moa-native-20260627)
moa.presets.orchestrator.reference_models now:
- codex-gpt-5.5 / gpt-5.5   (native, base_url 127.0.0.1:3458)
- xai-grok / grok-4.3       (native xAI key, ${XAI_API_KEY})
aggregator: claude-max-opus / claude-opus-4-8 (native 3458, unchanged)
Kimi + all draco-openrouter-fusion legs removed.

## Verified
- gpt-5.5 native chat on 3458 → "NATIVE READY" (finish=stop)
- grok-4.3 native → returns clean
- YAML loads, gateway restarted (`launchctl kickstart -k gui/501/ai.hermes.gateway`), /health 200 ok v0.17.0

## Note
OpenRouter still drained — gpt-5.5/kimi/fusion via OpenRouter stay dead until Adam tops up at openrouter.ai/settings/credits. Native path no longer depends on it.

## Boundary
Local config + gateway restart only. No secrets printed, no money/customer/external mutation.
