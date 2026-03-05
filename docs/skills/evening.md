# /evening - End-of-Day Reflection

| | |
|---|---|
| **Runtime** | ~5 minutes |
| **Reads** | Morning plan, `tasks.md`, session activity |
| **Writes** | Reflection appended to `daily-plan.md` |
| **Model** | Claude Code |

## What It Does

Compares what you planned against what actually happened. Surfaces slippage patterns, captures stray ideas, and sets up tomorrow's top 3.

## Why It Matters

Most productivity systems track tasks forward. Few track the gap between intention and execution backward. That gap is where the real signal lives.

If you consistently plan 7 items and complete 3, you don't have a discipline problem - you have a planning problem. `/evening` makes the pattern visible so you can calibrate.

## How It Works

```mermaid
graph LR
    A[Read morning plan] --> B[Compare to<br/>completed tasks]
    B --> C[Generate reflection<br/><small>planned vs done,<br/>slippage pattern,<br/>blockers</small>]
    C --> D[Set tomorrow's<br/>top 3]

    style A fill:#161b22,stroke:#5eead4,color:#e6edf3
    style B fill:#161b22,stroke:#5eead4,color:#e6edf3
    style C fill:#161b22,stroke:#5eead4,color:#e6edf3
    style D fill:#161b22,stroke:#5eead4,color:#e6edf3
```

### The Reflection

Output appended to `daily-plan.md`:

```markdown
## Evening Reflection

**Planned vs Done:**
| Status | Task |
|--------|------|
| Done | #project-a Investment portfolio review |
| Slipped | #project-a Quick wins identification |
| Unplanned | #system Fix daily-plan formatting |

**Completion Rate:** 3/4 planned (75%) + 1 unplanned
**What Slipped & Why:** Pattern analysis
**Blockers Discovered:** New blockers
**Tomorrow's Top 3:** Carried over + new priorities
```

### Capture Prompts

Before closing, `/evening` asks:

- **Ideas?** Routes to ideas file
- **Learnings?** Routes to memory
- **People notes?** Updates stakeholder context

### Calibration Signal

The completion rate over time is the calibration signal:

- Consistently > 80%: plans are too conservative
- Consistently < 50%: plans are too ambitious
- High variance: external interrupts are the problem, not planning

## Related

- [/morning](morning.md) - Bookend: morning plans, evening reflects
- [/show](show.md) - Related: evening uses task data for reflection
- [Self-Improvement](../architecture/self-improvement.md) - Evening patterns feed weekly improvement suggestions
- [Skills System](../architecture/skills-system.md) - How skills compose with each other
