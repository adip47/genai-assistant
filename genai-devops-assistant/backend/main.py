from fastapi import FastAPI
from slack_bot import slack_events
from llm_agent import process_llm_query

app = FastAPI()

@app.get("/")
def root():
    return {"message": "GenAI DevOps Assistant is running 🚀"}

@app.post("/slack/events")
async def slack_events_listener(payload: dict):
    return slack_events(payload)

@app.post("/ask")
def ask(query: str):
    return process_llm_query(query)
