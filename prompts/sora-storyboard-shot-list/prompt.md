# Sora Storyboard and Shot List

## Description

Turns a concept into a shot-by-shot storyboard and shot list ready for AI video tools like Sora, Veo, or Runway. Use it in pre-production to plan pacing, camera moves, and dialogue. Includes ready-to-paste generation prompts for each shot.

## Prompt

Act as a film director and AI video prompt engineer. I will describe a 30- to 60-second video idea, its audience, and the platform (YouTube, social, ad). Turn it into a shot list with exactly 8 to 12 shots, each with:

- Shot number, duration in seconds, and camera move (static, push-in, orbit, drone, pan, etc.).
- Scene description: subject, setting, action, and lighting.
- Audio cue: dialogue, music mood, or sound effect.
- A ready-to-paste generation prompt in a code block, following this structure: cinematic [camera move] shot of [subject and action], [setting], [lighting], [color grade], [style keywords], realistic motion, consistent character appearance.

Example shot:

```text
Cinematic slow push-in shot of a hiker in a red jacket standing at a misty mountain ridge at sunrise, golden light breaking through fog, teal and orange color grade, photorealistic, realistic motion, consistent character appearance
```

Finish with a production checklist: repeating the exact character description in every shot, lighting continuity notes, and which shots need a seed or reference image for consistency.

## Notes

- Repeat the exact character description in every shot to keep consistency across generations.
- Keep shots under 4 seconds: AI video tools generate short clips that edit together cleanly.
