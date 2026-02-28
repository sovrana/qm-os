# Quartermaster

A personal AI operating system that runs 24/7, processes meetings autonomously, manages your tasks, red-teams your work, and gets smarter every week. Built by a business exec who got tired of re-explaining context every morning.

**[Full documentation](https://sovrana.github.io/qm-os)** | **[What's different](https://sovrana.github.io/qm-os/what-makes-this-different/)** | **[Quickstart](https://sovrana.github.io/qm-os/quickstart/)**

---

## What this actually does

Your morning starts with a Telegram message: today's priorities, auto-drafted follow-ups for items slipping past 7 days, a waiting item flagged for escalation. You haven't opened your laptop.

You open Claude Code. The session-start hook loads a dashboard: tasks due today, items waiting on people, unprocessed inbox files, high-leverage quick wins. Yesterday's context is already in memory.

You record a meeting. Drop the transcript. Walk away. An hour later it's been auto-processed: decisions, actions, and insights extracted, routed to the right theme folder, action items appended to your task list. You didn't run a single command.

Before the board paper goes out, `/challenge` runs 5 independent agents in parallel: audience fit, logic gaps, vault contradictions, your known blind spots, and a pre-mortem. Verdict: Needs Work. Top issue: execution mechanics missing. Three fixes pushed to your task list.

The system gets smarter every week. Corrections auto-graduate into permanent rules. A weekly review surfaces improvements. After a month, it knows your preferences better than most human assistants.

8 weeks of daily production use. Not a proof of concept.

## Quick start

```bash
# 1. Clone and copy the template
git clone https://github.com/sovrana/qm-os.git
cp -r qm-os/template/ ~/my-vault/ && cd ~/my-vault/

# 2. Customise CLAUDE.md (your name, your blind spots, your stakeholders)
# Search for CUSTOMISE - there are ~20 marked sections

# 3. Run your first morning plan
claude /morning
```

Needs: [Claude Code](https://docs.anthropic.com/en/docs/claude-code) + Python 3.10+ (for search) + Git. Full setup with semantic search and hooks takes [30 minutes](https://sovrana.github.io/qm-os/quickstart/).

## Seven-layer architecture

```
Interface ─── Claude Code (deep work) + Obsidian/Telegram (mobile capture)
    │
Daemon ────── Always-on bot on a second machine. Hourly heartbeat:
    │         inbox processing, waiting alerts, morning plan, evening summary.
    │
Vault ─────── 00_Inbox/ → 01_Todos/ → 02_Themes/ → 03_Reference/ → 99_System/
    │         Plain markdown. Obsidian-compatible. Git-versioned. No database.
    │
Skills ────── 7 published SKILL.md files. Type /morning, get a prioritised plan.
    │         Write your own in 10 minutes.
    │
Hooks ─────── session-start (context load) → post-write (reindex) → session-stop (auto-commit)
    │         Zero manual maintenance.
    │
Memory ────── 6 files survive between sessions: live state, voice calibration,
    │         rejection patterns, cross-theme connections, stakeholder postures, decisions.
    │
Search ────── Semantic (concepts) + BM25 (keywords) + Grep (exact match)
              Run in parallel. Everything you've ever written, searchable in seconds.
```

[Architecture deep dive →](https://sovrana.github.io/qm-os/architecture/overview/)

## Skills

| Skill | What it does | Time |
|-------|-------------|------|
| `/morning` | Prioritised daily plan with leverage scoring and draft follow-ups | ~5 min |
| `/brief` | Pre-meeting one-pager: last 3 meetings, open tasks, "what NOT to say" | ~2 min |
| `/challenge` | 5 parallel red-team lenses: audience fit, logic, contradictions, blind spots, pre-mortem | ~5 min |
| `/transform` | Process transcript into structured knowledge: decisions, actions, insights, routing | ~5 min |
| `/draft` | Voice-calibrated outbound content: LinkedIn, emails, memos | ~5 min |
| `/weekly` | Full system audit: 7 parallel subagents for task cleanup, memory refresh, self-improvement | ~30 min |
| `/changelog` | View or log iteration decisions. Contradiction detection built in | ~1 min |

I've built another 10+ for my own workflows. Writing a new skill takes under 10 minutes. [How skills work →](https://sovrana.github.io/qm-os/architecture/skills-system/)

## The self-improvement loop

This is the part that compounds:

1. You correct something ("don't use that framing", "too formal", "wrong audience")
2. It logs to `calibration-log.md` with what was tried, what replaced it, and why
3. Same pattern appears 3+ times? Graduates to a permanent rule in CLAUDE.md
4. The system literally rewrites its own instructions

After 8 weeks: dozens of rules discovered through use, not designed upfront. The calibration log is the primary artifact for institutional memory transfer.

## Who this is for

- **Use AI for real work** and want something that compounds instead of resetting every session
- **Manage multiple workstreams** with different stakeholders, contexts, and communication styles
- **Process meetings and transcripts** and need decisions extracted automatically
- **Build AI systems** and want battle-tested architecture patterns for memory, search, and agent orchestration

Whether you're coming from ChatGPT, already running Claude Code, or building your own AI systems - [pick your starting point](https://sovrana.github.io/qm-os/new-to-claude-code/).

## Built by

Marc Lien. Senior Advisor at [Warburg Pincus](https://www.warburgpincus.com/), focused on AI transformation of professional services businesses. Before PE: McKinsey, then Managing Director and CEO of MBNA at Lloyds Banking Group. [More →](https://sovrana.github.io/qm-os/about/)

## License

MIT
