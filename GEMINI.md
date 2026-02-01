# Project Context: AI Bootcamp

## 1. Overview
This repository is a structured learning environment for Artificial Intelligence concepts.
*   **Goal:** Progress from basic Tools (MCP) to Autonomous Agents.
*   **OS:** macOS.

## 2. Tech Stack & Standards
**Package Management:**
*   Strictly use `uv` for all Python management (`uv init`, `uv add`, `uv run`).
*   Always include `.env` in `.gitignore`.

**LLM Standards:**
*   **Google:** Use `google-genai` (V1 SDK). Do NOT use `google-generativeai`.
*   **Standard Model:** `gemini-3-flash` (Target model for 2026).
*   **Anthropic:** Use `anthropic` SDK.
*   **Documentation:** Guides must separate Claude and Gemini instructions into distinct "Path A" and "Path B" sections.

**MCP Standards:**
*   Library: `mcp` (FastMCP).
*   Style: Prefer synchronous code (`def`) and `requests` library for readability in beginner guides.
*   Avoid `async/await` complexity unless necessary for performance.

## 3. Current Progress
*   **[COMPLETE] Module 1: MCP**
    *   Created `calculator-mcp` (Local logic).
    *   Created `weather-mcp` (Open-Meteo API, Tool Chaining).
*   **[IN PROGRESS] Module 2: Agents**
    *   Setup `agent-claude` and `agent-gemini`.
    *   Established connection to LLM APIs via Python.
    *   Next Step: Binding MCP tools to the Agent script.

## 4. Useful Commands
*   Run script: `uv run filename.py`
*   Add dependencies: `uv add library_name`
*   Inspector: `uv run mcp-inspector script.py`
