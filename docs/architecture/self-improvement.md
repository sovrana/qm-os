# Self-Improvement Loop

!!! abstract "TL;DR"
    The system tracks its own friction points. Suggestions that appear 3+ times become BEADs (validated improvements). Rejected framings log to a calibration file and graduate to permanent rules. After 8 weeks: 130+ suggestions extracted, 7 graduated to rules, each eliminating a recurring problem.

## What

QM gets smarter every week through two feedback mechanisms: the BEAD system (improvement suggestions tracked by frequency) and the calibration log (rejection patterns that graduate to formal rules). Neither requires manual intervention. The system observes how it's used, surfaces patterns, and promotes validated changes.

## Why

Most AI tool configurations are static. You write instructions once and they decay as your needs evolve. QM inverts this: the operating rules are a living document shaped by actual usage patterns. After 8 weeks, over 130 suggestions were extracted, 7 graduated to formal rules, and each one eliminated a recurring friction point.

## How

### The BEAD System

BEAD stands for a suggestion that's appeared 3+ times - it's validated and ready to implement.

**The flow:**

1. `/transform session` runs at the end of substantive conversations
2. It extracts improvement suggestions from the session (things Claude could do better, patterns worth codifying)
3. New suggestions are fuzzy-matched against existing ones in `improvement-suggestions.md`
4. Similar suggestions increment the count. Truly new ones are added at count 1
5. When a suggestion hits 3 occurrences, it becomes a BEAD
6. `/weekly` surfaces BEADs for implementation
7. Implemented suggestions move to an archive section

**Example progressions (real, from production):**

```
[1x] For budget discussions, create a numbers summary table early (2026-02-01)
[2x] For budget discussions, create a numbers summary table early (2026-02-15)
[3x] For budget discussions, create a numbers summary table early (2026-02-21)
[4x] BEAD - Implemented: Added to CLAUDE.md "Session Behaviour Defaults"
```

Four independent sessions surfaced the same suggestion. That's signal, not noise. The rule now fires automatically in every financial session.

```
[1x] When evaluating vendor decks, map against existing framework (2026-02-03)
[2x] When evaluating vendor decks, map against existing framework (2026-02-07)
[3x] BEAD - Implemented: Added mandatory framework grid to "External Analysis"
```

Different vendors, different weeks, same gap. The system noticed it preferred structured evaluation over freeform reactions.

```
[1x] For large file writes, use Write tool directly - background agents truncate (2026-02-06)
[2x] For large file writes, use Write tool directly - background agents truncate (2026-02-19)
[3x] BEAD - Implemented: Added to CLAUDE.md "System Operations"
```

The system caught its own bug. A background agent silently truncated a 155KB transcript to 75 lines. After three occurrences, the system now enforces direct writes for large files. Self-healing.

### What 130 Suggestions Actually Look Like

After 8 weeks, the improvement suggestions file had 130+ entries. The tier breakdown:

| Tier | Count | What happens |
|---|---|---|
| **BEADs (3+)** | ~7 | Graduated to permanent rules. Each one eliminated a recurring friction point. |
| **Building toward BEAD (2x)** | ~15 | One more occurrence validates them. Under observation. |
| **Recent (1x)** | ~110 | Fresh observations. Most never recur. |

The ~110 single observations that never recurred aren't waste. They're the filter working. If everything graduated, the rules would bloat with edge cases. The 3-occurrence threshold keeps the system lean: only patterns validated across multiple independent sessions survive.

### The Calibration Log

A parallel track for preferences and rejections. When a framing is killed ("don't use that word"), an approach is corrected ("too formal"), or a structural choice is made, it's logged in `calibration-log.md`.

**The graduation pattern:**

```
calibration-log.md (observed, append-only)
    -> 3+ similar entries
        -> Formal rule in CLAUDE.md (codified)
            -> Default behaviour (automatic)
```

This is how "stop using em dashes" goes from a one-off correction to a permanent editing rule.

### The Flywheel

```mermaid
graph LR
    A[Work Session] -->|extract| B[Suggestions]
    B -->|fuzzy match| C[Increment Count]
    C -->|3+ hits| D[BEAD]
    D -->|/weekly| E[Implement]
    E -->|update rules| F[Better Sessions]
    F --> A
```

### Improvement Suggestions File

The file tracks suggestions in three tiers:

- **BEADs (3+)** - Ready to implement. Surfaced by `/weekly`.
- **Building Toward BEAD (2x)** - One more occurrence validates them.
- **Recent (1x)** - Fresh observations. Most will never recur. That's fine.

Old suggestions (60+ days without recurrence) are archived during weekly maintenance.

## Key Insight

The 3-occurrence threshold matters. It filters noise from signal. A single suggestion might be situational. Two could be coincidence. Three means it's a real pattern worth codifying. This keeps the operating rules lean and battle-tested rather than bloated with edge cases.

## Customisation Points

- **Adjust the BEAD threshold** (2 for fast-moving environments, 5 for conservative ones)
- **Change extraction frequency** - per session, daily, or weekly
- **Add suggestion categories** to track improvement types (workflow, voice, analysis, etc.)
- **Modify archival rules** based on how fast your working patterns evolve

## Related

- [In Production](in-production.md) - Real numbers and lifecycles from 8 weeks of daily use
- [System Overview](overview.md) - Where the improvement loop sits in the seven-layer architecture
- [Six-File Memory](memory-system.md) - The calibration log is one of the six memory files
- [Skills System](skills-system.md) - `/weekly` surfaces BEADs for implementation
- [The full CLAUDE.md template](../reference/quartermaster-md.md) - Where graduated rules end up
