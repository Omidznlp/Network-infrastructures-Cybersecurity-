# Network Infrastructure Cybersecurity

Automated security intelligence for **network devices** — firewalls, VPN gateways, routers,
switches, wireless controllers, load balancers and SD-WAN edge. It collects security news and
vendor advisories, throws away everything that is not about network infrastructure, triages what
is left with Claude, and turns each story into **concrete upgrade and hardening actions** for
both current and legacy systems.

Every edition leads with a headline on **how AI impacts or attacks network devices, and how to
prevent it**.

Nothing publishes itself: each run opens a **pull request** for review. Merging to `main`
publishes the edition to the GitHub Pages site.

## How it works

```
 schedule (hourly + daily)
        │
        ▼
 collector/collect.py   fetch ~20 RSS/Atom feeds → date window → dedupe against data/seen.json
        │               → score for network-device relevance → extract CVEs
        │               → enrich with CISA KEV + FIRST EPSS
        ▼
 collector/analyze.py   Claude (claude-opus-5) triages each item and writes the advice:
        │               severity, affected devices, actions, legacy guidance, detection,
        │               AI angle + the AI headline. Structured JSON output, schema-enforced.
        │               No API key? → deterministic rule-based playbooks instead.
        ▼
 collector/render.py    writes docs/_posts/YYYY-MM-DD-network-security-digest.md
        │
        ▼
 .github/workflows/digest.yml   commits to a branch and opens a PR for your review
        │
        ▼  (you merge)
 .github/workflows/pages.yml    publishes the site
```

### Two cadences

| Run | Schedule | Window | Opens a PR |
|---|---|---|---|
| **Daily digest** | 06:00 UTC | last 24h | always |
| **Hourly watch** | manual dispatch only | last 3h | only when a **critical** item appears |

The hourly watch is no longer scheduled - run it by hand from the Actions tab when a
major advisory is breaking and you want an off-cycle check. To put it back on a schedule,
add `- cron: '15 * * * *'` under `on.schedule` in `.github/workflows/digest.yml`.

Both are also runnable by hand from the **Actions** tab (`workflow_dispatch`), with a `dry_run`
option that prints the digest without opening a PR.

## Setup

1. **Push this scaffold** to the repo (see below).
2. **Add the API key**: repo → Settings → Secrets and variables → Actions → New repository
   secret → `ANTHROPIC_API_KEY`. Without it the pipeline still runs, using rule-based advice.
3. **Allow PRs from Actions**: Settings → Actions → General → Workflow permissions →
   check *"Allow GitHub Actions to create and approve pull requests"*.
4. **Labels** (optional but the workflow uses them): create `digest` and `needs-review`.
5. **Pages**: Settings → Pages → Source: *GitHub Actions*, then add repository **variable**
   `PAGES_ENABLED=true`. Until that variable is set the publish workflow is a deliberate no-op,
   so it cannot fail while Pages is off. Pages on a **private** repo needs a paid plan; on a
   public repo it is free.
6. **Branch protection** (recommended before going public): Settings → Rules → require a pull
   request before merging to `main`, so no edition can publish without your review.

Optional repository *variables*: `DIGEST_MODEL` (default `claude-opus-5`), `DIGEST_EFFORT`
(`low`…`max`, default `high`), `DIGEST_MAX_ITEMS` (default `25`).

## Run it locally

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...        # optional
python collector/run.py --hours 24 --edition daily --dry-run
```

Drop `--dry-run` to write the post into `docs/_posts/`.

## Tuning what gets in

- `config/sources.json` — feeds. Add, remove, or flip `enabled`. A dead feed is logged and
  skipped, never fatal. Per-feed `user_agent` overrides the default agent.
  *Known issue:* `cisa.gov`'s advisories RSS returns 403 to GitHub Actions runner IPs. Its KEV
  JSON is reachable, so newly added KEV entries are ingested as items instead — that is the more
  actionable half anyway (confirmed exploitation + the mandated remediation date). The feed works
  from a local run.
- `config/keywords.json` — the filter. `vendors` and `device_classes` carry the weight;
  an item needs `min_score` (default 4) to reach the digest and `watchlist_score` (2) to reach
  the watchlist. Raise `min_score` for less noise, lower it for wider coverage.
- `config/keywords.json` → `playbooks` — the standing remediation advice per device class,
  used verbatim in rule-based mode and as grounding for the model.
- `collector/analyze.py` → `SYSTEM` — the analyst's brief. This is where you change tone,
  depth, or what counts as relevant.

## Repository layout

```
collector/      collect.py (stdlib only) · analyze.py (Claude) · render.py · run.py
config/         sources.json · keywords.json
data/           seen.json (dedupe state) · last_run.json
docs/           the GitHub Pages site; _posts/ holds every published edition
.github/        digest.yml (collect + PR) · pages.yml (publish)
SOURCES.md      full source list, including LinkedIn pages to follow
```

## Accuracy rules

The model is instructed never to invent CVE IDs, version numbers or patch levels — if the source
does not state a fixed release, the digest says to check the vendor advisory. **Verify every
version against the vendor's own advisory before scheduling a change.**
