# What Makes This Different

Three genuinely novel architectural ideas, plus five operational systems that make them useful. For each one: the transferable concept, then how I implemented it. Your tools will differ. The architecture won't.

---

## The novel bits

### 1. It rewrites its own instructions

Every AI tool starts from zero. You correct it, it forgets. You correct it again next week.

Quartermaster runs two parallel feedback mechanisms:

**The calibration log.** Every time you reject a framing, kill a word choice, redirect an approach, or correct a tone - it's logged. Format: what was tried, what replaced it, why. This file is append-only and compounds over time.

**The BEAD system.** Every `/transform session` extracts improvement suggestions from the conversation. New suggestions get fuzzy-matched against existing ones. Similar suggestions increment a counter. When a suggestion hits 3 occurrences across independent sessions, it becomes a BEAD - validated and ready to implement.

**The graduation pattern:** calibration log (observed) → 3+ similar entries → formal rule in CLAUDE.md (codified) → default behaviour (automatic).

This means "stop using em dashes" goes from a one-off correction to a permanent editing rule. "Start financial sessions with a numbers table" goes from a suggestion to a mandatory session default. The operating rules aren't designed upfront. They're discovered through use and promoted when validated.

After 8 weeks: 130+ suggestions extracted, 7 graduated to permanent rules. Each one eliminated a recurring friction point. [See real examples →](architecture/in-production.md)

!!! tip "The concept vs my implementation"
    **The concept:** An append-only correction log + a frequency-tracked suggestion system with a promotion threshold. Corrections that recur get codified as permanent rules. The system's operating instructions are a living document shaped by use.

    **My implementation:** `calibration-log.md` (append-only), `improvement-suggestions.md` (frequency-tracked), CLAUDE.md (graduated rules), `/weekly` (surfaces BEADs for promotion). All plain markdown files.

    **Your version:** The same architecture works with any LLM tool that reads a system prompt from a file. The key insight is the 3-occurrence threshold and the staging-to-production pipeline. The specific files don't matter.

### 2. Five-lens red team on every important document

Before anything important leaves the building, `/challenge` runs five independent analysis agents simultaneously:

1. **Audience Fit** - Would the target reader finish this? Does it match their communication preferences? Is the ask clear in 30 seconds?
2. **Logic & Evidence** - Are claims backed by numbers or just directional language? Would a sceptic find it compelling?
3. **Vault Contradictions** - Searches everything you've written for conflicts. Has the positioning shifted without acknowledging the change?
4. **Known Blind Spots** - Applies your documented blind spots from CLAUDE.md. Architecture without execution mechanics? Culture angle missing? Greenfield bias?
5. **Pre-Mortem** - How does this fail? Top 3 failure modes. Strongest counter-argument. The question your audience will ask that you haven't answered.

The five agents run as independent subprocesses. The pre-mortem doesn't know what the audience-fit lens found, and vice versa. That independence is the point - sequential review anchors on the first problem found. Parallel execution produces genuinely different angles.

Returns a verdict (Strong / Needs Work / Weak), the top 3 issues, and pushes actionable fixes to your task list.

!!! tip "The concept vs my implementation"
    **The concept:** Parallel independent agents evaluating the same document from different perspectives, with no shared context between them. Synthesis happens after all agents return, not during.

    **My implementation:** Claude Code's Agent tool launching 5 subagents, each with a different persona prompt. Results merged in a synthesis step.

    **Your version:** Any system that can run multiple LLM calls in parallel with different system prompts. The architectural insight is independence (no anchoring) and the fixed five lenses calibrated to your specific blind spots.

### 3. It remembers why you decided what you decided

You're deep in a document iteration. You want to add back the budget table. But you removed it two weeks ago for a reason you can't remember. Git tracks what changed. Quartermaster tracks **why**.

Every tracked document gets a companion changelog that records:

- **Changed:** What was added, removed, or restructured
- **Why:** The stated reason
- **Decided:** What was chosen
- **Rejected:** What was eliminated (this is the load-bearing field)

