# 🤖 18 July 2025 – Diving into OpenAI Agents SDK

A quick summary of today’s session on building smart and efficient AI agents!

---

## 💰 What are Tokens & How Do They Affect Price?

**Tokens** are chunks of words used in prompts and responses.  
You are billed based on the number of tokens used.

- 🔢 Try the **Token Counter Tool**: [OpenAI Tokenizer](https://platform.openai.com/tokenizer)

---

## 🧠 Giving Your AI a Context with RAG

**RAG (Retrieval-Augmented Generation)** helps give your agent a long-term memory by letting it **search your own documents** for answers.

### 🔍 Key Concepts:

- **Embeddings**: Converts your text into number vectors. Similar meanings get similar numbers.
- **Vector Databases**: Specialized databases (like **OpenAI’s vector store** or **Pinecone**) that store these vectors and retrieve relevant info instantly.

👉 To create your own vector store in OpenAI:

1. Go to **Dashboard → Storage → Vector Stores**  
2. Create a new database  
3. Upload your files  
4. Attach and copy the vector store **ID**  
5. Use it with `FileSearchTool`

---

## 🕵️‍♀️ Tracing & Handoffs

- **Tracing**: Watch step-by-step logic of how your agent thinks.  
  🔗 [View Traces](https://platform.openai.com/logs?api=traces)

- **Handoffs 🤝**: Agent-to-agent collaboration!  
  One agent can transfer a task to a more specialized agent for better results.

---

## 🚀 Your Task for the Week

> 💡 **Brainstorm an exciting product idea** using AI agents.  
> Start planning its workflow, features, and how agents can power it.

---

## 📘 Class Resources

- 📓 **Google Colab Notebook**: [Open Colab](https://colab.research.google.com/drive/1BE7dpOcGdLVqW5QIJaSrUrZfxSygMYFk)
- 🗂️ **GitHub Repository**: [Class 11 Code](https://github.com/syeda-hoorain-ali/giaic-q3/tree/main/class-11)

---

@everyone – Let’s create something amazing with AI agents! 🚀
