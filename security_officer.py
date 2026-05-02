"""
security_officer.py - The Chief Security Officer's periodic audit.

Two security layers exist in the system:

  1. PER-PROJECT GATE (pipeline.stage_security_review) — runs in every build,
     between final-verify and publish, can hard-block a publish on critical
     or high-severity findings. Implemented in pipeline.py.

  2. PERIODIC AUDIT (this file) — runs every 12 hours via
     .github/workflows/security_review.yml. Examines trends across the last
     N projects, looks for systemic security drift, and writes directives
     into memory_log.security_audits[]. The next plan stage prepends those
     directives to the architect prompt alongside the CEO's directives.

The CSO is parallel to the CEO in the hierarchy — both have direct authority
to constrain the next architect's plan. CEO cares about advancement and
quality; CSO cares about safety, privacy, and threat surface.
"""

from __future__ import annotations

import json
import logging
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from openai import OpenAI

import roles

log = logging.getLogger("brain.security_officer")

CSO_REVIEW_WINDOW = 8        # how many recent projects the CSO examines
CSO_DIRECTIVE_TTL_HOURS = 36  # plan stages older than this ignore the directives


CSO_SYSTEM = """You are the Chief Security Officer of an autonomous software-publishing pipeline. Every project ships to a public GitHub repo with a live demo on GitHub Pages. Your job is META-SECURITY: you don't audit a single project, you watch the trajectory of the whole pipeline.

You see: the security_review records of the last N shipped projects, plus their tech stacks and concepts. Your job is to spot:

- Systemic patterns of risky dependencies / deprecated CDN versions across projects
- Recurring categories of finding (e.g. "every project uses innerHTML on user input")
- Rising threat-surface trends (more network calls, more eval-shaped code, more user-text-to-LLM patterns)
- Safety drift — projects that look educational on the surface but encode techniques that could be repurposed
- Coverage gaps — security categories the per-project gate is failing to flag
- Privacy creep — projects that store more user data, do more fingerprinting, etc.

Return a strict JSON document. The next plan stage will read your `directives` and the architect MUST obey them.

OUTPUT — single JSON object, no prose, no markdown fences:
{
  "verdict": "secure" | "acceptable" | "drifting" | "alarming",
  "summary": "1-2 sentence executive summary of the security posture trend",
  "concerns": [
    "specific concerns about the trajectory — name projects and patterns"
  ],
  "directives": [
    "imperative instructions for the NEXT project. each one a single concrete thing. 0-5 entries."
  ],
  "praise": [ "what the system is doing well, security-wise (use sparingly)" ]
}

Rules for directives:
- Each is imperative, concrete, achievable in one project.
- Push the system to harden where it has been lax.
- Examples: 'The next project must add a strict <meta http-equiv=Content-Security-Policy> with default-src \\'self\\' and explicit allowlist for any CDN scripts.' / 'No project may use innerHTML with template literals containing user input — use textContent or sanitize.' / 'Any project that takes free-text input must include a visible note that the input is not sent to any server.'
"""


def _load_memory(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"projects": [], "security_audits": []}
    return json.loads(path.read_text(encoding="utf-8"))


def _save_memory(path: Path, memory: dict[str, Any]) -> None:
    path.write_text(
        json.dumps(memory, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _summarize_security_history(projects: list[dict]) -> str:
    if not projects:
        return "(no projects yet)"
    lines = []
    for p in projects:
        sec = p.get("security_review") or {}
        findings_summary = []
        for f in (sec.get("findings") or [])[:6]:
            if isinstance(f, dict):
                findings_summary.append(
                    f"{f.get('severity','?')}/{f.get('category','?')}:{f.get('issue','')[:80]}"
                )
        lines.append(
            f"- {p.get('date','?')} {p.get('name','?')}\n"
            f"    tech_stack: {', '.join(p.get('tech_stack', [])[:6])}\n"
            f"    sec_verdict: {sec.get('verdict','(no review)')}, "
            f"findings: {sec.get('findings_count', 0)}\n"
            f"    findings_detail: {findings_summary}"
        )
    return "\n".join(lines)


def latest_directives(memory: dict, ttl_hours: int = CSO_DIRECTIVE_TTL_HOURS) -> list[str]:
    audits = memory.get("security_audits", []) or []
    if not audits:
        return []
    last = audits[-1]
    issued = last.get("issued_at_unix", 0)
    age_hours = (datetime.now(timezone.utc).timestamp() - issued) / 3600.0
    if age_hours > ttl_hours:
        log.info("CSO directives are %.1fh old (>%.0fh TTL); ignoring.", age_hours, ttl_hours)
        return []
    return last.get("directives", []) or []


def run_security_audit(memory_log_path: Path = Path("memory_log.json")) -> int:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        log.error("GITHUB_TOKEN env var is required.")
        return 2
    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=token,
    )

    memory = _load_memory(memory_log_path)
    recent = (memory.get("projects") or [])[-CSO_REVIEW_WINDOW:]
    if len(recent) < 2:
        log.info("Not enough projects yet (%d). Skipping CSO audit.", len(recent))
        return 0

    summary = _summarize_security_history(recent)
    user = (
        f"Recent {len(recent)} projects' security history:\n{summary}\n\n"
        "Audit the trajectory. Issue strict directives for the NEXT project."
    )

    try:
        text, meta = roles.call_with_fallback(
            client, "cso",
            system=CSO_SYSTEM, user=user,
            max_tokens=2000, temperature=0.6,
        )
    except roles.AllModelsFailed as e:
        log.error("CSO audit failed: every model in chain unavailable. %s", e)
        return 1

    text = text.strip()
    if text.startswith("```"):
        import re
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    s, e = text.find("{"), text.rfind("}")
    if s < 0 or e < 0:
        log.error("CSO output not JSON. First 400 chars:\n%s", text[:400])
        return 1
    audit = json.loads(text[s:e + 1])

    record = {
        "issued_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "issued_at_unix": int(datetime.now(timezone.utc).timestamp()),
        "model": meta.get("model"),
        "verdict": audit.get("verdict", "acceptable"),
        "summary": audit.get("summary", ""),
        "concerns": audit.get("concerns", []) or [],
        "directives": audit.get("directives", []) or [],
        "praise": audit.get("praise", []) or [],
        "reviewed_project_count": len(recent),
    }
    memory.setdefault("security_audits", []).append(record)
    _save_memory(memory_log_path, memory)

    log.info("CSO verdict: %s | %d directives | %d concerns | model=%s",
             record["verdict"], len(record["directives"]),
             len(record["concerns"]), record["model"])
    for d in record["directives"]:
        log.info("  CSO directive: %s", d)
    return 0


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        stream=sys.stdout,
    )
    sys.exit(run_security_audit())