The system logs automatically during iteration - you don't invoke it. Structural changes, section removals, and explicit reasoning all trigger entries. Typo fixes and word swaps don't.

The killer feature is **contradiction detection.** When a new change reverses a previously logged decision, the system catches it immediately: "This reverses the decision to remove the competitive analysis. Intentional?"

Over weeks of iteration, it's easy to circle back to something you already tried and rejected. The changelog prevents accidental regression and forces conscious reversals. Rejected alternatives are permanent constraints unless explicitly overturned.

!!! tip "The concept vs my implementation"
    **The concept:** A structured decision log co-located with each important document, recording not just what changed but why and what was rejected. Plus automated detection when a new change contradicts a previous logged decision.

    **My implementation:** `.changelog/[filename].md` files alongside documents. Claude reads the changelog before editing and appends entries automatically during iteration.

    **Your version:** Any document iteration workflow benefits from this. The key is logging rejections (not just decisions) and checking new edits against previous rejections. The contradiction detection is the high-value feature.

---

## The operational backbone

These five are things other tools also do. Here's what I think we do well, and how the specific implementation works so you can adapt it.

### 4. It never sleeps

Most AI tools wait for you to open them. Quartermaster doesn't.

A daemon runs 24/7 on a separate machine, connected to the same vault via cloud sync. Every hour, it runs a heartbeat that checks five things:

- **Inbox processing.** New files in `00_Inbox/` get auto-detected. Transcripts under 5,000 words are processed autonomously: theme detection, decision extraction, action item routing, summary creation. You drop a file and walk away.
- **Waiting item alerts.** Items tagged `@waiting(PersonName)` age automatically. Past 7 days, you get a notification with the person, the item, and how long it's been. Past 14 days, it flags for escalation.
- **Due today reminders.** Tasks with today's date surface on your phone before you sit down.
- **Morning plan.** Between 6-8am, the system generates a prioritised daily plan and sends a condensed version to your phone.
- **Evening summary.** Between 5-7pm, it compares the morning plan to what actually got done.

The system has agency between sessions. That's fundamentally different from "open Claude Code and run a command."

!!! tip "The concept vs my implementation"
    **The concept:** An always-on process that watches your vault and acts on changes, scheduled events, and aging items without you being present.

    **My implementation:** A Telegram bot on a spare Mac, synced via iCloud, running Claude Code headlessly on an hourly cron.

    **Your version:** A VPS with a cron job, a Raspberry Pi, a GitHub Action on a schedule, or any always-on compute that can run the Claude CLI. The tools are swappable. The pattern - "agent that works between sessions" - is the point.

### 5. Every meeting becomes permanent, searchable, actionable knowledge

The pipeline:

1. **Record** the meeting with a transcription tool
2. **Drop** the transcript file into `00_Inbox/`
3. **Walk away.** The heartbeat picks it up within the hour

What happens autonomously: theme detection, decision extraction, action item extraction (routed straight to `tasks.md`), key insight capture, archival of the original.

For large files (>5,000 words), you get a notification and run `/transform` manually. For everything else, it's fully autonomous.

For conversations with Claude Code itself, `/transform session` captures the session's insights into the vault. It even runs a performance-vs-prep comparison: if you had a brief for this meeting, it scores what landed, what was missed, and what was improvised.

!!! tip "The concept vs my implementation"
    **The concept:** Autonomous transcript-to-knowledge pipeline with theme detection, structured extraction, and routing to the right location in your system.

    **My implementation:** MacWhisper for transcription, iCloud for sync, the always-on daemon for processing.

    **Your version:** Whisper (open source) or any transcription tool, Dropbox/Google Drive/git for sync, any scheduled process for the autonomous pipeline. The extraction logic lives in the `/transform` skill, which is a markdown SOP that any Claude Code instance can run.

### 6. Tasks managed like a chief of staff

