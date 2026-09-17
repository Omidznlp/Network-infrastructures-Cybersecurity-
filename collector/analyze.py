"""Summarize collected items with Claude and produce upgrade / mitigation advice.

Falls back to deterministic rule-based advice when no ANTHROPIC_API_KEY is present,
so the pipeline still produces a digest without the model.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODEL = os.environ.get("DIGEST_MODEL", "claude-opus-5")
MAX_ITEMS = int(os.environ.get("DIGEST_MAX_ITEMS", "25"))

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
- Be terse. No marketing language, no filler."""

SCHEMA = {
    "type": "object",
    "properties": {
        "headline": {
            "type": "object",
            "description": "The AI-and-network-devices lead story for this edition.",
            "properties": {
                "title": {"type": "string"},
                "body": {"type": "string", "description": "2-4 paragraphs on how AI is being used to attack or defend network devices this cycle, grounded in the supplied items. If no item touches AI, explain the week's dominant network-device risk pattern through an AI lens without inventing incidents."},
                "prevention_modern": {"type": "array", "items": {"type": "string"}},
                "prevention_legacy": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["title", "body", "prevention_modern", "prevention_legacy"],
            "additionalProperties": False,
        },
        "executive_summary": {"type": "array", "items": {"type": "string"},
                              "description": "3-6 bullets: what changed for the network team today."},
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "description": "index of the input item"},
                    "relevance": {"type": "string", "enum": ["critical", "high", "medium", "watch", "drop"]},
                    "device_types": {"type": "array", "items": {"type": "string"}},
                    "affected": {"type": "string", "description": "Vendor/product/versions exactly as stated in the source."},
                    "what_happened": {"type": "string"},
                    "why_it_matters": {"type": "string"},
                    "actions": {"type": "array", "items": {"type": "string"},
                                 "description": "Ordered, concrete remediation steps."},
                    "legacy_advice": {"type": "string"},
                    "detection": {"type": "string", "description": "What to hunt for in logs/flows, or empty string."},
                    "ai_angle": {"type": "string", "description": "AI relevance, or empty string."},
                },
                "required": ["id", "relevance", "device_types", "affected", "what_happened",
                             "why_it_matters", "actions", "legacy_advice", "detection", "ai_angle"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["headline", "executive_summary", "items"],
    "additionalProperties": False,
}


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
    out_items = []
    for idx, item in enumerate(payload["items"][:MAX_ITEMS]):
        cats = item["categories"] or ["generic"]
        actions: list[str] = []
        for cat in cats:
            actions += pb.get(cat, [])
        actions = list(dict.fromkeys(actions or pb["generic"]))[:5]
        hot = {"actively exploited", "in the wild", "zero-day", "0-day",
               "known exploited", "emergency directive"}
        if item["kev"] or hot & set(item["urgency"]):
            rel = "critical"
        elif item["score"] >= 14 or "unauthenticated" in item["urgency"]:
            rel = "high"
        elif item["score"] >= kw["min_score"]:
            rel = "medium"
        else:
            rel = "watch"
        out_items.append({
            "id": idx, "relevance": rel, "device_types": cats,
            "affected": ", ".join(item["vendors"]) or "see advisory",
            "what_happened": item["summary"][:400] or item["title"],
            "why_it_matters": ("Listed on the CISA KEV catalog - exploitation is confirmed."
                               if item["kev"] else
                               "Matched network-device keywords: " + ", ".join(item["urgency"] or cats)),
            "actions": actions,
            "legacy_advice": pb["legacy"][0],
            "detection": "", "ai_angle": "AI/ML mentioned in the source." if item["ai_related"] else "",
        })
    return {
        "headline": {
            "title": "AI and network devices: standing guidance",
            "body": ("No model summary was generated for this edition (ANTHROPIC_API_KEY not set), "
                     "so this section carries the standing guidance. AI shortens the gap between a "
                     "public advisory and mass exploitation of internet-facing network devices, and it "
                     "adds a new privileged surface wherever an assistant or agent can read device "
                     "state or push configuration."),
            "prevention_modern": pb["ai"],
            "prevention_legacy": pb["legacy"],
        },
        "executive_summary": [
            f"{len(payload['items'])} network-device items collected in the last "
            f"{payload['window_hours']}h from {payload['stats']['feeds_ok']} feeds.",
            f"{sum(1 for i in payload['items'] if i['kev'])} item(s) reference CISA KEV entries.",
            "Model summarization disabled - rule-based advice shown.",
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
            "effort": os.environ.get("DIGEST_EFFORT", "high"),
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
        return {"headline": {"title": "No network-device stories in this window",
                             "body": "No item cleared the relevance threshold.",
                             "prevention_modern": [], "prevention_legacy": []},
                "executive_summary": ["Nothing to report."], "items": [], "analysis_mode": "empty"}
    if not (os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN")):
        log("no API key - using rule-based fallback")
        return rule_based(payload)
    try:
        return with_claude(payload)
    except Exception as exc:
        log(f"model call failed ({exc.__class__.__name__}: {exc}) - falling back to rules")
        out = rule_based(payload)
        out["analysis_mode"] = f"rule-based (model error: {exc.__class__.__name__})"
        return out


if __name__ == "__main__":
    print(json.dumps(analyze(json.load(sys.stdin)), indent=2))
