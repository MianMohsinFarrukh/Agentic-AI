repo Link = https://github.com/panaversity/learn-agentic-ai
api Link = https://aistudio.google.com/

UV & Virtusl env :
1- uv init .       install uv pakge first .
2- uv venv         add virtual environment .
3- .venv\Scripts\activate   activate virtual env .
4- uv run explore-uv        uv.lock file create .

FOR AGENTS :
10- uv add openai-agents



CLASS CODE : 

# 🤖 25 July 2025: Diving into OpenAI Agents SDK

On this day, we explored how to **control AI agent behavior** and **manage memory** using two key concepts: **Guardrails** and **Context**.

---

## 🛤️ Guardrails: Keeping Your Agent on Track

**Guardrails** are safety measures that help define how your agent should behave. They allow you to validate or restrict both inputs and outputs to ensure responsible use.

- **Input Guardrails**: Validate user messages *before* they reach the agent (e.g., filtering inappropriate content).
- **Output Guardrails**: Review agent responses *before* they reach the user to ensure clarity, safety, and relevance.

---

## 🤔 Context: What Your Agent Knows

**Context** refers to the background knowledge available to the agent for carrying out tasks efficiently.

- **Local Context**: Short-term memory — relevant only to the current loop of conversation.
- **Agent/LLM Context**: Long-term memory — persists across multiple turns and includes:
  - 📌 **System Prompt** – foundational instructions for the agent.
  - 🧑‍💻 **User Prompts** – messages from the user during interaction.
  - 🧰 **Custom Tools** – functions and APIs the agent can call.
  - 🔎 **Retrieved Data** – from web searches or external sources.

---

## ⚠️ Important Model Limitation

> The `gemini-2.0-flash` model **cannot use Tool Calling and Structured Output simultaneously**.  
> 🔧 To implement both features, either:
> - Use **two separate agents**, or  
> - Switch to a model that supports **both capabilities**.

---

## 📚 Homework

Study the following concepts before our next session:

- 📘 [Context – OpenAI Agents SDK](https://openai.github.io/openai-agents-python/context/)
- 📘 [Dynamic Instructions](https://openai.github.io/openai-agents-python/agents/#dynamic-instructions)

---

## 📗 Class Resources

- 🔗 **GitHub Repository**: [Class 12 Code on GitHub](https://github.com/syeda-hoorain-ali/giaic-q3/tree/main/class-12)

---

@everyone – Let’s keep learning and building smarter agents! 🚀

