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
    head = analysis["headline"]

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
        "> Scope: firewalls, VPN gateways, routers, switches, wireless controllers, load balancers "
        "and SD-WAN edge. Everything else is filtered out.",
        "",
        "---",
        "",
    ]

    if kept:
        out += [
            f"## 🧠 Headline — {head['title']}",
            "",
            head["body"],
            "",
            "**Preventing it on current systems**",
            "",
            bullets(head.get("prevention_modern", [])),
            "",
            "**Preventing it on legacy / end-of-life systems**",
            "",
            bullets(head.get("prevention_legacy", [])),
            "",
            "---",
            "",
        ]

    out += [
        "## Executive summary",
        "",
        bullets(analysis.get("executive_summary", [])),
        "",
    ]

    if kev_cves:
        out += ["> **On the CISA KEV catalog in this edition:** " + ", ".join(kev_cves) +
                " — treat these as confirmed-exploited and patch on an emergency change.", ""]

    out += ["---", "", "## Items", ""]
    if not kept:
        out += ["**No network device security news in this window.**", "",
                "No advisory or report in the sources touched firewalls, VPN gateways, routers, "
                "switches, wireless controllers, load balancers or SD-WAN edge devices. "
                "Unrelated security news is deliberately not shown here.", ""]

    for analysed in kept:
        src = items_in[analysed["id"]] if analysed["id"] < len(items_in) else {}
        badge = BADGE.get(analysed["relevance"], analysed["relevance"])
        tags = " ".join(f"`{t}`" for t in src.get("tags", []))
        out += [
            f"### {badge} — {src.get('title', 'Untitled')}",
            "",
            f"*{src.get('source', '?')} · {src.get('published', '')[:10]} · "
            f"[source]({tidy_url(src.get('link', '#'))})* {tags}",
            "",
            f"**Affected:** {analysed['affected']}  ",
            f"**Device types:** {', '.join(analysed['device_types']) or 'n/a'}  ",
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
                "vendors": items_in[a["id"]]["vendors"],
                "cves": items_in[a["id"]]["cves"],
                "kev": bool(items_in[a["id"]]["kev"]),
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
