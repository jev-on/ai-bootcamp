# Module 2: Building AI Agents

In Module 1 (MCP), we built "Tools" (Hands). In Module 2, we will build the LLM that controls them.

## What is an Agent?
An **Agent** is a program that uses an LLM (Large Language Model) as its reasoning engine to perform multi-step tasks autonomously.

Unlike a simple chatbot, an agent can:
1.  **Plan:** Break a goal into steps.
2.  **Act:** Use tools (like your Weather MCP) to get information.
3.  **Observe:** Read the tool's output and decide what to do next.

## Recommended Resources
*   **[Video: What are AI Agents?](https://youtu.be/ftBWgcwvEk4?si=PnUs5kpVOtsE6HoJ)** - A highly recommended high-level overview of AI Agents and how they work.

## Learning Path
1.  **[LLM vs. Agent](./basics/learn-llm-vs-agent.md):** Understanding the "Chef vs. Kitchen" analogy.
2.  **[Hello Agent](./basics/guide-hello-agent.md):** Writing your first Python script to talk to an LLM API.
3.  **[Gemini API Reference](./basics/ref-gemini-api.md):** Rate limits and privacy info (2026).
4.  **[Guide: Weather Agent](./basics/guide-weather-agent.md):** The "Think-Act-Observe" loop. Connect your Weather functions to the LLM and build an autonomous agent.

## Prerequisites
*   **API Key:** You will need an API key from an LLM provider (Anthropic, OpenAI, or Gemini).
*   **Python:** Basic knowledge of Python functions.

## What Next?
In **Module 3 (Smart Agents)**, we will address the biggest limitations of the agent you just built:
1.  **Amnesia:** It forgets everything when you restart the script.
2.  **Danger:** It executes tools without asking.
We will learn to add **Memory** and **Safety Checks** to build a robust assistant.
