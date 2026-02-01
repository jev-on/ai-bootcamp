# ai-bootcamp

Welcome to the AI Bootcamp! This repository is a dedicated space for learning the basics of Artificial Intelligence. 

Here, we explore core concepts, build hands-on projects, and document our journey from AI beginners to advanced practitioners.

## Curriculum Modules

### 1. Model Context Protocol (MCP)
The [Model Context Protocol](./mcp/) is an open standard that enables AI assistants to connect to external data and tools.

*   **[Overview](./mcp/README.md)**: High-level concepts and architecture.
*   **[Guide: Calculator MCP](./mcp/guide-calculator-mcp.md)**: Build a simple, local MCP server (No internet required).
*   **[Guide: Weather MCP](./mcp/guide-weather-mcp.md)**: Build an internet-connected MCP server that uses APIs and tool-chaining.

### 2. Building AI Agents
Move beyond static tools. Build Python programs that can "think" and act autonomously.

*   **[Overview](./agent/README.md)**: What is an Agent?
*   **[LLM vs Agent](./agent/basics/learn-llm-vs-agent.md)**: Understanding the "Chef vs. Kitchen" analogy.
*   **[Guide: Hello Agent](./agent/basics/guide-hello-agent.md)**: Your first programmatic call to an LLM API.
*   **[Reference: Gemini API](./agent/basics/ref-gemini-api.md)**: Rate limits and model info.
*   **[Guide: Weather Agent](./agent/basics/guide-weather-agent.md)**: Build an autonomous agent loop that checks the weather.

### 3. Smart Agents (The Daily Briefing)
Learn the four pillars of advanced AI engineering: Side Effects, Persistence, Guardrails, and Orchestration.

*   **[Overview](./agent/smart-agent/README.md)**: Proactive Automation and Safety.
*   **[Guide: Notification MCPs](./agent/smart-agent/guide-notification-tools.md)**: Side Effects - Building tools that can "Write" to the outside world.
*   **[Guide: The Briefing Agent](./agent/smart-agent/guide-briefing-agent.md)**: Persistence & Guardrails - Memory and Safety without a human.
*   **[Guide: Scheduling](./agent/smart-agent/guide-scheduling.md)**: Orchestration - Setting your agent on autopilot.

---

### Future Modules
*   **Module 4: The Platform**: Building a Universal MCP Client to connect to *any* tool ecosystem.
