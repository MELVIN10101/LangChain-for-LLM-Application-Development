from fastapi import FastAPI
from pydantic import BaseModel
from chains.summarizer import summarize
from chains.sentiment import analyze_sentiment
from chains.qa import answer_question
from chains.chatbot import chat

app = FastAPI()

class TextInput(BaseModel):
    text: str

class ChatInput(BaseModel):
    user_id: str
    text: str
class QAInput(BaseModel):
    context: str
    question: str

@app.post("/summarize/")
def summarize_text(input: TextInput):
    return {"summary": summarize(input.text)}

@app.post("/sentiment/")
def sentiment_analysis(input: TextInput):
    return {"sentiment": analyze_sentiment(input.text)}

@app.post("/qa/")
def qa(input: QAInput):
    return {"answer": answer_question(input.context, input.question)}

@app.post("/chat/")
def chat(input: ChatInput):
    return {"reply": chat(input.user_id, input.text)}

@app.post("/run-all/")
def run_all(input: TextInput):
    return {
        "summary": summarize(input.text),
        "sentiment": analyze_sentiment(input.text),
        "reply": chat("default_user",input.text)
    }
