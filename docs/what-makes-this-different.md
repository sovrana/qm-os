# What Makes This Different

Five things this system does that nothing else I've seen comes close to.

---

## 1. It gets smarter every time you use it

Every AI tool starts from zero. You correct it, it forgets. You correct it again next week.

Quartermaster doesn't forget. When you kill a framing, reject a word choice, or redirect an approach, the system logs it as a calibration data point. Patterns that appear three or more times automatically graduate into permanent CLAUDE.md rules. A weekly review promotes them, retires stale ones, and surfaces new patterns worth capturing.

After a month of daily use, the CLAUDE.md file contains dozens of rules that were discovered through use, not designed upfront. The system literally rewrites its own instructions based on your behaviour. Every session makes the next one better. Every correction makes the same mistake impossible.

This is the single most important feature. Everything else exists to serve this loop.

## 2. It knows your context before you open your mouth

Six specialised memory files load automatically at session start. Not a generic memory dump - six distinct cognitive functions:

- **Where things stand right now** - live strategic state across all your workstreams, updated weekly
- **How you actually write** - real samples of your emails and memos, not a style guide
- **What each person cares about** - dynamic stakeholder postures that shift as relationships evolve
- **What you decided this week** - prevents the AI from proposing something you already rejected on Tuesday
- **Where your domains connect** - when work in one area changes the calculus of another, captured with evidence and dates
- **Every correction you've ever made** - the staging area for permanent rules

On top of this, the system detects what kind of work session you're in and loads the right defaults. Financial discussion? A numbers table starts building immediately. Legal review? Missing cross-references get flagged before you ask. Vendor analysis? Your framework scoring grid appears. Stakeholder prep? Communication style adjusts to who you're talking to.

You never explain context. The system already has it.

## 3. It writes like you, not like AI

You know the feeling. You ask an AI to draft an email and it comes back with "I hope this message finds you well" followed by three paragraphs of corporate mush sprinkled with words like "leverage" and "robust."

Quartermaster attacks this from two directions.

**Voice matching:** You give it 3-5 samples of your actual writing - your best emails, sharpest memos, strongest posts. Before any writing task, the system reads these and calibrates against your real cadence. Sentence length variation. Verb strength. How you open and close. The specificity level you actually use. Not "professional tone" - YOUR tone.

**Anti-slop enforcement:** 40+ banned words, phrases, and structures, enforced on every output. No "delve." No "robust." No em dashes (the single biggest AI tell). No strawman questions. No "Not X, but Y" cliches. British spelling if that's what you use. Paragraph length limits. A burstiness requirement - five words, then thirty.

The result reads like a human wrote it, because the most common AI tells are structurally eliminated and the voice is calibrated against real samples instead of vibes.

## 4. It makes your entire knowledge base searchable

Everything you write goes into a markdown vault. The system makes that vault genuinely searchable - not just grep.

Three modes, each for a different need: **semantic search** finds conceptually related content even when you can't name what you're looking for ("what have we discussed about organisational resistance?"). **Keyword ranking** surfaces exact term matches ordered by relevance. **Pattern matching** finds specific names, numbers, and file paths instantly.

Default behaviour runs semantic and exact search in parallel on every query. You get both conceptual matches and precise hits. Your notes from six months ago surface alongside yesterday's meeting notes when they're relevant.

The more you write, the smarter the search gets. Your vault becomes a genuine second brain - not a graveyard of files you'll never find again.

## 5. It publishes itself safely

This site is the proof.

The working system uses real names, real companies, real financial numbers. A publish pipeline maps every piece of identifying information to a sanitised replacement. It runs the full substitution, then greps the entire output for anything that slipped through. If a single match is found, the commit is blocked.

No separate "public version" to maintain by hand. No sanitised fork that drifts out of sync. Build in production with all the context you need. Share openly when you're ready. The privacy gate handles the rest.

This means you can open-source your actual operating system - the one you use every day, not a demo version - without exposing a single piece of private information.

---

## How these connect

These five aren't independent features. They form a single loop:

**Use the system** → corrections feed the calibration log → patterns graduate to permanent rules → rules improve every session → better output generates fewer corrections → the system stabilises around your actual preferences.

You don't configure this system. You grow it.
