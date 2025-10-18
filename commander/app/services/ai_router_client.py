# app/services/ai_router_client.py
import requests
import json
from app.config import AI_ROUTER_API_URL

def process_with_ai(email):
    try:
        response = requests.post(
            f"{AI_ROUTER_API_URL}/ai/process", 
            json=email,
            timeout=30  # AI processing might take longer
        )
        if not response.ok:
            print(f"❌ AI Router Error: {response.text}")
            return {}

        ai_raw = response.json().get("ai_response", "{}")

        # If it's a string, parse it again
        if isinstance(ai_raw, str):
            return json.loads(ai_raw)
        
        return ai_raw
    except requests.exceptions.ConnectionError:
        print(f"❌ Cannot connect to AI Router service at {AI_ROUTER_API_URL}")
        return {}
    except requests.exceptions.Timeout:
        print(f"❌ AI Router service timeout at {AI_ROUTER_API_URL}")
        return {}
    except json.JSONDecodeError as e:
        print(f"❌ Failed to parse AI response: {e}")
        return {}
    except Exception as e:
        print(f"❌ Unexpected error processing with AI: {e}")
        return {}