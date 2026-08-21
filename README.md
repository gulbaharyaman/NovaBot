# 🤖 NovaBot

**NovaBot** is a local Retrieval-Augmented Generation (RAG) based AI customer support assistant developed for a fictional cloud service environment called **NovaCloud**.

The project combines a local Large Language Model with a structured knowledge base to generate grounded responses based only on available documentation.

> 🚧 **Current Version: v0.1**
> NovaBot currently runs as a command-line application. Further improvements and interface development are planned.

---

## ✨ Features

* 🔎 Retrieval-Augmented Generation (RAG)
* 🧠 Local LLM inference with **Ollama**
* 🤖 **Gemma 3 1B** language model
* 📚 Knowledge-base driven responses
* 🗄️ Persistent vector storage with **ChromaDB**
* 🔍 Semantic document retrieval
* 🛡️ Public-document access filtering
* 📄 Top-3 relevant document retrieval
* 🚫 Controlled fallback when information is unavailable
* 💻 Command-line based interaction
* 🔒 Local-first architecture

---

## 🧠 How It Works

NovaBot processes a user question through a simple RAG pipeline:

```text
                    User Question
                         │
                         ▼
                  ┌─────────────┐
                  │   NovaBot   │
                  └──────┬──────┘
                         │
                         ▼
                Semantic Retrieval
                         │
                         ▼
                  ┌─────────────┐
                  │  ChromaDB   │
                  └──────┬──────┘
                         │
                         ▼
              NovaCloud Knowledge Base
                         │
                  Top 3 PUBLIC chunks
                         │
                         ▼
               Augmented Prompt
                         │
                         ▼
                  ┌─────────────┐
                  │ Gemma 3 1B  │
                  │   Ollama    │
                  └──────┬──────┘
                         │
                         ▼
                 Grounded Response
```

When a user submits a question, NovaBot:

1. Initializes the local ChromaDB vector store.
2. Indexes the knowledge-base documents if necessary.
3. Searches for the **three most relevant document chunks**.
4. Filters retrieval to documentation marked as **PUBLIC**.
5. Adds the retrieved information to the model context.
6. Sends the augmented prompt to **Gemma 3 1B through Ollama**.
7. Returns the generated answer to the user.

If the retrieved documentation does not contain enough information, NovaBot is instructed not to invent an answer.

---

## 🛡️ Grounded Response Strategy

NovaBot is designed to answer questions using only information retrieved from its knowledge base.

If sufficient documentation cannot be found, the assistant responds with:

> *"I cannot find this information in the available NovaCloud documentation."*

This approach helps reduce unsupported or hallucinated responses.

---

## 🛠️ Tech Stack

| Technology     | Purpose                      |
| -------------- | ---------------------------- |
| **Python**     | Core application development |
| **Ollama**     | Local LLM inference          |
| **Gemma 3 1B** | Language model               |
| **ChromaDB**   | Vector database              |
| **RAG**        | Grounded response generation |
| **Markdown**   | Knowledge-base documents     |

---

## 📂 Project Structure

```text
NovaBot/
│
├── knowledge_base/
│   ├── customer_support_policy.md
│   ├── dns_troubleshooting.md
│   ├── firewall_configuration.md
│   ├── internal_support_ops.md
│   ├── vm_troubleshooting.md
│   └── vpc_network_guide.md
│
├── target_bot/
│   ├── __init__.py
│   ├── document_loader.py
│   ├── prompts.py
│   ├── target_bot.py
│   └── vector_store.py
│
├── main.py
├── requirements.txt
└── .gitignore
```

---

## 📚 Knowledge Base

NovaBot uses a fictional cloud support knowledge base containing documentation related to topics such as:

* Firewall configuration
* DNS troubleshooting
* Virtual machine troubleshooting
* VPC networking
* Customer support policies
* Support operations

All NovaCloud information included in this project is created for **educational and demonstration purposes** and does not represent a real organization or production environment.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/gulbaharyaman/NovaBot.git
cd NovaBot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Install Ollama on your system and make sure the service is running.

### 5. Download the model

```bash
ollama pull gemma3:1b
```

---

## ▶️ Usage

Start NovaBot with:

```bash
python main.py
```

Example:

```text
NovaBot Support Chatbot (Type 'exit' to quit)

You: What should I check when troubleshooting DNS issues?

NovaBot: ...
```

Type:

```text
exit
```

to close the application.

---

## 🔐 Local Data

Generated local files such as the ChromaDB database, Python cache files, virtual environments, logs, and environment variables are excluded from version control through `.gitignore`.

---

## 🗺️ Roadmap

NovaBot is currently an early-stage CLI prototype.

Planned improvements include:

* [ ] Improved retrieval and response evaluation
* [ ] Source references in generated answers
* [ ] Enhanced prompt and access-control mechanisms
* [ ] Improved error handling
* [ ] Automated tests
* [ ] Web-based user interface
* [ ] Expanded cloud support knowledge base

---

## 🎯 Project Purpose

NovaBot was created as a hands-on exploration of:

* Retrieval-Augmented Generation
* Local LLM deployment
* Vector databases
* AI-powered customer support
* Grounded answer generation
* AI system quality and reliability

---

## 👩‍💻 Author

**Gülbahar Yaman**

Computer Engineering | Software Quality Assurance | Artificial Intelligence | Cloud Technologies
