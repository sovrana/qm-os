# What Makes This Different

Eight things this system does that nothing else I've seen comes close to.

---

## 1. It never sleeps

Most AI tools wait for you to open them. Quartermaster doesn't.

A daemon called OpenClaw runs 24/7 on a separate machine, connected to the same vault via iCloud sync. Every hour, it runs a heartbeat that checks five things:

- **Inbox processing.** New files in `00_Inbox/` get auto-detected. Transcripts under 5,000 words are processed autonomously: theme detection, decision extraction, action item routing, summary creation. You drop a file and walk away. It handles the rest.
- **Waiting item alerts.** Items tagged `@waiting(PersonName)` age automatically. Past 7 days, you get a Telegram notification with the person, the item, and how long it's been. Past 14 days, it flags for escalation.
- **Due today reminders.** Tasks with today's date surface on your phone before you sit down.
- **Morning plan.** Between 6-8am, the system generates a full prioritised daily plan and sends a condensed version to Telegram. You wake up knowing what matters.
- **Evening summary.** Between 5-7pm, it compares the morning plan to what actually got done. Tomorrow's top 3. Waiting items that moved. Captures that came in.

The system has agency between sessions. That's fundamentally different from "open Claude Code and run a command."

## 2. Every meeting becomes permanent, searchable, actionable knowledge

The pipeline works like this:

1. **Record** the meeting with MacWhisper (a desktop transcription app)
2. **Drop** the transcript file into `00_Inbox/` (or `00_Inbox/macwhisper/`)
3. **Walk away.** The heartbeat picks it up within the hour

What happens autonomously:

- Theme detection (which workstream does this belong to?)
- Decision extraction (what was agreed?)
- Action item extraction (who owes what, by when?) - actions go straight to `tasks.md` with the right theme tag
- Key insight capture (what shifted in the strategic picture?)
- Two files created: raw transcript (permanent reference) and processed summary (working document)
- Original archived to `99_System/logs/processed/`

For large files (>5,000 words), you get a Telegram flag and run `/transform` manually. For everything else, it's fully autonomous.

For conversations with Claude Code itself, `/transform session` captures the session's insights into the vault. It even runs a performance-vs-prep comparison: if you had a brief for this meeting, it scores what landed, what was missed, and what was improvised.

No meeting is wasted. No action item forgotten. No decision relitigated because nobody wrote it down.

## 3. Tasks managed like a chief of staff

Task systems sort by due date. That puts "buy new shoes" above "prepare for Monday's board session" if the shoes are due first.

Quartermaster's task management is built around three ideas most tools ignore:

**Leverage scoring.** Every task can carry impact and effort tags. The engine calculates leverage as Impact divided by Effort:

| Impact | Effort | What Happens |
|--------|--------|--------------|
| High | Low | **Highest leverage** - bumps to P1 even without a due date |
| High | Medium | Strong candidate for today |
| Medium | Low | Quick win, surfaces in P3 |
| Low | High | Flagged: "consider deferring" |

**Strategic weighting.** The daily plan reads the Live Strategic State from memory. If your biggest deal closes next week, tasks in that theme outrank routine admin regardless of due dates. The plan reflects what actually matters this week, not what's technically next.

**Proactive follow-up.** Waiting items don't just age silently. After 7 days, the system drafts actual follow-up messages you can send. Not just a flag saying "this is old" but a ready-to-send nudge. After 14 days, Telegram alerts for escalation. A weekly audit surfaces everything that slipped through cracks.

The result: you open your phone in the morning and your day is already planned by an agent that understands strategic priority, not just calendar deadlines.

## 4. Five-lens red team on every important document

Before anything important leaves the building, `/challenge` runs five independent analysis agents simultaneously:

1. **Audience Fit** - Would the target reader finish this? Does it match their communication preferences? Is the ask clear in 30 seconds?
2. **Logic & Evidence** - Are claims backed by numbers or just directional language? Would a sceptic find it compelling?
3. **Vault Contradictions** - Searches everything you've written for conflicts. Has the positioning shifted without acknowledging the change?
4. **Known Blind Spots** - Applies your documented blind spots from CLAUDE.md. Architecture without execution mechanics? Culture angle missing? Greenfield bias?
5. **Pre-Mortem** - How does this fail? Top 3 failure modes. Strongest counter-argument. The question your audience will ask that you haven't answered.

The five agents run as independent subprocesses. The pre-mortem doesn't know what the audience-fit lens found, and vice versa. That independence is the point - sequential review anchors on the first problem found. Parallel execution produces genuinely different angles.

Returns a verdict (Strong / Needs Work / Weak), the top 3 issues, and pushes actionable fixes to your task list.

## 5. It rewrites its own instructions

Every AI tool starts from zero. You correct it, it forgets. You correct it again next week.

