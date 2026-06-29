# 2026-06-19 06:28 - Codex - CNVS install gate

Adam asked Codex to install and set up the app from `https://x.com/_maxblade/status/2067757770820964694?s=46` on the Mac mini.

Codex read the local ops capsule first, refreshed `TEAM_CONTEXT.md`, and retrieved the X post through authenticated local `xurl`. The post points to `https://cnvs.dev/`, "CNVS - Command an army of agents with your voice."

Findings:

- CNVS is advertised as a native macOS Swift app for orchestrating Claude, GPT, Gemini, Cursor, and Codex.
- The public site does not expose a direct installer at the checked public paths.
- The billing config currently reports lifetime license #64 at $169, with Stripe checkout enabled.
- The Mac is an Apple M4 running macOS 27.0, but `/System/Volumes/Data` has only about 2.2 GiB free.

Boundary:

- No CNVS purchase was made.
- No payment details were submitted.
- No CNVS app was downloaded or installed.
- A live checkout URL was generated while probing the public checkout API, but it was not opened or paid.
- No credential, Stripe, customer, repo, public post, email, Telegram, Linear, Notion, deploy, DNS, or account-state change was performed.

Next action: Adam needs to explicitly approve the $169 CNVS purchase/license flow, or provide the post-purchase download/license email/link. After that, free disk space if needed, install the app, connect existing agent CLIs, and verify launch.
