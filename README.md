# A.R.T.E.M.I.S.
**A**I **R**esponse, **T**ask **E**xecution & **M**eeting **I**ntegration **S**ystem

---

A smart and customizable AI Secretary that handles your boring tasks like email replies, calendar scheduling(not implemmented yet), and even talking nice—or not so nice—to coworkers.

---

## 🧱 Architecture Overview

This repo is a **microservice-based AI secretary system**, currently made up of:

| Service      | Role                                                         |
|--------------|--------------------------------------------------------------|
| 📬 Mailer     | Interacts with Gmail – reads & sends messages                     |
| 🧠 AI Router  | Powered by Ollama LLM – decides what actions to take        |
| 🧩 Commander  | Master orchestrator – coordinates Mailer + AI + others      |

Each service runs independently with FastAPI. Commander calls the shots.

## 🚀 Getting Started

### 1. Clone the repo

```bash
cd artemis
```
### 2. Set up each microservice

Each service lives in its own folder: mailer, ai_router, commander.

  - ⚠️ You’ll need Python 3.10+ and Ollama installed.
  
  - Mailer: connects to Gmail (OAuth2 required)
  
  - AI Router: runs an LLM locally (default: dolphin-mixtral via Ollama)
  
  - Commander: glues everything together

See each subfolder’s README.md for setup instructions and API docs:

  - Mailer README

  - AI Router README

  - Commander README

## 🕹️ Run the System (Dev Mode for now)

In three separate terminals (or use something like tmux/pm2):

### Terminal 1 - Mailer
```bash
cd mailer
uvicorn app.main:app --reload --port 8001
```
### Terminal 2 - AI Router
```bash
cd ai_router
uvicorn app.main:app --reload --port 8002
```
### Terminal 3 - Commander
```bash
cd commander
uvicorn app.main:app --reload --port 8000
```

ARTEMIS will:

  - Check unread Gmail messages

  - Ask the AI model what to do

  - Send responses

🧠 Personality System

Customize ARTEMIS’ tone by adding system prompt files in ai_router/app/prompts/.

Change it via .env:

```env
ARTEMIS_SYSTEM_PROMPT=app/prompts/sarcastic.txt
```
🛠️ Roadmap

- Basic email reply loop

- Google Calendar integration 📅

- Task delegation to other systems (e.g. JIRA, Notion, Slack)

- Persistent task memory (DB or Redis)

- CI/CD deployment with Docker Compose or Kubernetes
