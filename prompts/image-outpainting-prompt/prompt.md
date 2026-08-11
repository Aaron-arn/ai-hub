# Image Outpainting

## Description

Seamlessly extend an image beyond its borders.

## Prompt

Outline: extend this image seamlessly to the {DIRECTION} (e.g., left, top) by {AMOUNT}.

Base image description: {IMAGE_DESCRIPTION}
Existing elements to continue: {ELEMENTS} (e.g., horizon line at 60%, wall texture, character at right edge)
Lighting: {LIGHTING} must match the original exactly (note sun direction and shadow angles)
Palette: {PALETTE} from the original

Generation recipe:
1. Keep the original image fixed at {POSITION} in the frame - do not regenerate or restyle it
2. Extend only: {NEW_CONTENT} matching perspective (vanishing point at {VP})
3. Match grain/noise and focus across the seam
4. Color grade the whole result uniformly

Negative: new content must not overlap or clip the original subject; no lighting change, no style shift.