Task systems sort by due date. That puts "buy new shoes" above "prepare for Monday's board session" if the shoes are due first.

Quartermaster's task management is built around three ideas:

**Leverage scoring.** Every task can carry impact and effort tags. The engine calculates leverage as Impact divided by Effort:

| Impact | Effort | What Happens |
|--------|--------|--------------|
| High | Low | **Highest leverage** - bumps to P1 even without a due date |
| High | Medium | Strong candidate for today |
| Medium | Low | Quick win, surfaces in P3 |
| Low | High | Flagged: "consider deferring" |

**Strategic weighting.** The daily plan reads the Live Strategic State from memory. If your biggest deal closes next week, tasks in that theme outrank routine admin regardless of due dates.

**Proactive follow-up.** Waiting items don't just age silently. After 7 days, the system drafts actual follow-up messages you can send. After 14 days, alerts for escalation. A weekly audit surfaces everything that slipped through cracks.

!!! tip "The concept vs my implementation"
    **The concept:** AI-prioritised task management that combines leverage scoring (Impact/Effort), strategic context weighting, and proactive follow-up drafting.

    **My implementation:** Plain markdown `tasks.md` with inline tags (`!impact(H)`, `!effort(L)`, `@waiting(Name)`). Claude reads the tags and MEMORY.md to generate the daily plan.

    **Your version:** Same tags in any text file. The `/morning` skill is a markdown SOP - adapt it to your prioritisation logic.

### 7. Captures from everywhere, processes centrally

The system isn't one tool. It's an ecosystem that captures from every device:

- **Phone app** - Browse the vault, edit tasks, read notes
- **Voice shortcuts** - Dictate a thought, it gets timestamped and appended
- **Chat bot** - Message a task, it lands in `tasks.md` with the right theme tag
- **Transcription tool** - Meeting transcripts. Record, export, drop in inbox
- **Share sheet** - Select text in any app, share to the system
- **Email forwarding** - Forward emails to the inbox for processing

Everything converges on `00_Inbox/`. From there, the `/inbox` skill or the autonomous heartbeat routes it: tasks to `tasks.md`, content to the right theme folder, references to `03_Reference/`.

!!! tip "The concept vs my implementation"
    **The concept:** Many capture points, one processing pipeline. Everything converges on a single inbox folder. Routing is automatic.

    **My implementation:** Obsidian (phone), iOS Shortcuts (voice), Telegram bot (chat), MacWhisper (transcription), iCloud (sync).

    **Your version:** Any note-taking app + any messaging bot + any transcription tool + any sync service. The architecture is the single inbox pattern and the automatic routing, not the specific tools.

### 8. Connected to your actual work tools

This isn't a closed system. It plugs into the tools you already use:

- **Email search** - Natural language search from the terminal. Results with subjects, dates, and full body text
- **Corporate email & calendar** - Browser automation for locked-down enterprise systems
- **Rich email output** - Markdown drafts convert to styled HTML and copy to clipboard. Paste into any email client with formatting preserved
- **Office documents** - Generate DOCX, PPTX, XLSX, and PDF directly from sessions

The output pipeline matters as much as the input. Writing a memo in markdown is pointless if you can't get it into the format stakeholders expect. One command converts and copies.

---

## How these connect

These eight aren't independent features. They form a loop:

**Capture from anywhere** → meetings and notes flow into the inbox → **autonomous processing** extracts decisions and actions → **task management** prioritises by leverage and strategic weight → **proactive alerts** flag what's slipping → **daily work sessions** produce documents → **/challenge** red-teams before sharing → **decision tracking** prevents regression → **corrections** feed the calibration log → patterns **graduate to permanent rules** → the system gets smarter → better output generates fewer corrections.

You don't configure this system. You grow it. And every change is auditable.

---

Ready to try it? [Get started →](quickstart.md)

<div class="feedback-line" markdown>
Something missing from this list? [Start a discussion](https://github.com/sovrana/qm-os/discussions).
</div>
