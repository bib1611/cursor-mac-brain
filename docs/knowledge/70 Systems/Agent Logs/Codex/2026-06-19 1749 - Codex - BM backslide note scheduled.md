# Codex - BM Backslide Note Scheduled

Time: 2026-06-19 17:49 CDT

Adam asked Codex to reformat a Biblical Man Substack note idea and post it at 6:15 PM.

Result:

- Publication: The Biblical Man / `biblicalman.substack.com`
- Substack scheduled feed draft id: `279372090`
- Scheduled for: 2026-06-19 18:15 CDT
- Trigger time: `2026-06-19T23:15:00.000Z`
- Artifact: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-19-bm-note-backslide-1815/README.md`

Scheduled copy:

```text
No man plans to backslide.

He just skips one morning.

Then a week.

Then prayer feels like talking to the ceiling.

Nobody falls.

They drift.

Esther 4:16: "if I perish, I perish."

She did not pray for safety.

She prepared to die, then walked in anyway.

We call it faith when it costs nothing.

It is not.

The danger for Peter on the water was not the waves.

It was the second he looked down.

Faith does not drown in the storm.

It drowns the moment you check the storm.
```

Verification:

- Authenticated Biblical Man publication API returned publication id `2572115`, subdomain `biblicalman`, and current-user author/admin context.
- Authenticated Substack scheduler call returned HTTP `200` from `POST https://biblicalman.substack.com/api/v1/comment/draft`.
- Schedule response returned id `279372090`, trigger `2026-06-19T23:15:00.000Z`, date `2026-06-19T22:48:51.842Z`, and body hash `646287ad32388820`.
- Draft verification endpoint returned exactly one matching scheduled feed draft for id `279372090`, with `trigger_at=2026-06-19T23:15:00.000Z`, `post_id=null`, `user_id=169765767`, and the exact body above.

Boundary:

Only this Biblical Man Substack Note was scheduled. No immediate publish, no X post, no email, no image upload, no subscriber/customer/Stripe mutation, no deploy, no Linear/Notion write, no credential change, and no account-setting change.
