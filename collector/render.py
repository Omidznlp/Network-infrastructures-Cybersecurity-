"""Render the analyzed digest into a Jekyll post (which is also the archive file)."""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "docs" / "_posts"

BADGE = {"critical": "🔴 CRITICAL", "high": "🟠 HIGH", "medium": "🟡 MEDIUM", "watch": "⚪ WATCH"}
ORDER = {"critical": 0, "high": 1, "medium": 2, "watch": 3}
DEVICE_LABEL = {
    "firewall": "Firewalls", "vpn-gateway": "VPN gateways", "router": "Routers",
    "switch": "Switches", "wireless": "Wireless", "load-balancer": "Load balancers",
    "sdwan": "SD-WAN / SASE", "management-platform": "Management platforms", "other": "Other",
}
DEVICE_ORDER = ["firewall", "vpn-gateway", "router", "switch", "wireless",
                "load-balancer", "sdwan", "management-platform", "other"]


def device_sort(device: str) -> int:
    return DEVICE_ORDER.index(device) if device in DEVICE_ORDER else 99


def tidy_url(url: str) -> str:
    """Strip feed tracking query strings (Cisco's vs_f=/vs_cat= etc.) for readable links."""
    return re.sub(r"[?&](vs_[a-z]+|utm_[a-z]+|source)=[^&]*", "", url or "").rstrip("?&")


def esc(text: str) -> str:
    return (text or "").replace('"', "'").strip()


def bullets(values, indent: str = "") -> str:
    return "\n".join(f"{indent}- {v}" for v in values if v) or f"{indent}- _none_"


