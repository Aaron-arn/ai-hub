# Cinematic Product Shot

## Description

Generates a detailed, ready-to-paste image generation prompt for a cinematic product photograph. Use it when you need hero imagery for a product launch, advertisement, or portfolio. Works with Midjourney, DALL-E, Stable Diffusion, and similar text-to-image tools.

## Prompt

Act as an expert product photographer and prompt engineer. I will tell you my product, its key features, and the mood or audience I am targeting. Then produce the final generation prompt inside a code block, built from these parts:

- Subject: the product described in 8-12 words, with materials, colors, and finish.
- Environment: a short backdrop and props suggestion.
- Lighting: one dominant light source plus a fill or rim light.
- Camera: lens, aperture, and angle (e.g. "85mm, f/1.8, low-angle").
- Style: mood keywords such as "moody", "minimal", or "luxurious".
- Technical: resolution and detail keywords.

Example result for a wireless keyboard:

```text
Cinematic hero shot of a matte-black wireless mechanical keyboard with brushed aluminum frame on a dark slate surface, dramatic low-key lighting with a warm rim light from the upper left, faint haze in the background, shallow depth of field, macro detail on the keycaps, premium tech advertisement mood, 8k, 85mm lens at f/1.4
```

Also give me a negative prompt (for Stable Diffusion) and two variations: one brighter and one more abstract. Ask clarifying questions first if the product or mood is unclear.

## Notes

- Swap the lens and lighting keywords to change the mood without changing the product.
- For DALL-E, drop the negative prompt; for Midjourney, add --ar 16:9 for a hero banner.
