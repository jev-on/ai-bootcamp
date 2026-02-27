import os
from dotenv import load_dotenv
from google import genai

from wiki_tools import get_wikipedia_summary, search_wikipedia

# Load API Key from .env
load_dotenv()

# Create the Gemini Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Register the Python function as a tool
tools = [get_wikipedia_summary, search_wikipedia]

# Start the Autonomous Chat
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
