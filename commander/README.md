# 🐳 ARTEMIS Commander - Docker Setup

This guide explains how to build and run the Commander microservice as a Docker container.

## 📋 Prerequisites
Docker installed on your system
Access to the Mailer and AI Router services (or their URLs)
## 🏗️ Building the Image

From the commander directory, build the Docker image:
```bash
docker build -t artemis-commander .
```
## 🚀 Running the Container
Basic Run
```bash
docker run -p 8000:8000 \
  -e MAILER_API_URL=http://mailer:8001 \
  -e AI_ROUTER_API_URL=http://ai-router:8002 \
  -e POLLING_INTERVAL=30 \
  -e TARGET_SENDER=your@email.com \
  artemis-commander
```

Run with Custom Configuration
```bash
docker run -p 8000:8000 \
  -e MAILER_API_URL=http://192.168.1.100:8001 \
  -e AI_ROUTER_API_URL=http://192.168.1.100:8002 \
  -e POLLING_INTERVAL=60 \
  -e TARGET_SENDER=boss@company.com \
  --name commander \
  -d \
  artemis-commander
```

Run in Detached Mode
```bash
docker run -d \
  -p 8000:8000 \
  -e MAILER_API_URL=http://mailer:8001 \
  -e AI_ROUTER_API_URL=http://ai-router:8002 \
  -e TARGET_SENDER=your@email.com \
  --name artemis-commander \
  --restart unless-stopped \
  artemis-commander
```

## 🔧 Environment Variables

| Variable | Description | Default | Required |
|---|---|---|---|
| MAILER_API_URL | URL of the Mailer service | http://mailer:8001 | Yes |
| AI_ROUTER_API_URL | URL of the AI Router service | http://ai-router:8002 | Yes |
| POLLING_INTERVAL | Seconds between email checks | 30 | No |
| TARGET_SENDER | Email address to filter/process	None | None | Yes |
## 📊 Viewing Logs
### Follow logs in real-time
```bash
docker logs -f artemis-commander
```

### View last 100 lines
```bash
docker logs --tail 100 artemis-commander
```

## 🛑 Stopping the Container
```bash
docker stop artemis-commander
docker rm artemis-commander
```

## 🔍 Troubleshooting
### Container crashes immediately
- Check that TARGET_SENDER is set
- Verify environment variables are correct
### "Cannot connect to Mailer/AI Router service"
- Ensure the service URLs are reachable from the container
- If running locally, use host IP instead of localhost
- For Docker networks, use service names (e.g., http://mailer:8001)
### Check container health
```bash
docker ps -a
docker inspect artemis-commander
```
## 🌐 API Endpoints

The Commander service runs on port 8000 and exposes:

- Health Check: GET http://localhost:8000/docs (FastAPI auto-docs)

The polling happens automatically in the background on startup.

## 🔗 Running with Other Services

When running all ARTEMIS services together, consider using Docker Compose for easier networking and orchestration. Service names will automatically resolve within the Docker network.
