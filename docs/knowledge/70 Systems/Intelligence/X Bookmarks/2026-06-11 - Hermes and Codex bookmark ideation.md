# Hermes and Codex Bookmark Ideation

Date: 2026-06-11 16:12 CDT
Source: X bookmarks via authenticated `xurl bookmarks -n 60`
Link/path: `/opt/homebrew/bin/xurl`; account verified as `@Biblicalman`
Captured by: Codex

## Why It Matters

Adam's newest bookmark cluster is mostly about Hermes/OpenClaw becoming a real operating layer: profiles, SOUL files, Obsidian memory, Telegram/mobile control, remote files, provider routing, and bookmark-to-second-brain capture.

The useful move is not to chase every shiny provider or re-arm automation. The useful move is to turn the bookmarks into a safe local agent-improvement lane while outbound posting/sending remains locked.

## Pattern

- Profiles are becoming the right unit of work: writer, support, store analyst, local-model researcher, and operator lanes.
- SOUL files are treated by the market as more important than model choice; local setup already agrees with this.
- Obsidian is being framed as Hermes' long memory, but local ops says the ops capsule remains canonical and Obsidian files can be dataless.
- X Articles are becoming a real agent-education format, but `xurl` often exposes only the article title, not full body.
- Bookmark rot is a known problem. The old local bookmark scraper is still disabled, so the safe replacement is manual/read-only capture.
- Provider-routing hype is high. Given today's Fable/outbound incident, new providers should go through a sandboxed eval before touching live workflows.

## Usable Moves

1. **Manual bookmark intelligence lane**
   Keep the old scraper disabled. Add/use a manual read-only pull that converts recent `xurl bookmarks` into a local Markdown packet with source links, classification, and "use / ignore / verify" status.

2. **Profile roster check**
   Current local profiles include `writer`, `support`, and `storeanalyst`, but only `default` is running. Treat profiles as on-demand specialist lanes with explicit allowed actions, model, receipt path, and outbound boundary.

3. **SOUL lint**
   Add a lightweight review checklist for Hermes profile `SOUL.md` files: role clarity, allowed writes, forbidden actions, voice rules, receipt rules, and escape clause when the wrong profile is loaded.

4. **Obsidian bridge with guardrails**
   Let Hermes/Codex capture source intelligence into Obsidian, but every note should say whether it came from live source, ops capsule, receipt, or memory. Do not let Obsidian mirror notes outrank the ops capsule.

5. **X Article reader gap**
   For X Articles, `xurl read` may only return the title and an `x.com/i/article/...` URL. Use browser/CDP when the full article body matters; otherwise classify title-only and mark `body not retrieved`.

6. **Remote file read-only usage**
   Hermes remote-instance file browsing is useful for future Mac mini/cloud handoff checks. Keep it read-only until there is a receipt-backed reason to write remotely.

7. **Provider sandbox**
   Bookmarks mention MixRoute, Newsportal/Step, local Gemma/Qwen, and similar routes. Do not add them to live support/publishing paths during lockdown. Use `qwenlocal` or another cheap profile only for isolated ideation/eval.

8. **Video/asset generation restraint**
   Mythos-for-Marketing style bulk video generation is useful as internal header/thumbnail ideation. Avoid "hundreds of warmed accounts" automation; that conflicts with the current safety posture and Adam's brand.

## Notable Sources

- YanXbt: SOUL.md guide article, title retrieved only: https://x.com/IBuzovskyi/status/2065125711401062758
- Jock Ferguson: Mythos-for-Marketing/bulk video angle: https://x.com/jock_ferguson/status/2064915420545761483
- marfin: OpenClaw agents through Telegram business-ops article, title/body wrapper only: https://x.com/marfinxx/status/2065002251802780031
- YanXbt: Hermes plus Obsidian long-memory angle: https://x.com/IBuzovskyi/status/2064997850526646524
- Garry Tan: Nessie memory/context import into OpenClaw/Hermes: https://x.com/garrytan/status/2064947145652994510
- Shann: profile-builder guide quoting Nous profile-builder release: https://x.com/shannholmberg/status/2065031898821435465
- Teknium: remote instance file browsing, read-only for now: https://x.com/Teknium/status/2065112576552526168
- Nous Research: Profile Builder release: https://x.com/NousResearch/status/2064760263224504719
- Nous Research: iMessage via Photon: https://x.com/NousResearch/status/2064102412076364207
- Ole Lehmann: X bookmarks into agent second brain: https://x.com/itsolelehmann/status/2061911202830401564
- Matt Van Horn: Agent Cookie/session persistence: https://x.com/mvanhorn/status/2061259423197372566

## Voice / Copy Notes

- The winning format in this cluster is practical infrastructure framed as a simple operational before/after.
- Avoid copying the hype voice. For Adam's system, the sharper angle is: "This is not another AI toy. It is a way to stop losing the thread between phone, Mac, receipts, and public work."

## Product / Funnel Notes

- Potential Dead Hidden/Biblical Man-facing product angle: "The Operator Desk" or "Study Desk" should be sold as continuity, proof, and source discipline, not generic automation.
- Potential internal offer: a paid "Ops Capsule" setup/service could be framed around profile roles, SOUL files, Obsidian capture, Telegram intake, and receipts.

## Follow-Up

- Do not re-enable the old bookmark scraper until Adam explicitly wants recurring bookmark ingestion.
- Implemented: read-only `/Users/adamjohnsson/.deadhidden-os/ops/bin/x-bookmark-intel` now pulls recent bookmarks and writes a Markdown packet locally without touching X writes or the disabled scraper.
- Verification packet: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/x-bookmark-intel/2026-06-11-1614-x-bookmark-intel.md`
- Best Hermes implementation: add a profile health/preflight packet showing model, gateway state, allowed actions, receipt path, and lock status.
- Best Codex implementation: before any public/customer/agent-routing task, check `OUTBOUND_LOCKDOWN.md` and state whether the task is read-only, draft-only, or write-capable.
