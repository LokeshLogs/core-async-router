# Core Async I/O Communication Router

An uncrashable, high-throughput, asynchronous backend engine designed to handle thousands of concurrent customer webhook requests (such as real-time multi-modal streams from the WhatsApp Business API or Twilio SMS) without dropping a single packet.

## 🛠️ The Tech Stack
* **FastAPI**: Modern, high-performance web framework utilizing asynchronous `async/await` patterns.
* **Celery**: Distributed task queue used to isolate and run CPU-heavy or high-latency processing tasks.
* **Redis**: In-memory message broker acting as the high-speed communication bridge between the API gateway and background workers.
* **Docker & Docker Compose**: Containerization of the entire ecosystem to ensure seamless deployment and environment replication.

---

## 📐 System Architecture

1. **Client / Webhook Source** (e.g., Twilio, WhatsApp) fires a payload to `/webhook`.
2. **FastAPI Gateway** validates the incoming data schema instantly using Pydantic.
3. **API offloads the payload** to the **Redis Broker** via Celery `delay()`.
4. **FastAPI instantly returns `202 Accepted`** back to the client in milliseconds.
5. **Celery Background Worker** pulls the job from Redis and performs the heavy execution isolated from the main web server.

---

## ⚡ Quick Start

### Prerequisites
Make sure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

### Spin Up the Stack
Run the following command in your root directory to build and launch the API gateway, Redis broker, and Celery worker simultaneously:

```bash
docker-compose up --build