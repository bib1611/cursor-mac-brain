# 2026-06-10 08:53 CDT - Codex - Plain Bible review feature

## Request

Adam said Christie remembered a strong reader review for The Plain Bible Manual and asked Codex to check comments from the past four days and find it.

## Source Checked

- Public Biblical Man archive API for posts since 2026-06-06.
- Public Substack comments API for these recent posts:
  - `201340823` - You Did Not Lose Faith in Christ
  - `201286332` - The Signs of a Christian Cult
  - `201212767` - You Cannot Serve Your Way Into the Family
  - `200946154` - The Man Who Bakes the Bread Alone

Local audit extract:

- `/Users/adamjohnsson/Documents/Codex/2026-06-10/so-as-you-know-i-have/work/bm-comments-past4days.json`

## Find

The standout Plain Bible Manual review is comment `273299573` by `Faithful Recovery` on:

`https://biblicalman.substack.com/p/the-signs-of-a-christian-cult`

Created at `2026-06-09T15:11:36.036Z`.

The useful sales-copy hook is that the reader explicitly said the manual is not a list, but a pathway into deeper Scripture. That fits the Galatians 4 / Christian-cult thread without making The Plain Bible Manual sound like another man-made rulebook.

## Local Change

Updated:

- `/Users/adamjohnsson/code/deadhidden/src/app/store/the-plain-bible-manual/page.tsx`

Added a lead proof block in the existing testimonial grid:

- short excerpt attributed to Faithful Recovery
- paraphrase of the rest of the review
- source context: Substack comment on The Signs of a Christian Cult

Also, during the same work block, the FaithWall beta page had already been updated locally at:

- `/Users/adamjohnsson/code/deadhidden/public/polsia/faithwall-beta.html`

with the Galatians 4 hero angle:

- `The tutor nobody appointed.`
- `Not another list`
- `A list counts you to keep you out. A wall guards you because you are already in.`

## Verification

- `npm run lint -- src/app/store/the-plain-bible-manual/page.tsx` passed.
- Local `GET http://127.0.0.1:3020/store/the-plain-bible-manual` returned `200` and contained `Faithful Recovery` plus the new excerpt.
- Local `GET http://127.0.0.1:3020/os/faithwall-beta` returned content containing `The tutor nobody appointed`, `Not another list`, and the TestFlight beta truth box.

## Boundary

No deploy, publish, Substack edit, X post, Stripe change, customer email, or live account change was performed.
