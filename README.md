# Autonomous Brain

A self-improving AI software-engineering pipeline. Every 24 hours a GitHub
Action wakes up, asks an LLM (via the free GitHub Models API) to design a
brand-new project that's more advanced than yesterday's, generates the code,
tests it, publishes it as a new public repo (with Pages if applicable), and
remembers what it built.

- **Schedule:** daily at 06:00 UTC (`.github/workflows/daily_build.yml`)
- **Brain:** `brain.py`
- **Memory:** `memory_log.json` (auto-updated by the bot)
- **Retry cap:** 5 attempts/day
- **Cost:** $0 (uses GitHub Models free tier)

All generated projects are educational/diagnostic. The system prompt in
`brain.py` enforces strict GitHub-TOS-compliant safety guardrails.
