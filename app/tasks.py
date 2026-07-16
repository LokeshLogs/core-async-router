import time
from celery import Celery
from app.config import settings

# Initialize Celery and connect it using our secure .env configuration
celery_app = Celery(
    "worker",
    broker=settings.REDIS_BROKER_URL,
    backend=settings.REDIS_BACKEND_URL
)

# Define the background task function (This was missing!)
@celery_app.task(name="process_webhook_payload")
def process_webhook_payload(payload: dict):
    # Defensive check: Fallback to 'unknown' if event_id is missing
    event_id = payload.get('event_id', 'unknown') if payload else 'unknown'
    
    print(f"--- [Worker Start] Heavy processing initiated for event {event_id} ---")
    
    # Simulate a heavy background operation
    time.sleep(5) 
    
    print(f"--- [Worker Finished] Successfully completed heavy processing for event {event_id} ---")
    return {"status": "success", "event_id": event_id}