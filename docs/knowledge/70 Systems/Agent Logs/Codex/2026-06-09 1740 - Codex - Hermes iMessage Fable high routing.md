# Codex - Hermes iMessage Fable high routing

Date: 2026-06-09 17:40 CDT

Adam asked to make sure Hermes iMessage is on Fable high.

Finding:

- `/Users/adamjohnsson/.hermes/config.yaml` already had `model.default: claude-fable-5`.
- `/Users/adamjohnsson/.hermes/config.yaml` already had `reasoning_effort: high`.
- The local Claude Max proxy still had an emergency rule from the iMessage repair that rerouted Photon/iMessage requests asking for Fable to `claude-opus-4-7` for latency.

Change:

- Patched `/Users/adamjohnsson/claude-max-proxy.js` so Photon/iMessage requests that ask for Fable now stay on `claude-fable-5`.
- Added proxy request logging for `effort`, so future verification shows whether requests are high/medium/low.
- Restarted `com.biblicalman.claude-max-proxy`.

Proof:

- `node --check /Users/adamjohnsson/claude-max-proxy.js` passed.
- Proxy health returned ok.
- Synthetic Photon-shaped request returned `FABLE_HIGH_OK` from `claude-fable-5`.
- Proxy log showed: `Photon/iMessage using requested claude-fable-5`.
- Proxy log showed: `model=claude-fable-5 effort=high`.
- Hermes gateway health remained ok and Photon sidecar stayed listening on `127.0.0.1:8789`.

Boundary:

No real iMessage was sent by Codex for this routing proof. No Photon account, webhook, tunnel, credential, customer, publishing, or external app state was changed.