Quartermaster runs two parallel feedback mechanisms:

**The calibration log.** Every time you reject a framing, kill a word choice, redirect an approach, or correct a tone - it's logged. Format: what was tried, what replaced it, why. This file is append-only and compounds over time.

**The BEAD system.** Every `/transform session` extracts improvement suggestions from the conversation. New suggestions get fuzzy-matched against existing ones. Similar suggestions increment a counter. When a suggestion hits 3 occurrences across independent sessions, it becomes a BEAD - validated and ready to implement.

**The graduation pattern:** calibration log (observed) → 3+ similar entries → formal rule in CLAUDE.md (codified) → default behaviour (automatic).

This means "stop using em dashes" goes from a one-off correction to a permanent editing rule. "Start financial sessions with a numbers table" goes from a suggestion to a mandatory session default. The operating rules aren't designed upfront. They're discovered through use and promoted when validated.

After 8 weeks: 130+ suggestions extracted, 7 graduated to permanent rules. Each one eliminated a recurring friction point.

## 6. Captures from everywhere, processes centrally

The system isn't one tool. It's an ecosystem that captures from every device you use:

- **Obsidian on your phone** - Browse the vault, read status docs, check meeting notes, edit tasks. Same markdown files, synced via iCloud.
- **iOS Shortcuts** - "Hey Siri, QM capture" dictates a thought, timestamps it, and appends to your capture file via Obsidian's URL scheme.
- **Telegram** - Message the bot: "Remind me to call Sean about the contract." Captured as a task in `tasks.md` with the right theme tag. Ask "waiting?" and get your full waiting list with ages.
- **MacWhisper** - Meeting transcripts. Record, export, drop in inbox.
- **Share sheet** - Select text in any iOS app, share to QM. Appended to your capture file.
- **Email forwarding** - Forward emails to the inbox for processing.

Everything converges on `00_Inbox/` or `01_Todos/capture.md`. From there, the `/inbox` skill or the autonomous heartbeat routes it: tasks to `tasks.md`, content to the right theme folder, references to `03_Reference/`.

One inbox. Multiple capture points. Automatic processing. Nothing falls through.

## 7. Connected to your actual work tools

This isn't a closed system. It plugs into the tools you already use:

- **Gmail** - Natural language search from the terminal. "Find emails from Sarah about the contract in the last month." Results with subjects, dates, and full body text.
- **Corporate Outlook & Calendar** - Accessed via browser automation through a Windows 365 VM. Claude reads emails, extracts calendar events, drafts responses.
- **Google Drive** - Access via the Google Workspace CLI.
- **Rich email output** - Markdown drafts convert to styled HTML and copy to clipboard. Paste into Gmail, Outlook, or Word with formatting preserved: tables, headers, bold, everything.
- **Office documents** - Generate DOCX, PPTX, XLSX, and PDF directly from Claude Code sessions.
- **School emails** - Filtered and summarised from Highgate and Channing school portals (yes, it handles the parenting admin too).

The output pipeline matters as much as the input. Writing a board memo in markdown is pointless if you can't get it into the format stakeholders expect. One command converts and copies.

## 8. Automatic decision tracking across 100-round iterations

When you're on round 47 of a document, you need to know why the budget table was removed in round 12. Git tracks what changed. Quartermaster tracks **why**.

Every tracked document gets a companion changelog that records:

- **Changed:** What was added, removed, or restructured
- **Why:** The stated reason
- **Decided:** What was chosen
- **Rejected:** What was eliminated (this is the load-bearing field)

The system logs automatically during iteration - you don't invoke it. Structural changes, section removals, and explicit reasoning all trigger entries. Typo fixes and word swaps don't.

The killer feature is **contradiction detection.** When a new change reverses a previously logged decision, the system catches it immediately: "This reverses the Round 3 decision to remove the competitive analysis. Intentional?"

In long iterations, it's easy to circle back to something you already tried and rejected. The changelog prevents accidental regression and forces conscious reversals. Rejected alternatives are permanent constraints unless explicitly overturned.

---

## How these connect

These eight aren't independent features. They form a loop:

**Capture from anywhere** → meetings and notes flow into the inbox → **autonomous processing** extracts decisions and actions → **task management** prioritises by leverage and strategic weight → **proactive alerts** flag what's slipping → **daily work sessions** produce documents → **/challenge** red-teams before sharing → **decision tracking** prevents regression → **corrections** feed the calibration log → patterns **graduate to permanent rules** → the system gets smarter → better output generates fewer corrections.

You don't configure this system. You grow it.

---

Ready to try it? [Get started in 30 minutes →](quickstart.md)

<div class="feedback-line" markdown>
Something missing from this list? [Start a discussion](https://github.com/sovrana/qm-os/discussions).
</div>
