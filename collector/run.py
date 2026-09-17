"""Digest pipeline. Runs as one process, or as stages around an external analysis step.

Stages exist so the Claude Code Action can sit between collection and rendering:
  collect -> data/collected.json
  (agent writes data/analysis.json)
  render  -> docs/_posts/...
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import analyze as analyzer  # noqa: E402
import collect as collector  # noqa: E402
import index_site  # noqa: E402
import render as renderer  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
COLLECTED = ROOT / "data" / "collected.json"
ANALYSIS = ROOT / "data" / "analysis.json"
NOTHING_TO_PUBLISH = 78


def summary_body(collected: dict, analysis: dict, edition: str) -> str:
    kept = [a for a in analysis["items"] if a["relevance"] != "drop"]
    crit = sum(1 for a in kept if a["relevance"] == "critical")
    high = sum(1 for a in kept if a["relevance"] == "high")
    kev = sorted({c for i in collected["items"] for c in i["kev"]})
    body = [
        f"Automated **{edition}** network-device security digest.",
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
    return "\n".join(body)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=int, default=24)
    ap.add_argument("--edition", default="daily", choices=["daily", "hourly"])
    ap.add_argument("--min-critical", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--stage", default="all", choices=["all", "collect", "render"],
                    help="'collect' and 'render' bracket an external analysis step")
    args = ap.parse_args()

    if args.stage == "render":
        collected = json.loads(COLLECTED.read_text())
        analysis = analyzer.load_external(ANALYSIS, collected)
    else:
        collected = collector.collect(args.hours, persist=not args.dry_run)
        if args.stage == "collect":
            COLLECTED.parent.mkdir(parents=True, exist_ok=True)
            COLLECTED.write_text(json.dumps(collected, indent=2))
            count = len(collected["items"])
            print(f"[run] collected {count} items -> {COLLECTED.relative_to(ROOT)}")
            return NOTHING_TO_PUBLISH if count == 0 else 0
        analysis = analyzer.analyze(collected)

    kept = [a for a in analysis["items"] if a["relevance"] != "drop"]
    crit = sum(1 for a in kept if a["relevance"] == "critical")

    if args.min_critical and crit < args.min_critical:
        print(f"[run] {crit} critical items < threshold {args.min_critical} - no post written")
        Path("digest_summary.txt").write_text("skipped: nothing urgent in this window\n")
        return NOTHING_TO_PUBLISH

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
    index_site.build()
    Path("digest_summary.txt").write_text(summary_body(collected, analysis, args.edition))
    print(f"[run] wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
