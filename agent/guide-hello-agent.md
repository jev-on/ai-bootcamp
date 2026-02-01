# Guide: Hello Agent (Your First LLM Call)

Before we can build an autonomous agent, we need to learn how to talk to the "Brain" (The LLM) using code, rather than a chat app.

## Prerequisites
*   **Python Installed**
*   **API Key:** You need an API key from Anthropic (for Claude).
    *   Get one here: [console.anthropic.com](https://console.anthropic.com/)
    *   *Note: This usually requires a small credit deposit ($5).*

---

## Step 1: Setup

1.  **Create a folder:**
    ```bash
    mkdir my-agent
    cd my-agent
    ```

2.  **Initialize & Install:**
    We will use the `anthropic` library.
    ```bash
    uv init
    uv add anthropic python-dotenv
    ```
    *(We also installed `python-dotenv` to handle your API key securely).*

3.  **Secure your Key:**
    Create a file named `.env` and paste your key inside:
    ```text
    ANTHROPIC_API_KEY=sk-ant-api03-...
    ```
    **IMPORTANT:** Add `.env` to your `.gitignore` file so you never accidentally upload your key to GitHub!

---

## Step 2: The Code

Create `hello_agent.py`:

```python
import os
from dotenv import load_dotenv
from anthropic import Anthropic

# 1. Load the secret key
load_dotenv()

# 2. Connect to the Brain
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# 3. Send a Message
print("Agent is thinking...")
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Hello! I am building my first AI agent. Who are you?"}
    ]
)

# 4. Print the Reply
print(f"Agent says: {response.content[0].text}")
```

## Step 3: Run It

```bash
uv run hello_agent.py
```

## What just happened?
You didn't use the Claude App. **Your code** sent a message to Anthropic's servers, waited for the AI to "think," and got the text back. 

This `response` object is the building block of everything. In the next guide, we will teach this script how to use your **Weather Tool**.
