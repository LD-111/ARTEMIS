# app/services/mailer_client.py
import requests
from app.config import MAILER_API_URL  # 💥 pull from config now

def read_emails(from_email):
    response = requests.get(f"{MAILER_API_URL}/email/read", json={"from_email": from_email})
    if not response.ok:
        print(f"❌ Failed to fetch emails: {response.text}")
        return []

    data = response.json()
    emails = data.get("emails", [])
    return emails

def send_email(to, subject, body):
    payload = {
        "to": to,
        "subject": subject,
        "body": body
    }
    response = requests.post(f"{MAILER_API_URL}/email/send", json=payload)
    if not response.ok:
        print(f"❌ Failed to send email: {response.text}")
    else:
        print(f"✅ Email sent to {to}")
