"""Summarize collected items with Claude and produce upgrade / mitigation advice.

Falls back to deterministic rule-based advice when no ANTHROPIC_API_KEY is present,
so the pipeline still produces a digest without the model.
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
def env(name: str, default: str) -> str:
    """Unset GitHub Actions variables arrive as empty strings, not as absent keys."""
    return os.environ.get(name) or default


MODEL = env("DIGEST_MODEL", "claude-opus-5")
MAX_ITEMS = int(env("DIGEST_MAX_ITEMS", "25"))

SYSTEM = """You are the network-infrastructure security analyst for an enterprise network team \
that runs firewalls, VPN gateways, routers, switches, wireless controllers and load balancers \
from vendors such as Cisco, Fortinet, Palo Alto, Juniper, F5, Citrix, Ivanti, HPE Aruba, MikroTik and Ubiquiti.

Your readers are network and security engineers. They need to know, for each story: does this touch \
our network devices, how urgent is it, and exactly what to do this week.

Rules:
- Use only the facts in the supplied items. Never invent CVE numbers, version numbers, patch \
  levels or dates. If a fixed version is not stated in the source, say "check the vendor advisory \
  for the fixed release" instead of guessing one.
- Drop anything that is not about network infrastructure devices (endpoint malware, SaaS breaches, \
  phone apps) by setting relevance to "drop".
- Recommendations must be concrete actions a network engineer can execute: upgrade paths, \
  management-plane restrictions, credential rotation, segmentation, detection queries.
- Always give separate advice for legacy/end-of-life gear that cannot be patched.
- Lead with the day's most consequential story, not with AI. Populate the AI section only when a
  collected item genuinely concerns AI; otherwise set has_new_ai false and the last real AI
  section is carried forward with its date. Never manufacture an AI angle to fill the slot.