def render(collected: dict, analysis: dict, edition: str) -> str:
    date = datetime.now(timezone.utc)
    items_in = collected["items"]
    kept = [a for a in analysis["items"] if a["relevance"] != "drop"]
    kept.sort(key=lambda a: ORDER.get(a["relevance"], 9))
    crit = sum(1 for a in kept if a["relevance"] == "critical")
    kev_cves = sorted({c for i in items_in for c in i["kev"]})

    out: list[str] = []
    out += [
        "---",
        "layout: post",
        f'title: "Network Device Security Digest - {date:%Y-%m-%d}"',
        f"date: {date:%Y-%m-%d %H:%M:%S} +0000",
        f"edition: {edition}",
        f"critical_count: {crit}",
        f"item_count: {len(kept)}",
        f'kev: "{", ".join(kev_cves) if kev_cves else "none"}"',
        f'analysis_mode: "{analysis.get("analysis_mode", "unknown")}"',
        "categories: digest",
        "---",
        "",
        f"# Network Device Security Digest — {date:%Y-%m-%d}",
        "",
        f"*{edition} edition · window {collected['window_hours']}h · "
        f"{collected['stats']['feeds_ok']} feeds · {len(kept)} items · "
        f"{crit} critical · generated {date:%Y-%m-%d %H:%M UTC}*",
        "",
        "> Scope: firewalls, VPN gateways, routers, switches, wireless controllers, load balancers, "
        "management platforms and SD-WAN edge. Everything else is filtered out.",
        "",
        "---",
        "",
    ]

    top = analysis.get("top_story") or {}
    if kept and top.get("title"):
        out += [f"## 📌 Top story — {top['title']}", "", top.get("body", ""), ""]
        if top.get("actions_now"):
            out += ["**Do this first**", "", bullets(top["actions_now"]), ""]
        out += ["---", ""]

    if kev_cves:
        out += ["> **On the CISA KEV catalog in this edition:** " + ", ".join(kev_cves) +
                " — treat these as confirmed-exploited and patch on an emergency change.", ""]

    out += ["## Executive summary", "", bullets(analysis.get("executive_summary", [])), "",
            "---", ""]

    # Items grouped by vendor, then by device type within each vendor.
    out += ["## Items by vendor", ""]
    if not kept:
        out += ["**No network device security news in this window.**", "",
                "No advisory or report in the sources touched firewalls, VPN gateways, routers, "
                "switches, wireless controllers, load balancers or SD-WAN edge devices. "
                "Unrelated security news is deliberately not shown here.", ""]

    by_vendor: dict[str, list] = {}
    for a in kept:
        by_vendor.setdefault(a.get("vendor") or "Unspecified", []).append(a)

    def vendor_rank(name: str) -> tuple:
        worst = min((ORDER.get(a["relevance"], 9) for a in by_vendor[name]), default=9)
        return (worst, -len(by_vendor[name]), name.lower())

    for vendor in sorted(by_vendor, key=vendor_rank):
        entries = by_vendor[vendor]
        counts = {}
        for a in entries:
            counts[a["relevance"]] = counts.get(a["relevance"], 0) + 1
        tally = ", ".join(f"{n} {r}" for r, n in sorted(counts.items(), key=lambda kv: ORDER.get(kv[0], 9)))
        out += [f"## {vendor}", "", f"*{len(entries)} item(s) — {tally}*", ""]

        by_device: dict[str, list] = {}
        for a in entries:
            primary = (a.get("device_types") or ["other"])[0]
            by_device.setdefault(primary, []).append(a)

        for device in sorted(by_device, key=device_sort):
            out += [f"### {DEVICE_LABEL.get(device, device.title())}", ""]
            for analysed in sorted(by_device[device], key=lambda a: ORDER.get(a["relevance"], 9)):
                src = items_in[analysed["id"]] if analysed["id"] < len(items_in) else {}
                badge = BADGE.get(analysed["relevance"], analysed["relevance"])
                tags = " ".join(f"`{t}`" for t in src.get("tags", []))
                out += [
                    f"#### {badge} — {src.get('title', 'Untitled')}",
                    "",
                    f"*[{src.get('source', 'source')}]({tidy_url(src.get('link', '#'))}) · "
                    f"{src.get('published', '')[:10]}* {tags}",
                    "",
                    f"> {analysed.get('summary') or analysed['what_happened'][:190]}",
                    "",
                    f"**Affected:** {analysed['affected']}  ",
                ]
                if src.get("cves"):
                    cve_bits = []
                    for cve in src["cves"]:
                        mark = " **[KEV]**" if cve in src.get("kev", []) else ""
                        epss = src.get("epss", {}).get(cve)
                        mark += f" (EPSS {epss:.2f})" if epss else ""
                        cve_bits.append(f"[{cve}](https://nvd.nist.gov/vuln/detail/{cve}){mark}")
                    out.append(f"**CVEs:** {', '.join(cve_bits)}  ")
                out += [
                    "",
                    f"**What happened.** {analysed['what_happened']}",
                    "",
                    f"**Why it matters.** {analysed['why_it_matters']}",
                    "",
                    "**Recommended actions**",
                    "",
                    bullets(analysed["actions"]),
                    "",
                ]
                if analysed.get("legacy_advice"):
                    out += [f"**Legacy / unpatchable gear.** {analysed['legacy_advice']}", ""]
                if analysed.get("detection"):
                    out += [f"**Detection.** {analysed['detection']}", ""]
                if analysed.get("ai_angle"):
                    out += [f"**AI angle.** {analysed['ai_angle']}", ""]
                out += [f"📄 **[Read the full report at {src.get('source', 'the source')} →]"
                        f"({tidy_url(src.get('link', '#'))})**", ""]
        out += ["---", ""]

    # AI section: today's if there is real AI news, otherwise the last one, dated.
    ai = analysis.get("ai_section") or {}
    ai_vendors = sorted({a.get("vendor") for a in kept
                         if (a.get("ai_angle") or "").strip() and a.get("vendor")})
    if ai.get("body"):
        stamp = ""
        if ai.get("carried_forward"):
            stamp = (f"  \n*No AI-related network-device news in this window. "
                     f"Carried forward from {ai.get('written', 'an earlier edition')}.*")
        out += [f"## 🧠 AI & network devices — {ai.get('title', '')}", "", ai["body"] + stamp, ""]
        if ai_vendors:
            out += [f"**Vendors with an AI angle in this edition:** {', '.join(ai_vendors)}", ""]
        if ai.get("prevention_modern"):
            out += ["**Preventing it on current systems**", "", bullets(ai["prevention_modern"]), ""]
        if ai.get("prevention_legacy"):
            out += ["**Preventing it on legacy / end-of-life systems**", "",
                    bullets(ai["prevention_legacy"]), ""]
        out += ["---", ""]

    index = {
        "url": f"/{date:%Y/%m/%d}/network-security-digest/",
        "date": f"{date:%Y-%m-%d}",
        "entries": [
            {
                "title": items_in[a["id"]]["title"],
                "link": tidy_url(items_in[a["id"]]["link"]),
                "source": items_in[a["id"]]["source"],
                "relevance": a["relevance"],
                "device_types": a["device_types"] or items_in[a["id"]]["categories"],
                "vendors": [a.get("vendor")] if a.get("vendor") else items_in[a["id"]]["vendors"],
                "cves": items_in[a["id"]]["cves"],
                "kev": bool(items_in[a["id"]]["kev"]),
                "ai": bool(items_in[a["id"]].get("ai_related") or (a.get("ai_angle") or "").strip()),
                "ai_angle": (a.get("ai_angle") or "").strip(),
            }
            for a in kept if a["id"] < len(items_in)
        ],
    }
    out += ["<!--index", json.dumps(index, indent=1), "-->", ""]

    out += [
        "## How this was produced",
        "",
        f"- Feeds polled: {collected['stats']['feeds_ok']} ok, {collected['stats']['feeds_failed']} failed",
        f"- Raw items: {collected['stats']['raw']} → in window: {collected['stats']['fresh']} → "
        f"network-device relevant: {collected['stats'].get('on_topic', 0)} → published: {len(kept)}",
        f"- Enrichment: CISA KEV, FIRST EPSS",
        f"- Analysis: `{analysis.get('analysis_mode', 'unknown')}`",
        "",
        "_Automated digest. Verify every version number against the vendor advisory before you "
        "schedule a change._",
        "",
    ]
    return "\n".join(out)


def write(collected: dict, analysis: dict, edition: str) -> Path:
    date = datetime.now(timezone.utc)
    slug = f"{date:%Y-%m-%d}-network-security-digest"
    if edition == "hourly":
        slug += f"-{date:%H%M}"
    path = POSTS / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render(collected, analysis, edition))
    return path


if __name__ == "__main__":
    data = json.load(sys.stdin)
    print(write(data["collected"], data["analysis"], data.get("edition", "daily")))
