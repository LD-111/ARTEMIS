# app/scheduler.py
from app.config import POLLING_INTERVAL, TARGET_SENDER

from app.services.mailer_client import read_emails, send_email
from app.services.ai_router_client import process_with_ai
import time, threading
import json

def poll_and_process():
    while True:
        try:
            print("⏰ Polling for new emails...")
            emails = read_emails(TARGET_SENDER)

            for email in emails:
                try:
                    print("📩 Raw email:", json.dumps(email, indent=2))
                    print(f"📨 Processing email from {email['content']['sender']}")
                    ai_payload = {
                        "content": {
                            "sender": email["content"]["sender"],
                            "subject": email["content"]["subject"],
                            "payload": email["content"]["body"]
                        }
                    }
                    ai_response = process_with_ai(ai_payload)

                    print(f"🤖 AI response: {ai_response}")

                    if ai_response.get("action") == "send_email":
                        content = ai_response["content"]
                        send_email(
                            to=content["receiver"],
                            subject=content["subject"],
                            body=content["body"]
                        )
                except KeyError as e:
                    print(f"❌ Malformed email data, missing key: {e}")
                except Exception as e:
                    print(f"❌ Error processing email: {e}")
                    # Continue to next email instead of crashing
                    continue

        except Exception as e:
            print(f"❌ Error in polling loop: {e}")
        
        time.sleep(POLLING_INTERVAL)

def start_polling():
    thread = threading.Thread(target=poll_and_process, daemon=True)
    thread.start()