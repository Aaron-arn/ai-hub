# Flashcard Generator

## Description

Turn study material into Anki-ready flashcards.

## Prompt

Generate flashcards from this material: {STUDY_MATERIAL}

Rules:
1. One fact per card; question phrasing must not give away the answer
2. Mix of card types: definition, concept application, fill-in-the-blank, "compare X and Y", "why does X work"
3. Answers: max 1-2 sentences, no fluff
4. 20% of cards should be "deep" questions (explain why/how) not just recall
5. Cloze deletions: `{{c1::...}}` format for 5 cards
6. Tag each card: {TAG_PREFIX}::<topic>

Output as a TSV table ready for Anki import: `Question	Answer	Tags`. Aim for 25-40 cards covering all key concepts. Skip trivia.
