# Long Document Summarizer

## Description

Summarizes long documents in layers: a one-paragraph top line, a bulleted key points list, and a reference section. Use it for reports, research papers, contracts, or book chapters. The layered format lets you use the summary at the depth you need and verify claims against the original.

## Prompt

You are an analytical reader who summarizes long documents without losing substance. Summarize the document I paste below.

Document: [paste the full text, or paste it in chunks if too long for one message]

Purpose of this summary: [e.g. decide whether to read the full document, extract arguments, prepare a briefing]

Output in exactly this structure:
1. One-paragraph summary: 80-120 words covering the document's purpose, main argument, and conclusion. No detail beyond the essentials.
2. Key points: 6-10 bullets, each one fact or finding with enough context to stand alone. Order by importance, not by document order.
3. Numbers and claims: a list of all specific numbers, statistics, or claims with the page or section they come from, if identifiable.
4. Notable quotes: up to 5 short direct quotes (under 30 words each) that capture the document's voice or strongest statements.
5. Gaps and weaknesses: 3-5 things the document leaves unclear, argues weakly, or omits.
6. Verdict: 2-3 sentences on whether the full document is worth reading for my stated purpose.

Rules: do not editorialize in the key points, only in the verdict and gaps sections. If a claim is repeated, say it once and note it is central. Do not invent page numbers; use section names if pages are unknown. If the document is shorter than 300 words, say so and summarize normally.

## Notes

For very long documents, paste in chunks and ask for the same structure, then merge the key points yourself. Works well on transcribed interviews too.
