"""Fetch security feeds, keep only network-device relevant items, enrich with KEV/EPSS.

Standard library only - no pip install needed for this stage.
"""
from __future__ import annotations

import json
import re
import ssl
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
UA = "netsec-digest/1.0 (+https://github.com/Omidznlp/Network-infrastructures-Cybersecurity-)"
CVE_RE = re.compile(r"CVE-\d{4}-\d{4,7}", re.I)
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")


@dataclass
class Item:
    title: str
    link: str
    summary: str
    source: str
    tier: str
    published: str                       # ISO-8601 UTC
    score: int = 0
    vendors: list = field(default_factory=list)
    categories: list = field(default_factory=list)
    cves: list = field(default_factory=list)
    kev: list = field(default_factory=list)          # CVEs on the CISA KEV list
    epss: dict = field(default_factory=dict)         # CVE -> probability
    urgency: list = field(default_factory=list)
    ai_related: bool = False
    tags: list = field(default_factory=list)


def log(msg: str) -> None:
    print(f"[collect] {msg}", file=sys.stderr)


BROWSER_UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def http_get(url: str, timeout: int = 25, agent: str | None = None) -> bytes:
    """Fetch a URL, retrying once with a browser User-Agent.

    Some publishers (cisa.gov's advisory feed among them) answer 403/406 to a
    non-browser agent when the request comes from a datacenter IP such as a
    GitHub Actions runner.
    """
    ctx = ssl.create_default_context()
    agents = [agent or UA]
    if agents[0] != BROWSER_UA:
        agents.append(BROWSER_UA)
    last: Exception | None = None
    for ua in agents:
        req = urllib.request.Request(url, headers={
            "User-Agent": ua,
            "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, application/json, */*",
            "Accept-Language": "en-US,en;q=0.9",
        })
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
                return resp.read()
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code not in (401, 403, 406, 429):
                raise
        except Exception as exc:
            last = exc
            raise
    raise last if last else RuntimeError("fetch failed")


def clean(text: str, limit: int = 900) -> str:
    text = TAG_RE.sub(" ", text or "")
    text = (text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
                .replace("&quot;", '"').replace("&#39;", "'").replace("&nbsp;", " "))
    text = WS_RE.sub(" ", text).strip()
    return text[:limit]


def parse_date(raw: str | None) -> datetime | None:
    if not raw:
        return None
    raw = raw.strip()
    try:
        dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except Exception:
        pass
    try:
        dt = parsedate_to_datetime(raw)
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except Exception:
        pass
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S.%fZ",
                "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            dt = datetime.strptime(raw.replace("Z", "+0000") if fmt.endswith("%z") else raw, fmt)
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
        except Exception:
            continue
    return None


def strip_ns(tag: str) -> str:
    return tag.split("}", 1)[-1]


def parse_feed(raw: bytes, source: str, tier: str) -> list[Item]:
    """Handle RSS 2.0, RDF and Atom without third-party parsers."""
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as exc:
        log(f"{source}: XML parse error ({exc})")
        return []

    entries = [e for e in root.iter() if strip_ns(e.tag) in ("item", "entry")]
    items: list[Item] = []
    for entry in entries:
        fields: dict[str, str] = {}
        link = ""
        for child in entry:
            name = strip_ns(child.tag)
            if name == "link":
                href = child.attrib.get("href")
                rel = child.attrib.get("rel", "alternate")
                if href and rel == "alternate":
                    link = href
                elif not href and (child.text or "").strip():
                    link = child.text.strip()
            else:
                fields.setdefault(name, "")
                fields[name] += " " + "".join(child.itertext())
        title = clean(fields.get("title", ""), 300)
        body = clean(fields.get("description") or fields.get("summary")
                     or fields.get("content") or fields.get("encoded") or "")
        published = parse_date(fields.get("published") or fields.get("pubDate")
                               or fields.get("updated") or fields.get("date"))
        if not title or not link:
            continue
        items.append(Item(
            title=title, link=link.strip(), summary=body, source=source, tier=tier,
            published=(published or datetime.now(timezone.utc)).astimezone(timezone.utc).isoformat(),
        ))
    return items


