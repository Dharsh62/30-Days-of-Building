"""
Day 2 example — LLM API basics using GROQ
-------------------------------------------
Setup:
    pip install groq python-dotenv
    Get a free key at https://console.groq.com  (API Keys section)
    Create a .env file in the same folder with:
        GROQ_API_KEY=your_key_here
    Add .env to .gitignore BEFORE committing anything.

Key difference from Gemini's shape:
    Groq uses the standard "chat completions" pattern: you send a
    LIST of messages, each with a role ("system", "user", "assistant")
    and content — not a single prompt string + separate system_instruction.
    This is the same pattern OpenAI, most other LLM APIs, and LangChain use,
    so learning it now pays off everywhere later in the roadmap.
"""

import os
from dotenv import load_dotenv
from groq import Groq

# ---- 1. Auth ----
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found. Did you create a .env file?")

client = Groq(api_key=api_key)
MODEL = "llama-3.3-70b-versatile"  # current, solid free-tier model


# ---- 2. Basic call ----
def basic_call(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


# ---- 3. Generation parameters: temperature, max_tokens, top_p ----
def call_with_params(prompt: str, temperature: float = 1.0, max_tokens: int = 200) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,   # 0 = deterministic, higher = more random
        max_tokens=max_tokens,
        top_p=0.9,
    )
    return response.choices[0].message.content


# ---- 4. System prompt / persona pattern ----
def call_with_persona(prompt: str, persona: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": persona},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content


# ---- 5. Error handling wrapper ----
def safe_call(prompt: str, **kwargs) -> str:
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            **kwargs,
        )
        if not response.choices:
            return "[No response generated]"
        return response.choices[0].message.content
    except Exception as e:
        return f"[Error: {e}]"


# ---- 6. Mini CLI Q&A loop (with conversation memory this time) ----
def main():
    print("Day 2 LLM Chat with Groq API")
    print("Please type 'quit' to exit.\n")

    demo_prompt = "Give me one word that describes a rainy day."
    print("Temp=0:", call_with_params(demo_prompt, temperature=0))
    print("Temp=1:", call_with_params(demo_prompt, temperature=1))
    print()

    question = "What is an API?"
    print("Persona=terse reviewer:",
          call_with_persona(question, "You are a terse technical reviewer. Answer in one sentence."))
    print("Persona=friendly explainer:",
          call_with_persona(question, "You are a friendly teacher explaining to a beginner."))
    print()

    while True:
        user_input = input("You: ")
        if user_input.lower() in ("quit", "exit"):
            break
        answer = safe_call(user_input)
        print("AI:", answer, "\n")


if __name__ == "__main__":
    main()