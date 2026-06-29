# 2026-06-22 0630 CDT - Codex - Fugu install

Adam provided a Sakana API key and asked to install Fugu via the official one-line installer.

Actions:

- Read the required Dead Hidden ops boot files before acting.
- Fetched and inspected `https://sakana.ai/fugu/install`.
- Cloned `https://github.com/SakanaAI/fugu.git` to `/Users/adamjohnsson/.fugu`.
- Ran `/Users/adamjohnsson/.fugu/scripts/install.sh --force --reconfigure`.
- Switched the standalone Codex CLI used from `/Users/adamjohnsson/.local/bin` to `0.141.0`.
- Installed Fugu config files into `/Users/adamjohnsson/.codex`.
- Stored `SAKANA_API_KEY` in `/Users/adamjohnsson/.codex/.env` with `0600` permissions. Secret value not recorded.
- Installed `/Users/adamjohnsson/.local/bin/codex-fugu`.
- Installer added `/Users/adamjohnsson/.local/bin` to `/Users/adamjohnsson/.zprofile`.

Backups:

- `/Users/adamjohnsson/.codex-backups/codex-config-20260622T112755Z`
- `/Users/adamjohnsson/.codex-backups/codex-config-20260622T112841Z`

Verification:

- `PATH="/Users/adamjohnsson/.local/bin:$PATH" codex --version` returned `codex-cli 0.141.0`.
- `codex-fugu --status` showed installed version `0.141.0`, bundle `configs`, deployed target `0.141.0`, format `modern`, repo ref `ed1535c4f14e715635bc0fcfb4dcf1e0683164b1`.
- `/Users/adamjohnsson/.codex/fugu.json`, `/Users/adamjohnsson/.codex/fugu.config.toml`, and `/Users/adamjohnsson/.codex/.fugu/state` are present.
- `/Users/adamjohnsson/.codex/.env` is `-rw-------`.
- `SAKANA_API_KEY` is present with expected `fish_` key shape, without printing the value.
- `codex doctor` loaded `/Users/adamjohnsson/.codex/config.toml` successfully with parse `ok`; the only failing check was `TERM=dumb` from the noninteractive Codex app environment.

Boundary:

- Local installer/config action only.
- No public post, email, Stripe/customer/money mutation, deploy, DNS/security/account-setting change, Linear/Notion write, or credential print happened.
