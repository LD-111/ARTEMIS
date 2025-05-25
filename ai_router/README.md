# 🤖 ARTEMIS AI Router Microservice

This is the brainstem of ARTEMIS — the router that decides what to do with incoming emails. It takes parsed emails and sends them to an AI model (like Mixtral via Ollama), and gets back structured action plans. Basically... this is where ARTEMIS thinks 💡🧠

## 🧠 Features

- 💬 Accepts structured emails from the Mailer service

- 🧠 Sends them to a local AI model (via Ollama)

- 📤 Receives AI-generated actions (like sending replies)

- 🧱 Returns standardized JSON responses, ready for the Commander

## 📦 Microservice Stack

- FastAPI – web framework

- Ollama – local LLM backend (default: dolphin-mixtral:latest)

- .env Configurable – easy model/personality swapping

- Prompt Modularization – prompt is stored as a file, editable for different vibes or use cases

## 🛠️ Setup Instructions

### 1. Clone the Repo (if not already)

```bash
cd artemis/ai_router
```

### 2. Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Environment Config (.env)

Create a .env file like this:

```bash
OLLAMA_MODEL=dolphin-mixtral:latest
ARTEMIS_SYSTEM_PROMPT=app/prompts/default.txt
```

- OLLAMA_MODEL: change this to try other LLMs (like llama3, phi3, etc)

- ARTEMIS_SYSTEM_PROMPT: point to different personality templates!

## 🧠 Prompt System

Prompts are kept in app/prompts/:

- default.txt: baseline ARTEMIS secretary behavior

- You can add more styles (e.g. sarcastic, executive, HR-nerd) and just swap the .env

## 🚀 Running the Microservice

```bash
uvicorn app.main:app --reload
```

Runs at http://localhost:8000/ by default.

## 📬 API Endpoint

### POST /ai/process

Processes an email and gets back what the AI thinks ARTEMIS should do.

🔢 Input Body (JSON)
```json
{
  "content": {
    "sender": "jane.doe@example.com",
    "subject": "Quick question about the project",
    "payload": "Hey ARTEMIS, can you please tell me when the next team meeting is scheduled?"
  }
}
```

✅ Output (JSON)
```json
{
  "status": "success",
  "ai_response": {
    "action": "send_email",
    "content": {
      "receiver": "jane.doe@example.com",
      "subject": "Re: Quick question about the project",
      "body": "Hi Jane,\n\nThe next team meeting is scheduled for Thursday at 2PM."
    }
  }
}
```
(Note: ai_response comes in as a string — if needed, you can json.loads() it for structured handling.)