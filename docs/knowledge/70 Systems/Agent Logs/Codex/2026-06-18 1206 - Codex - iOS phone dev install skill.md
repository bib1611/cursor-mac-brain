# 2026-06-18 1206 - Codex - iOS Phone Dev Install Skill

Adam asked Codex to turn the FaithWall Verse physical-iPhone/Xcode/Apple-account install process into a reusable skill.

Created local Codex skill:

`/Users/adamjohnsson/.codex/skills/ios-phone-dev-install/SKILL.md`

Also created UI metadata:

`/Users/adamjohnsson/.codex/skills/ios-phone-dev-install/agents/openai.yaml`

The skill captures:

- physical iPhone detection with `devicectl`
- Xcode command-line simulator sanity build
- physical-device build with automatic provisioning
- side-by-side `.dev` bundle ID rule so TestFlight/App Store installs are not overwritten by default
- Xcode Apple account/login recovery notes
- direct Xcode binary launch fallback
- disk-pressure handling for the regenerable `iOS DeviceSupport` cache
- FaithWall Verse known-good values from 2026-06-18
- receipt requirements for future phone-install work

Validation:

- Local structural check passed for required frontmatter, no TODO placeholders, default prompt, and ASCII-only skill files.
- The upstream `quick_validate.py` path from the transient system skill cache was unavailable after scaffolding, so no upstream validator result is claimed.

Boundary:

- No App Store Connect mutation.
- No TestFlight submission.
- No production bundle overwrite.
- No Apple credential, key, or account setting changed.
- No external/public action performed.
