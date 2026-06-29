# 2026-06-29 1349 CDT - Codex - disk cleanup

Adam asked over the Jarvis iMessage lane: "Free up space."

## Result

- Before: `/System/Volumes/Data` had `125Mi` free, `100%` capacity.
- After: `/System/Volumes/Data` had `7.1Gi` free, `96%` capacity.
- Approximate reclaimed space: `~7Gi`.

## Cleared

Rebuildable caches and logs only:

- `~/.cache/codex-runtimes`
- `~/.cache/whisper`
- `~/.bun/install/cache`
- `~/.npm/_npx`
- `~/Library/Caches/Aside`
- `~/Library/Caches/Google`
- `~/Library/Caches/Comet`
- `~/Library/Caches/electron`
- `~/Library/Caches/node-gyp`
- `~/Library/Caches/Homebrew`
- `~/Library/Caches/claude-cli-nodejs`
- `~/Library/Caches/com.openai.codex`
- updater/download/component caches under `~/Library/Application Support/Google`, `Aside`, `Comet`, and `Codex`
- `~/Library/Application Support/Google/DriveFS/Logs`

## Left Alone

- Google DriveFS `canceled_uploads`: `2.4G`, includes named video files and may be the only local copy of failed/canceled uploads.
- Google DriveFS account cache/profile data.
- Browser/app profile data such as Chrome, Aside `Default`, Comet `Default`, Codex `Default`.
- Codex sessions and SQLite logs.
- Claude app state, extensions, and local sessions.
- Personal files in Downloads, Documents, Desktop, Pictures, Movies, and code repos.
- Trash was already `0B`.

## Proof

Final check:

```text
Filesystem      Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s5   228Gi   168Gi   7.1Gi    96%    2.4M   74M    3%   /System/Volumes/Data
```

Boundary: no publish, send, post, spend, refund, deploy, DNS/security/credential change, Linear/Notion write, customer data access, or personal-file deletion happened.
