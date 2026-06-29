# 2026-06-08 21:34 CDT - Codex - Hermes Photon iMessage setup

## Goal

Adam asked Codex to set up the Nous Research announcement:

`https://x.com/nousresearch/status/2064102412076364207?s=46`

Tweet text verified through local `xurl`: Nous Research announced that Hermes Agent now lives in iMessage through Photon and said to run `hermes gateway setup` and choose Photon.

Official Photon/Hermes docs checked:

- `https://hermes-agent.nousresearch.com/docs/user-guide/messaging/photon`
- `https://photon.codes/docs/api-reference/users/create-user`
- `https://photon.codes/docs/api-reference/users/redirect-user-to-messaging-platform`
- `https://photon.codes/docs/spectrum-ts/platform-narrowing`

## Changes made

- Updated Hermes Agent from 84 commits behind to current `origin/main` at `b5f8996c`.
- Pre-update backup created at `/Users/adamjohnsson/.hermes/backups/pre-update-2026-06-08-210411.zip`.
- Installed Photon sidecar dependencies.
- Upgraded Photon sidecar SDK from stale `spectrum-ts@0.1.2` to `spectrum-ts@1.18.0` because the old SDK pointed at retired Spectrum hostnames.
- Patched `/Users/adamjohnsson/.hermes/hermes-agent/plugins/platforms/photon/sidecar/index.mjs` to normalize Hermes' raw iMessage DM guid shape (`any;-;+E164`) back into the user phone format expected by the newer `spectrum-ts` resolver.
- Enabled Photon in Hermes config.
- Saved Photon allowlist and security settings:
  - `PHOTON_ALLOWED_USERS` restricted to Adam's provided phone number.
  - `PHOTON_ALLOW_ALL_USERS=false`.
  - `PHOTON_REQUIRE_MENTION=true`.
  - `PHOTON_WEBHOOK_BIND=127.0.0.1`.
  - `SPECTRUM_CLOUD_URL=https://spectrum.photon.codes`.
  - `PHOTON_SIDECAR_TOKEN` persisted so standalone local sends can authenticate to the sidecar.
- Created Photon project `Adam Hermes Agent`.
- Stored Spectrum project credentials for project id `18e02786-de76-4180-b245-6e80b9cf6223`.
- Created shared Photon user for Adam's phone ending in `3328`.
- Photon assigned shared iMessage line `+1 (415) 579-6445`.
- Started Cloudflare quick tunnel in tmux session `hermes-photon-cloudflared`.
- Registered Photon webhook id `f4651e70-b1bd-42f6-b771-4ddb2d3f68c6` at:

`https://trials-hiring-specially-update.trycloudflare.com/photon/webhook`

## Verification

- `hermes photon status` shows:
  - device token stored
  - project id present
  - project key stored
  - webhook key set
  - sidecar deps installed
- `hermes photon webhook list` shows webhook id `f4651e70-b1bd-42f6-b771-4ddb2d3f68c6`.
- `hermes gateway status` reports the launchd service definition matches current Hermes and gateway is loaded.
- Ports verified:
  - gateway webhook: `127.0.0.1:8788`
  - Photon sidecar: `127.0.0.1:8789`
- Gateway logs confirm:
  - `photon-sidecar: listening on 127.0.0.1:8789`
  - `[photon] connected -- webhook at 127.0.0.1:8788/photon/webhook`
  - `Gateway running with 3 platform(s)`
- Local and public unsigned webhook POSTs return `401 invalid signature`, proving the route reaches Hermes and signature verification is active.
- Photon user list confirms one shared user for Adam, assigned to `+1 (415) 579-6445`.

## iMessage completion ping attempt

Adam asked: "have hermes message me on imessage when done."

Codex attempted to send a completion iMessage through the Photon sidecar to Adam's allowed number. Hermes' generic `hermes send` target resolver rejected the raw Photon space id, so Codex called the local Photon sidecar directly with the stored sidecar token.

Result:

- Sidecar request reached Photon.
- Photon returned a provider-side block.
- Gateway log shows: `[spectrum-imessage] Target not allowed for this project`.

Codex then checked native macOS Messages automation as a fallback. The AppleScript probe hung and was killed. No native Messages iMessage was sent.

Current conclusion: Photon shared-line setup is live, but proactive outbound iMessage to Adam is blocked by Photon's managed shared-line policy for this project. The likely next test is for Adam to initiate the conversation by texting the assigned Photon line:

`+1 (415) 579-6445`

Suggested test body:

`Hermes, say PHOTON_READY`

After that first inbound message, Hermes should receive the signed webhook and reply through the already-running Photon sidecar.

## 2026-06-08 21:42 CDT repair after Adam texted the line

