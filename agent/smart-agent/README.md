# Module 3: Smart Agents (The Daily Briefing) 📅☕

Welcome to the most practical module yet. In this section, we move from **Reactive Agents** (they wait for you) to **Proactive Agents** (they work for you while you sleep).

## The Goal
Build a "Daily Briefing Agent" that:
1.  **Starts automatically** every morning.
2.  **Fetches the weather** using your Weather MCP logic.
3.  **Summarizes the information** into a friendly briefing.
4.  **Notifies you** via Email and/or Discord.

## What you will learn
Building a scheduled agent teaches you the four pillars of advanced AI engineering:

1.  **Side Effects (Action Tools):** Building MCPs that *write* or *send* (not just read). 
2.  **Guardrails (Safety):** Implementing autonomous validation to ensure your agent doesn't spam or send empty data (Safety without a human-in-the-loop).
3.  **Persistence (Memory):** Using simple files to save state so your agent "remembers" what it sent yesterday.
4.  **Orchestration (Scheduling):** Moving from a script you run manually to a service that runs on autopilot (Local vs Cloud).

## Learning Path
1.  **[Email & Discord MCPs](./guide-notification-tools.md):** The "Hands." Learn to manage **Side Effects**.
2.  **[The Briefing Agent](./guide-briefing-agent.md):** The "Brain & Conscience." Combine multiple tools and implement **Guardrails** and **Persistence**.
3.  **[Scheduling](./guide-scheduling.md):** The "Clock." Set your agent on autopilot using **Orchestration**.

## Security Note 🔐
We will be using **GitHub Secrets** and **Environment Variables** to ensure your API keys and Email passwords are never exposed.
