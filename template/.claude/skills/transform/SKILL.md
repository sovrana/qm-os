---
name: transform
description: Transform external content into Brain system. Handles transcripts, documents, and conversation synthesis.
argument-hint: [file|inbox|session]
allowed-tools: Read, Write, Edit, Bash, AskUserQuestion, Glob
---

# Transform

Transform external content into the Brain system. Handles transcripts, documents, and conversation synthesis.

**Usage:**
- `/transform [file]` - Process a single file
- `/transform inbox` - Batch process all items in 00_Inbox/
- `/transform session` - Synthesise current conversation into vault

---

## Single File Mode (`/transform [file]`)

1. Read the input file: $ARGUMENTS
2. **For audio transcripts:** Ask if user has a speaker-labelled version available
3. Extract: Summary (3-5 sentences), Decisions, Action items, Key insights
4. Ask which theme this belongs to
5. **Create TWO files:**
   - Raw transcript -> `02_Themes/[theme]/processed/YYYY-MM-DD_[topic]-raw-transcript.md`
   - Processed summary -> `02_Themes/[theme]/meetings/YYYY-MM-DD_[topic].md`
   - Summary MUST link to raw: `**Raw Transcript:** [[processed/YYYY-MM-DD_topic-raw-transcript|Full transcript]]`
6. Add actions to `01_Todos/tasks.md`
7. Move original to `99_System/logs/processed/`

---

## Batch Mode (`/transform inbox`)

1. Find all markdown files in `00_Inbox/transcripts/` and `00_Inbox/`
2. Ask if user has speaker-labelled versions for transcripts
3. For each file: read, extract, present summary, ask theme
4. After collecting theme assignments:
   - Create structured meeting notes in appropriate theme/meetings/
   - Batch add action items to `01_Todos/tasks.md`
   - Move processed files to `99_System/logs/processed/`

---

## Session Synthesis Mode (`/transform session`)

After substantive conversations, synthesise insights into the Brain system.

### Process:

1. **Gather current context:**
   - Read relevant theme `claude.md`, `status.md`, `strategic-context.md`, `people.md`
   - Read `02_Themes/career/` for cross-domain context
   - Read `02_Themes/frameworks/` for framework IP

2. **Identify conversation insights:**
   - **New strategic insights** - not yet captured
   - **Framework IP emerged** - new or refined frameworks
   - **People/stakeholder updates** - new people, changed relationships
   - **Status changes** - now vs next, new blockers, new waiting items
   - **Cross-domain effects** - how insights affect other themes
   - **Open questions** - unresolved questions

3. **Propose updates:**
   - Strategic insight -> Update `strategic-context.md`
   - Framework IP -> Update frameworks theme files
   - People context -> Update `people.md`
   - Status change -> Update `status.md`
   - Cross-domain -> Update `02_Themes/career/`

4. **Execute updates:**
   - Show proposed changes before making them
   - Ask user to confirm if significant
   - Summarise what was updated

5. **Create discovery log (for substantial conversations):**
   - If conversation was long (50+ messages) or covered substantial ground
   - Create `99_System/logs/conversation-discoveries/YYYY-MM-DD_topic.md`

6. **Extract improvement suggestions:**
   - What would have made this workflow smoother?
   - What did Claude get wrong that needs an SOP update?
   - What pattern emerged that should be formalised?
   - Check `99_System/improvement-suggestions.md` for fuzzy matches
   - If similar: increment count. If 3+: mark **BEAD**
   - If new: add with `[1x]` and today's date

## Notes:

- Generate meeting note filenames: YYYY-MM-DD_[descriptive-slug].md
- Preserve original transcript alongside processed summary
- Theme options: <!-- CUSTOMISE: list your active themes here, e.g. project-a, project-b, project-c, frameworks, personal, family, system -->
- Don't over-capture - focus on insights that change understanding or positioning
- Framework IP should always be captured - core intellectual property
- Improvement suggestions run on EVERY `/transform session`
- **Performance vs prep scoring:** When processing a call/meeting transcript and a prep doc exists for that meeting (check theme `meetings/` and `context/` folders), automatically include a "Performance vs Prep" section: what landed, what was missed, what was improvised. This closes the feedback loop.
- **Capture vs synthesis:** Before starting any processing, determine whether the user wants a capture (what happened - factual record) or a synthesis (what should happen - recommendations). Ask if unclear. "Summary" does not default to "proposal".
- **Trusted advisor feedback:** When the user pastes feedback from trusted advisors via informal channels, process with the same structured rigour as professional stakeholder feedback. Each piece of feedback gets extracted, evaluated, and either acted on or explicitly parked.
