# Codex - Jarvis pipe repair and skill install

Date: 2026-06-18 18:18 CDT

## Summary

Recovered Codex Chrome Extension control after the earlier `native pipe is closed` failure, diagnosed the actual remaining blocker as Chrome extension file-upload permission, created a reusable local Codex repair skill, and successfully fed Jarvis the Dead Hidden ops-context skill through Chorus.

## Chrome repair proof

- Clean browser runtime reset restored extension communication.
- `browser.user.openTabs()` worked and saw the live `Jarvis - Chorus` tab.
- Chrome helper checks passed:
  - Chrome running.
  - Google Chrome installed.
  - Codex Chrome Extension installed and enabled in the `Default` Chrome profile.
  - Native host manifest exists and allows `chrome-extension://hehggadaopoacecdllhhajmbjkdcmajg/`.
- Isolated local smoke test proved textarea control and clipboard control worked.
- Isolated file chooser test failed with:

```text
{"code":-32000,"message":"Not allowed"}
fileChooser.setFiles failed
```

Interpretation: the native pipe was recoverable/healthy after reset; file attachment is blocked separately by Chrome extension file access.

Manual upload fix still needed for future direct file uploads:

`To enable file upload, go to chrome://extensions in Chrome, click Details under the Codex extension, and enable "Allow access to file URLs." See https://developers.openai.com/codex/app/chrome-extension#upload-files for details.`

Chrome automation was blocked from visiting `chrome://extensions`, so Codex did not work around it with raw CDP, AppleScript, or profile edits.

## Jarvis result

Jarvis URL:

`https://chorus.com/agents/65bca62c-e9de-4e5c-8758-5c18e0917dd8`

Actions:

- Used `Build with your agent`.
- First send only transmitted the Chorus starter prompt; Jarvis replied that the message cut off.
- Used coordinate focus plus browser clipboard paste.
- Verified the final composer contained `dead-hidden-ops-context`, `Trust order`, and `Codex task:` before send.
- Jarvis replied: `Created: dead-hidden-ops-context`.
- Jarvis test answer correctly described its role as Adam's cloud connected-app helper/read-only auditor, with Codex as Mac-local executor, and refused email/posting/Stripe/customer/file/Linear/app mutations without exact Adam approval.

State label: Jarvis skill created according to live Chorus response. Direct file upload remains blocked until Chrome extension file URL access is enabled.

## Local skill

Created and validated:

`/Users/adamjohnsson/.codex/skills/repair-chrome-extension-pipe/SKILL.md`

Validation command:

```bash
python3 /Users/adamjohnsson/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/adamjohnsson/.codex/skills/repair-chrome-extension-pipe
```

Output:

```text
Skill is valid!
```

## Boundary

No raw secrets were pasted. No email, post, Stripe/customer money action, Linear write, file deletion in Chorus, public publish, deploy, permission/account change, or credential change was performed. Temporary local smoke-test HTTP server was stopped and the temporary HTML page was deleted. Jarvis tab was kept open as Chrome handoff.
