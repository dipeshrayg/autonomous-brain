# 🤖 Autonomous Brain

> A self-improving AI software-engineering pipeline. An autonomous boardroom of LLMs designs, writes, tests, security-reviews, and publishes a brand-new browser-runnable project several times a day — each one more advanced than the last, in a different domain, polished and security-cleared before publish.

📊 **Live dashboard:** https://dipeshrayg.github.io/autonomous-brain/  
💰 **Cost to run:** $0 — powered entirely by [GitHub Models](https://github.com/marketplace/models)  
🔁 **Cadence:** Up to 5 projects/day · ≥5 hours between runs  

---

## What Is This?

Most AI coding tools use a single model to do everything. That ceiling is low.

`autonomous-brain` takes a different approach: a **hierarchy of specialised LLM agents**, each with a defined role, authority, and scope — collaborating like a real engineering organisation. The system doesn't just generate code. It manages the entire software engineering process autonomously.

Every project it produces is:
- Designed by competing architects
- Implemented by specialist engineers
- Reviewed by independent reviewers
- Security-cleared by a hard-gate security officer
- Verified by a headless browser (Playwright)
- Published as a one-click browser-runnable demo

---

## The Boardroom

```
┌─────────────────────────────────────────────────────────┐
│                    STRATEGIC LAYER                       │
│                                                         │
│   CEO (gpt-4o)              CSO (gpt-4o)               │
│   Every 6 hours             Every 12 hours              │
│   Reviews trajectory        Audits security posture     │
│   Issues directives         Issues security directives  │
└───────────────────┬─────────────────────────────────────┘
                    │ directives flow down
┌───────────────────▼─────────────────────────────────────┐
│                   EXECUTION LAYER                        │
│                                                         │
│   VP Engineering                                        │
│   Every 15 minutes · Dispatches builds                  │
│                                                         │
│   Architect A (gpt-4o-mini) ──┐                        │
│   Architect B (Phi-3.5-MoE)  ─┼─► Chief Architect/Judge│
│   [Propose in parallel]       │    (gpt-4o) synthesises │
│                               │                         │
│   Engineers (gpt-4o)          │                         │
│   [One LLM call per file]     │                         │
│                               │                         │
│   Reviewer A (gpt-4o-mini) ──┐│                        │
│   Reviewer B (Phi-3.5-MoE) ──┼┘                        │
│   [Critique in parallel]      │                         │
│                               ▼                         │
│   Security Officer (gpt-4o) ──► Hard veto gate          │
│   Fixer/Polisher (gpt-4o-mini)                         │
│   QA (Playwright + Chromium)                            │
└─────────────────────────────────────────────────────────┘
```

### Agent Roles

| Agent | Model | Fires | Responsibility |
|---|---|---|---|
| **CEO** | gpt-4o | Every 6h | Reviews trajectory, issues directives to steer domain and complexity |
| **CSO** | gpt-4o | Every 12h | Audits security posture, issues security directives |
| **VP Engineering** | — | Every 15m | Watchdog — dispatches builds, enforces cadence |
| **Architect Candidates** | gpt-4o-mini + Phi-3.5-MoE | Per build | Propose competing designs in parallel |
| **Chief Architect / Judge** | gpt-4o | Per build | Synthesises the best proposal into a final spec |
| **Engineers** | gpt-4o | Per file | Implement the spec — one focused LLM call per file |
| **Code Reviewers** | gpt-4o-mini + Phi-3.5-MoE | Per build | Independent parallel critique — results merged |
| **Security Officer** | gpt-4o | Per build | Hard veto: critical/high findings block publish |
| **Fixer / Polisher** | gpt-4o-mini | Per build | Applies review fixes and runs final polish pass |
| **QA** | Playwright + Chromium | Per build | Headless browser verification before publish |

---

## Self-Improvement

Each project is assigned a **complexity score**. The CEO tracks this metric across runs.

If complexity stagnates or regresses, the CEO issues a directive forcing the next Architect to push harder. This is not just a prompt — it's a tracked, enforced feedback loop built into the pipeline architecture.

### Current Stats
| Metric | Value |
|---|---|
| Total projects shipped | 28 |
| Peak complexity | 43 |
| Average complexity | 21.5 |
| Domains explored | 8+ |
| Languages | HTML+JS, JavaScript, Python, Markdown |

### Domains Covered
Mathematics · Healthcare · Environmental Science · Logistics · Arts · Cryptography · Bioinformatics · Game Design · History · Generative Art

---

## Why Multi-Agent?

| Problem with single-model approaches | How multi-agent solves it |
|---|---|
| Context pollution across design/implement/review | Fresh, scoped context per agent role |
| Model agrees with its own proposals | Two competing architects, one judge |
| Security is an afterthought | Hard-gate Security Officer with veto power |
| Complexity drifts without enforcement | CEO tracks metrics and issues binding directives |
| No parallelism | Architects and reviewers run in parallel async |

---

## Running Cost: $0

The entire pipeline — CEO, architects, engineers, reviewers, security, QA — runs on **GitHub Models**, which provides free access to:
- `gpt-4o`
- `gpt-4o-mini`
- `Phi-3.5-MoE`

No credit card. No cloud spend. The only resource used is GitHub Actions runner minutes (free within tier limits).

---

## Live Projects

Every project the system ships is a separate public repository with a one-click demo. No setup. No dependencies. Click and it runs in the browser.

**See all 28 projects:** [dipeshrayg.github.io/autonomous-brain](https://dipeshrayg.github.io/autonomous-brain/)

---

## Architecture Notes

- `brain.py` — the core orchestrator that coordinates all agents
- CEO and CSO directives are persisted and injected into downstream agent prompts
- The Security Officer receives only the finished code, not the design discussion — ensuring it sees what an attacker would see
- Playwright QA runs headless Chromium and verifies the project loads and passes basic interaction checks before any publish step

---

## Roadmap

- [ ] Long-term memory across projects for the CEO (currently reviews recent output only)
- [ ] Specialist engineer agents (frontend, backend, security) instead of generalist per-file
- [ ] Open-source `autonomous-brain-engine` (Python orchestrator) — pending API key handling cleanup
- [ ] External contributor mode — allow external prompts to influence CEO directives
- [ ] Complexity benchmark dataset for evaluating project quality beyond self-assessed scores

---

## Related

- [autonomous-brain-engine](https://github.com/dipeshrayg/autonomous-brain-engine) — the private Python orchestrator (open-sourcing soon)
- [Dev.to writeup](https://dev.to/dipeshray) — full architecture walkthrough

---

*Built by [Dipesh Ray](https://github.com/dipeshrayg) · Computing Systems student, London*  
*All generated projects are educational and TOS-compliant.*
