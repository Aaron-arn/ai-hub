# Isometric Icon Set

## Description

Builds a consistent isometric icon set prompt for a category you choose (e.g. finance, health, travel). Use it to generate matching icon families for apps, slides, or documentation. Works with Midjourney, DALL-E, and Stable Diffusion.

## Prompt

Act as a UI icon designer and prompt engineer. Ask me for the icon category and the number of icons needed (4 to 8). Then produce one code-block prompt that generates the whole set consistently, using this structure: isometric icon set of [N] icons for [category], each icon a 3D-looking flat-shaded isometric object with rounded edges, same perspective angle, single accent color [color] with neutral gray shading, soft drop shadow, on individual light gray tiles, clean vector style, no text.

Example for finance:

```text
Isometric icon set of 6 icons for personal finance, wallet, piggy bank, credit card, growth chart, coins, safe, each a 3D-looking flat-shaded isometric object with rounded edges, same perspective angle, single accent emerald green with neutral gray shading, soft drop shadow, on individual light gray tiles, clean vector style, no text
```

Then list the specific icons I requested so I can verify coverage, and suggest one alternative color scheme. If the tool generates fewer icons than requested, tell me how to regenerate the missing ones using the same description.

## Notes

- Keeping the accent color identical across icons is what makes the set feel cohesive.
- Regenerate with the same seed (Midjourney --seed) to keep consistency.
