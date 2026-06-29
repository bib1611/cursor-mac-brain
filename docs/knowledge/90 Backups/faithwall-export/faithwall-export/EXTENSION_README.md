# FaithWall Chrome Extension — Manual Install

This is the first Chrome extension version for founding-family testing.

## What it does

- Works in Chrome on desktop/laptop.
- Interrupts selected distracting websites.
- Shows Scripture before scrolling.
- Lets the user lay the brick.
- Gives temporary access after completion.
- Keeps settings local in Chrome storage.

## What it does not do yet

- It does not block phone apps.
- It does not work in Safari.
- It does not work across every app on a device.
- It can be removed by the user.
- Chrome Web Store submission is next.

## Build

```bash
npm run build:extension
```

The built extension is copied to:

```text
dist/extension/
```

## Manual install

1. Open Chrome.
2. Go to `chrome://extensions`.
3. Turn on Developer Mode.
4. Click Load unpacked.
5. Select the `extension/` folder, or select `dist/extension/` after running `npm run build:extension`.
6. Visit `youtube.com` or `x.com`.
7. FaithWall should show the Scripture gate first.
8. Click Lay the brick.
9. Chrome opens the site for the temporary access window.

## Settings

Click the FaithWall shield icon in Chrome to open settings.

You can:

- enable or disable the extension,
- edit interrupted domains,
- choose the access window.

Default interrupted domains:

- youtube.com
- x.com
- twitter.com
- facebook.com
- instagram.com
- reddit.com
- tiktok.com
- netflix.com
- twitch.tv

## Honest promise

When you type a blocked site in Chrome, you get Scripture first.

That is the prototype.
