import os
from fastapi.responses import JSONResponse

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")

def slack_events(payload: dict):
    if "challenge" in payload:
        return JSONResponse(content={"challenge": payload["challenge"]})
    
    event = payload.get("event", {})
    if event.get("type") == "app_mention":
        text = event.get("text")
        user = event.get("user")
        print(f"Received from {user}: {text}")
        # You can hook this into LangChain or custom agent
        return JSONResponse(content={"ok": True})

    return JSONResponse(content={"ok": True})
