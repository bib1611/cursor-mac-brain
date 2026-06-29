# Fix: CDP browser control restored (Chrome + Comet)

Date: 2026-06-15 0845 CDT

## Root cause (the whole thing)
Earlier sessions claimed Comet "strips the debug flag" and that a Chrome
relaunch with --remote-allow-origins (logout risk) was required. Both wrong.

Real cause: the websocket client auto-injected an `Origin` header. Chrome 111+
rejects DevTools websockets whose Origin isn't allow-listed → 403 Forbidden.
A *missing* Origin is always allowed. Fix = `suppress_origin=True`. No relaunch,
no logout, no flag.

## Verified live state
- Comet (PID 17137) serves CDP on IPv6 [::1]:9222 — 44 tabs, all real sessions
  (ClickFunnels, Stripe acct_1PeIdjLN6IypHVMV, Proton, deadhidden.org store,
  Substack). Eval confirmed working into the CF tab.
- Chrome (PID 714) holds IPv4 127.0.0.1:9222 but returns 404 on /json — not
  serving a usable DevTools endpoint; no real sessions in it. Comet is the
  operating surface.

## Deliverable
`/Users/adamjohnsson/.agents/bin/cdp` — auto-detects Comet(IPv6)+Chrome(IPv4),
suppresses Origin, runs Runtime.evaluate.
  cdp list
  cdp eval 'JS' <url-substr>
  cdp eval - <url-substr>   # JS from stdin

## Not done (no approval / out of scope)
- No CF page built, no Stripe/product change, no publish. Control only.