Adam texted the assigned Photon line from iMessage. Screenshot and gateway logs confirmed:

- Inbound Photon/iMessage webhook works.
- Gateway logged inbound chat `any;-;+170****3328`.
- Hermes generated a reply.
- Photon sent the first "No home channel" notice over iMessage.

Two follow-up defects were found and fixed:

1. `/sethome` did not persist `PHOTON_HOME_CHANNEL` for Photon.
2. The upgraded `spectrum-ts@1.18.0` no longer accepted raw string content in the sidecar send path; outbound replies failed with `TypeError: c.build is not a function`.

Repairs:

- Saved `PHOTON_HOME_CHANNEL=any;-;+17012023328`.
- Saved `PHOTON_HOME_CHANNEL_NAME=Adam iMessage`.
- Patched `plugins/platforms/photon/adapter.py` so `_env_enablement()` exposes `PHOTON_HOME_CHANNEL` as a real plugin `HomeChannel`.
- Patched `plugins/platforms/photon/sidecar/index.mjs` so `/send` wraps outbound text with Spectrum's `text()` content builder.
- Restarted the gateway and verified one gateway process plus one Photon sidecar process.

Final proof:

- `hermes send --list photon` lists `photon:any;-;+17012023328`.
- `hermes send --to photon --json 'Final repair check: Hermes iMessage outbound is working now.'` returned:
  - `success: true`
  - message id present: `spc-msg-25c092d1-ac2f-41b3-8007-c3fbdf7a55f4`
  - note: sent to Photon home channel.

This means the normal Hermes send path and the live gateway reply path are repaired.

## 2026-06-08 21:47 CDT follow-up after Adam's "Hello" got no visible reply

Adam's later iMessage `Hello` and `Ok` both reached Hermes through Photon, and Hermes generated responses for both. The missing visible reply was not an inbound/webhook problem; the live Node sidecar was still an old process and crashed on outbound send with `TypeError: c.build is not a function`.

Codex stopped stale gateway processes with `hermes gateway stop --all`, restarted Hermes with `hermes gateway start --all`, and verified the live state collapsed back to one gateway plus one Photon sidecar:

- gateway webhook listener: `127.0.0.1:8788`
- Photon sidecar listener: `127.0.0.1:8789`
- gateway PID at verification: `4024`
- sidecar PID at verification: `3672`

Final completion iMessage sent through the normal Hermes Photon home-channel path:

- command: `hermes send --to photon --json 'Codex repair complete: your earlier Hello reached Hermes, but the send sidecar was stale. I restarted the live Photon path; iMessage outbound is up now. Reply "Hermes ping" to test the full loop.'`
- result: `success: true`
- Photon message id: `spc-msg-134d253a-ae70-4c31-9146-7da9a1f6a3b8`

Current status: outbound iMessage is verified again after the process cleanup. Full automatic inbound-to-reply loop should be tested by Adam texting `Hermes ping` to the assigned Photon line.

## 2026-06-08 21:49 CDT correction: live replies still failed with reply anchor

Adam texted `Hermes ping`. Gateway logs showed:

- inbound received from `+170****3328`
- Hermes generated a 173-character response
- outbound failed again through Photon sidecar `/send`

Manual `hermes send` still worked, so the remaining defect was narrowed to the extra `replyTo` anchor Hermes passes for real inbound replies. Photon/Spectrum docs indicate guaranteed delivery should use `space.send(...)`; threaded replies are a separate message-level path. Codex patched Photon to ignore Hermes' `reply_to` value for normal iMessage text sends, keeping replies in the same chat instead of asking Spectrum to thread them to a specific inbound message.

Second repair:

- patched `plugins/platforms/photon/adapter.py` so `PhotonAdapter.send()` calls `_sidecar_send(chat_id, content)` without `reply_to`
- patched `plugins/platforms/photon/adapter.py` so `_sidecar_send()` never includes `replyTo` in the sidecar body
- patched `plugins/platforms/photon/sidecar/index.mjs` so `/send` ignores `replyTo` even if a caller provides it
- restarted Hermes; verified current gateway PID `10999`, sidecar PID `11207`

Proof after second repair:

- direct sidecar probe with a synthetic `replyTo` field returned HTTP 200
- Photon message id: `spc-msg-ae38eeed-16f0-4839-ae36-e9e82a75020a`
- normal Hermes send path returned success with Photon message id `spc-msg-29ebc845-c9b8-4e5d-922c-bac1a769594f`

Current status: outbound with a `replyTo`-shaped payload is verified after the second repair. Adam has been asked to send `Hermes ping` one more time to verify the full real inbound-to-agent-to-iMessage loop.

## 2026-06-08 21:52 CDT final live loop check

Adam sent `Hermes ping` again after the second repair. Gateway logs confirmed:

