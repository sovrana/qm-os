# External Input Processing

## Working with External AI Output

When the user shares ChatGPT, Gemini, or other AI analysis, don't accept or reject wholesale. Synthesise into three categories:
1. **Validation** - What confirms existing thinking (acknowledge briefly)
2. **Vulnerabilities** - What exposes genuine gaps or risks (address these)
3. **Language to steal** - Specific phrases or framings worth adopting (extract and use)

Also assess: what question did the external AI answer vs what question the user actually needs answered? External AI often optimises for the obvious frame, not the specific context.

**Frame check (mandatory):** Before synthesising any external AI input, explicitly state: "They answered [X question]. You actually need [Y question] answered." Then adjust the synthesis to answer Y, not X. If X and Y are the same, say so - but do the check.

**Archetype detection:** When multiple LLMs evaluate the same document, categorise by the archetype each defaults to (e.g., corporate template, startup founder, academic). This reveals their assumptions and helps identify which lens is most useful for the actual context.

## Competitive & External Analysis

When evaluating external companies, articles, or theses against existing work:

1. **"Same category?" first** - Before comparing, ask whether they're even in the same category (tech vendor vs advisory firm, tool vs platform, etc.). False equivalence wastes analysis and weakens positioning.
2. **Four-part separation** - (1) What overlaps (validate), (2) What they have that we don't (steal), (3) What we have that they don't (differentiate), (4) What they get wrong (avoid).
3. **Map terminology** - Explicitly translate their language to ours (their term = our term). Then identify what our version adds beyond theirs.
4. **Framework grid (mandatory for vendor decks):** Before any vendor/partner analysis, pull the most relevant framework from your frameworks catalogue and use it as the scoring grid. No freeform vendor analysis - always score against existing architecture.

## Importing External AI Conversations

**Key Principle:** Extract insights, don't dump conversations. Future-you needs decisions and context, not 50-message exploratory threads.

**Flow:**
1. Export from ChatGPT/Claude.ai to `00_Inbox/[source]-exports/`
2. Extract: Key decisions, specifications, open questions, next actions
3. Create synthesised file in appropriate theme's `processed/` folder
4. Archive original to `99_System/logs/external-ai-exports/`

**Don't import verbatim** - most conversation is exploratory noise.
