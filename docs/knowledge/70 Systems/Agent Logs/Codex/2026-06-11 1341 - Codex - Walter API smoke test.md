# Walter API smoke test

Date: 2026-06-11 13:41 CDT
Agent: Codex
Trigger: Adam provided a Walter Writes AI API key and asked Codex to integrate it and say whether it is good.

## Boundary

- The provided key was treated as sensitive and was not written into a persistent env file, config, receipt, or final response.
- No Hermes/Codex global config was changed because the key does not currently have the `Humanizer` scope.
- A local smoke-test wrapper was created in the current Codex workspace only:
  - `/Users/adamjohnsson/Documents/Codex/2026-06-11/there-is-a-new-update-for/work/walter-api-smoke.mjs`

## Sources checked

- Official developer docs:
  - `https://docs.walterwrites.ai/api-reference/humanizer`
  - `https://docs.walterwrites.ai/api-reference/detector`
  - `https://docs.walterwrites.ai/api-reference/detect-and-humanize`
  - `https://docs.walterwrites.ai/authentication`
  - `https://docs.walterwrites.ai/mcp-server/claude-code`
- Marketing/API page:
  - `https://walterwrites.ai/ai-humanizer-api/`

## Findings

- Official docs endpoint is `https://developer-portal.walterwrites.ai/api/...` using `X-API-Key`.
- Marketing page showed older-looking `https://api.walterwrites.ai/v1/...` Bearer examples; live tests against `/v1/humanize` and `/v1/detect` returned `404`, so do not use that endpoint.
- Humanizer endpoint test failed:
  - `403`
  - error: key does not have required scope `Humanizer`
- Detect-and-humanize endpoint test failed:
  - `403`
  - error: key does not have required scope(s) `Humanizer`
- Detector endpoint works with this key:
  - Short text under 50 words was rejected with `400`: request must contain at least 50 words.
  - 58-word throwaway corporate sample returned success.
  - Result: `ai`
  - AI score: `0.99`
  - Execution time: about `0.42s`
  - Credits remaining: `1942`

## Assessment

This key is currently useful only for AI detection, not humanization. Walter's detector responded quickly and correctly flagged an obvious AI/corporate sample, but Codex could not evaluate the humanizer quality because the key lacks Humanizer scope.

Recommended next action: create or update a Walter API key with both `Humanizer` and `AI Detector` scopes, then wire it into a local secret store/env and run a real before/after test: detector score before, humanized output quality review, detector score after, and Adam-voice preservation check.
