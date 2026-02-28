# Get Started

Pick your starting point. Each path gets you to a working Quartermaster setup - they just start from different places.

<div class="path-cards" markdown>
<div class="path-card" markdown>
<div class="path-icon">💬</div>

### I use ChatGPT or Claude chat

You know AI is powerful but you're copy-pasting between browser tabs. You want something that works inside your actual files and remembers what you told it yesterday.

[Start here ↓](#path-1-from-chatgpt-to-quartermaster)
</div>
<div class="path-card" markdown>
<div class="path-icon">⚡</div>

### I use Claude Code already

You run Claude Code daily but every session starts from zero. You want persistent memory, automated workflows, and skills that encode your operating patterns.

[Start here ↓](#path-2-from-claude-code-to-quartermaster)
</div>
<div class="path-card" markdown>
<div class="path-icon">🏗️</div>

### I build AI systems

You want the architecture patterns. Seven-layer design, self-improvement loops, three-mode search, hook automation. Built for forking and adapting.

[Start here ↓](#path-3-the-architecture)
</div>
</div>

## Path 1: From ChatGPT to Quartermaster

You're used to AI that lives in a browser tab. You type a question, get an answer, close the tab. Next time you start over.

Quartermaster is different in three ways:

**Claude Code works inside your files.** It's not a chat window. It runs in your terminal, reads your documents, edits them directly, runs commands. When you say "update the budget table," it opens the file and changes it. No copy-paste.

**Quartermaster adds memory.** Claude Code on its own is stateless - each conversation starts fresh. Quartermaster wraps it in a system that remembers your decisions, your stakeholders, your preferences, your blind spots. Session 50 is smarter than session 1.

**The system works while you sleep.** A daemon runs on a second machine, processing your inbox, flagging slipping tasks, sending you a morning plan via Telegram before you open your laptop. You don't need to be at your desk for the system to work.

### What you need to do

1. **Install Claude Code** - follow [Anthropic's official guide](https://docs.anthropic.com/en/docs/claude-code). Takes 10 minutes.
2. **Learn the basics** - Chris Blattman's [claudeblattman.com](https://claudeblattman.com) is the best beginner's guide. He's not a programmer, which makes his explanations clear for non-technical users.
3. **Run a few conversations** - get comfortable with Claude Code reading and editing files.
4. **Come back and run the [Quickstart](quickstart.md)** - 30 minutes to a working Quartermaster setup.

### Do I need to code?

No. The Quickstart involves running a few terminal commands (copy-paste), but everything after that is natural language. You tell Claude what you want. The system handles the rest.

## Path 2: From Claude Code to Quartermaster

You already know what Claude Code can do. Here's what it can't do on its own - and what Quartermaster adds.

| Claude Code alone | With Quartermaster |
|---|---|
| Every session starts blank | CLAUDE.md + MEMORY.md load your full context automatically |
| You remember what matters | The system tracks decisions, contradictions, and rejected alternatives |
| You run commands manually | 7 core skills included: `/morning`, `/challenge`, `/brief`, `/transform`, and more. Write your own in 10 minutes |
| Corrections disappear | Calibration log captures every correction, patterns graduate to permanent rules |
| Search = grep | Three-mode search: semantic + BM25 + grep in parallel |
| Nothing happens between sessions | Heartbeat daemon processes inbox, flags stale items, sends Telegram alerts |

### What you need to do

1. **Run the [Quickstart](quickstart.md)** - 30 minutes. Clone, configure, run `/morning`.
2. **Process a few real items** - drop a transcript through `/transform`, run `/challenge` on a document, let the calibration log start capturing your corrections.
3. **Explore the [Architecture](architecture/overview.md)** - understand the seven layers so you can extend the system yourself.

## Path 3: The Architecture

You want to understand the design decisions. Here's the system in engineering terms.

**Seven layers, each independent, together they compound:**

1. **Vault** - Obsidian-compatible markdown folder structure. Themes, tasks, reference, inbox. No database. No lock-in. Git-versioned. [Folder structure →](architecture/folder-structure.md)

2. **Skills** - Reusable SKILL.md files that encode complex workflows as slash commands. Each skill declares what it reads, what it writes, and which model to use. [Skills system →](architecture/skills-system.md)

3. **Hooks** - Shell scripts triggered on session start, session end, and file write. The session-start hook loads a dashboard. The session-end hook auto-commits. The file-write hook reindexes search. [Hooks →](architecture/hooks.md)

4. **Always-On Daemon** - A Telegram bot on a second machine, connected via iCloud sync. Hourly heartbeat processes inbox, flags waiting items, sends morning plans and evening summaries. [Always-on daemon →](architecture/always-on.md)

5. **Memory** - Six files that give Claude persistent context: CLAUDE.md (identity + rules), MEMORY.md (live state), calibration-log.md (corrections), connections.md (cross-theme links), voice-exemplars.md (writing samples), stakeholder-live.md (people dynamics). [Memory system →](architecture/memory-system.md)

6. **Search** - Three modes in parallel: semantic (concepts), BM25 (keywords), grep (exact match). Different retrieval strategies for different query types. [Search architecture →](architecture/search.md)

7. **Self-improvement** - Corrections log to a calibration file. Patterns that appear 3+ times graduate to permanent rules. A weekly review surfaces improvements. The system rewrites its own instructions. [Self-improvement loop →](architecture/self-improvement.md)

**Key design decisions:**

- **Local-first.** Everything is markdown files on disk. No cloud dependency beyond the LLM API. Full git history.
- **Two-machine architecture.** Your working machine runs Claude Code. A second machine runs an always-on daemon for heartbeat processing, Telegram alerts, and autonomous inbox handling. [Details →](architecture/always-on.md)
- **Rules, not prompts.** Behaviour is governed by CLAUDE.md files at global, theme, and project levels. Conditional rules load only when working in matching directories. This is configuration-as-code for AI assistants.
- **Accumulation over optimisation.** Every session makes the next one better. Corrections become rules. Rules become habits. The value compounds.

### What you need to do

1. **Read the [Architecture Overview](architecture/overview.md)** - the full seven-layer breakdown.
2. **Fork the [template repo](https://github.com/sovrana/qm-os)** - adapt the structure to your workflow.
3. **Run the [Quickstart](quickstart.md)** - get it running, then modify.

### What's worth stealing even if you build your own

- The **calibration log → rule graduation** pattern (corrections compound into permanent behaviour)
- **Three-mode parallel search** (semantic + BM25 + grep covers all retrieval failure modes)
- **CLAUDE.md tiered architecture** (global rules + conditional theme rules + skill-specific instructions)
- **Contradiction detection** in document changelogs (catches when you reverse a previous decision)
- **Leverage scoring** for task prioritisation (Impact / Effort trumps due dates)
