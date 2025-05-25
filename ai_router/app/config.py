import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "dolphin-mixtral:latest")
SYSTEM_PROMPT_PATH = os.getenv("ARTEMIS_SYSTEM_PROMPT", "app/prompts/default.txt")
