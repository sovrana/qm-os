{"name": "visualise", "description": "Generate visual infographics and diagrams from vault notes using Nano Banana Pro", "user-invocable": false}

# Visualise

Generate infographics, diagrams, and knowledge cards from vault notes using Google's Nano Banana Pro (Gemini Image) API.

## When to Use

Trigger this skill when the user says things like:
- "Visualise this note"
- "Make a diagram of this framework"
- "Create an infographic from this"
- "Turn this into a visual"
- "Generate an image for this concept"

## Prerequisites

- `GOOGLE_API_KEY` environment variable set (get free key at https://aistudio.google.com/apikey)
- Script: `~/bin/visualise`

## Process

### 1. Read the Source Note

Read the full note the user references. Understand:
- What the core concept/framework is
- The key relationships, hierarchies, or flows
- Any numbers, labels, or specific terms that must appear accurately
- Whether this is a framework, process, comparison, timeline, or knowledge card

### 2. Craft the Image Prompt

This is where the value is. Write a detailed, specific prompt optimised for Nano Banana Pro's strengths (accurate text rendering, logical layouts, clean design).

**Prompt structure:**
```
Create a [type: infographic / diagram / knowledge card / comparison chart / process flow / mind map] about [topic].

[Describe the visual layout - what goes where, how elements connect]

[List ALL text labels, headings, and values that must appear accurately]

Style: [modern minimal / dark mode / blueprint / whiteboard sketch / corporate clean].
Use [color guidance]. White or light background unless specified otherwise.
Make text large and legible. Use clear visual hierarchy.
```

**Prompt rules:**
- ALWAYS list the exact text that must appear in the image - Nano Banana Pro renders text accurately but needs it spelled out
- Describe spatial relationships explicitly ("top to bottom", "left column / right column", "three boxes connected by arrows")
- Keep it narrative, not keyword soup
- Include aspect ratio guidance in the prompt if relevant ("landscape format", "tall portrait")
- For frameworks with specific terms, use the exact terminology

**Type-specific guidance:**

| Source Content | Best Visual Type | Key Prompt Elements |
|---------------|-----------------|---------------------|
| Framework (tiers/levels) | Layered diagram | Vertical stack, labels per tier, progression arrows |
| Process/workflow | Flow diagram | Sequential steps, decision points, directional arrows |
| Comparison (A vs B) | Side-by-side chart | Two columns, matching rows, contrast colours |
| Hierarchy | Org/tree diagram | Parent-child relationships, clear nesting |
| Timeline | Horizontal timeline | Date markers, milestone labels |
| Concept/definition | Knowledge card | Title, description, key attributes, icon suggestions |
| Multi-factor model | Matrix/grid | Row and column headers, cell content |

### 3. Generate the Image

```bash
~/bin/visualise "YOUR CRAFTED PROMPT" -o "OUTPUT_PATH.png"
```

**Output path conventions:**
- Same directory as the source note: `[note-dir]/[descriptive-name].png`
- If the note is in a theme folder, keep the image there
- Name descriptively: `framework-diagram.png`, not `image1.png`

**Options:**
- `-m flash` (default) - Fast and cheap (~$0.04/image)
- `-m pro` - Best quality, superior text rendering (~$0.13/image)
- `--aspect 16:9` (default) - Good for infographics, diagrams
- `--aspect 1:1` - Square, good for knowledge cards, social media
- `--aspect 3:2` - Slides
- `--aspect 9:16` - Tall/portrait, good for mobile or detailed flows
- `--input-image path.png` - Edit an existing image (add elements, restyle, etc.)

### 4. Embed in the Note

After successful generation, add the image embed to the source note:

```markdown
![[descriptive-name.png]]
```

Place it where it makes visual sense - usually near the top of the note or directly after the section it illustrates.

### 5. Iterate if Asked

If the user wants changes:
- For minor tweaks ("make it darker", "bigger text"): use `--input-image` with the existing PNG + modification prompt
- For structural changes: craft a new prompt from scratch
- Always save iterations with the same filename (overwrite) unless user asks to keep versions

## Examples

**User:** "Visualise this framework"

Claude reads the source note, then:

```bash
~/bin/visualise "Create a vertical three-tier diagram showing a framework for AI autonomy.

Three gears stacked vertically, largest at bottom, smallest at top. Each gear is a distinct colour.

Bottom gear (blue, largest): Label 'TIER 1'. Subtitle: 'System observes, humans do all work'. Right side text: 'Visibility economics.'

Middle gear (amber, medium): Label 'TIER 2'. Subtitle: 'Agents handle prep, humans own judgment'. Right side text: 'Leverage economics.'

Top gear (green, smallest): Label 'TIER 3'. Subtitle: 'Agents own full workflow, humans govern exceptions'. Right side text: 'Factory economics.'

Upward arrows between gears showing progression.

Style: modern minimal, dark navy background, clean sans-serif typography. Make all text crisp and legible." -o "02_Themes/project-c/context/framework-diagram.png" --aspect 3:2 -m pro
```

**User:** "Turn this meeting note into a visual summary"

Claude reads the note, identifies key decisions, and:

```bash
~/bin/visualise "Create a clean meeting summary card with four decisions in a 2x2 grid..." -o "path/meeting-visual.png" --aspect 16:9
```

## Error Handling

- **No API key:** Tell user to get one at https://aistudio.google.com/apikey and set `GOOGLE_API_KEY` in their shell profile
- **Safety filter:** Nano Banana Pro may refuse certain prompts. Rephrase without anything that could trigger content filters
- **No image returned:** Model returned text instead of image. Check stderr output and adjust prompt
- **Large/complex prompts:** If generation fails, simplify. Break complex visuals into 2 images rather than one overloaded one

## Notes

- Nano Banana Pro excels at text accuracy - use this. Put labels, numbers, headings in the prompt
- Images include an invisible SynthID watermark (Google policy)
- For LinkedIn/external use, 16:9 or 1:1 aspect ratios work best
- Use `-m pro` for anything going external; `-m flash` for internal vault visuals
