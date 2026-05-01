# 🤖 Autonomous Brain

A self-improving software-engineering pipeline. Every day at 06:17 UTC, a
GitHub Action wakes up, asks an LLM (free GitHub Models) to design a brand-new
browser-runnable project that's more advanced than yesterday's. The pipeline:

1. **Plan** — architect the project at the design level.
2. **Implement** — generate each file in its own LLM call.
3. **Critique + Browser-verify** — review with senior-engineer prompt + run the
   page in real headless Chrome to detect blank canvases, JS errors, missing
   controls, and so on.
4. **Fix** — feed every issue back to the LLM and iterate (up to 3 cycles).
5. **Polish** — final pass for visual quality, animations, accessibility.
6. **Final-verify + publish** — confirm the polished version still works, then
   create a public repo and enable GitHub Pages.

📊 **Live dashboard:** https://dipeshrayg.github.io/autonomous-brain/
🔁 **Schedule:** daily 06:17 UTC (backup 18:17 UTC) · **Cost:** $0 · **Source:** [`brain.py`](brain.py)

## Stats

- **Total projects:** 8 (3 today, target 2/day)
- **Peak complexity:** 12 (open-ended scale, no cap)
- **Average complexity:** 8.1
- **Latest run:** 2026-05-01
- **Languages explored:** JavaScript, Python
- **Patterns used recently:** visualizer, dashboard
- **Domains explored:** Mathematics, Healthcare

## Latest creations

