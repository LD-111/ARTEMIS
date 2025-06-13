# app/config.py
import os
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(dotenv_path=env_path)

MAILER_API_URL = os.getenv("MAILER_API_URL")
AI_ROUTER_API_URL = os.getenv("AI_ROUTER_API_URL")
POLLING_INTERVAL = int(os.getenv("POLLING_INTERVAL", 60))
TARGET_SENDER = os.getenv("TARGET_SENDER")
