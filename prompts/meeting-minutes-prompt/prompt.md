# Meeting Minutes

## Description

Summarize meeting transcripts into actionable minutes.

## Prompt

Convert this meeting transcript into professional minutes: {TRANSCRIPT}

Output:
1. **Header**: meeting title, date, attendees, duration
2. **Summary**: 3-4 sentence overview
3. **Decisions**: bullet list - each decision with context (who proposed, any dissent)
4. **Action items**: table with columns: Task | Owner | Due date | Priority (only explicit commitments, nothing invented)
5. **Discussion notes**: key points per agenda topic, max 3 bullets each
6. **Open questions**: anything unresolved

Rules: never invent action items or dates - if the transcript doesn't specify an owner/due date, mark as TBD. Preserve disagreement. Neutral tone, no opinions.
