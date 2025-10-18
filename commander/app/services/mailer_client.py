# app/services/mailer_client.py
import requests
from app.config import MAILER_API_URL  # 💥 pull from config now

def read_emails(from_email):
    try:
        response = requests.get(
            f"{MAILER_API_URL}/email/read", 
            json={"from_email": from_email},
            timeout=10
        )
        if not response.ok:
            print(f"❌ Failed to fetch emails: {response.text}")
            return []

        data = response.json()
        emails = data.get("emails", [])
        return emails
    except requests.exceptions.ConnectionError:
        print(f"❌ Cannot connect to Mailer service at {MAILER_API_URL}")
        return []
    except requests.exceptions.Timeout:
        print(f"❌ Mailer service timeout at {MAILER_API_URL}")
        return []
    except Exception as e:
        print(f"❌ Unexpected error reading emails: {e}")
        return []

def send_email(to, subject, body):
    payload = {
        "to": to,
        "subject": subject,
        "body": body
    }
    try:
        response = requests.post(
            f"{MAILER_API_URL}/email/send", 
            json=payload,
            timeout=10
        )
        if not response.ok:
            print(f"❌ Failed to send email: {response.text}")
        else:
            print(f"✅ Email sent to {to}")
    except requests.exceptions.ConnectionError:
        print(f"❌ Cannot connect to Mailer service at {MAILER_API_URL}")
    except requests.exceptions.Timeout:
        print(f"❌ Mailer service timeout at {MAILER_API_URL}")
    except Exception as e:
        print(f"❌ Unexpected error sending email: {e}")