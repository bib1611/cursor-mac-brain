#!/usr/bin/env python3
"""Lint brain/ note frontmatter against SCHEMA.md.

Enforces the frontmatter schema (SCHEMA §3), the category taxonomy (§5), the
controlled tag vocabulary (§6), and the naming convention (§7). Exit code is
non-zero if any note has an error, so this can gate a release.

Usage:
    python3 pipeline/lint.py            # lint brain/, human report
    python3 pipeline/lint.py --json     # machine-readable findings
    python3 pipeline/lint.py path ...   # lint specific files/dirs
"""
import argparse
import datetime as dt
import glob
import json
import os
import sys

import yaml

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BRAIN = os.path.join(BASE, "brain")

# SCHEMA §3 — required frontmatter keys.
REQUIRED = ["title", "category", "tags", "source_url", "source_drive_id", "status", "updated_at"]

# SCHEMA §5 — the twelve categories (folder == category).
CATEGORIES = {
    "x-algorithm", "x-craft", "x-growth", "content-creation", "content-strategy",
    "consistency-systems", "offers", "email", "book-launch", "substack",
    "personas", "meta-frameworks",
}

# SCHEMA §6 — controlled tag vocabulary.
TAGS = {
    # Mechanics
    "hook", "thread-structure", "reply-strategy", "cta", "subject-line",
    "offer-stack", "pricing", "lead-magnet", "auto-dm", "posting-cadence",
    "reach", "engagement-bait", "repurposing",
    # Outcomes
    "growth", "monetization", "retention", "authority",
    # Format
    "swipe", "worksheet", "framework", "case-study", "checklist",
}

# SCHEMA §3 — status lifecycle + optional enumerations.
STATUSES = {"raw", "distilled", "folded", "deprecated"}
PLATFORMS = {"x", "substack", "email", "book", "cross"}
FUNNEL_STAGES = {"awareness", "engagement", "capture", "offer", "retention"}
CONFIDENCE = {"high", "medium", "low"}


def split_frontmatter(text):
    """Return (frontmatter_dict_or_None, error_str_or_None)."""
    if not text.startswith("---"):
        return None, "no frontmatter block (file must open with '---')"
    parts = text.split("\n---", 1)
    if len(parts) < 2:
        return None, "frontmatter block is not closed with '---'"
    raw = parts[0][len("---"):]
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as e:
        return None, f"invalid YAML: {e}"
    if not isinstance(data, dict):
        return None, "frontmatter did not parse to a mapping"
    return data, None


