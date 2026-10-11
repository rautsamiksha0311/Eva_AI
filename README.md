# ✨ EVA AI — Your Personal AI Assistant

\<p align="center">
&#x20; \<img src="[https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white](https://img.shields.io/badge/Python-3.10-blue?logo=python\&logoColor=white)" alt="Python">
&#x20; \<img src="[https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi\&logoColor=white)" alt="FastAPI">
&#x20; \<img src="[https://img.shields.io/badge/Ollama-Local%20AI-black?logo=ollama&logoColor=white](https://img.shields.io/badge/Ollama-Local%20AI-black?logo=ollama\&logoColor=white)" alt="Ollama">
&#x20; \<img src="[https://img.shields.io/badge/Model-Llama%203.2-purple](https://img.shields.io/badge/Model-Llama%203.2-purple)" alt="Llama 3.2">
\</p>

\<p align="center">
&#x20; A locally running AI chatbot built with Python, FastAPI, and Ollama.
&#x20; \<br>
&#x20; Chat with EVA, manage conversations, and keep your chat history in your browser.
\</p>

---

## 🌟 About the Project

**EVA AI** is a personal AI chatbot that uses the Llama 3.2 language model through Ollama. It provides a simple, modern chat interface and runs locally on your computer.

This project was created to explore AI integration, backend development, and building a complete web application with Python.

## 🚀 Features

- 💬 **AI Conversations** — Ask questions and receive AI-generated responses.
- 🗂️ **Chat Management** — Create, rename, and delete conversations.
- 💾 **Local Chat History** — Save conversations in your browser.
- 🌙 **Dark Mode** — Use a dark-themed interface.
- 📋 **Copy Responses** — Copy answers with one click.
- ⚡ **FastAPI Backend** — Connect the web interface to the AI model.
- 🔒 **Local Model** — Run inference locally through Ollama without paying per API request.

## 🛠️ Tech Stack

| Technology            | Purpose                       |
| --------------------- | ----------------------------- |
| Python                | Backend programming           |
| FastAPI               | API and web server            |
| Ollama                | Runs the local language model |
| Llama 3.2 (1B)        | Generates AI responses        |
| HTML, CSS, JavaScript | Chat interface                |

## 📸 Application Preview

*Add a screenshot of your EVA AI chatbot here.*

\<!-- To add a screenshot, upload it to your repository and replace the line above with:
![EVA AI Screenshot]\(screenshots/eva-ai.png)
\-->

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/rautsamiksha0311/Eva_AI.git
cd Eva_AI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Ollama

Download Ollama from [ollama.com](https://ollama.com/).

Pull the model:

```bash
ollama pull llama3.2:1b
```

### 6. Run EVA AI

Start the FastAPI server:

```bash
python -m uvicorn main:app --reload
```

Open your browser and visit:

**[http://127.0.0.1:8000](http://127.0.0.1:8000)**

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
- Do not upload API keys, passwords, `.env` files, or your virtual environment to GitHub.

## 🎯 Future Improvements

- Streaming AI responses
- Voice input and output
- Better conversation memory
- Optional document-based question answering (RAG)
- Improved error handling

## 👩‍💻 Author

**Samiksha Raut**

MSc IT Student | Aspiring AI Engineer

---

\<p align="center">
&#x20; ⭐ If you find this project interesting, consider giving it a star!
\</p>
