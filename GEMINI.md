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
*   **Standard Model:** `gemini-3-flash-preview` (Target model for 2026).
*   **Anthropic:** Use `anthropic` SDK.
*   **Documentation:** Guides must separate Claude and Gemini instructions into distinct "Path A" and "Path B" sections.

**MCP Standards:**
*   Library: `mcp` (FastMCP).
*   Style: Prefer synchronous code (`def`) and `requests` library for readability in beginner guides.
*   Avoid `async/await` complexity unless necessary for performance.

## 3. Directory Structure
The repository is organized by learning modules:
*   **`mcp/` (Module 1):** Documentation and guides for the Model Context Protocol.
    *   Contains: `guide-calculator-mcp.md`, `guide-weather-mcp.md`.
*   **`agent/` (Module 2 & 3):** Documentation for building Autonomous Agents.
    *   **`basics/` (Module 2):** `guide-hello-agent.md`, `guide-weather-agent.md`, `learn-llm-vs-agent.md`, `ref-gemini-api.md`.
    *   **`smart-agent/` (Module 3):** Guides for the Daily Briefing Agent.
*   **Root Files:**
    *   `GEMINI.md`: Context anchor for the AI assistant (Tech stack, progress, rules).
    *   `README.md`: The curriculum homepage for students.

## 4. Current Progress
*   **[COMPLETE] Module 1: MCP**
    *   Created `calculator-mcp` (Local logic).
    *   Created `weather-mcp` (Open-Meteo API, Tool Chaining).
*   **[COMPLETE] Module 2: Basic Agents**
    *   Setup `hello-claude` and `hello-gemini`.
    *   Created `guide-weather-agent.md` (weather-claude, weather-gemini).
*   **[IN PROGRESS] Module 3: Smart Agents (The Daily Briefing)**
    *   Focus: Advanced AI engineering pillars.
    *   Topics: Side Effects (Action tools), Guardrails (Autonomous safety), Persistence (File state), Reflection (Self-correction), Orchestration (Scheduling).
    *   Deployment: Local (NAS/Desktop) and Cloud (GitHub Actions).
*   **[PLANNED] Module 4: The Platform**
    *   Focus: Systems Engineering.
    *   Goal: Build a Universal MCP Client using `subprocess` and `stdio` pipes to connect to ANY server.

## 5. Useful Commands
*   Run script: `uv run filename.py`
*   Add dependencies: `uv add library_name`
*   Inspector: `uv run mcp-inspector script.py`