| Date | Project | Lang | ★ | Pattern | Domain | Plan model | Concepts | Run |
|------|---------|------|---|---------|--------|------------|----------|-----|
| 2026-05-01 | [healthcare-simulation-dashboard](https://github.com/dipeshrayg/2026-05-01-healthcare-simulation-dashboard) | JavaScript | 12 | dashboard | Healthcare | gpt-4o | Resource allocation simulation, Dynamic patient flow visualization, Interactive logs and statistics | [▶ run](https://dipeshrayg.github.io/2026-05-01-healthcare-simulation-dashboard/) · [⚡ codespaces](https://codespaces.new/dipeshrayg/2026-05-01-healthcare-simulation-dashboard) |
| 2026-05-01 | [differential-equation-visualizer](https://github.com/dipeshrayg/2026-05-01-differential-equation-visualizer) | JavaScript | 11 | visualizer | Mathematics | — | Numerical solutions of differential equations using the Runge-Kutta method, Interactive parameter adjustment for real-time updates, Dynamic visualization with phase planes and time series | [▶ run](https://dipeshrayg.github.io/2026-05-01-differential-equation-visualizer/) · [⚡ codespaces](https://codespaces.new/dipeshrayg/2026-05-01-differential-equation-visualizer) |
| 2026-05-01 | [multi-agent-systems-simulator](https://github.com/dipeshrayg/2026-05-01-multi-agent-systems-simulator) | JavaScript | 10 | — | — | — | Emergent behavior in multi-agent systems, Swarm intelligence and flocking behavior, Dynamic obstacle avoidance | [▶ run](https://dipeshrayg.github.io/2026-05-01-multi-agent-systems-simulator/) · [⚡ codespaces](https://codespaces.new/dipeshrayg/2026-05-01-multi-agent-systems-simulator) |
| 2026-04-30 | [cellular-automata-pattern-generator](https://github.com/dipeshrayg/2026-04-30-cellular-automata-pattern-generator) | JavaScript | 9 | — | — | — | Cellular automata theory, Rule-based simulation, Dynamic visualization | [▶ run](https://dipeshrayg.github.io/2026-04-30-cellular-automata-pattern-generator/) · [⚡ codespaces](https://codespaces.new/dipeshrayg/2026-04-30-cellular-automata-pattern-generator) |
| 2026-04-29 | [genetic-algorithm-art-optimizer](https://github.com/dipeshrayg/2026-04-29-genetic-algorithm-art-optimizer) | JavaScript | 8 | — | — | — | Genetic algorithms, Crossover and mutation operations, Fitness function customization | [▶ run](https://dipeshrayg.github.io/2026-04-29-genetic-algorithm-art-optimizer/) · [⚡ codespaces](https://codespaces.new/dipeshrayg/2026-04-29-genetic-algorithm-art-optimizer) |
| 2026-04-28 | [dynamic-physics-simulator](https://github.com/dipeshrayg/2026-04-28-dynamic-physics-simulator) | JavaScript | 7 | — | — | — | Physics simulation, Collision detection, Elastic collisions | [▶ run](https://dipeshrayg.github.io/2026-04-28-dynamic-physics-simulator/) · [⚡ codespaces](https://codespaces.new/dipeshrayg/2026-04-28-dynamic-physics-simulator) |
| 2026-04-28 | [maze-solver-using-a-star](https://github.com/dipeshrayg/2026-04-28-maze-solver-using-a-star) | Python | 5 | — | — | — | A* search algorithm, heuristic optimization, graph traversal | [⚡ codespaces](https://codespaces.new/dipeshrayg/2026-04-28-maze-solver-using-a-star) |
| 2026-04-28 | [basic-neural-net-trainer](https://github.com/dipeshrayg/2026-04-28-basic-neural-net-trainer) | Python | 3 | — | — | — | neural networks, gradient descent, classification | [⚡ codespaces](https://codespaces.new/dipeshrayg/2026-04-28-basic-neural-net-trainer) |

## Latest CEO review

**Verdict:** `drifting` — _issued 2026-05-01T22:59:01Z by gpt-4o_

> The pipeline is drifting toward superficial complexity and repetitive projects, with an overuse of visualizers and academic domains. While raw complexity has increased, user experience, domain diversity, and real-world relevance are lacking, and the projects do not appear polished or innovative. The next project must break this pattern by incorporating a multi-pane layout, a significant backend simulation, and exploration of a novel, practical domain with improved user experience and visual design.

**Active directives** (architect must obey):
- The next project must include a multi-pane workspace layout (e.g., left sidebar for configuration, main canvas for visualization, and right panel for detailed data or logs). Avoid single-pane layouts entirely.
- Develop a project with a substantial backend component that simulates a real-world use case (e.g., a live data feed, a fake marketplace with transactions, or a supply chain simulation). The backend must meaningfully interact with the front end.
- Explore a completely new domain that has not been touched in recent projects, such as healthcare, finance, e-commerce, or social networks. Avoid Mathematics and pure visualizers.
- Incorporate keyboard shortcuts and advanced interaction mechanisms to improve user experience. For example, allow users to control the application without relying solely on mouse clicks.
- Design a project that uses a unique and polished visual identity, including a new typography pairing and a cohesive color scheme. Track the visual_identity field and ensure it is distinct from prior projects.
- Create a project with a clear, practical use case and ensure it is polished to a level that a senior engineer would ship. Avoid projects that feel like theoretical exercises or academic proofs of concept.

**Concerns:**
- The recent projects show a consistent increase in complexity, but the added complexity appears superficial — the projects are not significantly advancing in terms of user experience or innovation.
- The 'visualizer' pattern is over-represented, and the projects are beginning to feel repetitive, particularly in the Mathematics domain (e.g., 'differential-equation-visualizer', 'cellular-automata-pattern-generator').
- Despite the increasing complexity, user experience remains weak. Projects are lacking multi-pane layouts, real-time interactivity, and features that go beyond basic controls like sliders and buttons.
- There is minimal exploration of new domains or real-world applications. Recent projects are heavily focused on academic or abstract concepts (e.g., neural nets, cellular automata, differential equations) without practical utility or relevance.


## The boardroom

This system runs as a hierarchy of LLMs with distinct roles, not a single model:

- **CEO** (`gpt-4o`) — runs every 6 hours, reviews recent trajectory, issues strict directives the architect must obey. See above.
- **VP Engineering** (the watchdog) — fires every 15 minutes, dispatches builds when the system is below target.
- **Chief Architect — Judge** (`gpt-4o`) — synthesizes the candidate plans into the final design.
- **Architect Candidates** (`Mistral-Large` + `Llama-3.1-70B`) — propose plans in parallel.
- **Engineers** (`gpt-4o`) — implement files, one LLM call per file.
- **Code Reviewers** (`Mistral-Large` + `Llama-3.1-70B`) — critique in parallel; results merged.
- **Fixer / Polisher** (`gpt-4o-mini`) — applies fixes and the final polish pass.
- **QA** (Playwright + Chromium) — mechanical headless-browser verification before publish.

---

*Generated automatically by `brain.py`. All projects are educational/diagnostic
and TOS-compliant. Last updated 2026-05-01.*
