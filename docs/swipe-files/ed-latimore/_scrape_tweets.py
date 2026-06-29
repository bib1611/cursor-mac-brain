#!/usr/bin/env python3
"""Scrape @EdLatimore's posts via Chrome CDP by intercepting X's GraphQL
timeline responses (UserTweets / UserTweetsAndReplies). Other users' tweets
DO include views.count in these payloads, so we get impressions + full metrics
without the X API. Opens a fresh tab, scrolls to paginate, closes the tab.

Outputs (Dakota format):
  tweets/_tweets_raw.json   - full objects
  tweets/_tweets_top.md     - sorted by views then likes
"""
import json
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from websocket import create_connection
from websocket._exceptions import WebSocketTimeoutException

CDP = "http://127.0.0.1:9333"
HANDLE = "EdLatimore"
ROOT = Path("/Users/adamjohnsson/Downloads/ed-latimore-corpus")
TWEETS = ROOT / "tweets"
MAX_SCROLLS = 90
SCROLL_PAUSE = 2.0
NO_GROWTH_STOP = 10  # stop after this many consecutive scrolls with no new tweets


def log(msg):
    print(msg, flush=True)


def http(method, path):
    req = urllib.request.Request(CDP + path, method=method)
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.loads(r.read().decode())


def new_tab():
    # PUT is required on modern Chrome for /json/new
    return http("PUT", "/json/new?about:blank")


def close_tab(tab_id):
    try:
        urllib.request.urlopen(CDP + f"/json/close/{tab_id}", timeout=10).read()
    except Exception as e:
        log(f"WARN close tab: {e}")


class CDPClient:
    def __init__(self, ws_url):
        self.ws = create_connection(ws_url, max_size=None, suppress_origin=True)
        self.ws.settimeout(1.0)
        self._id = 0
        self.match_reqs = {}     # requestId -> url (matched GraphQL)
        self.body_pending = {}   # cmd id -> requestId
        self.bodies = {}         # requestId -> raw body text
        self.cmd_results = {}    # cmd id -> result

    def send(self, method, params=None):
        self._id += 1
        self.ws.send(json.dumps({"id": self._id, "method": method,
                                 "params": params or {}}))
        return self._id

    def pump(self, seconds):
        end = time.time() + seconds
        while time.time() < end:
            try:
                raw = self.ws.recv()
            except WebSocketTimeoutException:
                continue
            except Exception as e:
                log(f"WARN recv: {e}")
                break
            if not raw:
                continue
            try:
                msg = json.loads(raw)
            except Exception:
                continue
            if "method" in msg:
                self._on_event(msg["method"], msg.get("params", {}))
            elif "id" in msg:
                self._on_reply(msg["id"], msg.get("result", {}))

    def _on_event(self, method, params):
        if method == "Network.responseReceived":
            url = params.get("response", {}).get("url", "")
            if "UserTweets" in url or "UserTweetsAndReplies" in url:
                self.match_reqs[params["requestId"]] = url
        elif method == "Network.loadingFinished":
            rid = params.get("requestId")
            if rid in self.match_reqs and rid not in self.bodies:
                cid = self.send("Network.getResponseBody", {"requestId": rid})
                self.body_pending[cid] = rid

    def _on_reply(self, cid, result):
        if cid in self.body_pending:
            rid = self.body_pending.pop(cid)
            body = result.get("body", "")
            if result.get("base64Encoded"):
                import base64
                body = base64.b64decode(body).decode("utf-8", "replace")
            self.bodies[rid] = body
        else:
            self.cmd_results[cid] = result

    def evaluate(self, expr):
        cid = self.send("Runtime.evaluate",
                        {"expression": expr, "returnByValue": True})
        end = time.time() + 5
        while time.time() < end:
            self.pump(0.3)
            if cid in self.cmd_results:
                return self.cmd_results.pop(cid).get("result", {}).get("value")
        return None


def extract_tweets(obj, found):
    if isinstance(obj, dict):
        legacy = obj.get("legacy")
        if isinstance(legacy, dict) and "full_text" in legacy and legacy.get("id_str"):
            text = legacy.get("full_text") or ""
            note = obj.get("note_tweet")
            if isinstance(note, dict):
                try:
                    nt = note["note_tweet_results"]["result"]["text"]
                    if nt and len(nt) >= len(text):
                        text = nt
                except Exception:
                    pass
            screen = None
            core = obj.get("core", {})
            for path in (
                lambda: core["user_results"]["result"]["legacy"]["screen_name"],
                lambda: core["user_results"]["result"]["core"]["screen_name"],
            ):
                try:
                    screen = path()
                    if screen:
                        break
                except Exception:
                    pass
            views = None
            v = obj.get("views")
            if isinstance(v, dict) and v.get("count") is not None:
                try:
                    views = int(v["count"])
                except Exception:
                    views = None
            found[legacy["id_str"]] = {
                "id": legacy["id_str"],
                "screen_name": screen,
                "created_at": legacy.get("created_at"),
                "full_text": text,
                "lang": legacy.get("lang"),
                "favorite_count": legacy.get("favorite_count"),
                "retweet_count": legacy.get("retweet_count"),
                "reply_count": legacy.get("reply_count"),
                "quote_count": legacy.get("quote_count"),
                "bookmark_count": legacy.get("bookmark_count"),
                "views": views,
                "is_retweet": "retweeted_status_result" in legacy,
            }
        for val in obj.values():
            extract_tweets(val, found)
    elif isinstance(obj, list):
        for it in obj:
            extract_tweets(it, found)


