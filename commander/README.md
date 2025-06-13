# 🧩 ARTEMIS Commander Microservice

This microservice coordinates all others—receiving high-level input and issuing instructions to components like the Mailer and AI Router.

---

## ⚙️ Role in the System

The Commander runs the full loop of the ARTEMIS system:

1. **Email Check** 👉 Triggers the Mailer to fetch new unread emails.
2. **AI Processing** 👉 Passes parsed emails to the AI Router to interpret and decide on actions.
3. **Execution** 👉 Sends back AI-decided replies through the Mailer.
4. **Future-Ready** 👉 Can be extended to support calendar scheduling, database access, Slack messages, and whatever else you throw at it.

---

## 🧠 Features

- 📬 Triggers Gmail inbox polling via the Mailer service.
- 🧠 Passes incoming mail to the AI Router for interpretation.
- 📤 Dispatches AI-generated responses as real emails.
- 🧱 Modular structure – plug in new microservices as needed.
- 📡 Central orchestration logic.

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
cd artemis/commander
```
2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Add Environment Configuration

Create a .env file in the root with:
```env
MAILER_API_URL=http://localhost:8001
AI_ROUTER_API_URL=http://localhost:8002
POLLING_INTERVAL=30 
TARGET_SENDER={email here}
```
Change the ports/hosts to match your actual deployment setup. For now, it only works with an authorized email to avoid answering to every mail, perhaps a proper filter could be added in the future.
## 🚀 Running the Microservice
```bash
uvicorn app.main:app --reload
```
Defaults to running on http://localhost:8000.
## 🔁 How It Works (Request Flow)

1. Trigger endpoint (e.g. /run) is called manually or on a timer.
2. Commander:
    - Calls GET /email/read on the Mailer.

    - For each message, calls POST /ai/process on the AI Router.

    - Parses the response.

    - Sends results via POST /email/send through the Mailer.
