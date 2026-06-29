# 2026-06-10 20:18 CDT - Codex - Hermes Profile Builder Check

Adam asked whether the Nous Research X link he gave Hermes had been updated into Hermes Agent on the Mac Mini, whether the local install was fully upgraded, and what the feature means.

External link checked:

- `https://x.com/nousresearch/status/2064760263224504719?s=46`
- X text retrieved via local `xurl`: "Introducing the Hermes Agent Profile Builder..." with dashboard control over identity/name/description, model/provider, built-in and optional skills, skills-hub installs, and MCP servers.

Local machine proof:

- Host hardware: Mac mini, model identifier `Mac16,10`, Apple M4.
- Hermes health: `http://127.0.0.1:8642/health` returned `{"status":"ok","platform":"hermes-agent","version":"0.16.0"}`.
- `hermes status` showed gateway running through launchd, default model `claude-fable-5`, provider `claude-max-opus`, Telegram configured.
- Dashboard process: PID `69093`, command `/Users/adamjohnsson/.hermes/hermes-agent/venv/bin/python -m hermes_cli.main dashboard --no-open --host 127.0.0.1 --port 9120`.
- Live dashboard route `http://127.0.0.1:9120/profiles/new` returned HTTP 200 and served the compiled app bundle.

Version / update state:

- Local repo HEAD: `3acf73161fe224a3dcdb985547966dc7fd9f78b6` (`Move folder creation into dialog`).
- Origin/main after fetch: `9dd9ef0ec99a87f078f7272b4323df5440b4b3f9` (`fix(web): profiles page modal (#43858)`).
- `git rev-list --count HEAD..origin/main` returned `17`.
- `hermes update --check` reported update available, 17 commits behind `origin/main`.
- Conclusion: Hermes is not fully current as of this check.

Feature presence:

- Feature commit present locally and in origin: `d986bb0c6de6bcffda4981e83652284d481a90f4` (`feat(dashboard): full-featured profile builder (model + skills + MCPs) (#39084)`).
- Desktop app install stamp: commit `d986bb0c6de6bcffda4981e83652284d481a90f4`, built at `2026-06-10T16:46:05.351Z`, bundle `0.15.1`.
- Source files present locally: `web/src/pages/ProfileBuilderPage.tsx`, route in `web/src/App.tsx`, API extension in `hermes_cli/web_server.py`, API client fields in `web/src/lib/api.ts`.
- Live API checks using the page-injected session token found 15 profiles, 42 model providers, 178 skills, and 3 MCP servers (`agentmemory`, `chrome_cdp`, `cua-driver`).

Meaning:

- The Profile Builder is a dashboard-native wizard for creating separate Hermes profiles in one flow instead of hand-configuring them across multiple pages.
- It can set the profile's name/description, model/provider, skills to keep, hub skills to install, and MCP servers to write into the new profile's config.
- Hub skill installs are async and scoped to the new profile with `hermes -p <profile> skills install <identifier>`.

Boundary:

- No Hermes update was installed.
- No profile was created.
- No Hermes config, API keys, customer state, money state, publishing state, webhook, or external account setting was changed.
