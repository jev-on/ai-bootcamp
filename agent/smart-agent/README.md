# Module 3: Smart Agents (The Daily Briefing) 📅☕

Welcome to the most practical module yet. In this section, we move from **Reactive Agents** (they wait for you) to **Proactive Agents** (they work for you while you sleep).

## The Goal
Build a "Daily Briefing Agent" that:
1.  **Starts automatically** every morning.
2.  **Fetches the weather** using your Weather MCP logic.
3.  **Summarizes the information** into a friendly briefing.
4.  **Notifies you** via Email and/or Discord.

## What you will learn
*   **Action Tools:** Building MCPs that *write* or *send* (not just read).
*   **Integration:** How to give one Agent access to multiple toolsets.
*   **Persistance:** Using simple files to save state.
*   **Scheduling:** Setting up "Autopilot" using local `cron` and **GitHub Actions**.

## Learning Path
1.  **[Email & Discord MCPs](./guide-notification-tools.md):** Build the "hands" that can send messages.
2.  **[The Briefing Agent](./guide-briefing-agent.md):** Build the "brain" that coordinates everything.
3.  **[Scheduling](./guide-scheduling.md):** Deploy your agent to run on a schedule (Local vs Cloud).

## Security Note 🔐
We will be using **GitHub Secrets** and **Environment Variables** to ensure your API keys and Email passwords are never exposed.
