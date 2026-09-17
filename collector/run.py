"""End-to-end run: collect -> analyze -> render. Writes a PR body to $GITHUB_OUTPUT-friendly files."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import analyze as analyzer  # noqa: E402
import collect as collector  # noqa: E402
import render as renderer  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=int, default=24, help="look-back window")
    ap.add_argument("--edition", default="daily", choices=["daily", "hourly"])
    ap.add_argument("--min-critical", type=int, default=0,
                    help="hourly mode: only publish when at least this many critical items appear")
    ap.add_argument("--dry-run", action="store_true", help="print, do not write files")
    args = ap.parse_args()

    collected = collector.collect(args.hours, persist=not args.dry_run)
    analysis = analyzer.analyze(collected)

    kept = [a for a in analysis["items"] if a["relevance"] != "drop"]
    crit = sum(1 for a in kept if a["relevance"] == "critical")
    high = sum(1 for a in kept if a["relevance"] == "high")

    if args.min_critical and crit < args.min_critical:
        print(f"[run] {crit} critical items < threshold {args.min_critical} - no post written")
        Path("digest_summary.txt").write_text("skipped: nothing urgent in this window\n")
        return 78  # neutral: nothing to publish

    if args.dry_run:
        print(renderer.render(collected, analysis, args.edition))
        return 0

    path = renderer.write(collected, analysis, args.edition)
    (ROOT / "data" / "last_run.json").write_text(json.dumps({
        "at": datetime.now(timezone.utc).isoformat(),
        "edition": args.edition,
        "stats": collected["stats"],
        "analysis_mode": analysis.get("analysis_mode"),
        "post": str(path.relative_to(ROOT)),
    }, indent=2))

    kev = sorted({c for i in collected["items"] for c in i["kev"]})
    body = [
        f"Automated **{args.edition}** network-device security digest.",
        "",
        f"- Items published: **{len(kept)}** ({crit} critical, {high} high)",
        f"- KEV CVEs referenced: {', '.join(kev) if kev else 'none'}",
        f"- Feeds: {collected['stats']['feeds_ok']} ok / {collected['stats']['feeds_failed']} failed",
        f"- Analysis: `{analysis.get('analysis_mode')}`",
        "",
        "### Top items",
        "",
    ]
    for a in kept[:8]:
        src = collected["items"][a["id"]]
        body.append(f"- **{a['relevance'].upper()}** — "
                    f"[{src['title']}]({renderer.tidy_url(src['link'])})")
    body += ["", "Review the digest file, then merge to publish it to the site."]
    Path("digest_summary.txt").write_text("\n".join(body))
    print(f"[run] wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
