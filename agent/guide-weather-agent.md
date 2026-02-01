# Guide: Building Your First Agent (Weather Bot)

Now that you can talk to the LLM via code, it's time to give it **superpowers**. 🚀

In this guide, we will build a **Weather Agent**.
*   It won't just "chat." 💬
*   It will **autonomously** use Python functions to look up real-time data from the internet! 🌍

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

**Choose your path below:**
*   [**Path A: Anthropic (Claude)**](#path-a-anthropic-claude) - Manual tool loop (The "Mechanics" path).
*   [**Path B: Google (Gemini)**](#path-b-google-gemini) - Automatic tool loop (The "Self-Driving" path).

## Path A: Anthropic (Claude)

Claude handles tools using a **Manual Loop**. This is great because it lets you see exactly how the "Think-Act-Observe" cycle works step-by-step.

### 1. Setup
Make sure you are in your `agent-claude` folder.
```bash
cd agent-claude
uv add anthropic requests
```

### 2. Create the Tools
Create a file named `weather_tools.py` inside your `agent-claude` folder.

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

### 3. The Code
Create `weather_agent_claude.py`. 

```python
import os
import json
from dotenv import load_dotenv
from anthropic import Anthropic
from weather_tools import get_coordinates, get_weather

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# 1. Define the tools for Claude
# Claude needs a specific JSON format to understand what your tools do.
tools_definition = [
    {
        "name": "get_coordinates",
        "description": "Finds latitude and longitude for a city name.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city_name": {"type": "string", "description": "The city name, e.g. London"}
            },
            "required": ["city_name"]
        }
    },
    {
        "name": "get_weather",
        "description": "Fetches weather for a specific latitude and longitude.",
        "input_schema": {
            "type": "object",
            "properties": {
                "latitude": {"type": "number"},
                "longitude": {"type": "number"}
            },
            "required": ["latitude", "longitude"]
        }
    }
]

def run_agent(user_message):
    # Step 1: THE THINKING PHASE
    # We send the message and the tool definitions to Claude.
    messages = [{"role": "user", "content": user_message}]
    
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        tools=tools_definition,
        messages=messages
    )

    # Step 2: THE ACTING PHASE
    # We check if Claude wants to use a tool.
    while response.stop_reason == "tool_use":
        # Find the tool request in the response
        tool_use = next(block for block in response.content if block.type == "tool_use")
        tool_name = tool_use.name
        tool_input = tool_use.input

        # Actually run the Python function
        if tool_name == "get_coordinates":
            result = get_coordinates(tool_input["city_name"])
        elif tool_name == "get_weather":
            result = get_weather(tool_input["latitude"], tool_input["longitude"])

        # Step 3: THE OBSERVING PHASE
        # We put the tool result into a new message and send it back to Claude.
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

        # Ask Claude to think again now that it has the tool data
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            tools=tools_definition,
            messages=messages
        )

    return response.content[0].text

print("Agent ready! Ask me about the weather.")
query = input("You: ")
print(f"Agent: {run_agent(query)}")
```

### 3. Run It
```bash
uv run weather_agent_claude.py
```

---

## Path B: Google (Gemini)

Gemini has a feature called **"Automatic Function Calling"**. You just give it the functions, and it handles the loop for you!

### 1. Setup
Make sure you are in your `agent-gemini` folder.
```bash
cd agent-gemini
# Ensure you have the library
uv add google-genai requests
```

### 2. Create the Tools
Create a file named `weather_tools.py` inside your `agent-gemini` folder.

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

### 3. The Code
Create `weather_agent_gemini.py`.

```python
import os
from dotenv import load_dotenv
from google import genai

# 1. Import the specific tools we wrote in the other file
# These are just regular Python functions!
from weather_tools import get_coordinates, get_weather

# 2. Load our API key from the .env file
load_dotenv()

# 3. Create the Gemini Client
# This is our connection to the Google AI servers.
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 4. Tool Registration
# We put our functions into a list. 
# This tells Gemini: "You are allowed to use these specific Python tools."
tools = [get_coordinates, get_weather]

# 5. Start the Autonomous Chat
# We use gemini-3-flash and enable 'AUTO' function calling.
# This means if Gemini needs the weather, it will ASK our script to run 
# the Python functions, get the result, and continue the conversation!
chat = client.chats.create(
    model="gemini-3-flash",
    config={
        "tools": tools, 
        "tool_config": {"function_calling_config": {"mode": "AUTO"}}
    }
)

print("Agent ready! Ask me about the weather (or type 'quit').")

# 6. The User Loop
# This keeps the program running so we can have a back-and-forth conversation.
while True:
    user_input = input("You: ")
    
    # Allow the user to exit the program
    if user_input.lower() in ["quit", "exit"]:
        print("Goodbye!")
        break
        
    # Send the user's question to the agent.
    # Because 'AUTO' mode is on, Gemini will handle all the tool calls 
    # in the background before returning the final text answer.
    response = chat.send_message(user_input)
    
    # Print the final answer from the AI
    print(f"Agent: {response.text}")
```

### 3. Run It
```bash
uv run weather_agent_gemini.py
```

**Try asking:** "What is the weather in London?"
Watch the console. You will see it print `--- [TOOL] ...` automatically!
