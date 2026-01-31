# Guide: Building a Simple Calculator MCP Server

This guide will walk you through creating your very first **Model Context Protocol (MCP)** server. We will build a "Calculator Server" that gives Claude a new "tool" to add numbers together. 

This example is completely local and does not require any internet access or API keys.

## Prerequisites

*   **Claude Desktop App:** Download and install from [anthropic.com/claude/desktop](https://anthropic.com/claude/desktop).
*   **Python:** Ensure Python is installed on your machine.
*   **uv:** A fast Python tool manager.
    ```bash
    # Install uv via curl
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

---

## Step 1: Set Up Your Project

1.  **Create a directory:**
    ```bash
    mkdir calculator-mcp
    cd calculator-mcp
    ```

2.  **Initialize the project:**
    ```bash
    uv init
    ```

3.  **Add the MCP dependency:**
    ```bash
    uv add "mcp[cli]"
    ```

---

## Step 2: Write the Server Code

Create a file named `calculator.py` in your folder and paste this code:

```python
# calculator.py
from mcp.server.fastmcp import FastMCP

# 1. Initialize the MCP Server
mcp = FastMCP("Calculator")

# 2. Define a "Tool" - This is what Claude will see and use
# The @mcp.tool() decorator tells the system: "Hey, let the AI use this function!"
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """
    Adds two numbers together. Use this when you need to perform addition.
    
    Args:
        a: The first number to add.
        b: The second number to add.
    """
    # This is standard Python code. 
    # When Claude calls this tool, it runs this logic on your machine.
    return a + b

# 3. Start the server
if __name__ == "__main__":
    # This keeps the program running and listening for messages from Claude.
    # "transport='stdio'" means it talks through Standard Input/Output (terminal pipes).
    mcp.run(transport="stdio")
```

---

## Step 3: Configure Claude Desktop

Now we need to tell Claude where to find your calculator.

1.  **Open the Config File:**
    Run this in your terminal:
    ```bash
    code ~/Library/Application\ Support/Claude/claude_desktop_config.json
    ```

2.  **Add the Server Config:**
    Paste this JSON into the file. 
    **Important:** Replace `/Users/YOUR_NAME/path/to/calculator-mcp` with your actual folder path (run `pwd` in your terminal to find it).

    ```json
    {
      "mcpServers": {
        "my_calculator": {
          "command": "uv",
          "args": [
            "--directory",
            "/Users/YOUR_NAME/path/to/calculator-mcp",
            "run",
            "calculator.py"
          ]
        }
      }
    }
    ```

3.  **Restart Claude:**
    Completely Quit (Cmd+Q) and reopen Claude Desktop.

---

## Step 4: Test It Out!

1.  Look for the 🔌 (plug icon) in Claude's message box. You should see "Calculator" listed.
2.  Type:
    > "What is 12345 + 67890?"
3.  **Watch it work:** 
    Claude will realize it has a "tool" for addition, send the numbers to your Python script, get the result, and show it to you.

---

## Step 5: Behind the Scenes - What Just Happened?

When you asked "What is 12345 + 67890?", a conversation happened between Claude and your script:

1.  **Claude (The Brain):** "I need to add two numbers. I see a tool called `add_numbers`. I'll use that."
2.  **Claude App (The Host):** Sends a message to your `calculator.py` script: 
    *   *Message:* `{"name": "add_numbers", "args": {"a": 12345, "b": 67890}}`
3.  **calculator.py (The Server):** 
    *   Receives the message.
    *   Runs your python function `return 12345 + 67890`.
    *   Sends back the answer: `80235`.
4.  **Claude (The Brain):** Receives the answer `80235` and writes the final response to you.

This is the power of MCP: **Claude didn't guess the answer; it actually ran your code to calculate it.**

```