---
name: draft
description: Draft outbound content from vault context. LinkedIn posts, stakeholder updates, thought leadership.
argument-hint: [type] [topic]
allowed-tools: Read, Glob, Grep, Write, Edit, Task, AskUserQuestion, mcp__qm-search__semantic_search
---

# Draft

Generate outbound content - LinkedIn posts, stakeholder update emails, thought leadership pieces - synthesised from vault context. Turns internal thinking into external positioning.

**Examples:**
- `/draft linkedin AI transformation frameworks` - LinkedIn post about a framework
- `/draft email project-c-update [INVESTMENT_PARTNER]` - Project update email for [INVESTMENT_PARTNER]
- `/draft email weekly-update [TEAM_MEMBER_B]` - Weekly update email for [TEAM_MEMBER_B]
- `/draft linkedin agentic-transformation` - Thought leadership post
- `/draft thread professional-work-architecture` - LinkedIn thread (multi-post)

---

## Content Types

### `linkedin` - Single LinkedIn Post
- 150-250 words (LinkedIn sweet spot for engagement)
- Hook in first line (shows in feed preview before "...see more")
- One idea, one framework, one insight
- End with a question or provocation, not a summary
- No hashtags unless specifically asked

### `thread` - LinkedIn Thread (Multi-Post)
- 3-5 connected posts
- First post: hook + thesis
- Middle posts: evidence, examples, framework detail
- Final post: implication or question
- Each post stands alone but builds

### `email` - Stakeholder Update Email
- Apply stakeholder-specific framing from claude.md
- Lead with what changed since last communication
- Clear ask or decision point
- Follow the user's email style (prose flow, warm opening, inclusive language)

### `memo` - Internal Positioning Memo
- 1-2 pages max
- Decisions and asks up front
- Evidence-backed assertions
- Target audience explicitly stated

---

## Process

### 1. Parse input
- **Type:** linkedin | thread | email | memo
- **Topic:** framework name, theme, or specific subject
- **Audience:** inferred from type, or explicit (e.g., person name)
- If unclear, ask one question max. Don't over-clarify.

### 2. Mine the vault

Search for source material relevant to the topic:

**Semantic search** for conceptual context:
- The framework or concept being written about
- Related discussions, decisions, meeting notes

**Grep/Glob** for specific references:
- Framework definitions in `frameworks-catalog.md`
- Theme status files for current state
- Meeting notes for real examples and proof points
- Prior emails in `emails/` folders for tone calibration

**Key sources to check:**
- `02_Themes/frameworks/frameworks-catalog.md` - framework definitions
- `02_Themes/[theme]/status.md` - current context
- `02_Themes/[theme]/meetings/` - real examples
- `02_Themes/[theme]/emails/` - previous tone/framing
- `99_System/logs/conversation-discoveries/` - recent insights

### 3. Draft content

**LinkedIn posts:**
- Write in the user's voice: direct, slightly edgy, economics-first
- Use specific numbers, not vague claims
- Reference real experience without naming clients (unless cleared)
- Avoid: "In my experience...", "I'm excited to share...", "Here's the thing..."
- Good openers: A bold claim. A counterintuitive stat. A question that reframes.
- Apply ALL anti-slop rules from claude.md

**Emails:**
- Apply stakeholder-specific framing from claude.md
- Prose flow for peers (not structured memo)
- Warm but efficient
- Clear next action

### 4. Present the draft

Write draft to stdout first. Don't save to a file until approved.

After presenting:
- Ask if they want to iterate, save, or copy to clipboard
- If saving: `02_Themes/[theme]/emails/YYYY-MM-DD_[topic].md` for emails
- If clipboard: run `~/bin/md2email` for rich HTML copy
- For LinkedIn: save to `02_Themes/frameworks/content/YYYY-MM-DD_[topic].md`

---

## LinkedIn Voice Guide

**Your LinkedIn voice is NOT your internal memo voice.** Adjust:

| Internal (vault) | External (LinkedIn) |
|---|---|
| Technical architecture labels | "Three types of professional work" |
| "Orchestration layer prerequisite" | "Before AI agents work, you need..." |
| Basis point margin improvements | Percentage point equivalents |
| Framework jargon | Plain language with one memorable label |
| Comprehensive analysis | One sharp insight |

**Principles:**
- Teach, don't lecture. Share the insight, not the framework name.
- One concept per post. If it needs a table, it's too complex for LinkedIn.
- Real examples beat abstract frameworks. "At a [AMOUNT] professional services firm..." is better than "In the context of agentic transformation..."
- Controversial > comprehensive. "Most AI transformations fail because they start with AI" gets more engagement than a balanced overview.
- No client names without permission. Use descriptive proxies ("a mid-market fund admin", "a professional services competitor").

---

## Rules

- **Don't create files until asked.** Draft to stdout first.
- **One question max.** If the request is unclear, ask ONE clarifying question, then write.
- **Anti-slop is non-negotiable.** Every banned word, phrase, and structure from claude.md applies double here. External content gets scrutinised.
- **British spellings.** Always.
- **Auto-copy for emails.** If the user says "send it" or "copy it", run `~/bin/md2email` automatically.
- **No self-congratulation.** LinkedIn posts should share insight, not signal virtue.
- **Economics always.** Every post should have at least one specific number or quantified claim.
- **Batch options for short-form.** For LinkedIn hooks, taglines, email subject lines: offer 5-10 options rather than iterating one at a time. Single-proposal iteration produces 5+ rejection cycles. Batch options resolve in one round.
- **Challenge during drafting, not after.** Apply challenge criteria (audience fit, confidentiality of specific numbers, tone for recipient) DURING writing. Don't wait for a post-hoc `/challenge` to catch issues that should never have been written. Especially: don't put commercially sensitive numbers in writing to someone without NDA coverage.
- **Writing FOR vs ABOUT.** When writing a document FOR someone (not about them), check every header and column name for third-person framing. "Her Metrics, Measured" reads as about her. "Measuring What Matters" reads as for her.
