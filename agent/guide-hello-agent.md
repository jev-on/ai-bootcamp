# Guide: Hello Agent (Your First LLM Call)

Before we can build an autonomous agent, we need to learn how to talk to the "Brain" (The LLM) using code, rather than a chat app.

## Prerequisites
*   **Python Installed**
*   **API Key:** You need a key from **one** of these providers:
    *   **Anthropic (Claude):** [console.anthropic.com](https://console.anthropic.com/) (Requires credit deposit).
    *   **Google (Gemini):** [aistudio.google.com](https://aistudio.google.com/) (Has a generous free tier).

---

## Step 1: Setup

1.  **Create a folder:**
    ```bash
    mkdir my-agent
    cd my-agent
    ```

2.  **Initialize & Install:**
    We will install libraries for both providers so you can choose.
    ```bash
    uv init
    uv add anthropic google-generativeai python-dotenv
    ```

3.  **Secure your Key:**
    Create a file named `.env` and paste your key(s) inside. You only need one, but you can add both.
    ```text
    ANTHROPIC_API_KEY=sk-ant-api03-...
    GEMINI_API_KEY=AIzaSy...
    ```
    **IMPORTANT:** Add `.env` to your `.gitignore` file so you never accidentally upload your key to GitHub!

---

## Step 2: The Code

Create `hello_agent.py`. Choose the code below that matches the API key you have.

### Option A: Using Anthropic (Claude)

```python
import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

print("Asking Claude...")
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Hello! Who are you?"}
    ]
)
print(f"Claude says: {response.content[0].text}")
```

### Option B: Using Google (Gemini)

```python
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

print("Asking Gemini...")
response = model.generate_content("Hello! Who are you?")
print(f"Gemini says: {response.text}")
```

## Step 3: Run It

```bash
uv run hello_agent.py
```
*Make sure you uncommented one of the options in the file!*

## What just happened?
You didn't use an app. **Your code** sent a message to the AI servers, waited for the "Brain" to think, and got the text back. 

This `response` object is the building block of everything. In the next guide, we will teach this script how to use your **Weather Tool**.
