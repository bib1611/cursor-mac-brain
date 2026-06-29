# 2026-06-16 1455 CDT — Polly (orchestrator) — OpenRouter API key rotation

## What changed
Rotated the OpenRouter API key used by the `pi` sub-agent / gateway model inference (Kimi, GLM, openrouter/fusion, Fable attempts, etc.). The previous key was dead — it returned 404 / a Clerk login wall on every inference call, blocking `pi` twice during the PR #47 live-money review.

## Action
- Adam provided a new OpenRouter workspace key in-session. Value is NOT reproduced here; stored only in the locations below.
- New key written to: `~/.config/env/global.env`
- New key written to: macOS Keychain, service `OpenRouterAPI`
- Old (dead) key backed up before overwrite.

## Verification
- `GET https://openrouter.ai/api/v1/key` with the new key returned HTTP 200 (key live).
- `pi` inference restored: the Kimi review of PR #47 subsequently ran to completion on the new key.

## Scope / boundaries
- Credential change only. No publish, no send, no Stripe/money action, no deploy.
- Key value never printed to the chat transcript or this receipt.

## Why this receipt exists
Per the ops-capsule Receipt Rule (`RULES.md`): credential/agent-routing changes require a dated receipt. This documents a rotation performed earlier in the session, before the capsule was loaded.
