from fastapi import FastAPI, status
from pydantic import BaseModel
from app.tasks import process_webhook_payload

# This is the exact line Uvicorn is looking for!
app = FastAPI(title="Core Async Communication Router")

class WebhookPayload(BaseModel):
    event_id: str
    source: str       
    data: dict

@app.post("/webhook", status_code=status.HTTP_202_ACCEPTED)
async def receive_webhook(payload: WebhookPayload):
    print(f"--> Gateway received event {payload.event_id}. Offloading instantly...")
    
    # Push work payload to Redis (.model_dump() replaces .dict() in Pydantic v2)
    process_webhook_payload.delay(payload.model_dump())
    
    return {
        "status": "accepted",
        "message": "Payload handed off to background worker smoothly."
    }