def lint_file(path):
    """Return (errors, warnings) lists of strings for one note."""
    errors, warnings = [], []
    with open(path) as f:
        text = f.read()

    fm, err = split_frontmatter(text)
    if err:
        return [err], warnings

    # Required keys present (never omit, even if empty per §3).
    for key in REQUIRED:
        if key not in fm:
            errors.append(f"missing required field: {key}")

    # title
    title = fm.get("title")
    if "title" in fm:
        if not isinstance(title, str) or not title.strip():
            errors.append("title must be a non-empty string")
        elif title.lstrip().startswith("#"):
            errors.append("title must not start with '#' (§3)")

    # category — one of §5, and must match the folder it lives in.
    category = fm.get("category")
    folder = os.path.basename(os.path.dirname(path))
    if "category" in fm:
        if category not in CATEGORIES:
            errors.append(f"category '{category}' not in §5 taxonomy")
        elif folder in CATEGORIES and category != folder:
            errors.append(f"category '{category}' does not match folder '{folder}' (§5)")

    # tags — list, lowercase, from §6 only.
    tags = fm.get("tags")
    if "tags" in fm:
        if not isinstance(tags, list):
            errors.append("tags must be a list")
        else:
            for t in tags:
                if not isinstance(t, str):
                    errors.append(f"tag {t!r} is not a string")
                    continue
                if t != t.lower():
                    errors.append(f"tag '{t}' must be lowercase (§6)")
                if t.lower() not in TAGS:
                    errors.append(f"tag '{t}' not in §6 controlled vocabulary")
            if not tags:
                warnings.append("tags list is empty")

    # source_url — key required (checked above); empty string allowed.
    if "source_url" in fm and not isinstance(fm["source_url"], str):
        errors.append("source_url must be a string ('' if none)")

    # source_drive_id — required, should be non-empty.
    sdi = fm.get("source_drive_id")
    if "source_drive_id" in fm:
        if not isinstance(sdi, str):
            errors.append("source_drive_id must be a string")
        elif not sdi.strip():
            warnings.append("source_drive_id is empty")

    # status — lifecycle enum.
    status = fm.get("status")
    if "status" in fm and status not in STATUSES:
        errors.append(f"status '{status}' not in lifecycle {sorted(STATUSES)}")

    # updated_at — ISO date.
    ua = fm.get("updated_at")
    if "updated_at" in fm:
        ok = False
        if isinstance(ua, dt.date):
            ok = True
        elif isinstance(ua, str):
            try:
                dt.date.fromisoformat(ua)
                ok = True
            except ValueError:
                ok = False
        if not ok:
            errors.append(f"updated_at '{ua}' is not an ISO date (YYYY-MM-DD)")

    # --- Optional fields: validate only when present. ---
    if "platform" in fm:
        pf = fm["platform"]
        if not isinstance(pf, list):
            errors.append("platform must be a list")
        else:
            for v in pf:
                if v not in PLATFORMS:
                    errors.append(f"platform '{v}' not in {sorted(PLATFORMS)}")

    if "funnel_stage" in fm:
        fs = fm["funnel_stage"]
        if not isinstance(fs, list):
            errors.append("funnel_stage must be a list")
        else:
            for v in fs:
                if v not in FUNNEL_STAGES:
                    errors.append(f"funnel_stage '{v}' not in {sorted(FUNNEL_STAGES)}")

    if "confidence" in fm and fm["confidence"] not in CONFIDENCE:
        errors.append(f"confidence '{fm['confidence']}' not in {sorted(CONFIDENCE)}")

    if "folded_into_master" in fm and not isinstance(fm["folded_into_master"], bool):
        errors.append("folded_into_master must be a boolean")

    if "id" in fm:
        _id = fm["id"]
        if not isinstance(_id, str) or not _id.startswith(f"{category}-"):
            errors.append(f"id '{_id}' should start with category prefix '{category}-' (§7)")

    # folded status implies folded_into_master true.
    if status == "folded" and fm.get("folded_into_master") is not True:
        warnings.append("status 'folded' but folded_into_master is not true")

    # --- Filename naming convention (§7). ---
    name = os.path.basename(path)
    if not name.endswith(".md"):
        errors.append("file does not end in .md")
    else:
        stem = name[:-3]
        if stem != stem.lower():
            errors.append(f"filename '{name}' must be lowercase (§7)")
        if any(c not in "abcdefghijklmnopqrstuvwxyz0123456789-" for c in stem):
            errors.append(f"filename '{name}' must be kebab-case [a-z0-9-] (§7)")
        if "--" not in stem:
            warnings.append(f"filename '{name}' has no '--' instructor/topic separator (§7)")

    return errors, warnings


def collect(paths):
    files = []
    for p in paths:
        if os.path.isdir(p):
            files.extend(sorted(glob.glob(os.path.join(p, "**", "*.md"), recursive=True)))
        elif p.endswith(".md"):
            files.append(p)
    return files


def main():
    ap = argparse.ArgumentParser(description="Lint brain/ note frontmatter against SCHEMA.md")
    ap.add_argument("paths", nargs="*", default=[BRAIN],
                    help="files or dirs to lint (default: brain/)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    paths = args.paths or [BRAIN]
    files = collect(paths)

    results = {}
    n_err = n_warn = 0
    for path in files:
        errs, warns = lint_file(path)
        if errs or warns:
            results[path] = {"errors": errs, "warnings": warns}
        n_err += len(errs)
        n_warn += len(warns)

    if args.json:
        print(json.dumps({
            "files": len(files), "errors": n_err, "warnings": n_warn,
            "findings": {os.path.relpath(p, BASE): v for p, v in results.items()},
        }, indent=2))
    else:
        for path in files:
            v = results.get(path)
            if not v:
                continue
            rel = os.path.relpath(path, BASE)
            for e in v["errors"]:
                print(f"ERROR  {rel}: {e}")
            for w in v["warnings"]:
                print(f"WARN   {rel}: {w}")
        clean = len(files) - len(results)
        print(f"\nlinted {len(files)} notes — {clean} clean, "
              f"{n_err} errors, {n_warn} warnings")

    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
