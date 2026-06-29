# Codex - Hermes iMessage Fable-assisted final repair

Date: 2026-06-09 17:38 CDT

Adam reported the Hermes iMessage lane still had no read confirmation and no output, and explicitly asked Codex to use Fable. Codex consulted `claude-fable-5` through the local proxy with sanitized evidence. Fable called out the key distinction: missing read receipt was separate from `send ok` with no visible UI, so the next proof needed to check both restored read handling and Apple Messages delivery metadata.

Root issue found in this pass: the Hermes desktop installer/build process had overwritten parts of the active Photon source after the earlier repair. The running sidecar still had send logging in memory, but the disk copy had lost the mark-read implementation and had partially reverted the active Photon adapter. This meant the next restart could silently break read receipts again.

Changes:

- Restored Photon adapter mark-read scheduling in `/Users/adamjohnsson/.hermes/hermes-agent/plugins/platforms/photon/adapter.py`.
- Restored sidecar `/mark-read` endpoint in `/Users/adamjohnsson/.hermes/hermes-agent/plugins/platforms/photon/sidecar/index.mjs`.
- Added sidecar inbound message caching so Spectrum can call the iMessage `read(message)` primitive on the exact inbound message.
- Confirmed the active Photon adapter has 120s sidecar HTTP timeouts and typed send errors.
- Confirmed sidecar outbound `send start` / `send ok` logging remains on disk.
- Restarted `ai.hermes.gateway` cleanly so the patched disk copy is what is running.

Verification:

- `node --check` passed for the Photon sidecar.
- `python -m py_compile` passed for the Photon adapter.
- Gateway restarted and connected all three platforms: Telegram, Photon, API server.
- Photon sidecar is a child of the live gateway and listens on `127.0.0.1:8789`.
- API health returns `{"status":"ok","platform":"hermes-agent","version":"0.16.0"}`.
- Adam sent `Ping3` from iMessage at 17:36 CDT.
- Gateway logged inbound `Ping3`.
- Adapter logged `mark-read scheduled`.
- Sidecar logged `mark-read start` and `mark-read ok`.
- Adapter logged `mark-read ok`.
- Gateway logged response ready in 24.8s.
- Sidecar logged outbound `send start`.
- Sidecar logged outbound `send ok` with Photon message id.
- Local Messages database showed the corresponding post-fix iMessage rows in the same DM lane with iMessage service, sent/delivered flags set, and `error=0`.

Boundary:

Codex did not change Photon account credentials, public webhook/tunnel config, Stripe/customer data, Substack/X/Gmail, or unrelated Hermes platform settings. Raw iMessage content was not exported to cloud agents; only local metadata and sanitized evidence were used for the Fable consult.
