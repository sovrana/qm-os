# What 2+ Months of Production Use Looks Like

!!! abstract "TL;DR"
    Architecture pages explain mechanisms. This page shows results. Real numbers, real lifecycles, real examples of the system rewriting itself - all from 2+ months of daily production use managing multiple domains.

## The Numbers

After 2+ months of daily use across 5 active domains:

| Metric | Count | What it means |
|---|---|---|
| Improvement suggestions extracted | 130+ | Raw observations from `/transform session` |
| Graduated to permanent rules (BEADs) | 7 | Validated patterns now running automatically |
| Calibration log entries | 60+ | Voice, framing, and structure corrections |
| Cross-theme connections discovered | 12 | Non-obvious links between domains |
| Suggestions that never recurred | ~110 | The filter working correctly |

The ratio matters. 7 out of 130+ graduated. That's a ~5% promotion rate. Everything else was either too situational to generalise or didn't recur. A system that promoted everything would drown in rules. The threshold keeps it lean.

## A BEAD Lifecycle: Budget Table Rule

**Day 1 (Session: financial review)**
The system notices it should have created a numbers summary table at the start of a budget discussion. Logs the suggestion at count 1.

**Day 15 (Session: different project, different budget)**
Same gap surfaces independently. Count increments to 2. Still under observation.

**Day 21 (Session: third project, PE document review)**
Third occurrence. The suggestion becomes a BEAD: validated and ready to implement.

**Day 22 (Implementation)**
`/weekly` surfaces the BEAD. One line added to CLAUDE.md session defaults:

```
Financial/budget sessions: Create a numbers summary table early.
```

**Day 23 onwards**
Every financial session now opens with a structured numbers table automatically. The system learned a behaviour from three independent observations across 16 days. No one asked it to. The pattern was extracted, tracked, validated, and codified without manual intervention.

A fourth occurrence appeared later, further confirming the pattern. By then, it was already running.

## A Calibration That Became a Permanent Rule

**The correction:**
During a strategy session, Claude hedged: "It could potentially indicate..." and "There might be an opportunity to..."

The response: "Commit to a take. 'It depends' is a last resort."

**The log entry:**
```
**[Voice | REJECTED]** Hedging language ("it could potentially",
  "there might be") -> Commit to a take
Why: Wants opinions, not options.
```

**The graduation:**
Similar corrections appeared across multiple sessions: "Have an opinion", "Don't give me three options, tell me which one", "Stop hedging." The pattern promoted to a permanent rule in the Vibe section of CLAUDE.md:

```
Have opinions. Commit to a take. "It depends" is a last resort,
not a default.
```

Now every session, across every topic, starts with that rule loaded. The hedging stopped. One correction, properly logged and promoted, eliminated a class of friction permanently.

## A Connection That Shifted Strategy

During a session about personal productivity tooling - completely unrelated to platform strategy - the system noticed something:

> The personal vault uses three-tier knowledge retrieval, automated inbox processing, a changelog as decision trace, and persistent context. Built from zero to production in under 2 months.

It logged a cross-theme connection:

```
### Personal system validates platform thesis
- Bridges: #personal-productivity + #platform-strategy
- Claim: The personal system IS the accumulation thesis
  running on one person. Proves the architecture works
  before selling it to clients.
- Added: 2026-02-21
```

That connection - discovered by the system, not by deliberate analysis - became a talking point in a subsequent stakeholder meeting. "I'm not proposing theoretical architecture. I've been running it for two months." The connection file turned an accidental insight into a strategic asset.

## The Session Close Ritual

Every substantive session ends with a scan for three things:

1. **Unlogged calibrations** - Corrections that happened during the session but weren't captured in `calibration-log.md`
2. **Unlogged connections** - Cross-theme links discovered but not yet in `connections.md`
3. **Rule candidates** - Patterns that should be saved to CLAUDE.md

This isn't optional. The commit message notes what was captured. Missing a calibration means the same mistake can recur tomorrow. Missing a connection means a strategic insight dies with the session.

The ritual takes 30 seconds. It's the difference between a system that remembers and one that forgets.

## The Changelog System

Every important document gets automatic iteration tracking. When a section is added, removed, or structurally changed, a changelog entry is created:

```
## Round 3 (2026-02-25)

**Changed:** Moved "thought partner" from first to last position
**Why:** Lead with operational work, end with the relationship
**Decided:** Six items (not five, not eight). Each with a single measure.
**Rejected:** First-person possessive framing ("What I Own")
```

The system also detects contradictions. If Round 5 reverses a Round 2 decision, it flags it:

> "This reverses the Round 2 decision to lead with the relationship dimension. Intentional?"

Over 20+ rounds of iteration on a single document (normal for high-stakes deliverables), the changelog becomes the decision history. Why was that section removed? Check the changelog. Was this framing tried before? Check the changelog. It prevents relitigating settled questions and preserves the reasoning behind structural choices.

## What the System Knows After 8 Weeks

By week 8, the accumulated institutional memory includes:

- **7 session-type defaults** that fire automatically (financial, legal, PE, retrospective, vendor analysis, negotiation, construction)
- **60+ calibration entries** covering voice, framing, structure, and stakeholder preferences
- **A banned words list** of 30+ AI-slop terms, each discovered through actual corrections
- **Communication rules** calibrated per stakeholder (one gets 180 words max with metrics leading; another gets conversational prose)
- **12 cross-theme connections** linking domains in non-obvious ways
- **Anti-patterns** codified from real failures (overclaiming maturity, mixing strategic observations with resource asks, editing others' documents too aggressively)

None of this was designed upfront. It was discovered, validated, and promoted through use. The system on day 1 was a blank CLAUDE.md with basic instructions. The system on day 56 is a calibrated operating manual that knows how its user thinks, writes, and decides.

That's the point. You don't configure it. You grow it.

## Related

- [Self-Improvement Loop](self-improvement.md) - The BEAD mechanism that drives suggestion-to-rule graduation
- [Six-File Memory](memory-system.md) - The calibration log, connections register, and other memory files
- [The full CLAUDE.md template](../reference/quartermaster-md.md) - Where graduated rules end up
