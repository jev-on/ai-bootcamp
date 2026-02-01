# Guide: Hello Agent (Your First LLM Call)

Before we can build an autonomous agent, we need to learn how to talk to the LLM (Large Language Model) using code.

**Choose your path below:**

*   [**Path A: Anthropic (Claude)**](#path-a-anthropic-claude) - Best for complex reasoning and coding.
*   [**Path B: Google (Gemini)**](#path-b-google-gemini) - Best for speed and a free tier.

---

## Path A: Anthropic (Claude)

### 1. Prerequisites
*   **API Key:** Get one from [console.anthropic.com](https://console.anthropic.com/).
*   **Cost:** Requires a small credit deposit (approx. $5).

### 2. Setup
Run these commands in your terminal:

```bash
mkdir agent-claude
cd agent-claude
uv init
uv add anthropic python-dotenv
```

Create a `.env` file with your key:
```text
ANTHROPIC_API_KEY=sk-ant-...
```

### 3. The Code
Create `hello_claude.py`:

```python
import os
from dotenv import load_dotenv
from anthropic import Anthropic

# 1. Load secrets from the .env file
# This is a security step so we don't put passwords directly in the code.
load_dotenv()

# 2. Connect to Anthropic
# We create a "client" object that knows how to talk to Claude.
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

print("Asking Claude...")

# 3. Send the message
# We ask for "claude-3-5-sonnet" (the smart one).
# max_tokens=1000 means "don't write an essay longer than 1000 words".
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Hello! Who are you?"}
    ]
)

# 4. Print the answer
# The response comes back as a complex object. We dig into it to find the text.
print(f"Claude says: {response.content[0].text}")
```

### 4. Run It
```bash
uv run hello_claude.py
```

---

## Path B: Google (Gemini)

### 1. Prerequisites
*   **API Key:** Get one from [aistudio.google.com](https://aistudio.google.com/).
*   **Cost:** Generous free tier available.

### 2. Setup
Run these commands in your terminal:

```bash
mkdir agent-gemini
cd agent-gemini
uv init
uv add google-genai python-dotenv
```

Create a `.env` file with your key:
```text
GEMINI_API_KEY=AIzaSy...
```

### 3. The Code
Create `hello_gemini.py`.
*Note: We are using the modern `google-genai` SDK.*

```python
import os
from dotenv import load_dotenv
from google import genai

# 1. Load secrets from the .env file
# This keeps your API key safe and out of the code.
load_dotenv()

# 2. Connect to Google
# We create a "client" using the key we just loaded.
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("Asking Gemini...")

# 3. Send the message
# We use the "gemini-3-flash" model (Target standard).
response = client.models.generate_content(
    model="gemini-3-flash",
    contents="Hello! Who are you?"
)

# 4. Print the answer
# Gemini's response object is simpler; we just ask for .text
print(f"Gemini says: {response.text}")
```

### 4. Run It
```bash
uv run hello_gemini.py
```

---

## What just happened?
You didn't use an app. **Your code** sent a message to the AI servers, waited for the LLM to think, and got the text back. 

This `response` object is the building block of everything. In the next guide, we will teach this script how to use your **Weather Tool**.
