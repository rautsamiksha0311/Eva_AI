# ✨ EVA AI — Your Personal AI Assistant

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white) ![Ollama](https://img.shields.io/badge/Ollama-Local%20AI-black?logo=ollama&logoColor=white) ![Llama 3.2](https://img.shields.io/badge/Model-Llama%203.2-purple)

A locally running AI chatbot built with Python, FastAPI, and Ollama.

Chat with EVA, manage conversations, and keep your chat history in your browser.

---

## 🌟 About the Project

**EVA AI** is a personal AI chatbot powered by the Llama 3.2 language model through Ollama. It provides a modern chat interface and runs locally on your computer.

This project explores AI integration, backend development, and building a complete web application using Python.

## 🚀 Features

- 💬 **AI Conversations** — Ask questions and receive AI-generated responses.
- 🗂️ **Chat Management** — Create, rename, and delete conversations.
- 💾 **Local Chat History** — Save conversations in your browser.
- 🌙 **Dark Mode** — Use a dark-themed interface.
- 📋 **Copy Responses** — Copy AI responses with one click.
- ⚡ **FastAPI Backend** — Connect the web interface to the AI model.
- 🤖 **Local AI Model** — Generate responses through Ollama without paying per API request.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | Web server and API |
| Ollama | Runs the local language model |
| Llama 3.2 (1B) | Generates AI responses |
| HTML | Webpage structure |
| CSS | Interface styling |
| JavaScript | Chat functionality |

## 📸 Application Preview

_Add a screenshot of EVA AI here._

To add a screenshot, upload it to your repository and use:

```markdown
![EVA AI Screenshot](screenshots/eva-ai.png)
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/rautsamiksha0311/Eva_AI.git
cd Eva_AI
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Ollama and Download the Model

Download and install [Ollama](https://ollama.com/).

Open your terminal and run:

```bash
ollama pull llama3.2:1b
```

### 6. Run EVA AI

Start the FastAPI server:

```bash
python -m uvicorn main:app --reload
```

Open your browser and visit:

**http://127.0.0.1:8000**

Make sure Ollama is running on your computer.

## 📁 Project Structure

```text
Eva_AI/
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
└── templates/
    └── index.html
```

## 🔐 Privacy and Security

- The AI model runs locally through Ollama.
- Chat history is stored in your browser's local storage.
- Never upload API keys, passwords, or your `.env` file to GitHub.
- Keep your virtual environment (`venv/`) out of the repository.

## 🎯 Future Improvements

- ⚡ Streaming AI responses
- 🎙️ Voice input and output
- 🧠 Improved conversation memory
- 📚 Document-based question answering (RAG)
- 🛠️ Improved error handling

## 📜 License

This project is available for educational and portfolio purposes.

## 📞 Contact

For questions or suggestions, reach out at **rautsamiksha0811@gmail.com**
