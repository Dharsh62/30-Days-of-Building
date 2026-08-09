# Day 2 — LLM API Basics

## What I did
- Made my first LLM API calls using Groq
- Explored generation parameters: `temperature`, `top_p`, `max_tokens`
- Built a system prompt / persona pattern (same question, different personas)
- Added basic error handling around API calls
- Built a small CLI Q&A chat tool (`llm_chat.py`)

## Key learnings
- Chat completions APIs take a **list of role/content messages**, not just a single prompt string — this pattern shows up everywhere, including LangChain later in the roadmap
- `temperature=0` = deterministic output, higher = more random/creative
- `input()` needs a real terminal — doesn't work in VS Code Code Runner's output panel

## Files
- `llm_chat.py` — CLI tool that calls the Groq API, with temperature/persona demos and an interactive loop

## Next
Day 3 — structured outputs / JSON mode
