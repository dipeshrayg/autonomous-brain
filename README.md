# 🤖 Autonomous Brain

A self-improving AI software-engineering pipeline. An autonomous boardroom of
LLMs designs, writes, tests, security-reviews, and publishes a brand-new
browser-runnable project several times a day. Each one more advanced than the
last, in a different domain, polished and security-cleared before publish.

📊 **Live dashboard:** https://dipeshrayg.github.io/autonomous-brain/
🔁 **Cadence:** up to 5 projects/day · ≥5 hours between projects · **Cost:** $0

Every project below is a separate public repository with a one-click playable
demo. Click **▶ Run it** on any card.

## Stats

- **Total projects:** 10 (2 today, target up to 5/day)
- **Peak complexity:** 15 (open-ended scale, no cap)
- **Average complexity:** 9.4
- **Latest run:** 2026-05-02
- **Languages explored:** JavaScript, Python
- **Patterns used recently:** visualizer, dashboard, explorer
- **Domains explored:** Mathematics, Healthcare, Environmental Science

## Latest creations

| Date | Project | Lang | ★ | Pattern | Domain | Plan model | Concepts | Run |
|------|---------|------|---|---------|--------|------------|----------|-----|
| 2026-05-02 | [data-visualization-toolkit](https://github.com/dipeshrayg/2026-05-02-data-visualization-toolkit) | JavaScript | 15 | visualizer | Mathematics | — | Real-time data visualization, Interactive parameter control, Mathematical function plotting | [▶ run](https://dipeshrayg.github.io/2026-05-02-data-visualization-toolkit/) · [⚡ codespaces](https://codespaces.new/dipeshrayg/2026-05-02-data-visualization-toolkit) |
| 2026-05-02 | [interactive-environmental-science-explorer](https://github.com/dipeshrayg/2026-05-02-interactive-environmental-science-explorer) | JavaScript | 14 | explorer | Environmental Science | — | Environmental data visualization, User interaction with drag-and-drop, Simulated real-time data updates | [▶ run](https://dipeshrayg.github.io/2026-05-02-interactive-environmental-science-explorer/) · [⚡ codespaces](https://codespaces.new/dipeshrayg/2026-05-02-interactive-environmental-science-explorer) |
| 2026-05-01 | [healthcare-simulation-dashboard](https://github.com/dipeshrayg/2026-05-01-healthcare-simulation-dashboard) | JavaScript | 12 | dashboard | Healthcare | — | Resource allocation simulation, Dynamic patient flow visualization, Interactive logs and statistics | [▶ run](https://dipeshrayg.github.io/2026-05-01-healthcare-simulation-dashboard/) · [⚡ codespaces](https://codespaces.new/dipeshrayg/2026-05-01-healthcare-simulation-dashboard) |
| 2026-05-01 | [differential-equation-visualizer](https://github.com/dipeshrayg/2026-05-01-differential-equation-visualizer) | JavaScript | 11 | visualizer | Mathematics | — | Numerical solutions of differential equations using the Runge-Kutta method, Interactive parameter adjustment for real-time updates, Dynamic visualization with phase planes and time series | [▶ run](https://dipeshrayg.github.io/2026-05-01-differential-equation-visualizer/) · [⚡ codespaces](https://codespaces.new/dipeshrayg/2026-05-01-differential-equation-visualizer) |
| 2026-05-01 | [multi-agent-systems-simulator](https://github.com/dipeshrayg/2026-05-01-multi-agent-systems-simulator) | JavaScript | 10 | — | — | — | Emergent behavior in multi-agent systems, Swarm intelligence and flocking behavior, Dynamic obstacle avoidance | [▶ run](https://dipeshrayg.github.io/2026-05-01-multi-agent-systems-simulator/) · [⚡ codespaces](https://codespaces.new/dipeshrayg/2026-05-01-multi-agent-systems-simulator) |
| 2026-04-30 | [cellular-automata-pattern-generator](https://github.com/dipeshrayg/2026-04-30-cellular-automata-pattern-generator) | JavaScript | 9 | — | — | — | Cellular automata theory, Rule-based simulation, Dynamic visualization | [▶ run](https://dipeshrayg.github.io/2026-04-30-cellular-automata-pattern-generator/) · [⚡ codespaces](https://codespaces.new/dipeshrayg/2026-04-30-cellular-automata-pattern-generator) |
| 2026-04-29 | [genetic-algorithm-art-optimizer](https://github.com/dipeshrayg/2026-04-29-genetic-algorithm-art-optimizer) | JavaScript | 8 | — | — | — | Genetic algorithms, Crossover and mutation operations, Fitness function customization | [▶ run](https://dipeshrayg.github.io/2026-04-29-genetic-algorithm-art-optimizer/) · [⚡ codespaces](https://codespaces.new/dipeshrayg/2026-04-29-genetic-algorithm-art-optimizer) |
| 2026-04-28 | [dynamic-physics-simulator](https://github.com/dipeshrayg/2026-04-28-dynamic-physics-simulator) | JavaScript | 7 | — | — | — | Physics simulation, Collision detection, Elastic collisions | [▶ run](https://dipeshrayg.github.io/2026-04-28-dynamic-physics-simulator/) · [⚡ codespaces](https://codespaces.new/dipeshrayg/2026-04-28-dynamic-physics-simulator) |
| 2026-04-28 | [maze-solver-using-a-star](https://github.com/dipeshrayg/2026-04-28-maze-solver-using-a-star) | Python | 5 | — | — | — | A* search algorithm, heuristic optimization, graph traversal | [⚡ codespaces](https://codespaces.new/dipeshrayg/2026-04-28-maze-solver-using-a-star) |
| 2026-04-28 | [basic-neural-net-trainer](https://github.com/dipeshrayg/2026-04-28-basic-neural-net-trainer) | Python | 3 | — | — | — | neural networks, gradient descent, classification | [⚡ codespaces](https://codespaces.new/dipeshrayg/2026-04-28-basic-neural-net-trainer) |

## Latest CEO review

**Verdict:** `alarming` — _issued 2026-05-02T20:18:40Z by gpt-4o_

> The system is overreaching with high-complexity projects in new domains, resulting in complete QA failures and stagnation in shipped project patterns. To stabilize and regain momentum, the next project must reduce complexity, avoid problematic patterns like 'workspace' and 'simulator', and focus on delivering a functional, single-pane project in a proven domain. The goal is to reset expectations and rebuild reliability while maintaining a small degree of innovation.


## The boardroom

This system runs as a hierarchy of LLMs with distinct roles, not a single model:

- **CEO** (`gpt-4o`) — every 6 hours, reviews recent trajectory, issues strict directives.
- **CSO** (`gpt-4o`) — every 12 hours, audits security posture across recent projects, issues security directives.
- **VP Engineering** (the watchdog) — every 15 minutes, dispatches builds when needed.
- **Chief Architect — Judge** (`gpt-4o`) — synthesizes the candidate plans into the final design.
- **Architect Candidates** (`gpt-4o-mini` + `Phi-3.5-MoE`) — propose plans in parallel.
- **Engineers** (`gpt-4o`) — implement files, one LLM call per file.
- **Code Reviewers** (`gpt-4o-mini` + `Phi-3.5-MoE`) — critique in parallel; results merged.
- **Security Officer** (`gpt-4o`) — per-project pre-publish gate. Hard veto on critical/high findings.
- **Fixer / Polisher** (`gpt-4o-mini`) — applies fixes and the final polish pass.
- **QA** (Playwright + Chromium) — mechanical headless-browser verification before publish.

---

*Generated automatically by `brain.py`. All projects are educational/diagnostic
and TOS-compliant. Last updated 2026-05-02.*
