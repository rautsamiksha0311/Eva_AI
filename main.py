
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
import requests

app = FastAPI(title="EVA AI")

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
MODEL_NAME = "llama3.2:1b"
SYSTEM_PROMPT = (
    "You are EVA, a friendly, helpful AI assistant. "
    "Give clear, accurate answers. Explain technical concepts simply. "
    "If you are unsure, say so instead of inventing facts."
)

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=10000)
    history: list[ChatMessage] = Field(default_factory=list)

@app.get("/", response_class=HTMLResponse)
def home():
    try:
        with open("templates/index.html", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Chat interface file not found.")

@app.get("/health")
def health():
    try:
        response = requests.get("http://127.0.0.1:11434/api/tags", timeout=5)
        response.raise_for_status()
        return {"status": "ok", "model": MODEL_NAME}
    except requests.RequestException:
        raise HTTPException(status_code=503, detail="Ollama is not available.")

@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message.strip()

    if not user_message:
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for item in request.history[-20:]:
        if item.role in ("user", "assistant") and item.content.strip():
            messages.append({
                "role": item.role,
                "content": item.content[:10000]
            })

    messages.append({"role": "user", "content": user_message})

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "messages": messages,
                "stream": False
            },
            timeout=(5, 300)
        )
        response.raise_for_status()
        data = response.json()
        reply = data.get("message", {}).get("content", "").strip()

        if not reply:
            raise HTTPException(status_code=502, detail="The model returned an empty response.")

        return {"reply": reply}

    except requests.Timeout:
        raise HTTPException(
            status_code=504,
            detail="EVA took too long to respond. Try a shorter question."
        )
    except requests.RequestException:
        raise HTTPException(
            status_code=503,
            detail="Could not connect to Ollama. Make sure Ollama is running."
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
