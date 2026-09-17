"""Build the browse-by-device-type and browse-by-vendor pages from every published digest.

Each digest post carries its items' device types and vendors in front matter; this walks
docs/_posts, aggregates them, and regenerates docs/browse/ so the site can be navigated by
"firewall -> Fortinet" rather than only by date.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "docs" / "_posts"
BROWSE = ROOT / "docs" / "browse"

DEVICE_LABEL = {
    "firewall": "Firewalls", "vpn": "VPN gateways", "router": "Routers", "switch": "Switches",
    "wireless": "Wireless", "load-balancer": "Load balancers", "sdwan": "SD-WAN / SASE",
    "mgmt-protocols": "Management protocols", "ot-network": "OT / industrial network",
    "generic": "Other network devices",
}
DEVICE_ORDER = ["firewall", "vpn", "router", "switch", "wireless", "load-balancer",
                "sdwan", "mgmt-protocols", "ot-network", "generic"]
SLUG_RE = re.compile(r"[^a-z0-9]+")


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
            body += [f"## {vendor.title()}", ""]
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
        path.write_text(page(vendor.title(), body, f"/browse/vendor/{slug(vendor)}/"))
        written.append(path)

    # The browse hub.
    body = ["Pick a device type, or jump straight to a vendor.", "", "## By device type", ""]
    for device in [d for d in DEVICE_ORDER if d in by_device] + \
                  [d for d in sorted(by_device) if d not in DEVICE_ORDER]:
        vendors = ", ".join(sorted(v.title() for v in device_vendors[device])[:8]) or "—"
        body.append(f"- [{DEVICE_LABEL.get(device, device.title())}]"
                    f"({{{{ '/browse/device/{slug(device)}/' | relative_url }}}}) "
                    f"({len(by_device[device])}) <small>{vendors}</small>")
    body += ["", "## By vendor", ""]
    for vendor in sorted(by_vendor):
        body.append(f"- [{vendor.title()}]({{{{ '/browse/vendor/{slug(vendor)}/' | relative_url }}}}) "
                    f"({len(by_vendor[vendor])})")
    hub = BROWSE / "index.md"
    hub.write_text(page("Browse by device and vendor", body, "/browse/"))
    written.append(hub)

    print(f"[index] {len(entries)} entries -> {len(by_device)} device pages, "
          f"{len(by_vendor)} vendor pages")
    return written


if __name__ == "__main__":
    build()
