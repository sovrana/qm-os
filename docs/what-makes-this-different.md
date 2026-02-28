# What Makes This Different

Most Claude Code setups are stateless. You open a conversation, do some work, close it. Next time, you start from zero. Quartermaster is designed around a different premise: **every session should make the next one better.**

Here are ten things this system does that vanilla Claude Code - or any other AI setup I've seen - doesn't.

---

## 1. Your AI gets smarter every week, automatically

When you correct Claude - kill a framing, reject a word choice, redirect an approach - the system logs it. Not as a one-off fix, but as a calibration data point.

Patterns that appear three or more times graduate automatically from the calibration log into permanent CLAUDE.md rules. Weekly review promotes them. After a month, corrections you've already made never need making again.

This is the single most valuable feature. The system compounds.

## 2. Six-file memory architecture

Not a single memory dump. Six specialised files, each serving a distinct cognitive function:

| File | What It Holds | Why It's Separate |
|------|--------------|-------------------|
| `MEMORY.md` | Live strategic state - where things stand RIGHT NOW | Changes weekly. The "current situation" briefing. |
| `voice-exemplars.md` | 3-5 real writing samples | Calibrates output against your actual cadence, not generic "professional tone" |
| `stakeholder-live.md` | What each key person cares about right now | Dynamic postures, not static profiles. Updated as relationships shift. |
| `recent-decisions.md` | Key decisions from the last 2 weeks | Prevents re-litigation. Claude won't propose what you already rejected Tuesday. |
| `connections.md` | Cross-domain links with evidence and dates | When work in one area changes the calculus of another |
| `calibration-log.md` | Every correction, rejection, and preference shift | The staging area for permanent rules |

Claude loads these automatically at session start. You never explain context twice.

## 3. Built for 100-round document iteration

Most AI tools assume one-shot: prompt, get output, done. This system is built for the way important documents actually get written - through dozens of rounds.

**Auto-changelog** tracks structural decisions (not wordsmithing) in a co-located `.changelog/` file. Why a section was removed. Why a framing was reversed. What was tried and rejected.

**Rejection logging** captures explicit kills as hard constraints. If you cut a framing in Round 4, Claude won't quietly reintroduce it in Round 17.

**"Approval does not equal closure."** Positive feedback means "good enough to think from," not "stop iterating." The system treats "this is great" as a platform for the next thought unless you explicitly say "ship it."

## 4. Voice matching from real samples

The difference between "write in a professional tone" and "write like me" is enormous.

You provide 3-5 real writing samples - your best emails, memos, posts. Claude matches your actual patterns: sentence length variation (burstiness), verb strength, level of specificity, how you open and close.

Before any writing task, the system reads `voice-exemplars.md` and tests output against your real samples. Not against generic executive prose.

## 5. Anti-slop as enforceable rules

Not a vague instruction to "write naturally." Specific, measurable constraints:

- **12 banned verbs** (delve, leverage, embark, navigate, unleash...)
- **10 banned nouns** (tapestry, landscape, realm, symphony...)
- **11 banned adjectives** (robust, seamless, pivotal, cutting-edge...)
- **6 banned phrases** ("It is important to note...", "Let's dive in...")
- **5 banned structures** (em dashes, horizontal rules between headers, strawman questions, "Not X, but Y" cliches, colon titles)

Plus British spelling enforcement, paragraph length limits, and a burstiness requirement (vary sentence length aggressively - five words, then thirty).

Every output runs against these. The result reads like a human wrote it, because the most common AI tells are structurally eliminated.

## 6. Session-type pre-flights

The system detects what kind of work you're doing and loads the right defaults before you ask.

| Session Type | What Happens Automatically |
|-------------|---------------------------|
| Financial/budget | Numbers summary table started immediately |
| Legal document review | Missing cross-references flagged as critical gaps |
| Vendor/partner analysis | Framework scoring grid pulled from your catalogue |
| Document iteration | Source file and changelog read before touching anything |
| Stakeholder prep | Stakeholder posture file loaded, communication style adjusted |

You never have to explain "this is a budget session, so make sure to track the numbers." The system already knows.

## 7. Three search modes with a decision matrix

Your vault becomes genuinely searchable. Not just grep.

| Mode | Use When | Example |
|------|----------|---------|
| **Semantic** | You can't name what you're looking for | "What have we discussed about organisational resistance?" |
| **BM25 keyword** | You know the words, want ranked results | "Find files mentioning McKinsey" |
| **Grep/Glob** | Exact strings, file paths, patterns | A specific person's name, a number, a file type |

Default behaviour: run semantic AND grep in parallel for any non-trivial search. Catches both conceptual matches and exact hits. Add BM25 as a third mode when semantic results drift.

## 8. Stakeholder-adapted output

Same analysis. Different packaging. Built into the system instructions, not bolted on per prompt.

For each key audience, the system knows:

- **What to lead with** (investment committee gets ROI numbers, board gets memorable metaphors, CEOs get practical next steps)
- **What tone to hit** (diagnostic questions for boards, execution translation for CEOs, quantified outcomes for investors)
- **What to leave out** (methodology for investors, politics for board presentations, abstract frameworks for operators)

You define your stakeholders once. Every output adapts automatically.

## 9. Cross-domain connection tracking

Working on five things at once? The system captures when one domain affects another.

Not abstract flows ("success in A helps B"). Specific, dated, evidence-backed connections: "The regression in Project A proves Project B needs a dedicated technical lead - because the same architectural gap caused both failures."

Weekly review surfaces connections that have gone stale or need action. Your knowledge graph builds itself.

## 10. Privacy-first publishing pipeline

This is how this site exists.

The working system uses real names, real companies, real numbers. A `.publish-config.json` file maps every piece of PII to a sanitised replacement. The publish pipeline runs the full replacement, then greps the entire output for any PII that slipped through. If anything matches, the commit is blocked.

Build in production. Publish safely. No separate "public version" to maintain by hand.

---

## How these connect

These aren't independent features. They form a loop:

**Use the system** → corrections feed the calibration log → patterns graduate to permanent rules → rules improve every session → better output generates fewer corrections → the system stabilises around your actual preferences.

After 8 weeks of daily use, the CLAUDE.md file contains dozens of rules that were discovered through use, not designed upfront. That's the point. You don't configure this system. You grow it.
