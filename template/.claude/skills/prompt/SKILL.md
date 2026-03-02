{"name": "qm-prompt", "description": "Structure messy thinking into clean executable briefs", "user-invocable": true}

# Prompt

Take unstructured input (dictated thoughts, rambling voice notes, stream-of-consciousness text) and structure it into a clean, actionable brief.

This skill sits upstream of execution. It turns "what you're thinking" into "what Claude should do."

## When to Use

- `/prompt` with pasted text - Structure rambling thoughts into a brief
- `/prompt [file]` - Structure a voice transcript or text file
- `/prompt` with no args - Ask user to paste or dictate what's on their mind

**Not for:**
- Processing meeting transcripts (use `/transform`)
- Exploring vault context before writing (use `/prep`)
- Capturing a quick task (use brain-capture or just say it)

## Process

### 1. Ingest the Raw Input

Accept input from:
- **Pasted text** in $ARGUMENTS or the message body
- **File path** - Read the file (MacWhisper transcript, text dump, etc.)
- **No input** - Ask: "What's on your mind? Paste text, point me to a file, or just talk."

If the input is a MacWhisper transcript, strip timestamps and speaker labels. Focus on the user's words, not the transcript metadata.

### 2. Identify the Intent

Read the messy input and determine what the user is actually trying to accomplish. Ask yourself:

- **What do they want to exist that doesn't exist yet?** (A document, an email, a plan, a decision, an analysis)
- **Who is it for?** (Themselves, a specific stakeholder, a group)
- **What's the implicit quality bar?** (Quick and dirty, or polished and strategic)
- **Is there a deadline signal?** ("Before Monday", "for the meeting", "at some point")

Don't ask to clarify unless the intent is genuinely ambiguous. If they dictated it while walking, they don't want 4 follow-up questions. Make your best read and let them correct.

### 3. Structure the Brief

Output a clean brief with these sections. Skip any section that doesn't apply.

```
## Brief

**Goal:** [One sentence. What needs to exist when this is done.]

**Context:** [2-3 sentences. What the user knows that Claude needs to know. Pull from the raw input - don't pad with vault searches yet.]

**Audience:** [Who will read/use the output. Skip if it's just for the user.]

**Constraints:**
- [Hard requirements extracted from the input]
- [Implicit constraints not stated but clearly intended - flag these as "Inferred:"]

**Output:** [What the deliverable looks like. Format, length, tone.]

**Success looks like:** [One sentence. The "done" test.]
```

### 4. Suggest the Next Move

After the brief, suggest what to do with it:

- **If it's a writing task** - "Run `/draft` or `/prep [theme] [stakeholder]` against this brief"
- **If it's a strategic analysis** - "Start a session with this brief as the opening prompt"
- **If it's a vault task** - "This maps to `/transform`, `/weekly`, `/inbox`, etc."
- **If it's a thinking exercise** - "Want to work through this now, or save the brief to [theme]/context/ for later?"
- **If it routes to a specific skill** - Name it explicitly

Don't auto-execute. The brief is the deliverable. The user decides what to do with it.

### 5. Save Option

If the brief is substantial (not a one-liner), offer:
- "Save to `00_Inbox/briefs/YYYY-MM-DD_[slug].md`?"

Only save if the user says yes. Most briefs are immediate-use and don't need filing.

## Edge Cases

**Input is already structured:** If they paste something that's already a clear prompt, say so. "This is already clean. Want me to tighten it or just run it?"

**Input is a task, not a brief:** If it's clearly a single action item ("remind me to call someone"), route to brain-capture instead. Don't over-structure a simple task.

**Input is very long (>2000 words):** Likely a raw transcript or brain dump. Summarise the key threads first, then ask: "I see 3 threads here: [A], [B], [C]. Structure all three, or focus on one?"

**Multiple distinct asks:** If the input contains several unrelated things, split into separate briefs. Number them.

**Emotional/venting content:** Sometimes users dictate frustration alongside actionable content. Extract the action, acknowledge the energy, skip the therapy. "Sounds like [X] is frustrating. Here's what I think you actually want done:"

## Examples

**Input:** "I need to write something for the investment partner about how the project went, the whole thing, what we proved, what the methodology looks like, maybe position it as the playbook for other portfolio companies"

**Output:**
```
## Brief

**Goal:** Strategic memo positioning a completed project as proof-of-concept for a replicable AI transformation methodology.

**Audience:** Investment partner - lead with quantified outcomes, methodology second.

**Context:** Project engagement recently ended. Board approved next phase investment. Need to convert success into funding conviction for a platform entity.

**Constraints:**
- Must include specific metrics (margin impact, timeline compression, cost benchmarks)
- Position as portfolio-replicable, not one-off consulting
- Inferred: Tone should be confident but not overclaiming - partner values evidence over ambition

**Output:** 2-3 page strategic memo. Economics-first framing. Include "before/after" proof points.

**Success looks like:** Partner reads it and asks "which portfolio company is next?" not "prove it works."

-> Run `/prep [project] [stakeholder]` with this brief as input.
```

---

**Input:** "ok so I need to think about what the first 90 days looks like, like what do I actually do when I start, the tech platform stuff, getting the team, understanding the current stack, probably need to not break anything while I figure it out, and the board needs to see early wins"

**Output:**
```
## Brief

**Goal:** 90-day plan for starting a new executive role.

**Context:** Role confirmed. Tech platform being built by partner team. Existing tech stack unknown. Board expects visible early wins. Can't disrupt current operations while learning.

**Constraints:**
- Must balance learning (tech stack, people, processes) with visible action
- Platform integration is a known dependency
- Inferred: "Don't break anything" = run foundational + transformational tracks in parallel
- Board early wins needed within 30-60 days

**Output:** Structured 30/60/90 plan. Week-level granularity for first 30 days, then monthly.

**Success looks like:** Walk into Day 1 with a clear playbook, not a blank page.

-> Start a strategic session with this brief. Pull relevant context from vault first.
```

## Anti-Patterns

- **Don't vault-search during structuring.** The brief captures raw thinking. Vault enrichment happens when the brief is executed (via /prep, /draft, etc.)
- **Don't over-structure simple things.** "Write a LinkedIn post about X" doesn't need a full brief. Just say "Got it. Want me to draft it now, or should I /prep first?"
- **Don't add your own strategic opinions.** The brief reflects what was said, structured. Save the "have you considered..." for when asked.
- **Don't ask 4 clarifying questions.** Make your best read. One clarifying question max, and only if the intent is genuinely unclear.
