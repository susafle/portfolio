#!/usr/bin/env python3
"""Refresh Google Scholar metrics (h-index + total citations) for the portfolio.

Source of truth: scholar-metrics.json (repo root). A copy is also written to
docs/scholar-metrics.json so the published site serves the new values without a
full re-render.

Strategy:
  1. If SERPAPI_KEY is set -> SerpAPI Google Scholar Author API (reliable).
  2. Otherwise -> best-effort scrape of the public profile (often blocked on CI).

If no valid numbers are obtained, the existing file is left untouched (the site
keeps the last known-good values, which can also be edited by hand).
"""

import datetime
import json
import os
import re
import sys
import urllib.request

AUTHOR_ID = "d0RZmGoAAAAJ"
ROOT_JSON = "scholar-metrics.json"
DOCS_JSON = os.path.join("docs", "scholar-metrics.json")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def via_serpapi(key):
    url = ("https://serpapi.com/search.json?engine=google_scholar_author"
           f"&author_id={AUTHOR_ID}&hl=en&api_key={key}")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=40) as r:
        data = json.load(r)
    table = data.get("cited_by", {}).get("table", [])
    citations = hindex = None
    for row in table:
        if "citations" in row:
            citations = row["citations"].get("all")
        if "h_index" in row:
            hindex = row["h_index"].get("all")
    return hindex, citations


def via_scrape():
    url = f"https://scholar.google.com/citations?user={AUTHOR_ID}&hl=en"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=40) as r:
        html = r.read().decode("utf-8", "ignore")
    # Order in the stats table: Citations(all, since), h-index(all, since), i10(all, since)
    nums = re.findall(r'gsc_rsb_std">(\d+)<', html)
    if len(nums) >= 3:
        return int(nums[2]), int(nums[0])  # (h-index all, citations all)
    return None, None


def main():
    key = os.environ.get("SERPAPI_KEY")
    hindex = citations = None
    try:
        if key:
            print("Fetching via SerpAPI...")
            hindex, citations = via_serpapi(key)
        else:
            print("No SERPAPI_KEY; attempting best-effort scrape...")
            hindex, citations = via_scrape()
    except Exception as exc:  # noqa: BLE001
        print(f"Fetch failed: {exc}")

    try:
        hindex = int(hindex)
        citations = int(citations)
    except (TypeError, ValueError):
        print("No valid metrics obtained; keeping existing file.")
        return 0

    if hindex <= 0 or citations <= 0:
        print("Non-positive metrics; keeping existing file.")
        return 0

    payload = {
        "hindex": hindex,
        "citations": citations,
        "updated": datetime.date.today().strftime("%Y-%m"),
    }
    text = json.dumps(payload, indent=2) + "\n"
    for path in (ROOT_JSON, DOCS_JSON):
        d = os.path.dirname(path)
        if d:
            os.makedirs(d, exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
    print(f"Updated metrics: {payload}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
