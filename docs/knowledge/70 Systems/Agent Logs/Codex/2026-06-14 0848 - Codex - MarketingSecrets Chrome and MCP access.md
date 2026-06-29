# Codex - MarketingSecrets Chrome and MCP access

Date: 2026-06-14 08:48 CDT

Adam pushed back that Codex had full Mac/disk access and should not stop at the unavailable Chrome extension path. Codex switched to the local Browserbase `browse`/CDP route instead of relying on the Codex Chrome Extension.

## What worked

- `browse doctor` passed: daemon connected, `mode=cdp`, 12 Chrome pages visible.
- `browse status` and `browse tab list` could read and control the existing Chrome session.
- MarketingSecrets URL was opened in the controlled Chrome tab.
- Google sign-in for `thebiblicalman1611@gmail.com` succeeded.
- Native MarketingSecrets MCP tools were loaded directly in Codex:
  - `memory_search`
  - `memory_get_profile`
  - `memory_save`
  - `memory_get_recent`
- `memory_get_profile` returned the correct Dead Hidden Ministries / DeadhiddenOS business profile.
- A project note was saved to MarketingSecrets Brain documenting the access state and blocker.

## What blocked web chat access

- The Chrome session initially redirected the provided MarketingSecrets chat URL to sign-in.
- Google sign-in with the only signed-in desktop account, `thebiblicalman1611@gmail.com`, opened a new/empty `Personal` workspace, not `deadhiddenos`.
- Re-opening `https://www.marketingsecrets.ai/home/deadhiddenos/chat/aabb7e97-b0dd-48f2-88b4-d624f743bb91` after that login redirected to `/home`, showing only the Personal workspace.
- Codex signed out of that accidental MarketingSecrets web account.
- Codex requested an email sign-in link/code for `adam@deadhidden.org`.
- The connected Gmail app is scoped to `thebiblicalman1611@gmail.com`; searches for MarketingSecrets / sign-in code / 6-digit code did not find the `adam@deadhidden.org` link.
- Therefore the web chat account is blocked by mailbox/account scope, not by lack of Chrome control.

## Chrome/CDP facts

- `http://localhost:9222/json/version` works.
- `http://[::1]:9222/json/version` works.
- `http://127.0.0.1:9222/json/version` returns 404.
- The local `mcp-chrome` server uses `http://localhost:9222`, so Python/urllib resolves successfully, but tools hardcoding `127.0.0.1` can fail.
- The Codex Chrome Extension remains unavailable/missing in the selected profile, but it is no longer the only viable path because `browse` works.

## Safety

- No cookies, localStorage, passwords, or session stores were inspected.
- Browser history was queried only for targeted `marketingsecrets.ai` entries.
- No email was sent.
- No MarketingSecrets chat prompt was sent through the web UI.
- No Stripe, Resend, Substack, X, product, or site mutation happened in this pass.

## Current operating guidance

Use MarketingSecrets through the native MCP tools inside Codex for Brain reads/writes. Use `browse` for authenticated browser work when the target session is present. The MarketingSecrets web chat for `deadhiddenos` needs access to the actual account inbox/session, likely `adam@deadhidden.org`, before Codex can use the browser page itself.
