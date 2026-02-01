# Guide: Building Your First Agent (Weather Bot)

Now that you can talk to the LLM via code, it's time to give it **superpowers**.

In this guide, we will build a **Weather Agent**.
*   It won't just "chat."
*   It will **autonomously** use Python functions to look up real data.

## The Concept: The Agent Loop 🔄

**Buckle up! This is the most exciting part yet.** 🎢

Until now, you have been *using* AI. Now, you are *engineering* it. 

We are effectively going to build a mini version of **Claude Desktop** ourselves! 🛠️

When you used the MCP server before, the Claude app handled all the hard work behind the scenes. Now, **YOU** are building that engine. You are writing the code that decides when to talk, when to act, and when to answer.

1.  **User:** "What is the weather in Tokyo?"
2.  **LLM (Think):** "I don't know, but I have a tool called `get_weather`. I should use it." -> *Returns a Tool Call Request*.
3.  **Your Script (Act):** Sees the request. Runs the Python function. Gets "15°C".
4.  **LLM (Observe):** Sees the result "15°C".
5.  **LLM (Answer):** "The weather in Tokyo is 15°C."

---

## Step 1: The Tools

We need the actual Python functions first. We will use the same logic from our MCP module, but we'll paste it here so our agent can use it directly.

Create a file named `weather_tools.py`:

```python
import requests

def get_coordinates(city_name: str):
    """Finds latitude and longitude for a city."""
    print(f"--- [TOOL] Looking up coordinates for {city_name}...")
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    response = requests.get(url).json()
    if "results" in response:
        return response["results"][0]
    return None

def get_weather(latitude: float, longitude: float):
    """Fetches weather for lat/long."""
    print(f"--- [TOOL] Fetching weather for {latitude},{longitude}...")
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url).json()
    return response["current_weather"]
```

---

## Step 2: Choose Your Path

Different LLMs handle tools differently. Choose your path:

*   [**Path A: Anthropic (Claude)**](#path-a-anthropic-claude) - Manual tool loop (Great for understanding how it works).
*   [**Path B: Google (Gemini)**](#path-b-google-gemini) - Automatic tool loop (Easier/Magic).

---

## Path A: Anthropic (Claude)

*Coming Soon! We are finalizing the easiest way to teach the manual loop.*

---

## Path B: Google (Gemini)

Gemini has a feature called **"Automatic Function Calling"**. You just give it the functions, and it handles the loop for you!

### 1. Setup
Make sure you are in your `agent-gemini` folder (from the previous guide).
```bash
cd agent-gemini
# Ensure you have the library
uv add google-genai
```

### 2. The Code
Create `weather_agent_gemini.py`.

```python
import os
from dotenv import load_dotenv
from google import genai
# Import the tools we just wrote
from weather_tools import get_coordinates, get_weather

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 1. We wrap our functions in a simple dictionary configuration
# This tells Gemini: "Here are the tools you are allowed to use."
tools = [get_coordinates, get_weather]

# 2. Start the Chat
# We enable 'automatic_function_calling=True'. 
# This is the magic. The SDK will run the Python code for us!
chat = client.chats.create(
    model="gemini-3-flash",
    config={
        "tools": tools, 
        "tool_config": {"function_calling_config": {"mode": "AUTO"}}
    }
)

print("Agent ready! Ask me about the weather (or type 'quit').")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        break
        
    response = chat.send_message(user_input)
    print(f"Agent: {response.text}")
```

### 3. Run It
```bash
uv run weather_agent_gemini.py
```

**Try asking:** "What is the weather in London?"
Watch the console. You will see it print `--- [TOOL] ...` automatically!
