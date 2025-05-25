import requests
from app.config import OLLAMA_MODEL, SYSTEM_PROMPT_PATH

class OllamaAPI:
    def __init__(self):
        self.api_url = "http://localhost:11434/api/generate"
        self.model_name = OLLAMA_MODEL
        with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as f:
            self.system_prompt = f.read()

    def send_prompt(self, user_prompt: str) -> str:
        payload = {
            "model": self.model_name,
            "system": self.system_prompt,
            "prompt": user_prompt,
            "stream": False,
            "format": "json"
        }

        try:
            res = requests.post(self.api_url, json=payload)
            res.raise_for_status()
            return res.json().get("response", "No response from the model.")
        except requests.RequestException as e:
            return f"Error talking to Ollama: {e}"

