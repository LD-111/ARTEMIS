from pydantic import BaseModel

class EmailContent(BaseModel):
    sender: str
    subject: str
    payload: str

class ProcessRequest(BaseModel):
    content: EmailContent

class ProcessResponse(BaseModel):
    status: str
    ai_response: str
