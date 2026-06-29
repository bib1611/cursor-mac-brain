---
name: Jarvis / Chorus Content Pipeline
description: Use when coordinating with Adam's Jarvis agent or the Chorus QC
  loop for drafting, saving, critiquing, or revising Biblical Man / Dead Hidden
  content. Trigger when Adam references Jarvis, Chorus, the Mac Mini OUTPUTS
  folder, draft critique, or the verse-text SMS product.
autoInject:
  keywords:
    - Jarvis
    - Chorus
    - OUTPUTS
    - Mac Mini
    - verse-text
    - Linq
    - Hermes
    - draft critique
    - money pulse
---
# Jarvis / Chorus Content Pipeline

How Adam's content moves from draft to QC to publish. Pair with the Voice and Matched-Pair Launch skills.

## The pipeline
1. **Jarvis drafts** posts and saves to `~/cowork/Claude-Cowork/OUTPUTS/` on the Mac Mini. File naming: `YYYYMMDD_slug.md`.
2. **Chorus QC** — Adam runs drafts through Chorus (chorus.com, by Riley Brown) for quality-control critique.
3. **Revision** — the critique goes back to Jarvis for revision. Stated goal: Jarvis eventually matches or exceeds Chorus. When I produce drafts, pre-empt likely Chorus notes by running the hostile-editor self-critique loop first.

## What Jarvis is
- Adam's personal Claude-powered agent over **Linq** iMessage, running on his Mac Mini ("Claude Tag for iMessage"). Stack includes a Hermes Agent, an async rip pipeline (yt-dlp + whisper/MLX), and OpenMontage (image-based video gen).
- **Proactive watcher** (`jarvis_watch.py` + LaunchAgent every 30 min): disk <6GB, core services down, new Stripe sale, climbing tweet, morning brief.
- **Daily money pulse** at 9:39 AM: X revenue, Stripe sales, top tweet, disk. **Do NOT duplicate this in any routine I suggest.**

## Verse-text product (7-day devotional SMS beta)
- Lives in `~/.deadhidden-os/verse-text/`: texts.md (7 verses; Day 7 = $5/mo offer), optin.py, broadcast.py, config.json.
- Loop: user texts VERSE -> captured + welcomed -> 1 verse/morning x7 -> Day 7 $5/mo Stripe.
- $5/mo Stripe link is LIVE (phone collection on), on the **Biblical Man** Stripe account.
- Open items historically: dedicated Linq number (ask Josh, Linq Partner Success Manager), fresh ElevenLabs key (was 401/stale). Confirm current status with Adam before acting.

## Linq Partner API integration (two-way iMessage bridge)
Aside can both READ and SEND over Adam's Linq harness. Base: `https://api.linqapp.com/api/partner/v3`, auth `Authorization: Bearer {token}`.

### Setup each session (secrets never stored in memory)
- Token comes from the Linq dashboard "Show token" button. Hold it in a REPL global only.
- `from` must be a Linq number assigned to Adam's account (the Jarvis line). Jarvis<->Adam chat ID (last known): `6288ab94-229c-4252-820e-3e13299575c6` (re-confirm; it can rotate).
- Phone numbers must be E.164 (`+12025550123`), no spaces/dashes.

### Endpoints
- **Read thread:** `GET /chats/{chatId}/messages?limit=N`
- **Send to existing chat:** `POST /chats/{chatId}/messages` body `{ "message": { "parts": [{ "type":"text", "value":"..." }] } }`
- **Threaded reply:** add `"reply_to": { "message_id": "...", "part_index": 0 }` to the message.
- **Rich link preview:** a `link` part must be the ONLY part in its message.
- **Start a new chat:** `POST /chats` `{ from, to:[...], message:{parts:[...]} }`. The FIRST outbound message must contain NO links/URLs (rejected); send a link as a follow-up.
- Also supports: media parts (url or attachment_id), reactions/tapbacks, iMessage effects, text decorations, typing indicators, edit (5x/15min, iMessage), delete (record-only, does not unsend).
- Limits: 100 parts/msg, text 10,000 chars, link URL 2,048 chars, no consecutive text parts.
- Idempotency: put `"idempotency_key"` INSIDE the `message` object (not an HTTP header) to make retries safe.
- Webhooks deliver real-time events (incoming `message.received`, delivery, read, reactions, `message.edited`). Dashboard Delivery Logs show only event type/status/duration, no body.

### Reusable REPL client (paste once per session, then call)
```js
globalThis.LINQ_TOKEN = null; globalThis.LINQ_FROM = null;
globalThis.LINQ_CHAT = "6288ab94-229c-4252-820e-3e13299575c6";
const B = "https://api.linqapp.com/api/partner/v3";
async function lf(p, i = {}) {
  const r = await fetch(B + p, { ...i, headers: { Authorization: `Bearer ${LINQ_TOKEN}`, "Content-Type": "application/json", ...(i.headers||{}) } });
  const t = await r.text(); let b; try { b = JSON.parse(t); } catch { b = t; }
  return { ok: r.ok, status: r.status, body: b };
}
globalThis.linq = {
  listMessages: (n=20, c=LINQ_CHAT) => lf(`/chats/${c}/messages?limit=${n}`),
  send: (text, {chatId=LINQ_CHAT, mediaUrls=[], idempotencyKey}={}) => {
    const parts=[{type:"text",value:text}]; for(const u of mediaUrls) parts.push({type:"media",url:u});
    const m={parts}; if(idempotencyKey) m.idempotency_key=idempotencyKey;
    return lf(`/chats/${chatId}/messages`,{method:"POST",body:JSON.stringify({message:m})}); },
  sendLink: (url, {chatId=LINQ_CHAT}={}) => lf(`/chats/${chatId}/messages`,{method:"POST",body:JSON.stringify({message:{parts:[{type:"link",value:url}]}})}),
  reply: (text, messageId, {chatId=LINQ_CHAT, partIndex=0}={}) => lf(`/chats/${chatId}/messages`,{method:"POST",body:JSON.stringify({message:{parts:[{type:"text",value:text}],reply_to:{message_id:messageId,part_index:partIndex}}})}),
  startChat: (to, text, {from=LINQ_FROM}={}) => lf(`/chats`,{method:"POST",body:JSON.stringify({from,to:Array.isArray(to)?to:[to],message:{parts:[{type:"text",value:text}]}})}),
};
```

### What to use it for
- Text Adam a finished-task summary or a draft for approval straight to iMessage.
- Read recent thread messages to pick up commands/context Adam left for Jarvis.
- Hand off: drop a draft link or file into the thread so Jarvis/Adam can pick it up.
- Event-driven: pair a Linq webhook (`message.received`) with an Aside event routine to wake on Adam's reply instead of polling.

### Guardrail (hard)
- Sending an iMessage is an externally visible action. Under final-confirm mode, DRAFT the exact message text and recipient/chat, get Adam's confirmation, THEN send. Never auto-send.
- Always set an `idempotency_key` on sends to avoid duplicates on retry.
- Never store the token, `from` number, or any key in memory.

## Guardrails
- Secrets (Stripe/Linq/API keys) live in the session/Mac env, never in memory by design.
- Publishing/sending is externally visible: draft and confirm with Adam first.