def score_item(item: Item, kw: dict) -> Item:
    blob = f" {item.title.lower()} {item.summary.lower()} "
    score = 0

    for vendor, spec in kw["vendors"].items():
        if any(term in blob for term in spec["terms"]):
            item.vendors.append(vendor)
            score += spec["weight"]

    for category, spec in kw["device_classes"].items():
        if any(term in blob for term in spec["terms"]):
            item.categories.append(category)
            score += spec["weight"]

    generic = kw["generic_terms"]
    if any(term in blob for term in generic["terms"]):
        score += generic["weight"]

    for term, weight in kw["urgency_terms"].items():
        if term in blob:
            item.urgency.append(term)
            score += weight

    ai = kw["ai_terms"]
    if any(term in blob for term in ai["terms"]):
        item.ai_related = True
        score += ai["weight"]

    if any(term in blob for term in kw["exclude_terms"]):
        score -= 10

    # Vendor PSIRT feeds are network-device sources by definition.
    if item.tier == "psirt":
        score += kw["min_score"]

    item.cves = sorted({c.upper() for c in CVE_RE.findall(f"{item.title} {item.summary}")})
    item.score = score
    return item


def load_kev(url: str) -> dict:
    try:
        data = json.loads(http_get(url, timeout=40))
    except Exception as exc:
        log(f"KEV fetch failed: {exc}")
        return {}
    out = {}
    for v in data.get("vulnerabilities", []):
        out[v.get("cveID", "").upper()] = {
            "vendor": v.get("vendorProject", ""),
            "product": v.get("product", ""),
            "name": v.get("vulnerabilityName", ""),
            "description": v.get("shortDescription", ""),
            "action": v.get("requiredAction", ""),
            "added": v.get("dateAdded", ""),
            "due": v.get("dueDate", ""),
            "ransomware": v.get("knownRansomwareCampaignUse", "Unknown"),
        }
    log(f"KEV entries: {len(out)}")
    return out



def kev_items(kev: dict, window_hours: int) -> list[Item]:
    """Turn freshly added KEV catalog entries into digest items.

    The KEV JSON is reachable where the CISA advisories RSS feed is not, and a new
    KEV entry is the single strongest signal this digest can carry: confirmed
    exploitation, plus the federally mandated remediation date.
    """
    cutoff = datetime.now(timezone.utc) - timedelta(hours=max(window_hours, 24))
    out: list[Item] = []
    for cve, meta in kev.items():
        added = parse_date(meta.get("added", ""))
        if not added or added < cutoff:
            continue
        product = f"{meta.get('vendor', '')} {meta.get('product', '')}".strip()
        summary = (f"{meta.get('name', '')}. {meta.get('description', '')} "
                   f"Required action: {meta.get('action', 'Apply mitigations per vendor instructions.')} "
                   f"Federal remediation due {meta.get('due', 'n/a')}. "
                   f"Known ransomware campaign use: {meta.get('ransomware', 'Unknown')}.")
        out.append(Item(
            title=f"CISA KEV addition: {product} - {cve}",
            link=f"https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext={cve}",
            summary=clean(summary),
            source="CISA KEV catalog",
            tier="gov",
            published=added.isoformat(),
        ))
    return out


def load_epss(cves: list[str], url: str) -> dict:
    if not cves:
        return {}
    scores: dict[str, float] = {}
    for i in range(0, len(cves), 50):
        chunk = ",".join(cves[i:i + 50])
        try:
            data = json.loads(http_get(f"{url}{chunk}", timeout=30))
            for row in data.get("data", []):
                scores[row["cve"].upper()] = float(row.get("epss", 0))
        except Exception as exc:
            log(f"EPSS fetch failed: {exc}")
            break
    return scores


def load_seen(path: Path) -> dict:
    if path.exists():
        try:
            return json.loads(path.read_text())
        except Exception:
            pass
    return {}


def prune_seen(seen: dict, days: int = 120) -> dict:
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    out = {}
    for key, ts in seen.items():
        dt = parse_date(ts)
        if dt and dt > cutoff:
            out[key] = ts
    return out


