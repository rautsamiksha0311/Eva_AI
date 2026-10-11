# ✨ EVA AI — Your Personal AI Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Ollama-Local%20AI-black?logo=ollama&logoColor=white" alt="Ollama">
  <img src="https://img.shields.io/badge/Model-Llama%203.2-purple" alt="Llama 3.2">
</p>

<p align="center">
  <b>A locally running AI chatbot built with Python, FastAPI, and Ollama.</b>
  <br>
  Chat with EVA, manage conversations, and keep your chat history in your browser.
</p>

---

## 🌟 About the Project

**EVA AI** is a personal AI chatbot powered by the Llama 3.2 language model through Ollama. It provides a modern chat interface and runs locally on your computer.

## 🚀 Features

- 💬 AI-powered conversations
- 🗂️ Create, rename, and delete chats
- 💾 Save chat history in your browser
- 🌙 Dark mode interface
- 📋 Copy AI responses
- ⚡ FastAPI backend
- 🤖 Local AI model using Ollama

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | Web server and API |
| Ollama | Local model runtime |
| Llama 3.2 (1B) | AI response generation |
| HTML, CSS, JavaScript | User interface |

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/rautsamiksha0311/Eva_AI.git
cd Eva_AI
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and download the AI model

Install [Ollama](https://ollama.com/), then run:

```bash
ollama pull llama3.2:1b
```

### 5. Start EVA AI

```bash
python -m uvicorn main:app --reload
```

Open **http://127.0.0.1:8000** in your browser.

## 📁 Project Structure

```text
Eva_AI/
├── main.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

## 🔐 Privacy

- The model runs locally through Ollama.
- Chat history is stored in browser local storage.
- Never commit API keys, passwords, or your `.env` file.

## 🎯 Future Improvements

- Streaming responses
- Voice input and output
- Document-based question answering (RAG)
- Improved conversation memory

---

## 📜 License

This project is available for educational and portfolio purposes.

## 📞 Contact

For questions or suggestions, reach out at **rautsamiksha0811@gmail.com** 
