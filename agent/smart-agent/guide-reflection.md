# Guide: Self-Correction (Reflection) 🧐📝

In this guide, we will add the "Editor" to our agent. This concept is called **Reflection**, and it's one of the most powerful patterns for making agents reliable.

## The Concept: The Editor Pattern
Most agents are "one and done." They write something and send it. Reflection adds a second step:
1.  **The Writer:** Generates the initial draft.
2.  **The Critic (Reflection):** Reviews the draft and looks for mistakes.
3.  **The Rewriter:** Fixes the draft based on the critique.

---

## 🛠️ The Reflection Logic

Adding reflection is as simple as making a second API call with a specific prompt.

### 1. The Critique Prompt
After your agent generates its briefing, you don't send it immediately. Instead, you ask the LLM:
> "Review this weather briefing: [DRAFT]. Does it mention the temperature? Is it too long? Reply with a list of improvements or say 'GOOD'."

### 2. The Rewrite Step
If the LLM doesn't say "GOOD", you make one last call:
> "Rewrite the briefing based on these improvements: [CRITIQUE]."

---

## 💻 Code Example (Conceptual)

Here is how you would add it to your `daily_briefing.py` script:

```python
# Step 1: Initial Draft
briefing = chat.send_message("Get weather and write a summary.")

# Step 2: Reflection (The Critique)
critique = chat.send_message(f"Review this briefing: '{briefing}'. Is it professional? Does it mention the rain? If it's perfect, reply 'GOOD'.")

# Step 3: Decision
if "GOOD" not in critique.text:
    print("--- [REFLECTION] Agent found improvements! Rewriting...")
    final_briefing = chat.send_message(f"Rewrite the briefing perfectly based on your own critique.")
else:
    final_briefing = briefing

# Step 4: Final Action
send_email(final_briefing)
```

---

## Why this is a "Smart Agent" feature:
*   **Accuracy:** It catches its own hallucinations.
*   **Formatting:** It ensures the output matches the user's requirements every single time.
*   **Tone:** It can self-correct from "boring" to "friendly."

By adding this, your **Daily Briefing Agent** becomes significantly higher quality!
