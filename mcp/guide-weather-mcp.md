# Guide: Building a Weather MCP Server

This guide builds upon the Calculator example. Now, we will give Claude the power to reach out to the internet and fetch real-world data.

We will build a **Weather Server** that fetches the forecast from **Open-Meteo** (a free weather API).

## Prerequisites

*   You have completed the [Calculator Guide](./guide-calculator-mcp.md).
*   **uv** is installed.

---

## Step 1: Set Up Your Project

1.  **Create a new directory:**
    ```bash
    mkdir weather-mcp
    cd weather-mcp
    ```

2.  **Initialize the project:**
    ```bash
    uv init
    ```

3.  **Add dependencies:**
    We need `mcp` (for the server) and `requests` (to make simple web requests).
    ```bash
    uv add "mcp[cli]" requests
    ```

---

## Step 2: Write the Server Code

Create a file named `weather.py`.

Notice how this code looks just like a normal Python function. No `async` or `await` is needed here!

```python
# weather.py
from mcp.server.fastmcp import FastMCP
import requests

# 1. Initialize the Server
mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(latitude: float, longitude: float) -> str:
    """
    Get the current weather for a specific location.
    
    Args:
        latitude: The latitude of the location.
        longitude: The longitude of the location.
    """
    # Using Open-Meteo: A free weather API that doesn't need a key
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    
    # Make the request and get the data
    response = requests.get(url)
    data = response.json()
    
    # Extract the current temperature
    temp = data["current_weather"]["temperature"]
    return f"The current temperature at {latitude}, {longitude} is {temp}°C."

@mcp.tool()
def get_coordinates(city_name: str) -> str:
    """
    Find the latitude and longitude for a city name.
    
    Args:
        city_name: The name of the city (e.g., "Paris", "San Francisco").
    """
    # Use Open-Meteo's Geocoding API to find the location
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    
    response = requests.get(url)
    data = response.json()
    
    if "results" in data:
        result = data["results"][0]
        lat = result["latitude"]
        lon = result["longitude"]
        return f"{lat},{lon}"
    else:
        return "City not found."

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

---

## Step 3: Configure Claude Desktop

1.  **Open your config:**
    ```bash
    code ~/Library/Application\ Support/Claude/claude_desktop_config.json
    ```

2.  **Add the "weather" server:**
    Add a new entry to your `mcpServers` list.
    *(Replace `/Users/YOUR_NAME/...` with your actual path)*

    ```json
    {
      "mcpServers": {
        "my_calculator": { ... }, 
        "weather": {
          "command": "uv",
          "args": [
            "--directory",
            "/Users/YOUR_NAME/path/to/weather-mcp",
            "run",
            "weather.py"
          ]
        }
      }
    }
    ```

3.  **Restart Claude.**

---

## Step 4: Test It Out!

1.  Check the 🔌 icon. You should see both **Calculator** and **Weather**.
2.  Ask Claude:
    > "What is the weather in San Francisco?"
3.  **Watch the Magic (Tool Chaining):**
    *   Claude sees it has a `get_weather` tool, but that tool needs coordinates.
    *   It sees it has a `get_coordinates` tool that takes a city name.
    *   **Step 1:** Claude calls `get_coordinates("San Francisco")` -> gets "37.77,-122.41".
    *   **Step 2:** Claude takes that result and calls `get_weather(37.77, -122.41)`.
    *   **Step 3:** It tells you the answer.
    
    You didn't have to program this logic. Claude figured out the workflow on its own!

---

## Step 5: Key Concepts Learned

1.  **Async/Await:** Web requests are slow. We use `async` so our code doesn't freeze while waiting for the NWS website to reply.
2.  **External APIs:** This MCP server acts as a bridge. Claude asks the server, the server asks NWS, and the answer flows back.
3.  **Multiple Servers:** You can have as many MCP servers running as you want (Calculator + Weather + Files, etc.).