- inbound received at `2026-06-08 21:50:44 CDT`
- Hermes generated a 180-character response at `2026-06-08 21:51:15 CDT`
- Photon send started for `any;-;+170****3328`
- no Photon send failure was logged through the follow-up check at `2026-06-08 21:52:45 CDT`
- current gateway/sidecar state remained stable: gateway PID `10999`, sidecar PID `11207`, listeners on `127.0.0.1:8788` and `127.0.0.1:8789`

Current status: the real inbound-to-agent-to-iMessage loop is repaired to the observable point available from gateway logs. Hermes does not currently log successful Photon message ids for automatic replies, so success is inferred from the absence of a post-send failure plus the stable sidecar after the live test.

## Known limitations

- The Cloudflare quick tunnel URL is ephemeral and can die if the tmux session or machine stops. For production, replace it with a named Cloudflare tunnel or stable public hostname.
- `npm audit` in the Photon sidecar reports 7 high-severity findings in the current dependency tree, primarily through Photon/OpenTelemetry/protobuf packages. Kept `spectrum-ts@1.18.0` because it fixed the live retired-hostname failure.
- Proactive outbound iMessage before Adam initiated the chat was blocked by Photon with `Target not allowed for this project`; after Adam texted the assigned line, outbound delivery works.

## 2026-06-08 22:14 CDT read receipts + inbound media hydration

Adam clarified that the desired "got it" signal was the native iMessage `Read` state, not a one-word ack. Codex implemented the Photon/Spectrum mark-read path:

- added `PHOTON_MARK_READ_ON_INBOUND` / `PHOTON_SEND_READ_RECEIPTS` support in `plugins/platforms/photon/adapter.py`
- enabled `PHOTON_MARK_READ_ON_INBOUND=true`
- scheduled sidecar `/read` on inbound messages before dispatching to Hermes
- added sidecar `/read`, using Spectrum `space.read(message)` with an inbound message shape
- verified live sidecar `/read` returned HTTP 200 `{ok: true}`

Codex then implemented inbound iMessage media hydration so Photon attachments no longer have to remain metadata-only when Photon exposes an attachment GUID:

- added sidecar `/download-attachment`, using `imessage(app).getAttachment(attachmentId)` and saving bytes under `~/.hermes/photon-attachments/YYYY-MM-DD/`
- updated `PhotonAdapter` to hydrate `attachment` / `voice` / grouped attachment content before creating `MessageEvent`
- populated `MessageEvent.media_urls` and `media_types` so downstream image/audio/video/document handling can see local files
- added rich-link handling so URL cards surface as text instead of unknown content
- updated Photon README and runtime platform hint to stop telling Hermes that all inbound attachments are metadata-only

Verification:

- `uv run --extra dev pytest tests/plugins/platforms/photon -q` -> 51 passed
- `node --check plugins/platforms/photon/sidecar/index.mjs` -> passed
- `venv/bin/python -m py_compile plugins/platforms/photon/adapter.py tests/plugins/platforms/photon/test_inbound.py tests/plugins/platforms/photon/test_mention_gating.py` -> passed
- restarted live gateway; current verified listeners after restart:
  - gateway PID `48995`, `127.0.0.1:8788`
  - Photon sidecar PID `49193`, `127.0.0.1:8789`
- live sidecar smoke:
  - `/healthz` -> HTTP 200 `{ok: true}`
  - `/download-attachment` with missing id -> HTTP 400 `attachmentId is required` (endpoint present)
  - `/read` -> HTTP 200 `{ok: true}`

Fresh live media proof after restart:

- Adam sent `IMG_3095.JPG` through the Photon iMessage line after the patch.
- Gateway logs changed from the old `no download URL yet` marker to `saved to /Users/adamjoh...`.
- Hermes image routing started: `Pre-analyzing 1 image(s) via vision_analyze`.
- Local files exist:
  - `/Users/adamjohnsson/.hermes/photon-attachments/2026-06-09/1780974900323-spc-att-e1e6b41b-e220-42f9-9ab8-ee6fde54f310-IMG_3095.JPG`
  - `/Users/adamjohnsson/.hermes/photon-attachments/2026-06-09/1780974927409-spc-att-2ed206f5-e3f3-4983-85c1-4ed9889ebafe-IMG_3095.JPG`
- Both files are 431 KB.
- Gateway reached `response ready` and started Photon send after image routing; no delayed send failure appeared in the follow-up tail.

Current status: live iMessage image hydration is verified. The same sidecar path should handle videos, audio/voice, and documents when Photon exposes their attachment GUIDs.
- No public post, email, X action, payment action, deploy, refund, cancellation, or account-state change was performed beyond the explicitly requested setup.
