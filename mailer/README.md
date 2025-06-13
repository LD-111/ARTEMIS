# 📬 ARTEMIS Mailer Microservice

**Welcome to the mail-slingin' arm of Project ARTEMIS.**  
This microservice handles Gmail-based sending and reading of emails via the Gmail API, wrapped in a clean FastAPI interface.

---

## 💼 Features

- ✉️ Send emails via Gmail
- 📥 Read unread emails from a specified sender
- 🧠 Parses emails into structured JSON for AI routing
- 🔐 OAuth2 authentication via Gmail API
- 🚀 REST API powered by FastAPI

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone <your-private-repo-url>
cd artemis/mailer
```

### 2. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Add Google Credentials

- Download your credentials.json from Google Cloud Console (OAuth Client ID)

- Place it in the mailer/ directory

- The first time you run the service, it will generate a token.json after OAuth flow

### 4. Run the Microservice

```bash
uvicorn app.main:app --reload
```

## 🧪 API Endpoints

### POST /email/send

Send a Gmail message

JSON Body:

```json
{
  "to": "recipient@gmail.com",
  "subject": "Hello!",
  "body": "ARTEMIS reporting for booty... I mean, duty."
}
```

### GET /email/read

Read unread messages from a specific sender

JSON Body:

```json
{
  "from_email": "someone@example.com"
}
```

Returns a list of parsed emails.

## 🔐 OAuth Notes

- This service runs in Testing Mode by default

- Make sure your Google account is added to the OAuth Consent Screen > Test Users

- You’ll see a warning during OAuth flow — just click Advanced > Continue