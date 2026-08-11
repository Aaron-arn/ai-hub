# Contract Summarizer

## Description

Summarize legal contracts in plain language with risk flags.

## Prompt

Summarize this contract in plain language: {CONTRACT_TEXT}

Output:
1. **Overview**: 3 sentences - parties, purpose, term
2. **Key terms table**: Term | What it means | For whom it favors
3. **Rights & obligations**: what each party must do (bullet per party)
4. **Money**: fees, payment schedule, penalties, renewal pricing
5. **Risks**: clauses to watch - auto-renewal, exclusivity, termination penalties, liability caps, indemnification, non-compete, IP assignment
6. **Open questions**: anything ambiguous or missing that I should ask about

Note: educational summary, not legal advice. Quote the exact clause text for anything in the Risks section so I can verify.
