# Anti-Slop Rules

## Why This Matters

AI output that reads like AI output is useless. If your stakeholders can smell the ChatGPT, the content loses credibility before they finish the first paragraph. Anti-slop rules are hard constraints on Claude's output - not style suggestions, compile errors.

## Banned Words

### Verbs
Delve, leverage, embark, navigate, unleash, unlock, foster, elevate, underscore, harness, optimize, facilitate.

### Nouns
Tapestry, landscape, realm, symphony, testament, game-changer, paradigm shift, kaleidoscope, plethora.

### Adjectives
Robust, seamless, pivotal, crucial, vital, intricate, innovative, cutting-edge, ever-evolving, dynamic, bespoke.

## Banned Phrases

- "It is important to note..."
- "In conclusion..."
- "Furthermore / Moreover / Additionally" (use "Also" or just start the sentence)
- "In the fast-paced world of..."
- "Let's dive in."
- "To wrap up..."

## Banned Structures

**Em dashes and en dashes.** Telltale AI markers. Replace with standard hyphens, commas, or restructure the sentence.

**Horizontal lines (---).** Don't use as section breaks between headers. Headers provide enough separation on their own.

**The "Not X, but Y" cliche.** "It's not just software, it's a solution." Just say what it is.

**Strawman questions.** "So, why does this matter?" Don't ask rhetorical questions. State the value directly.

**The colon title.** "Project Management: A Guide to Efficiency." Avoid this generic format entirely.

## Prose Style Rules

**Burstiness.** Vary sentence length aggressively. A five-word sentence. Then a longer one that develops the point with specificity. Short again.

**Strong verbs over "is/are":**

- Bad: "The software is fast."
- Good: "The software loads instantly."

**Specifics over generalities.** Never say "various factors" - name them. Never say "improved efficiency" - state the exact percentage or time saved. If a claim can't be quantified, it's not ready.

## British Spelling Conventions

All `.md` files use British spellings:

| British (correct) | American (wrong) |
|-------------------|------------------|
| organise, optimise, realise, analyse | organize, optimize, realize, analyze |
| behaviour, favour, colour, labour | behavior, favor, color, labor |
| centre, metre | center, meter |
| defence, licence (noun) | defense, license |
| digitisation, monetisation, standardised | digitization, monetization, standardized |

## Formatting

- **Short paragraphs.** Max 3-4 lines.
- **No wall of bullets.** Bullet points for actual data lists, not for prose.
- **Cut aggressively.** If a sentence can be removed without losing the core meaning, remove it.

## How to Enforce

These rules live in the Anti-Slop Rules section of your CLAUDE.md. They apply to every piece of output Claude generates. The `/draft` skill applies them double for outbound content - anything going external gets extra scrutiny.

When you catch slop that made it through, add the offending word or pattern to the banned list. The list grows over time as you notice new AI tells.
