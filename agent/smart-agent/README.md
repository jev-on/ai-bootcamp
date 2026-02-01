# Module 3: Smart Agents (The Daily Briefing) 📅☕

Welcome to the most practical module yet. In this section, we move from **Reactive Agents** (they wait for you) to **Proactive Agents** (they work for you while you sleep).

## The Goal
Build a "Daily Briefing Agent" that:
1.  **Starts automatically** every morning.
2.  **Fetches the weather** using your Weather MCP logic.
3.  **Summarizes the information** into a friendly briefing.
4.  **Notifies you** via Email and/or Discord.

## What you will learn
In this module, we move from "Toys" to "Production Systems" by mastering the **5 Pillars of Agentic Design**:

1.  **Side Effects (Action Tools) ⚡**
    *   **Concept:** Learning how to manage tools that *change* the world (Send Email, Delete File, Buy Stock) rather than just *reading* data (Calculator, Weather).
    *   **Why it matters:** Real agents are useless if they can't take action.

2.  **Autonomous Guardrails (Safety) 🛡️**
    *   **Concept:** Writing deterministic code (Python logic) that checks the AI's "Tool Requests" before they execute.
    *   **Why it matters:** Since this runs on a schedule (Cron), there is no human to stop the bot if it decides to send 1,000 emails by mistake.

3.  **State Persistence (Memory) 💾**
    *   **Concept:** Saving the agent's work to a file (JSON) so it "remembers" context between separate runs.
    *   **Why it matters:** Most LLMs are "stateless" (they forget everything after the script ends). Persistence gives them a "long-term memory."

4.  **Reflection (Self-Correction) 🧐**
    *   **Concept:** The "Editor Pattern." Forcing the AI to critique its own draft and fix errors before the final output.
    *   **Why it matters:** It dramatically increases the quality and reliability of the agent's response.

5.  **Orchestration (Scheduling) ⏰**
    *   **Concept:** Moving from "User-Triggered" code to "System-Triggered" services using Cron and GitHub Actions.
    *   **Why it matters:** This is how you turn a script into a reliable automated employee.

## Learning Path
1.  **[Email & Discord MCPs](./guide-notification-tools.md):** The "Hands." Learn to manage **Side Effects**.
2.  **[The Briefing Agent](./guide-briefing-agent.md):** The "Brain & Conscience." Combine multiple tools and implement **Guardrails** and **Persistence**.
3.  **[Self-Correction](./guide-reflection.md):** The "Editor." Implement **Reflection** to improve output quality.
4.  **[Scheduling](./guide-scheduling.md):** The "Clock." Set your agent on autopilot using **Orchestration**.

## Security Note 🔐
We will be using **GitHub Secrets** and **Environment Variables** to ensure your API keys and Email passwords are never exposed.
