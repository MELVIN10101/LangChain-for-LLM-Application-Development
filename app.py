from fastapi import FastAPI
from pydantic import BaseModel
from chains.sentiment import sentiment
from chains.summarizer import summarize
from chatbot import chat
from agents.executor import run_agent

app = FastAPI()

class TextInput(BaseModel):
    user_id: str
    text: str

@app.post("/summarize")
def summarize_route(input: TextInput):
    return {"summary": summarize(input.text)}

@app.post("/sentiment")
def sentiment_route(input: TextInput):
    return {"sentiment": sentiment(input.text)}

@app.post("/chat")
def chat_route(input: TextInput):
    return {"reply": chat(input.user_id, input.text)}

@app.post("/agent")
def agent_route(input: TextInput):
    print("inside agent_route function in app.py")
    return {"result": run_agent(input.user_id, input.text)}

@app.post("/run-all")
def run_all(input: TextInput):
    print("inside run_all function in app.py")
    return {
        "summary": summarize(input.text),
        "sentiment": analyze_sentiment(input.text),
        "chat_reply": chat(input.user_id, input.text),
    }
