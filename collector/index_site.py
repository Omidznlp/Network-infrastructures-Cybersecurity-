"""Build the browse-by-device-type and browse-by-vendor pages from every published digest.

Each digest post carries its items' device types and vendors in front matter; this walks
docs/_posts, aggregates them, and regenerates docs/browse/ so the site can be navigated by
"firewall -> Fortinet" rather than only by date.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import date as _date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "docs" / "_posts"
BROWSE = ROOT / "docs" / "browse"

DEVICE_LABEL = {
    "firewall": "Firewalls", "vpn-gateway": "VPN gateways", "router": "Routers",
    "switch": "Switches", "wireless": "Wireless", "load-balancer": "Load balancers",
    "sdwan": "SD-WAN / SASE", "management-platform": "Management platforms", "other": "Other",
    # legacy names from editions published before the enum was fixed
    "vpn": "VPN gateways", "mgmt-protocols": "Management platforms",
    "ot-network": "Other", "generic": "Other",
}
DEVICE_ORDER = ["firewall", "vpn-gateway", "router", "switch", "wireless", "load-balancer",
                "sdwan", "management-platform", "other"]
SLUG_RE = re.compile(r"[^a-z0-9]+")

# Vendor names arrive from two eras and two writers: the collector's internal lowercase keys
# and whatever the model typed. Canonicalise so "cisco" and "Cisco" are one page.
VENDOR_CANON = {
    "cisco": "Cisco", "cisco systems": "Cisco", "fortinet": "Fortinet",
    "palo alto": "Palo Alto Networks", "palo alto networks": "Palo Alto Networks",
    "pan-os": "Palo Alto Networks", "check point": "Check Point", "checkpoint": "Check Point",
    "juniper": "Juniper Networks", "juniper networks": "Juniper Networks",
    "f5": "F5", "f5 networks": "F5", "citrix": "Citrix", "ivanti": "Ivanti",
    "sonicwall": "SonicWall", "sophos": "Sophos", "watchguard": "WatchGuard",
    "hpe aruba": "HPE Aruba Networking", "aruba": "HPE Aruba Networking",
    "hpe aruba networking": "HPE Aruba Networking", "arista": "Arista Networks",
    "arista networks": "Arista Networks", "extreme": "Extreme Networks",
    "extreme networks": "Extreme Networks", "mikrotik": "MikroTik", "ubiquiti": "Ubiquiti",
    "netgear": "NETGEAR", "tp-link": "TP-Link", "tplink": "TP-Link", "d-link": "D-Link",
    "dlink": "D-Link", "zyxel": "Zyxel", "barracuda": "Barracuda", "huawei": "Huawei",
    "asus": "ASUS", "nokia": "Nokia", "draytek": "DrayTek", "qnap-synology-edge": "QNAP / Synology",
    "vpn-gateways": "Multiple", "telco-core": "Multiple", "multiple": "Multiple",
    "unspecified": "Unspecified", "": "Unspecified",
}

# Editions published before device_types was constrained to an enum used free text.
DEVICE_CANON = {
    "vpn": "vpn-gateway", "vpn gateway": "vpn-gateway", "mgmt-protocols": "management-platform",
    "firewall management platform": "management-platform",
    "management platform": "management-platform", "ips": "firewall",
    "perimeter appliance": "firewall", "email security gateway": "other",
    "vpn client endpoint software": "other", "unified communications / pbx server": "other",
    "voice infrastructure": "other", "network infrastructure generally": "other",
    "ot-network": "other", "generic": "other",
}


# Editions published before entries carried an "ai" flag: fall back to the title.
AI_HINTS = ("ai-", " ai ", "artificial intelligence", "llm", "genai", "generative ai",
            "machine learning", "prompt injection", "ai agent", "agentic", "deepfake",
            "ai-driven", "ai-assisted", "ai-powered", "copilot", "chatgpt")


def is_ai(entry: dict) -> bool:
    if "ai" in entry:
        return bool(entry["ai"])
    blob = f" {entry.get('title', '').lower()} "
    return any(h in blob for h in AI_HINTS)


def vendor_from_source(source: str) -> str:
    """Infer the vendor from the feed name when the item text named none."""
    low = (source or "").lower()
    for key, canon in VENDOR_CANON.items():
        if key and len(key) > 2 and key in low:
            return canon
    if "talos" in low:
        return "Cisco"
    if "unit 42" in low:
        return "Palo Alto Networks"
    return "Unspecified"


def canon_vendor(name: str) -> str:
    key = (name or "").strip().lower()
    return VENDOR_CANON.get(key, (name or "Unspecified").strip())


def canon_device(name: str) -> str:
    key = (name or "").strip().lower()
    if key in DEVICE_LABEL and key not in DEVICE_CANON:
        return key
    return DEVICE_CANON.get(key, key if key in DEVICE_LABEL else "other")


def slug(text: str) -> str:
    return SLUG_RE.sub("-", text.lower()).strip("-")


def read_index() -> list[dict]:
    """Every entry ever published, from the per-post index blocks."""
    entries: list[dict] = []
    for post in sorted(POSTS.glob("*.md")):
        text = post.read_text()
        match = re.search(r"<!--index\n(.*?)\n-->", text, re.S)
        if not match:
            continue
        try:
            data = json.loads(match.group(1))
        except json.JSONDecodeError:
            continue
        for entry in data.get("entries", []):
            entry["post_url"] = data.get("url", "")
            entry["date"] = data.get("date", "")
            vendors = sorted({canon_vendor(v) for v in (entry.get("vendors") or []) if v})
            if not vendors or vendors == ["Unspecified"]:
                # A vendor PSIRT or vendor research blog identifies the vendor even when the
                # item text never names a product ("Cisco Talos" -> Cisco).
                vendors = [vendor_from_source(entry.get("source", ""))]
            entry["vendors"] = vendors
            entry["device_types"] = sorted({canon_device(d) for d in
                                            (entry.get("device_types") or [])}) or ["other"]
            entry["ai"] = is_ai(entry)
            entries.append(entry)
    return entries


def page(title: str, body: list[str], permalink: str) -> str:
    return "\n".join([
        "---", "layout: default", f'title: "{title}"', f"permalink: {permalink}",
        "---", "", f"# {title}", "", *body, "",
        '<p><a href="{{ "/" | relative_url }}">← All editions</a> · '
        '<a href="{{ "/browse/" | relative_url }}">Browse index</a></p>', "",
    ])


def entry_line(e: dict) -> str:
    badge = {"critical": "🔴", "high": "🟠", "medium": "🟡", "watch": "⚪"}.get(e.get("relevance"), "")
    cves = f" — {', '.join(e['cves'])}" if e.get("cves") else ""
    kev = " **[KEV]**" if e.get("kev") else ""
    return (f"- {badge} [{e['title']}]({e['link']}){cves}{kev}  \n"
            f"  <small>{e.get('date', '')} · {e.get('source', '')} · "
            f"[in digest]({{{{ '{e['post_url']}' | relative_url }}}})</small>")


def build() -> list[Path]:
    entries = read_index()
    by_device: dict[str, list[dict]] = defaultdict(list)
    by_vendor: dict[str, list[dict]] = defaultdict(list)
    device_vendors: dict[str, set] = defaultdict(set)

    for e in entries:
        for d in e.get("device_types") or ["generic"]:
            by_device[d].append(e)
            for v in e.get("vendors", []):
                device_vendors[d].add(v)
        for v in e.get("vendors", []):
            by_vendor[v].append(e)

    BROWSE.mkdir(parents=True, exist_ok=True)
    for stale in BROWSE.glob("*.md"):
        stale.unlink()
    written: list[Path] = []

    # Device pages, each grouped by vendor underneath.
    for device in [d for d in DEVICE_ORDER if d in by_device] + \
                  [d for d in sorted(by_device) if d not in DEVICE_ORDER]:
        items = by_device[device]
        body = [f"*{len(items)} item(s) across all editions.*", ""]
        grouped: dict[str, list[dict]] = defaultdict(list)
        for e in items:
            for v in e.get("vendors") or ["(vendor not identified)"]:
                grouped[v].append(e)
        for vendor in sorted(grouped):
            body += [f"## {vendor}", ""]
            body += [entry_line(e) for e in sorted(grouped[vendor],
                                                   key=lambda x: x.get("date", ""), reverse=True)]
            body += [""]
        label = DEVICE_LABEL.get(device, device.title())
        path = BROWSE / f"device-{slug(device)}.md"
        path.write_text(page(label, body, f"/browse/device/{slug(device)}/"))
        written.append(path)

    # Vendor pages, each grouped by device type underneath.
    for vendor, items in sorted(by_vendor.items()):
        body = [f"*{len(items)} item(s) across all editions.*", ""]
        grouped: dict[str, list[dict]] = defaultdict(list)
        for e in items:
            for d in e.get("device_types") or ["generic"]:
                grouped[d].append(e)
        for device in sorted(grouped, key=lambda d: DEVICE_ORDER.index(d) if d in DEVICE_ORDER else 99):
            body += [f"## {DEVICE_LABEL.get(device, device.title())}", ""]
            body += [entry_line(e) for e in sorted(grouped[device],
                                                   key=lambda x: x.get("date", ""), reverse=True)]
            body += [""]
        path = BROWSE / f"vendor-{slug(vendor)}.md"
        path.write_text(page(vendor, body, f"/browse/vendor/{slug(vendor)}/"))
        written.append(path)

    # AI topic page - same vendor-first shape as the device pages.
    ai_entries = [e for e in entries if e.get("ai")]
    if ai_entries:
        body = [f"*{len(ai_entries)} item(s) with an AI angle, across all editions.*", "",
                "Items where AI is part of the story: AI-assisted attacks or vulnerability "
                "discovery, AI/LLM/AIOps integrations on network gear, or prompt injection "
                "against network management.", ""]
        grouped: dict[str, list[dict]] = defaultdict(list)
        for e in ai_entries:
            for v in e.get("vendors") or ["Unspecified"]:
                grouped[v].append(e)
        for vendor in sorted(grouped):
            body += [f"## {vendor}", ""]
            for e in sorted(grouped[vendor], key=lambda x: x.get("date", ""), reverse=True):
                body.append(entry_line(e))
                if e.get("ai_angle"):
                    body.append(f"  <small>**AI angle:** {e['ai_angle']}</small>")
            body += [""]
        path = BROWSE / "topic-ai.md"
        path.write_text(page("AI & network devices", body, "/browse/ai/"))
        written.append(path)

    # Time archives: week, month and year, each grouped by vendor.
    def parse_day(value: str):
        try:
            return _date.fromisoformat((value or "")[:10])
        except ValueError:
            return None

    by_week: dict[str, list[dict]] = defaultdict(list)
    by_month: dict[str, list[dict]] = defaultdict(list)
    by_year: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        day = parse_day(e.get("date", ""))
        if not day:
            continue
        iso_year, iso_week, _ = day.isocalendar()
        by_week[f"{iso_year}-W{iso_week:02d}"].append(e)
        by_month[f"{day:%Y-%m}"].append(e)
        by_year[f"{day:%Y}"].append(e)

    MONTH_NAME = ["", "January", "February", "March", "April", "May", "June", "July",
                  "August", "September", "October", "November", "December"]

    def period_page(entries_in: list[dict], title: str, permalink: str, filename: str) -> None:
        body = [f"*{len(entries_in)} item(s) in this period.*", ""]
        grouped: dict[str, list[dict]] = defaultdict(list)
        for e in entries_in:
            for v in e.get("vendors") or ["Unspecified"]:
                grouped[v].append(e)
        for vendor in sorted(grouped, key=lambda v: (-len(grouped[v]), v)):
            body += [f"## {vendor} ({len(grouped[vendor])})", ""]
            body += [entry_line(e) for e in sorted(grouped[vendor],
                                                   key=lambda x: x.get("date", ""), reverse=True)]
            body += [""]
        path = BROWSE / filename
        path.write_text(page(title, body, permalink))
        written.append(path)

    for week, rows in by_week.items():
        period_page(rows, f"Week {week.split('-W')[1]} of {week.split('-W')[0]}",
                    f"/browse/week/{week}/", f"period-week-{week}.md")
    for month, rows in by_month.items():
        y, m = month.split("-")
        period_page(rows, f"{MONTH_NAME[int(m)]} {y}", f"/browse/month/{month}/",
                    f"period-month-{month}.md")
    for year, rows in by_year.items():
        period_page(rows, f"Year {year}", f"/browse/year/{year}/", f"period-year-{year}.md")

    # Archive hub listing every period.
    abody = ["Everything published, grouped by period. Each page breaks the period down by vendor.", ""]
    for year in sorted(by_year, reverse=True):
        abody += [f"## {year} — {len(by_year[year])} items", "",
                  f"- [Whole year]({{{{ '/browse/year/{year}/' | relative_url }}}}) "
                  f"({len(by_year[year])})", "", "**Months**", ""]
        for month in sorted((m for m in by_month if m.startswith(year)), reverse=True):
            mn = MONTH_NAME[int(month.split("-")[1])]
            abody.append(f"- [{mn} {year}]({{{{ '/browse/month/{month}/' | relative_url }}}}) "
                         f"({len(by_month[month])})")
        abody += ["", "**Weeks**", ""]
        for week in sorted((w for w in by_week if w.startswith(year)), reverse=True):
            num = week.split("-W")[1]
            days = sorted({e["date"][:10] for e in by_week[week] if e.get("date")})
            span = f"{days[0]} to {days[-1]}" if days else ""
            abody.append(f"- [Week {num}]({{{{ '/browse/week/{week}/' | relative_url }}}}) "
                         f"({len(by_week[week])}) <small>{span}</small>")
        abody += [""]
    (BROWSE / "archive.md").write_text(page("Archive by week, month and year", abody, "/browse/archive/"))
    written.append(BROWSE / "archive.md")

    # The browse hub.
    body = ["Pick a vendor, or browse by device type.", "", "## By vendor", ""]
    for vendor in sorted(by_vendor):
        devices = ", ".join(sorted({DEVICE_LABEL.get(d, d)
                                    for e in by_vendor[vendor]
                                    for d in (e.get("device_types") or ["other"])}))
        body.append(f"- [{vendor}]({{{{ '/browse/vendor/{slug(vendor)}/' | relative_url }}}}) "
                    f"({len(by_vendor[vendor])}) <small>{devices}</small>")
    if ai_entries:
        ai_vendors = ", ".join(sorted({v for e in ai_entries for v in e["vendors"]}))
        body += ["", "## By topic", "",
                 f"- [🧠 AI & network devices]({{{{ '/browse/ai/' | relative_url }}}}) "
                 f"({len(ai_entries)}) <small>{ai_vendors}</small>"]
    if by_year:
        latest_week = sorted(by_week, reverse=True)[0] if by_week else None
        latest_month = sorted(by_month, reverse=True)[0] if by_month else None
        body += ["", "## By period", ""]
        if latest_week:
            body.append(f"- [This week]({{{{ '/browse/week/{latest_week}/' | relative_url }}}}) "
                        f"({len(by_week[latest_week])})")
        if latest_month:
            mn = MONTH_NAME[int(latest_month.split("-")[1])]
            body.append(f"- [{mn}]({{{{ '/browse/month/{latest_month}/' | relative_url }}}}) "
                        f"({len(by_month[latest_month])})")
        body.append(f"- [Full archive by week, month and year]"
                    f"({{{{ '/browse/archive/' | relative_url }}}})")
    body += ["", "## By device type", ""]
    for device in [d for d in DEVICE_ORDER if d in by_device] + \
                  [d for d in sorted(by_device) if d not in DEVICE_ORDER]:
        vendors = ", ".join(sorted(v.title() for v in device_vendors[device])[:8]) or "—"
        body.append(f"- [{DEVICE_LABEL.get(device, device.title())}]"
                    f"({{{{ '/browse/device/{slug(device)}/' | relative_url }}}}) "
                    f"({len(by_device[device])}) <small>{vendors}</small>")
    hub = BROWSE / "index.md"
    hub.write_text(page("Browse by vendor and device", body, "/browse/"))
    written.append(hub)

    print(f"[index] {len(entries)} entries -> {len(by_device)} device pages, "
          f"{len(by_vendor)} vendor pages, {len(by_week)} weeks, {len(by_month)} months, "
          f"{len(by_year)} years")
    return written


if __name__ == "__main__":
    build()
