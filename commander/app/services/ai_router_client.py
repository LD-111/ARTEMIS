# app/services/ai_router_client.py
import requests
import json
from app.config import AI_ROUTER_API_URL  # 💥 pull from config now

def process_with_ai(email):
    response = requests.post(f"{AI_ROUTER_API_URL}/ai/process", json=email)
    if not response.ok:
        print(f"❌ AI Router Error: {response.text}")
        return {}

    try:
        ai_raw = response.json().get("ai_response", "{}")

        # If it's a string, parse it again
        if isinstance(ai_raw, str):
            return json.loads(ai_raw)
        
        return ai_raw  # if it somehow already came parsed
    except Exception as e:
        print(f"❌ Failed to parse AI response: {e}")
        return {}

