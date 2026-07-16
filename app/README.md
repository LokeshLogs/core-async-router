# Core Asynchronous Communication Router

A production-grade, event-driven backend gateway built to ingest high-throughput webhooks (e.g., WhatsApp, Stripe) asynchronously. It handles instant traffic acceptance and offloads heavy computation workloads cleanly onto a background worker pool using an isolated database broker.

## 🛠️ The Architecture Stack
* **API Layer:** FastAPI (Asynchronous ASGI Web Server)
* **Data Validation:** Pydantic (Strict compile-time schema protection)
* **Message Broker:** Redis (Running inside a Docker infrastructure container)
* **Task Queue:** Celery (Distributed background processing engine)

## ⚡ Key Architectural Wins
* **Non-Blocking Gateway:** Returns a strict HTTP `202 Accepted` status code within milliseconds, disconnecting the client instantly while processing continues seamlessly.
* **Decoupled Workloads:** Isolates heavy compute operations (like AI generation or database updates) away from the primary API server thread to ensure zero downtime.
* **Windows-Optimized Threading:** Configured with specific concurrency thread execution pools to eliminate process-forking issues on Windows environments.

## 🚀 Quick Start Guide

### 1. Provision Infrastructure
Ensure Docker Desktop is running, then spin up the isolated Redis instance:
```bash
docker-compose up -d