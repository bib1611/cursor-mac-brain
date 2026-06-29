# 2026-06-14 0841 - Codex - Chrome extension recovery opened

Adam asked Codex to fix Chrome access so Codex can attach to the MarketingSecrets web session.

Checks:

- Chrome was running.
- Native messaging host check passed:
  - Manifest exists at `/Users/adamjohnsson/Library/Application Support/Google/Chrome/NativeMessagingHosts/com.openai.codexextension.json`.
  - Host name matched `com.openai.codexextension`.
  - Allowed origin included `chrome-extension://hehggadaopoacecdllhhajmbjkdcmajg/`.
- Codex Chrome Extension check failed for selected Chrome profile `Default`:
  - Extension ID `hehggadaopoacecdllhhajmbjkdcmajg`.
  - Installed: false.
  - Enabled: false.

Action:

- Opened the official Codex Chrome Extension page in Google Chrome:
  - `https://chromewebstore.google.com/detail/codex/hehggadaopoacecdllhhajmbjkdcmajg`
- Also opened it with Chrome `--profile-directory=Default` so the extension can be installed into the profile Codex is trying to control.

Status:

- Human click still required in Chrome to install/enable the extension.
- Once Adam confirms installation, Codex should rerun extension detection, reconnect through the Chrome plugin, then claim the MarketingSecrets tab.

No browser cookies, local storage, passwords, or session stores inspected.
