# Anti-Slop Rules

!!! abstract "TL;DR"
    Hard constraints on AI output. Banned words, phrases, and structures that make text read like ChatGPT. British spellings. Short paragraphs. Specifics over generalities. These are compile errors, not style suggestions.

## Why This Matters

AI output that reads like AI output is useless. If your stakeholders can smell the ChatGPT, the content loses credibility before they finish the first paragraph. Anti-slop rules are hard constraints on Claude's output - not style suggestions, compile errors.

## Banned Words

=== "Verbs"

    | Banned | Use Instead |
    |--------|-------------|
    | Delve | Examine, explore, dig into |
    | Leverage | Use, apply, build on |
    | Embark | Start, begin, launch |
    | Navigate | Handle, manage, work through |
    | Unleash | Release, enable, deploy |
    | Unlock | Enable, open up, access |
    | Foster | Build, create, encourage |
    | Elevate | Raise, improve, lift |
    | Underscore | Show, highlight, reinforce |
    | Harness | Use, capture, apply |
    | Optimize | Improve, tune, tighten |
    | Facilitate | Run, enable, support |

=== "Nouns"

    | Banned | Use Instead |
    |--------|-------------|
    | Tapestry | (Just describe the thing) |
    | Landscape | Market, environment, space |
    | Realm | Area, domain, field |
    | Symphony | (Just describe the thing) |
    | Testament | Proof, evidence, sign |
    | Game-changer | Shift, breakthrough, step change |
    | Paradigm shift | Change, transformation, rethink |
    | Kaleidoscope | (Just describe the thing) |
    | Plethora | Many, several, a range of |

=== "Adjectives"

    | Banned | Use Instead |
    |--------|-------------|
    | Robust | Strong, reliable, solid |
    | Seamless | Smooth, integrated, clean |
    | Pivotal | Key, critical, turning-point |
    | Crucial | Important, essential, key |
    | Vital | Essential, necessary, core |
    | Intricate | Complex, detailed, layered |
    | Innovative | New, novel, original |
    | Cutting-edge | Latest, advanced, modern |
    | Ever-evolving | Changing, shifting, growing |
    | Dynamic | Active, changing, fast-moving |
    | Bespoke | Custom, tailored, specific |

## Banned Phrases

| Phrase | Why |
|--------|-----|
| "It is important to note..." | Filler. Just state the thing. |
| "In conclusion..." | The reader knows it's the end. |
| "Furthermore / Moreover / Additionally" | Use "Also" or just start the sentence. |
| "In the fast-paced world of..." | Generic throat-clearing. |
| "Let's dive in." | You're not diving. You're reading. |
| "To wrap up..." | See "In conclusion." |

## Banned Structures

!!! failure "Em dashes and en dashes"
    Telltale AI markers. Replace with standard hyphens, commas, or restructure the sentence.

!!! failure "Horizontal lines (---)"
    Don't use as section breaks between headers. Headers provide enough separation on their own.

!!! failure "The 'Not X, but Y' cliche"
    "It's not just software, it's a solution." Just say what it is.

!!! failure "Strawman questions"
    "So, why does this matter?" Don't ask rhetorical questions. State the value directly.

!!! failure "The colon title"
    "Project Management: A Guide to Efficiency." Avoid this generic format entirely.

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
