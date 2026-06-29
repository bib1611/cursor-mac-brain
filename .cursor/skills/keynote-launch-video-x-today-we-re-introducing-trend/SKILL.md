---
name: Keynote Launch Video (X "Today we're introducing" trend)
description: Use when Adam wants a viral-style product LAUNCH HYPE VIDEO for X
  in the deadpan big-lab keynote format ("Today, we're introducing ___") for a
  Biblical Man / Dead Hidden product. Covers the trend formula, the HTML-frames
  + ffmpeg render pipeline that actually works on his Mac (Remotion/Chromium is
  blocked in the sandbox), the brand visual system, the music fallback chain,
  and how to post the video to X.
autoInject:
  keywords:
    - launch video
    - hype video
    - keynote video
    - today we're introducing
    - product video
    - video ad
    - launch trailer
---
# Keynote Launch Video (X "Today we're introducing" trend)

Produce a premium, deadpan "big-lab keynote" launch video (the viral X trend) for a Biblical Man / Dead Hidden product, then post it. Pair with the **Biblical Man / Dead Hidden Voice** and **Matched-Pair Launch Workflow** skills for copy.

## 1. The viral trend formula (study source: high bookmark/like ratio = save-worthy)
Format that goes viral: small product launch dressed in Apple/OpenAI/Anthropic keynote clothes.
1. **Keynote opener:** "Today, we're introducing ___." Gravity is the joke and the hook.
2. **One plain mechanism line:** what it does in dead-simple words. No adjectives.
3. **Awe button:** short reaction line ("What a time to be alive." / "This is unbelievable."). For Adam, use a sacred-weight closer, not techno-awe.
4. **A short slick video is the actual view engine.** Copy frames it; video carries it. On X, video autoplays MUTED, so it must read with sound off.
5. **Link rides in a self-reply, never the hook.** Keeps the main tweet clean and lifts reach.
6. Make it feel like an event. Reference examples: @fin465 "Claude for Sales", @jock_ferguson "Claude for Content", @hyojun_at "Aside" launch (bulleted-feature variant), @alephneuro "first look" cold open.

## 2. Voice + hard guardrails (non-negotiable)
- No em dashes, no hashtags. Say "the Bible," not "KJV"/"King James" in copy.
- **No dollar figures / revenue / subscriber counts in public copy.** Convey urgency without numbers ("Intro price runs through Wednesday, then it steps up").
- Women-inclusive (BM audience is ~60% women). Generic "you," not male-only.
- One ask per piece. The video's ask is "out now"; the link goes in the self-reply.

## 3. Render pipeline — CRITICAL
**Remotion exists** (`~/code/OpenMontage/remotion-composer`, node v26, ffmpeg, the data-driven `Explainer` composition), **but Chromium cannot launch from the Aside Bash sandbox** (`mach_port_rendezvous ... Permission denied`). Remotion render FAILS from here even with a valid Chrome. **Do not fight it.** Use this instead:

**HTML frames (via Aside browser) + ffmpeg.** ffmpeg (`/opt/homebrew/bin/ffmpeg`, v8) runs fine in the sandbox; only Chromium launch is blocked. The Aside `page` (Playwright) renders HTML perfectly.

Steps:
1. Write one HTML file per scene. Wrap content in `#stage` and set `html,body{width:1920px;height:1080px;margin:0;overflow:hidden}`. Cap `.headline{max-width:~1480px}` so long lines wrap instead of clipping.
2. Render each via the Aside browser: `openTab('file://.../scene.html')`, `await page.evaluate(()=>document.fonts.ready)`, `await page.screenshot({fullPage:true})` -> save PNG. **Use fullPage** — the `Emulation.setDeviceMetricsOverride` device-metrics path is unreliable here (viewport stays 1440x900); fullPage on a 1920x1080-sized body gives a true 1920x1080 PNG. Verify with `file frame.png`.
3. Per-scene Ken Burns clip: `ffmpeg -loop 1 -i s.png -t DUR -r 30 -filter_complex "[0:v]scale=3200:1800:flags=lanczos,zoompan=z='min(zoom+0.00035,1.045)':d=DUR*30:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=30,format=yuv420p,setsar=1[v]" -map "[v]" -c:v libx264 -crf 18 c.mp4`. Scale up first to kill zoompan jitter. Text scenes zoom cap ~1.045; cover ~1.09. Add `fade=t=in:st=0:d=0.6` on clip 1, `fade=t=out:st=DUR-0.8:d=0.8` on the last.
4. Crossfade-chain with `xfade=transition=fade:duration=0.6:offset=Ok`. Offset_k = (sum of durations so far) - 0.6*k. Output 1920x1080 30fps H.264 `-movflags +faststart`.

## 4. Brand visual system (match the product cover)
- Background: `radial-gradient(ellipse 90% 70% at 50% 38%, #16223b 0%, #0b1220 56%, #070b14 100%)`.
- Serif headlines: **Cormorant Garamond** 500-700, cream `#F4ECD8`. Italic for the opener and the closer.
- Eyebrow / small caps: **Inter** 600, letter-spacing .36em, gold `#C9A24A` ("Dead Hidden · The Biblical Man").
- Accent gold `#E0C074` for the product name / "2.0" / closer. Thin gold frame border (`inset:46px`, `1px rgba(201,162,74,.28)`) + center vignette.
- Always grab the live product cover (Gumroad og:image) and Ken-Burns it as the reveal scene so the video and cover feel native.

## 5. Scene template (~19s, 7 beats)
Intro "Today, we're introducing" (2.6s) -> product name + "2.0" (3.3s) -> tension line ("Open to the chapter that made you quit.") (3s) -> payoff ("Read it once and actually understand it.") (3s) -> differentiator ("No degree, no middleman between you and the page.") (3s) -> **cover reveal** Ken Burns (4.2s) -> closer ("The Bible, made plain." + "Out now") (3.6s, fade to black).

## 6. Music
- Preferred: **ElevenLabs Music API** (`music` skill, `POST https://api.elevenlabs.io/v1/music`). As of Jun 2026 it returns 401 payment_issue (failed invoice) — check first.
- The **FAL_KEY and SUNO_API_KEY in OpenMontage `.env` are placeholder text, not real keys** (FAL stable-audio returns 401). OPENAI/ELEVENLABS keys are real.
- Fallback: procedural ffmpeg ambient bed (soft octave+fifth sine drones + airy pink-noise swell + `aecho` reverb, mixed low, `afade` in/out). NOTE: you cannot hear-test it. Since X autoplays muted, **shipping the silent master is the safe default**; add a verified score later.
- Mux: `ffmpeg -i silent.mp4 -i bed.wav -c:v copy -c:a aac -b:a 192k -shortest out.mp4`. Save both silent + scored to `./artifacts/`.

## 7. Posting to X
- Confirm account with `twitter.getMe()` — must be **@Biblicalman** (The Biblical Man). Dead Hidden is a separate login.
- **The `twitter` global has NO media-upload method.** `twitter.tweet({mediaIds})` exists but you cannot mint a mediaId. So post the VIDEO via the X web composer: open `https://x.com/compose/post`, `page.locator('input[type=file]').setInputFiles(mp4Path)`, wait for the upload/processing bar to finish, type the hook, click Post.
- Then post the **link self-reply via API**: find the new tweet id with `twitter.getUserTweets('Biblicalman',{count:3})` and `twitter.reply(id, replyText)`.
- Final-confirm mode: always `request_action_confirmation` (x-tweet-draft) before posting. Optimal Friday slots (Central): 9-11 AM morning peak; afternoon tapers. Post when Adam is online to engage early replies.
