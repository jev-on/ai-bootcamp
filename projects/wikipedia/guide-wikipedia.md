# Guide: Building a Wikipedia Agent

Now that you've built a Weather Agent, let's explore retrieving and processing vast amounts of text-based information. We will build an AI agent that can query **Wikipedia**, retrieve summaries of topics, and answer your questions based on that specific information.

## The Concept: Knowledge Retrieval 📚

In the Weather Agent, we fetched small, specific data points (temperatures, coordinates). With this Wikipedia Agent, we are practicing **RAG (Retrieval-Augmented Generation)** fundamentals.

1.  **User:** "Who was Alan Turing?"
2.  **LLM (Think):** "I need information about Alan Turing. I'll use `get_wikipedia_summary`."
3.  **The Agent (Act):** Your script queries the official Wikipedia API for "Alan Turing".
4.  **LLM (Observe):** Receives the biographical summary text.
5.  **The Agent (Answer):** Synthesizes the text to give you a clear, accurate answer based *only* on the retrieved data.

**Choose your path below:**
*   [**Path A: Anthropic (Claude)**](#path-a-anthropic-claude) - Manual tool loop.
*   [**Path B: Google (Gemini)**](#path-b-google-gemini) - Automatic tool loop.

---

## Path A: Anthropic (Claude)

### 1. Setup
Create a new folder for this agent:
```bash
mkdir wiki-claude
cd wiki-claude
uv init
uv add anthropic requests python-dotenv
```

### 2. Create the Tools
Create a file named `wiki_tools.py` inside your `wiki-claude` folder. We will use the beginner-friendly Wikipedia REST API.

```python
import requests

def get_wikipedia_summary(topic: str) -> str:
    """Fetches a summary of a topic from Wikipedia."""
    print(f"--- [TOOL] Searching Wikipedia for: {topic}...")
    
    # Format the topic for the URL (replace spaces with underscores)
    formatted_topic = topic.replace(" ", "_")
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{formatted_topic}"
    
    # We must include a User-Agent header as requested by Wikipedia's API policies
    headers = {
        "User-Agent": "AIBootcampAgent/1.0 (https://github.com/jev-on/ai-bootcamp)"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("extract", "No summary found for this topic.")
    elif response.status_code == 404:
        return "Topic not found on Wikipedia. Try a different search term."
    else:
        return f"Error connecting to Wikipedia: Status {response.status_code}"
```

### 3. The Code
Create `wiki_agent_claude.py`. 

```python
import os
import json
from dotenv import load_dotenv
from anthropic import Anthropic
from wiki_tools import get_wikipedia_summary

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# 1. Define the tool for Claude
tools_definition = [
    {
        "name": "get_wikipedia_summary",
        "description": "Fetches a text summary of a topic from Wikipedia.",
        "input_schema": {
            "type": "object",
            "properties": {
                "topic": {"type": "string", "description": "The subject to look up, e.g. Alan Turing"}
            },
            "required": ["topic"]
        }
    }
]

def run_agent(user_message):
    messages = [{"role": "user", "content": user_message}]
    
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        tools=tools_definition,
        messages=messages
    )

    while response.stop_reason == "tool_use":
        tool_use = next(block for block in response.content if block.type == "tool_use")
        tool_name = tool_use.name
        tool_input = tool_use.input

        if tool_name == "get_wikipedia_summary":
            result = get_wikipedia_summary(tool_input["topic"])

        messages.append({"role": "assistant", "content": response.content})
        messages.append({
            "role": "user", 
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": json.dumps(result)
                }
            ]
        })

        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            tools=tools_definition,
            messages=messages
        )

    return response.content[0].text

print("Wikipedia Agent ready! Ask me about any topic.")
query = input("You: ")
print(f"Agent: {run_agent(query)}")
```

### 4. Run It
Be sure your `.env` file in this directory contains `ANTHROPIC_API_KEY`.
```bash
uv run wiki_agent_claude.py
```

---

## Path B: Google (Gemini)

### 1. Setup
Create a new folder for this agent:
```bash
mkdir wiki-gemini
cd wiki-gemini
uv init
uv add google-genai requests python-dotenv
```

### 2. Create the Tools
Create a file named `wiki_tools.py` inside your `wiki-gemini` folder. (This is exactly the same as Path A).

```python
import requests

def get_wikipedia_summary(topic: str) -> str:
    """Fetches a summary of a topic from Wikipedia."""
    print(f"--- [TOOL] Searching Wikipedia for: {topic}...")
    
    formatted_topic = topic.replace(" ", "_")
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{formatted_topic}"
    
    headers = {
        "User-Agent": "AIBootcampAgent/1.0 (https://github.com/jev-on/ai-bootcamp)"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("extract", "No summary found for this topic.")
    elif response.status_code == 404:
        return "Topic not found on Wikipedia. Try a different search term."
    else:
        return f"Error connecting to Wikipedia: Status {response.status_code}"
```

### 3. The Code
Create `wiki_agent_gemini.py`.

```python
import os
from dotenv import load_dotenv
from google import genai
from wiki_tools import get_wikipedia_summary

load_dotenv()

# Always use genai (V1 SDK) as per the project standards
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Register the Python function as a tool
tools = [get_wikipedia_summary]

# Start the Autonomous Chat utilizing AUTO function calling
chat = client.chats.create(
    model="gemini-3-flash-preview",
    config={
        "tools": tools, 
        "tool_config": {"function_calling_config": {"mode": "AUTO"}}
    }
)

print("Wikipedia Agent ready! Ask me about any topic (or type 'quit').")

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["quit", "exit"]:
        print("Goodbye!")
        break
        
    response = chat.send_message(user_input)
    print(f"Agent: {response.text}")
```

### 4. Run It
Be sure your `.env` file in this directory contains `GEMINI_API_KEY`.
```bash
uv run wiki_agent_gemini.py
```

**Try asking:** "Can you summarize the plot of The Matrix?"
Watch the console to see the agent automatically querying Wikipedia!
