# Art Style Consistency

## Description

Lock a consistent art style across multiple generations.

## Prompt

Create a reusable style block to keep consistent art across generations.

Style reference description: {STYLE_DESCRIPTION}

Output:
1. **Style lock paragraph** (copy-paste into every generation):
   - Art medium + technique, line weight, texture type
   - Palette (exact hex values) with dominant ratio 60/30/10
   - Lighting model, shadow style, highlight treatment
   - Character features: face shape, eye style, proportions (if characters present)
   - Rendering finish: (e.g., clean cel, painterly, textured matte)
2. **Anti-drift words**: terms that pull the style (e.g., "flat vector, consistent lighting")
3. **Negative prompt block**: what to exclude
4. **Settings**: recommended model, CFG range, seed workflow
5. **Test prompt**: a sample scene using the style block

Keep the style block under 100 words so it fits in most generators.
