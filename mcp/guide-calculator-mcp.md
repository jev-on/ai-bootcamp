# Guide: Building a Simple Calculator MCP Server

This guide will walk you through creating your very first **Model Context Protocol (MCP)** server. We will build a "Calculator Server" that gives Claude a new "tool" to add numbers together. 

This example is completely local and does not require any internet access or API keys.

## Prerequisites

*   **Claude Desktop App:** Download and install from [claude.ai/download](https://claude.ai/download).
    *   *Note:* Other apps like **Cursor**, **Zed**, and **Sourcegraph Cody** also support MCP!
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
    *This creates a few standard files:*
    *   `pyproject.toml`: The recipe book for your project (lists dependencies).
    *   `.python-version`: Locks the Python version so it works consistently.
    *   `.gitignore`: Tells Git which files to ignore.
    *   `hello.py` (or `main.py`): A starter file. You can delete this, as we'll create our own.

3.  **Add the MCP dependency:**
    ```bash
    uv add "mcp[cli]"
    ```
    *   **mcp**: The core Python library (SDK) that allows us to build the server.
    *   **[cli]**: Installs extra developer tools, like the **MCP Inspector**, which helps you test your server in a web browser before connecting it to Claude.

    *After running this command, you will see a new file called `uv.lock`:*
    *   **uv.lock (The "Itemized Receipt"):** While `pyproject.toml` is your "grocery list" (general needs), `uv.lock` records the **exact version** of every library installed. This ensures the project works identically on every computer. **Don't edit this file manually!**

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
Alternatively, you can try the below code that does addition, subtraction, division and multiplication.

```python
################ Full Calculator ###############
#def main():
#    print("Hello from p1-calculator!")


#if __name__ == "__main__":
#    main()


from mcp.server.fastmcp import FastMCP
from typing import Union

# 1. Initialize the MCP Server
mcp = FastMCP("Calculator")

# 2. Define a "Tool" - This is what Claude will see and use
# The @mcp.tool() decorator tells the system: "Hey, let the AI use this function!"
@mcp.tool()
def calc(a: int, b: int, operation: str) -> Union[int, float]:
    """
    Performs a mathematical calculation between two numbers.

    :param a: The first number.
    :param b: The second number.
    :param operation: The operation to perform.
                      Can be 'add', 'plus', 'addition',
                      'sub', 'minus', 'subtract', 'subtraction', 'substration',
                      'mul', 'times', 'multiply', 'multiplication',
                      'div', 'divide', 'division'.
    :return: The result of the calculation.
    """
    print("Hello from p1-calculator!")
    op = operation.lower()
    if op in ["add", "plus", "addition"]:
        return a + b
    elif op in ["sub", "minus", "subtract", "subtraction", "substration"]:
        return a - b
    elif op in ["mul", "times", "multiply", "multiplication"]:
        return a * b
    elif op in ["div", "divide", "division"]:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError(f"Unknown operation: {operation}")


    
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

    OR for VSCode

    ```bash
    code /Users/jevon/Library/Application\ Support/Code/User/mcp.json
    ```

3.  **Add the Server Config:**
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

4.  **Restart Claude:**
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

1.  **Claude (The LLM):** "I need to add two numbers. I see a tool called `add_numbers`. I'll use that."
2.  **Claude App (The Host):** Sends a message to your `calculator.py` script: 
    *   *Message:* `{"name": "add_numbers", "args": {"a": 12345, "b": 67890}}`
3.  **calculator.py (The Server):** 
    *   Receives the message.
    *   Runs your python function `return 12345 + 67890`.
    *   Sends back the answer: `80235`.
4.  **Claude (The LLM):** Receives the answer `80235` and writes the final response to you.

This is the power of MCP: **Claude didn't guess the answer; it actually ran your code to calculate it.**

```