- Name the vendor as the vendor writes it, and use only the schema's fixed device-type list.
- Be terse. No marketing language, no filler."""

SCHEMA = json.loads((ROOT / "config" / "analysis_schema.json").read_text())


def log(msg: str) -> None:
    print(f"[analyze] {msg}", file=sys.stderr)


def build_prompt(payload: dict) -> str:
    lines = ["Today's collected items (already filtered for network-device relevance):", ""]
    for idx, item in enumerate(payload["items"][:MAX_ITEMS]):
        lines += [
            f"### Item {idx}",
            f"Title: {item['title']}",
            f"Source: {item['source']} ({item['tier']}) | Published: {item['published']}",
            f"URL: {item['link']}",
            f"Vendors matched: {', '.join(item['vendors']) or 'n/a'}",
            f"Device classes matched: {', '.join(item['categories']) or 'n/a'}",
            f"CVEs: {', '.join(item['cves']) or 'none'}",
            f"On CISA KEV: {', '.join(item['kev']) or 'no'}",
            f"EPSS: {json.dumps(item['epss']) if item['epss'] else 'n/a'}",
            f"Excerpt: {item['summary'][:700]}",
            "",
        ]
    if payload.get("kev_context"):
        lines += ["### KEV context for the CVEs above", json.dumps(payload["kev_context"], indent=1)[:4000], ""]
    lines += [
        "Produce the digest as JSON matching the schema.",
        "Mark an item 'drop' if it is not about network infrastructure devices.",
        "The headline must be about how AI impacts or attacks network devices and how to prevent it, "
        "covering both legacy and current systems.",
    ]
    return "\n".join(lines)


def rule_based(payload: dict) -> dict:
    """Deterministic fallback - no model required."""
    kw = json.loads((ROOT / "config" / "keywords.json").read_text())
    pb = kw["playbooks"]
    # Map the collector's internal category names onto the schema's fixed device enum.
    DEVICE_MAP = {"firewall": "firewall", "vpn": "vpn-gateway", "router": "router",
                  "switch": "switch", "wireless": "wireless", "load-balancer": "load-balancer",
                  "sdwan": "sdwan", "mgmt-protocols": "management-platform",
                  "ot-network": "other", "generic": "other"}
    hot = {"actively exploited", "in the wild", "zero-day", "0-day",
           "known exploited", "emergency directive"}

    out_items = []
    for idx, item in enumerate(payload["items"][:MAX_ITEMS]):
        cats = item["categories"] or ["generic"]
        actions: list[str] = []
        for cat in cats:
            actions += pb.get(cat, [])
        actions = list(dict.fromkeys(actions or pb["generic"]))[:5]
        if item["kev"] or hot & set(item["urgency"]):
            rel = "critical"
        elif item["score"] >= 14 or "unauthenticated" in item["urgency"]:
            rel = "high"
        elif item["score"] >= kw["min_score"]:
            rel = "medium"
        else:
            rel = "watch"
        out_items.append({
            "id": idx, "relevance": rel,
            "vendor": (item["vendors"][0].title() if item["vendors"] else "Unspecified"),
            "device_types": sorted({DEVICE_MAP.get(c, "other") for c in cats}),
            "affected": ", ".join(v.title() for v in item["vendors"]) or "see advisory",
            "what_happened": item["summary"][:400] or item["title"],
            "why_it_matters": ("Listed on the CISA KEV catalog - exploitation is confirmed."
                               if item["kev"] else
                               "Matched network-device keywords: " + ", ".join(item["urgency"] or cats)),
            "actions": actions,
            "legacy_advice": pb["legacy"][0],
            "detection": "", "ai_angle": "AI/ML mentioned in the source." if item["ai_related"] else "",
        })

    worst = out_items[0] if out_items else None
    return {
        "top_story": {
            "title": (payload["items"][0]["title"] if payload["items"]
                      else "No network device news in this window"),
            "body": (worst["what_happened"] if worst else
                     "No advisory or report in this window concerned network infrastructure devices."),
            "actions_now": worst["actions"] if worst else [],
        },
        # No model ran, so there is no new AI reading; the carry-forward step fills this.
        "ai_section": {"has_new_ai": False, "title": "", "body": "",
                       "prevention_modern": [], "prevention_legacy": []},
        "executive_summary": [
            f"{len(payload['items'])} network-device items collected in the last "
            f"{payload['window_hours']}h from {payload['stats']['feeds_ok']} feeds.",
            f"{sum(1 for i in payload['items'] if i['kev'])} item(s) reference CISA KEV entries.",
            "Model summarization unavailable - rule-based advice shown.",
        ],
        "items": out_items,
        "analysis_mode": "rule-based",
    }


def with_claude(payload: dict) -> dict:
    import anthropic

    client = anthropic.Anthropic()
    log(f"calling {MODEL} on {min(len(payload['items']), MAX_ITEMS)} items")
    with client.messages.stream(
        model=MODEL,
        max_tokens=32000,
        system=SYSTEM,
        thinking={"type": "adaptive"},
        output_config={
            "effort": env("DIGEST_EFFORT", "high"),
            "format": {"type": "json_schema", "schema": SCHEMA},
        },
        messages=[{"role": "user", "content": build_prompt(payload)}],
    ) as stream:
        response = stream.get_final_message()

    if response.stop_reason == "refusal":
        raise RuntimeError(f"model refused: {getattr(response, 'stop_details', None)}")

    text = next(b.text for b in response.content if b.type == "text")
    result = json.loads(text)
    result["analysis_mode"] = MODEL
    result["usage"] = {"input": response.usage.input_tokens, "output": response.usage.output_tokens}
    log(f"usage: {result['usage']}")
    return result


def analyze(payload: dict) -> dict:
    if not payload.get("items"):
        return carry_forward_ai({
            "top_story": {"title": "No network device security news in this window",
                          "body": "No advisory or report in the sources concerned network "
                                  "infrastructure devices.", "actions_now": []},
            "ai_section": {"has_new_ai": False, "title": "", "body": "",
                           "prevention_modern": [], "prevention_legacy": []},
            "executive_summary": ["Nothing to report."], "items": [], "analysis_mode": "empty"})
    if not (os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN")):
        log("no API key - using rule-based fallback")
        return carry_forward_ai(rule_based(payload))
    try:
        return carry_forward_ai(with_claude(payload))
    except Exception as exc:
        log(f"model call failed ({exc.__class__.__name__}: {exc}) - falling back to rules")
        out = rule_based(payload)
        out["analysis_mode"] = f"rule-based (model error: {exc.__class__.__name__})"
        return carry_forward_ai(out)


if __name__ == "__main__":
    print(json.dumps(analyze(json.load(sys.stdin)), indent=2))


REQUIRED_ITEM_KEYS = set(SCHEMA["properties"]["items"]["items"]["required"])
RELEVANCE = set(SCHEMA["properties"]["items"]["items"]["properties"]["relevance"]["enum"])
DEVICE_ENUM = set(SCHEMA["properties"]["items"]["items"]["properties"]["device_types"]["items"]["enum"])
AI_STORE = ROOT / "data" / "ai_section.json"


def validate(result: object, item_count: int) -> dict:
    """Validate an analysis produced outside this process (e.g. by the Claude Code Action)."""
    if not isinstance(result, dict):
        raise ValueError("analysis is not a JSON object")

    top = result.get("top_story")
    if not isinstance(top, dict) or not top.get("title") or not top.get("body"):
        raise ValueError("top_story missing title or body")
    top.setdefault("actions_now", [])

    ai = result.get("ai_section")
    if not isinstance(ai, dict) or "has_new_ai" not in ai:
        raise ValueError("ai_section missing has_new_ai")
    if ai["has_new_ai"] and not ai.get("body"):
        raise ValueError("ai_section claims new AI content but has no body")

    if not isinstance(result.get("executive_summary"), list):
        raise ValueError("executive_summary must be a list")

    items = result.get("items")
    if not isinstance(items, list):
        raise ValueError("items must be a list")
    for pos, item in enumerate(items):
        if not isinstance(item, dict):
            raise ValueError(f"item {pos} is not an object")
        missing = REQUIRED_ITEM_KEYS - set(item)
        if missing:
            raise ValueError(f"item {pos} missing {sorted(missing)}")
        if item["relevance"] not in RELEVANCE:
            raise ValueError(f"item {pos} has invalid relevance {item['relevance']!r}")
        if not isinstance(item["id"], int) or not 0 <= item["id"] < item_count:
            raise ValueError(f"item {pos} has out-of-range id {item['id']!r}")
        bad = [d for d in item["device_types"] if d not in DEVICE_ENUM]
        if bad:
            raise ValueError(f"item {pos} has device types outside the enum: {bad}")
        if not isinstance(item["actions"], list):
            raise ValueError(f"item {pos} actions must be a list")
    return result


def carry_forward_ai(result: dict) -> dict:
    """Keep the AI section meaningful on days with no AI news.

    A fresh section is stored; on a day with none, the stored one is reused and stamped
    with the date it was written so it is never presented as today's reporting.
    """
    ai = result.get("ai_section") or {"has_new_ai": False}
    if ai.get("has_new_ai") and ai.get("body"):
        ai["written"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        ai["carried_forward"] = False
        AI_STORE.parent.mkdir(parents=True, exist_ok=True)
        AI_STORE.write_text(json.dumps(ai, indent=2))
        log(f"stored new AI section: {ai.get('title', '')[:60]}")
    else:
        try:
            stored = json.loads(AI_STORE.read_text())
            stored["carried_forward"] = True
            result["ai_section"] = stored
            log(f"no new AI content - carrying forward section from {stored.get('written')}")
        except (FileNotFoundError, json.JSONDecodeError):
            result["ai_section"] = {"has_new_ai": False, "carried_forward": False,
                                    "title": "", "body": "",
                                    "prevention_modern": [], "prevention_legacy": []}
            log("no new AI content and nothing stored to carry forward")
    return result


def load_external(path: Path, payload: dict) -> dict:
    """Load an analysis file written by the agent, falling back to rules if it is unusable."""
    try:
        result = validate(json.loads(path.read_text()), len(payload["items"][:MAX_ITEMS]))
        result.setdefault("analysis_mode", "claude-code-action")
        log(f"external analysis accepted: {len(result['items'])} items")
        return carry_forward_ai(result)
    except FileNotFoundError:
        log(f"{path} not found - falling back to rules")
    except (ValueError, json.JSONDecodeError) as exc:
        log(f"external analysis rejected ({exc}) - falling back to rules")
    out = rule_based(payload)
    out["analysis_mode"] = "rule-based (agent output unusable)"
    return carry_forward_ai(out)
