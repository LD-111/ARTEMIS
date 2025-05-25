from fastapi import APIRouter
from app.schemas import ProcessRequest, ProcessResponse
from app.ollama_client import OllamaAPI

router = APIRouter()
ollama = OllamaAPI()

@router.post("/process", response_model=ProcessResponse)
def process_command(req: ProcessRequest):
    email = req.content

    user_prompt = f"""{{
  "sender": "{email.sender}",
  "subject": "{email.subject}",
  "payload": "{email.payload}"
}}"""

    ai_response = ollama.send_prompt(user_prompt)

    return {
        "status": "success",
        "ai_response": ai_response
    }

