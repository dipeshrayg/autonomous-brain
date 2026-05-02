# Autonomous Brain — Engine

This is the **private engine** that drives the [autonomous-brain public dashboard](https://github.com/dipeshrayg/autonomous-brain).
Outsiders should never see this repo.

## Public face

- Dashboard: https://dipeshrayg.github.io/autonomous-brain/
- Public repo: https://github.com/dipeshrayg/autonomous-brain (slim — only `index.html`, `README.md`, sanitized `memory_log.json`)
- Daily project repos: `dipeshrayg/YYYY-MM-DD-<name>` (public, intentionally — they're the juice)

## Architecture

A hierarchy of LLM roles, each with primary + fallback model chain. Models routed via [`roles.py`](roles.py):

| Role | Primary | Job |
|---|---|---|
| **CEO** | gpt-4o | Periodic trajectory review (`executive.py`, `.github/workflows/ceo_review.yml`) |
| **CSO** | gpt-4o | Periodic security audit (`security_officer.py`, `.github/workflows/security_review.yml`) |
| **VP Engineering** | n/a (script) | Watchdog dispatcher (`.github/workflows/watchdog.yml`) |
| **Architect Judge** | gpt-4o | Synthesizes candidate plans |
| **Architect Candidates** | gpt-4o-mini, Phi-3.5-MoE | Propose plans in parallel |
| **Engineer** | gpt-4o | Per-file implementation |
| **Reviewers** | gpt-4o-mini, Phi-3.5-MoE | Critique conference, results merged |
| **Security Officer** | gpt-4o | Per-project pre-publish security gate |
| **Fixer / Polisher** | gpt-4o-mini | Iterative repair + final polish |
| **QA** | Playwright + Chromium | Mechanical browser verify |

## Files

- `brain.py` — orchestrator (the slim entry point you read first)
- `pipeline.py` — five LLM stages (plan / implement / critique / fix / polish) + security gate
- `verifier.py` — Playwright headless browser verification
- `dashboard.py` — README + index.html generators
- `executive.py` — CEO periodic review
- `security_officer.py` — CSO periodic audit
- `roles.py` — model registry + role-to-model mapping with fallback chains
- `publish_public.py` — sanitize memory + cross-repo push to public dashboard
- `memory_log.json` — full history, including engine internals
- `.github/workflows/` — all four scheduled workflows

## Workflows

- `daily_build.yml` — runs on cron + manual; the full pipeline. 9 staggered crons/day, ≤5 projects/day, ≥5h spacing.
- `watchdog.yml` — every 30 min; force-dispatches `daily_build` when needed.
- `ceo_review.yml` — 4×/day; CEO trajectory review.
- `security_review.yml` — 2×/day; CSO security audit.

Every workflow that mutates `memory_log.json` ends with a `Sync public dashboard` step that runs `publish_public.py` to push a sanitized snapshot to the public repo.

## Secrets required

- `GH_PAT` — fine-grained PAT with: Contents:Write, Administration:Write, Pages:Write, Workflows:Write on **all repos under dipeshrayg** (used to create new daily project repos AND to push the dashboard to the public repo).
- `GITHUB_TOKEN` — auto-injected; needs `models: read`, `contents: write`, `actions: write`.