def dedupe_key(item: Item) -> str:
    link = re.sub(r"[?#].*$", "", item.link.lower().rstrip("/"))
    return link or re.sub(r"[^a-z0-9]+", "-", item.title.lower())[:120]


def collect(window_hours: int, include_seen: bool = False, persist: bool = True) -> dict:
    sources = json.loads((ROOT / "config" / "sources.json").read_text())
    kw = json.loads((ROOT / "config" / "keywords.json").read_text())
    seen_path = ROOT / "data" / "seen.json"
    seen = prune_seen(load_seen(seen_path))

    cutoff = datetime.now(timezone.utc) - timedelta(hours=window_hours)
    raw_items: list[Item] = []
    stats = {"feeds_ok": 0, "feeds_failed": 0, "raw": 0}

    for feed in sources["feeds"]:
        if not feed.get("enabled", True):
            continue
        try:
            body = http_get(feed["url"], agent=feed.get("user_agent"))
        except Exception as exc:
            stats["feeds_failed"] += 1
            log(f"{feed['name']}: fetch failed ({exc})")
            continue
        parsed = parse_feed(body, feed["name"], feed["tier"])
        stats["feeds_ok"] += 1
        stats["raw"] += len(parsed)
        raw_items.extend(parsed)
        log(f"{feed['name']}: {len(parsed)} items")

    enr = sources["enrichment"]
    kev = load_kev(enr["kev_url"]) if enr.get("enable_kev") else {}
    if kev:
        added = kev_items(kev, window_hours)
        log(f"CISA KEV catalog: {len(added)} newly added entries in window")
        raw_items.extend(added)

    fresh, skipped_old, skipped_seen = [], 0, 0
    run_keys: set[str] = set()
    for item in raw_items:
        dt = parse_date(item.published)
        if dt and dt < cutoff:
            skipped_old += 1
            continue
        key = dedupe_key(item)
        if key in run_keys:
            continue
        run_keys.add(key)
        if not include_seen and key in seen:
            skipped_seen += 1
            continue
        fresh.append(item)

    scored = [score_item(i, kw) for i in fresh]
    on_topic = [i for i in scored if i.vendors or i.categories or i.tier == "psirt"]
    log(f"dropped {len(scored) - len(on_topic)} items with no network-device or vendor match")
    relevant = [i for i in on_topic if i.score >= kw["min_score"]]

    all_cves = sorted({c for i in relevant for c in i.cves})
    epss = load_epss(all_cves, enr["epss_url"]) if enr.get("enable_epss") and all_cves else {}

    for item in relevant:
        item.kev = [c for c in item.cves if c in kev]
        item.epss = {c: epss[c] for c in item.cves if c in epss}
        if item.kev:
            item.score += 6
            item.tags.append("KEV")
        if any(v >= 0.5 for v in item.epss.values()):
            item.score += 2
            item.tags.append("high-EPSS")
        if item.ai_related:
            item.tags.append("AI")
        if item.tier == "psirt":
            item.tags.append("vendor-advisory")

    relevant.sort(key=lambda i: (i.score, i.published), reverse=True)
    digest = relevant

    now = datetime.now(timezone.utc)
    if persist:
        for item in relevant:
            seen[dedupe_key(item)] = now.isoformat()
        seen_path.parent.mkdir(parents=True, exist_ok=True)
        seen_path.write_text(json.dumps(seen, indent=0, sort_keys=True))

    stats.update({"fresh": len(fresh), "on_topic": len(on_topic), "digest": len(digest),
                  "skipped_old": skipped_old, "skipped_seen": skipped_seen})
    log(json.dumps(stats))

    return {
        "generated_at": now.isoformat(),
        "window_hours": window_hours,
        "stats": stats,
        "kev_context": {c: kev[c] for c in all_cves if c in kev},
        "items": [asdict(i) for i in digest],
    }


if __name__ == "__main__":
    hours = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    out = collect(hours)
    print(json.dumps(out, indent=2))
