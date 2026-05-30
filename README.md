# 🤖 AI Tutor Web App

A conversational AI tutor built with FastAPI and Meta's Llama 3.3 LLM via HuggingFace.

## What it does
- Answers questions about AI and Machine Learning
- Remembers conversation history
- Explains concepts in simple beginner friendly language
- Gives real world examples with every answer

## Tech Stack
- **Backend:** Python, FastAPI
- **AI Model:** Meta Llama 3.3 70B via HuggingFace
- **Frontend:** HTML, CSS, JavaScript
- **Prompt Engineering:** Custom system prompt

## How to run
1. Clone this repo
2. Install dependencies: `pip install fastapi uvicorn huggingface_hub`
3. Add your HuggingFace token in `main.py`
4. Run: `uvicorn main:app --reload`
5. Open: `http://127.0.0.1:8000`

## Built by
Preethi Reddy — MS Data Science @ Bryant University
