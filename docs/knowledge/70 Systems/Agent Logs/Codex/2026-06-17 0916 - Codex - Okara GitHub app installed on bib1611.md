# 2026-06-17 0916 - Codex - Okara GitHub app installed on bib1611

Adam asked Codex to finish the Okara GitHub integration after logging into GitHub as `bib1611`.

## Actions

- Opened the Okara Coding Agent GitHub App install flow while signed in as `bib1611`.
- Selected install target `bib1611`.
- Changed repository access from the default `All repositories` to `Only select repositories`.
- Selected only `bib1611/deadhidden`.
- Installed/authorized Okara Coding Agent.

## Proof

- GitHub installed-apps page for `bib1611` now lists `Okara Coding Agent`.
- New GitHub installation ID: `140906336`.
- Installation configuration shows:
  - Installed June 17, 2026.
  - Repository access: `Only select repositories`.
  - Selected 1 repository: `bib1611/deadhidden`.
  - Permissions: read metadata; read/write code and pull requests.

## Okara State

- Okara received the callback and redirected to `https://okara.ai/cmo?github_connected=true`.
- Okara settings URL checked: `https://okara.ai/settings?tab=integrations&website=fc0937d5-f7d8-4a3c-bbe5-795e2c548c11`.
- Before the verified install, Okara's repo picker still showed only the stale `@biblicalman1611` installation and returned `No matches` for `bib1611/deadhidden`.
- After the verified GitHub install, Okara's integrations screen stayed stuck on `Checking...` for the Code Repository connector and other connector cards.
- Page console showed repeated Okara-side warnings plus `Error fetching subscription data (attempt 1): AbortError: signal is aborted without reason`.

## Boundary

- No SEO audit was run.
- No credits were spent.
- No repository PR was opened by Okara.
- No Stripe, email, Substack, X, product, checkout, or customer-facing action was performed.

## Current Blocker

GitHub-side installation is correct. Okara-side settings data/connector state is not resolving in the UI, so Codex could not yet select `bib1611/deadhidden` inside Okara or trigger a fresh audit.