def parse_date(created_at):
    if not created_at:
        return ""
    try:
        dt = datetime.strptime(created_at, "%a %b %d %H:%M:%S %z %Y")
        return dt.astimezone(timezone.utc).strftime("%Y-%m-%d")
    except Exception:
        return ""


def harvest(client):
    found = {}
    for rid, body in list(client.bodies.items()):
        try:
            data = json.loads(body)
        except Exception:
            continue
        extract_tweets(data, found)
    return found


def main():
    tab = new_tab()
    tab_id = tab["id"]
    ws_url = tab["webSocketDebuggerUrl"]
    log(f"PROGRESS opened tab {tab_id}")
    client = CDPClient(ws_url)
    try:
        client.send("Network.enable")
        client.send("Page.enable")
        client.send("Runtime.enable")
        # Keep this background tab rendered + "focused" so X's IntersectionObserver
        # fires and the timeline paginates on scroll (otherwise it freezes at page 1).
        client.send("Emulation.setFocusEmulationEnabled", {"enabled": True})
        client.send("Emulation.setDeviceMetricsOverride",
                    {"width": 1280, "height": 2200, "deviceScaleFactor": 1,
                     "mobile": False, "screenWidth": 1280, "screenHeight": 2200})
        client.pump(1.0)
        client.send("Page.navigate", {"url": f"https://x.com/{HANDLE}"})
        log("PROGRESS navigating to profile, waiting for first paint")
        client.pump(7.0)
        client.send("Page.setWebLifecycleState", {"state": "active"})

        all_found = {}
        no_growth = 0
        last_total = 0
        for i in range(1, MAX_SCROLLS + 1):
            client.evaluate(
                "window.scrollTo(0, document.documentElement.scrollHeight)")
            client.pump(SCROLL_PAUSE)
            # If a page seems stalled, jiggle up then back to bottom to
            # re-trigger the infinite-scroll loader.
            if no_growth and no_growth % 3 == 0:
                client.evaluate("window.scrollTo(0, "
                                "document.documentElement.scrollHeight*0.6)")
                client.pump(0.6)
                client.evaluate("window.scrollTo(0, "
                                "document.documentElement.scrollHeight)")
                client.pump(SCROLL_PAUSE)
            cur = harvest(client)
            all_found.update(cur)
            ed = [t for t in all_found.values()
                  if (t["screen_name"] or "").lower() == HANDLE.lower()
                  and not t["is_retweet"]]
            total = len(ed)
            log(f"PROGRESS scroll={i} bodies={len(client.bodies)} "
                f"unique_all={len(all_found)} ed_posts={total}")
            if total <= last_total:
                no_growth += 1
            else:
                no_growth = 0
            last_total = total
            if no_growth >= NO_GROWTH_STOP:
                log(f"PROGRESS no growth for {NO_GROWTH_STOP} scrolls, stopping")
                break

        # Final harvest
        all_found.update(harvest(client))
        ed = [t for t in all_found.values()
              if (t["screen_name"] or "").lower() == HANDLE.lower()
              and not t["is_retweet"]]
        ed.sort(key=lambda t: ((t["views"] or 0), (t["favorite_count"] or 0)),
                reverse=True)

        TWEETS.mkdir(parents=True, exist_ok=True)
        (TWEETS / "_tweets_raw.json").write_text(
            json.dumps(ed, indent=2, ensure_ascii=False), encoding="utf-8")

        lines = [
            "# Ed Latimore (@EdLatimore) — tweet capture",
            "",
            f"- Total captured: {len(ed)}",
            f"- Captured: {datetime.now().strftime('%Y-%m-%d %H:%M')} "
            "via Chrome CDP (x.com/EdLatimore GraphQL timeline)",
            "",
            "## Sorted by impressions (views from live timeline; "
            "sorted by views then likes)",
            "",
        ]
        for t in ed:
            d = parse_date(t["created_at"])
            txt = " ".join((t["full_text"] or "").split())
            lines.append(
                f"- [{d}] {t['views'] if t['views'] is not None else 0} views / "
                f"{t['favorite_count'] or 0} likes / {t['retweet_count'] or 0} RT / "
                f"{t['reply_count'] or 0} replies — {txt}")
        (TWEETS / "_tweets_top.md").write_text("\n".join(lines) + "\n",
                                               encoding="utf-8")
        log(f"DONE ed_posts={len(ed)} unique_all={len(all_found)} "
            f"bodies={len(client.bodies)}")
    except Exception as e:
        import traceback
        log("ERROR " + repr(e))
        traceback.print_exc()
    finally:
        try:
            client.ws.close()
        except Exception:
            pass
        close_tab(tab_id)
        log("PROGRESS closed tab")


if __name__ == "__main__":
    main()
