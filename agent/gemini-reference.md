# Gemini API Free Tier Reference (2026)

This reference provides the current rate limits and policies for the Gemini API free tier (via Google AI Studio).

## 1. Model Rate Limits (Google AI Studio)

Rate limits are enforced at the **Project Level**, meaning multiple API keys in the same project share these quotas.

| Model ID | RPM | TPM | RPD | Context Window |
| :--- | :--- | :--- | :--- | :--- |
| **gemini-2.5-flash-lite** | 15 | 250,000 | 1,000 | 1,000,000 |
| **gemini-2.5-flash** | 10 | 250,000 | 250 | 1,000,000 |
| **gemini-2.5-pro** | 5 | 250,000 | 100 | 1,000,000 |
| **gemini-3-flash-preview** | 15 | 250,000 | 250 | 1,000,000+ |
| **gemini-3-pro-preview** | 10 | 250,000 | 100 | 1,000,000+ |

### Key Definitions:
*   **RPM:** Requests Per Minute (How fast you can call).
*   **TPM:** Tokens Per Minute (Combined input and output size).
*   **RPD:** Requests Per Day (Total volume per 24 hours).
*   **Reset Time:** Daily limits reset at **Midnight Pacific Time (PT)**.

---

## 2. Feature-Specific Quotas

If your automation uses advanced features, additional shared limits apply:
*   **Grounding with Google Search:** 500 RPD (Shared across all Flash models).
*   **Grounding with Google Maps:** 500 RPD.
*   **Image Generation (Nano Banana):** ~100 images per day (Subject to high-demand fluctuations).
*   **Code Execution:** Supported on all 2.5 and 3.0 models for free.

---

## 3. Data Privacy Policy

> [!WARNING]
> **Free Tier Privacy Notice:** When using the Free Tier (Unpaid Services), Google uses your input prompts and model outputs to improve its products. This may include review by human annotators.

**To ensure privacy:** You must enable Billing (Pay-as-you-go). Once billing is active, your data is no longer used for model training, even if you stay within the free usage limits.

---

## 4. Implementation Tips

*   **Error Handling:** Watch for **HTTP 429 (Resource Exhausted)**. Implement an exponential backoff strategy in your script.
*   **Lite for Logic:** Use `flash-lite` for the "Orchestrator" glue code to maximize your daily 1,000 request quota.
*   **Tier 1 Upgrade:** Simply linking a credit card (without spending) usually upgrades you to **Tier 1**, which significantly increases RPM and TPM limits while providing data privacy.

---

## 5. Official Documentation

*   **[Gemini API Python Quickstart](https://ai.google.dev/gemini-api/docs/quickstart)** - The official guide for the SDK we are using in this module.
