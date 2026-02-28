---
hide:
  - toc
---

<div class="hero-intro" markdown>

# Quartermaster

<p class="subtitle">Stop re-explaining context to your AI. Every correction becomes a permanent rule. Every session builds on the last.</p>

[Get Started](quickstart.md){ .md-button .md-button--primary }
[What's Different](what-makes-this-different.md){ .md-button }
[GitHub](https://github.com/sovrana/qm-os){ .md-button }

</div>

<div class="intro-note" markdown>
Built by [Marc Lien](about.md), an AI transformation lead inside a global PE firm. I manage five workstreams across multiple portfolio companies. Every morning I'd open Claude Code and spend ten minutes re-explaining context it had yesterday. So I built a system that doesn't forget. 8 weeks of daily production use. Open source. [Read the backstory →](about.md)
</div>

<p class="section-label">Who this is for</p>

## Built for people who

- **Run on Claude Code daily** and are tired of stateless conversations
- **Manage multiple workstreams** with different stakeholders, contexts, and communication styles
- **Write documents that go through 10+ rounds** of iteration, not one-shot prompts
- **Want AI output that sounds like them**, not like a corporate chatbot

Not for you if you're looking for a chatbot wrapper, a coding assistant, or a one-click productivity hack. This is a system you build and grow over weeks.

<p class="section-label">What makes this different</p>

## Five things nothing else does

<div class="features" markdown>
<div class="feature" markdown>
<div class="feature-icon">🔄</div>
<div class="feature-text" markdown>
<strong>It gets smarter every time you use it</strong>
<span>Corrections auto-graduate into permanent rules. The system rewrites its own instructions based on your behaviour. After a month, it knows your preferences better than most human assistants.</span>
</div>
</div>
<div class="feature" markdown>
<div class="feature-icon">🧠</div>
<div class="feature-text" markdown>
<strong>It knows your context before you explain it</strong>
<span>Six-file memory architecture, session-type pre-flights, stakeholder-adapted output. Financial session starts a numbers table. Legal review flags missing cross-references. Automatically.</span>
</div>
</div>
<div class="feature" markdown>
<div class="feature-icon">✍️</div>
<div class="feature-text" markdown>
<strong>It writes like you, not like AI</strong>
<span>Voice-matched against your real writing samples. 40+ banned AI-slop words and structures. No "delve." No em dashes. Output reads like a human wrote it.</span>
</div>
</div>
<div class="feature" markdown>
<div class="feature-icon">🔍</div>
<div class="feature-text" markdown>
<strong>It makes your knowledge searchable</strong>
<span>Three-mode search across everything you've ever written. Semantic finds concepts. Keywords rank matches. Grep finds exact patterns. Run them in parallel.</span>
</div>
</div>
<div class="feature" markdown>
<div class="feature-icon">🔒</div>
<div class="feature-text" markdown>
<strong>It publishes itself safely</strong>
<span>Build with real names and real numbers. The privacy pipeline sanitises everything before it touches GitHub. This is how this site exists.</span>
</div>
</div>
</div>

[Read the full breakdown →](what-makes-this-different.md)

<p class="section-label">Get running in 3 steps</p>

## Quick start

```bash
# 1. Clone and copy the template
git clone https://github.com/sovrana/qm-os.git
cp -r qm-os/template/ ~/my-vault/ && cd ~/my-vault/

# 2. Customise CLAUDE.md (your name, your blind spots, your stakeholders)
# Search for CUSTOMISE — there are ~20 marked sections

# 3. Run your first morning plan
claude /morning
```

Needs: [Claude Code](https://docs.anthropic.com/en/docs/claude-code) + Python 3.10+ (for search) + Git. Full setup with semantic search and hooks takes [30 minutes →](quickstart.md)

<p class="section-label">A typical day</p>

## What a day looks like

<div class="timeline" markdown>
<div class="moment" markdown>
<span class="time">8:30am</span>

Open Claude Code. The session-start hook loads a dashboard: tasks due today, items waiting on people for 7+ days, unprocessed inbox items. Claude already knows what matters.
</div>
<div class="moment" markdown>
<span class="time">8:31am — /morning</span>

Claude reads your tasks, applies leverage scoring (Impact / Effort), checks strategic priorities from MEMORY.md, and generates a prioritised daily plan.
</div>
<div class="moment" markdown>
<span class="time">9:00am — /brief</span>

Before a meeting, Claude pulls the last 3 meeting notes, open tasks, waiting items, and stakeholder preferences into a one-pager. Includes "what NOT to say" based on political context.
</div>
<div class="moment" markdown>
<span class="time">11:00am — /challenge</span>

Red-team a strategy doc before sharing it with the board. Five parallel analysis lenses run simultaneously: logical holes, evidence gaps, audience fit, political risk, blind spot check.
</div>
<div class="moment" markdown>
<span class="time">5:00pm — session ends</span>

The stop hook auto-commits all changes. Search reindexes. Nothing is lost.
</div>
<div class="moment" markdown>
<span class="time">Sunday — /weekly</span>

7 parallel subagents: task audit, stale item cleanup, memory review, cross-theme connection discovery, improvement suggestions. The system gets smarter every week.
</div>
</div>

<p class="section-label">Explore</p>

## Where to start

<div class="grid" markdown>
<div class="card" markdown>
<div class="card-icon">💡</div>

### New to Claude Code?

Start here if you haven't used Claude Code before. We'll point you to the best beginner resources.

[The Essentials →](new-to-claude-code.md)
</div>
<div class="card" markdown>
<div class="card-icon">🚀</div>

### Quickstart

Clone the template, set up search, wire the hooks, customise CLAUDE.md, run your first `/morning`. 30 minutes.

[Get started →](quickstart.md)
</div>
<div class="card" markdown>
<div class="card-icon">🏗️</div>

### Architecture

How the six layers work together: vault structure, skills, hooks, memory, search, and the self-improvement loop.

[Deep dive →](architecture/overview.md)
</div>
<div class="card" markdown>
<div class="card-icon">⚡</div>

### Skills <span class="badge">7 published</span>

Daily planning, document challenge, weekly review, content transform, meeting briefs, changelogs, voice-calibrated drafting.

[Browse skills →](skills/morning.md)
</div>
<div class="card" markdown>
<div class="card-icon">📖</div>

### Reference

The full CLAUDE.md template, task format specification, anti-slop rules, and the rules system.

[Reference docs →](reference/quartermaster-md.md)
</div>
<div class="card" markdown>
<div class="card-icon">👤</div>

### About

Who built this, why it exists, and the thesis behind it.

[Read more →](about.md)
</div>
</div>

<div class="cta-bar" markdown>
**Stay in the loop.** I add new skills and documentation regularly. [Star the repo](https://github.com/sovrana/qm-os) so others can find it. Something broken or unclear? [Open an issue](https://github.com/sovrana/qm-os/issues) or [start a discussion](https://github.com/sovrana/qm-os/discussions).
</div>

<div class="feedback-line" markdown>
Built with [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). Inspired by [Claude Blattman](https://claudeblattman.com).
</div>
