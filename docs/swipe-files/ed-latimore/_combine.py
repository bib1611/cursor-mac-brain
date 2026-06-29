#!/usr/bin/env python3
"""Combine the Ed Latimore corpus parts into one Ed-Latimore-Corpus-Combined.md.

Mirrors the Dakota-Corpus-Combined.md format:
  # <Title> Corpus
  Source: ...
  ---
  ## Source: <relpath>
  - **Source:** <url if known>
  - **Length:** <N> chars
  ## Body (verbatim, study/swipe)
  <verbatim file content>
"""
import json
import re
from pathlib import Path

ROOT = Path("/Users/adamjohnsson/Downloads/ed-latimore-corpus")
OUT = ROOT / "Ed-Latimore-Corpus-Combined.md"

# Section order: tweets first, then funnels (offers), newsletter (emails), blog (articles)
ORDER = ["tweets", "funnels", "newsletter", "blog"]

URL_RE = re.compile(r"https?://[^\s)>\]]+")


def first_url(text: str) -> str:
    m = URL_RE.search(text)
    return m.group(0) if m else ""


def section_files(sub: str):
    d = ROOT / sub
    if not d.is_dir():
        return []
    # .md only, skip private _NOTE etc kept (they are informative); sort stable
    return sorted([p for p in d.glob("*.md")])


def main():
    parts = []
    parts.append("# Ed Latimore (@EdLatimore) Corpus\n")
    parts.append(
        "Source: https://edlatimore.com + X @EdLatimore\n"
        f"Staged: {ROOT}\n"
    )

    counts = {}
    for sub in ORDER:
        files = section_files(sub)
        counts[sub] = len(files)
        for p in files:
            text = p.read_text(encoding="utf-8", errors="replace")
            rel = p.relative_to(ROOT).as_posix()
            url = first_url(text)
            parts.append("\n\n---\n")
            parts.append(f"\n## Source: {rel}\n")
            if url:
                parts.append(f"\n- **Source:** {url}")
            parts.append(f"\n- **Length:** {len(text)} chars\n")
            parts.append("\n## Body (verbatim, study/swipe)\n\n")
            parts.append(text.rstrip() + "\n")

    OUT.write_text("".join(parts), encoding="utf-8")

    # Build merged _archive_index.json from any sub-index files + scraped urls
    urls = []
    for idx_name in ["blog/_blog_index.json", "funnels/_funnels_index.json",
                     "newsletter/_newsletter_index.json"]:
        f = ROOT / idx_name
        if f.is_file():
            try:
                data = json.loads(f.read_text())
                if isinstance(data, list):
                    urls.extend(data)
            except Exception:
                pass
    # de-dupe preserve order
    seen = set()
    deduped = [u for u in urls if not (u in seen or seen.add(u))]
    (ROOT / "_archive_index.json").write_text(
        json.dumps(deduped, indent=2), encoding="utf-8")

    size = OUT.stat().st_size
    print(f"Wrote {OUT} ({size} bytes)")
    for sub in ORDER:
        print(f"  {sub}: {counts[sub]} files")
    print(f"  _archive_index.json: {len(deduped)} urls")


if __name__ == "__main__":
    main()
