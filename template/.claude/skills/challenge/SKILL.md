---
name: challenge
description: Critical review of any file or idea. Surfaces weaknesses, contradictions, and blind spots before sharing externally.
argument-hint: [file-path or topic]
allowed-tools: Read, Glob, Grep, Task, mcp__brain-search__semantic_search, AskUserQuestion
---

# Challenge

Red-team any document, plan, or idea. Returns the top weaknesses, contradictions with vault context, and missing considerations - before it leaves the building.

**Examples:**
- `/challenge 02_Themes/project-b/emails/2026-02-13_board-update.md` - Challenge a specific file
- `/challenge project-b board deck` - Challenge by topic (will search for relevant files)
- `/challenge` (no args, in-conversation) - Challenge whatever we've been working on this session

---

## Workflow

### 1. Identify the target

**If a file path is provided:** Read it directly.

**If a topic/keyword is provided:** Search the vault (semantic + grep) to find the most relevant recent file, then confirm with user before proceeding.

**If no argument:** Review the conversation context - challenge the most recent document or plan discussed.

### 2. Understand the context

Before critiquing, understand what this document is trying to do:
- **Who is the audience?** (Check theme `claude.md`, `people.md`, stakeholder templates)
- **What decision or action should it drive?**
- **What's the strategic context?** (Check `status.md`, `strategic-context.md`)

Search for:
- Previous versions or related documents on this topic
- Meeting notes where this was discussed
- Relevant framework files that should inform it
- Contradictory information elsewhere in the vault

### 3. Run five challenge lenses (parallel)

Launch ALL five lenses as parallel `Task` subagents (`subagent_type: "Explore"`) in a single message. Each receives:
- The full document text
- The audience and strategic context gathered in step 2
- Its specific lens questions below

Be direct and specific - no hedging.

**Subagent 1 - Audience Fit:**
> Would the target audience actually read this? Or would they bounce after paragraph 2? Does it match their stated preferences? (Check stakeholder profiles.) Is the ask clear within the first 30 seconds of reading? Does it answer "so what?" for THIS reader?

**Subagent 2 - Logic & Evidence:**
> Are claims supported with specific numbers, not directional language? Are there logical gaps where A doesn't actually lead to B? Are assumptions stated or hidden? Would a sceptic find the argument compelling, or just the believers?

**Subagent 3 - Vault Contradictions:**
> Search the vault for contradictions. Does this contradict anything said in previous meetings, emails, or status docs? Has the positioning shifted without acknowledging the change? Are there commitments elsewhere that conflict with what's proposed here? Does this align with the theme's `strategic-context.md`? Cite specific vault files.

**Subagent 4 - Known Blind Spots:**
> Apply your known blind spots from CLAUDE.md. <!-- CUSTOMISE: Replace with your actual blind spots -->
> Common patterns to check: (1) Architecture without execution mechanics? (2) People/change management missing? (3) Defaulting to greenfield when existing systems deserve consideration? (4) Going comprehensive when audience wants directives?

**Subagent 5 - Pre-Mortem:**
> How does this fail? What are the top 3 failure modes? What's the strongest counter-argument someone could make? What question would a key stakeholder ask that isn't answered here? What's missing that the audience expects to see?

### 4. Output format

```markdown
## Challenge: [Document/Topic Name]

### Verdict: [Strong / Needs Work / Weak]

### Top 3 Issues (fix these before sending)
1. **[Issue]** - [Specific problem + what to do about it]
2. **[Issue]** - [Specific problem + what to do about it]
3. **[Issue]** - [Specific problem + what to do about it]

### Audience Fit
[1-2 sentences on whether this lands for the intended reader]

### Vault Contradictions
[Any conflicts with other vault content, or "None found"]

### Blind Spot Check
[Which known blind spots are showing, if any]

### Pre-Mortem
- **Most likely failure:** [What goes wrong]
- **Strongest counter-argument:** [What a sceptic says]
- **Missing question:** [What the audience will ask that isn't answered]

### What's Actually Good
[1-2 genuine strengths - not filler praise]
```

---

### 5. Extract tasks

If the challenge surfaces actionable items (not just critique), immediately create tasks in `01_Todos/tasks.md` during the challenge output. The gap between insight and action is where things get lost. Don't wait for a `/transform session`.

---

## Rules

- **Be direct.** This skill exists to catch problems. Politeness that obscures the issue defeats the purpose.
- **Be specific.** "The argument is weak" is useless. "Paragraph 3 claims 40% cost reduction but the only evidence is a single pilot - the board will want at least 2 data points" is useful.
- **Cite vault sources.** If you find a contradiction, link to the file.
- **Don't pad.** If only 2 issues are significant, don't invent a third. If the document is strong, say so quickly and focus on the 1-2 things that could still bite.
- **Match the stakes.** A quick Slack message doesn't need the full five-lens treatment. A board paper does. Scale effort to consequence.
- **Verify before challenging claims.** Before calling out a claim as overclaiming, search the vault to check if it's established positioning language. Search first, challenge second.
- **British spellings** in all output.
