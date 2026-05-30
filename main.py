from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from huggingface_hub import InferenceClient

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = InferenceClient(
    provider="novita",
    api_key="YOUR_TOKEN_HERE",
)

# Store conversation history
messages = [
    {
        "role": "system",
        "content": """You are a friendly AI and ML tutor for beginners.
        Follow these rules strictly:
        1. Always explain in simple language like the student is a beginner
        2. Keep every answer under 5 sentences
        3. Always give one real world example
        4. If asked something not related to AI or ML, politely say you only teach AI and ML
        5. Encourage the student after every answer"""
    }
]

class Message(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html") as f:
        return f.read()

@app.post("/chat")
def chat(message: Message):
    messages.append({
        "role": "user",
        "content": message.text
    })
    
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct",
        messages=messages,
    )
    
    ai_response = response.choices[0].message.content
    
    messages.append({
        "role": "assistant",
        "content": ai_response
    })
    
    return {"response": ai_response}