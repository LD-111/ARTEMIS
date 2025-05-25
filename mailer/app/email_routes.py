from fastapi import APIRouter
from .schemas import EmailRequest, EmailQuery
from . import gmail_service

router = APIRouter()

@router.post("/send")
def send_email(req: EmailRequest):
    gmail_service.send_email(req.to, req.subject, req.body)
    return {"status": "sent"}

@router.get("/read")
def read_emails(req: EmailQuery):
    emails = gmail_service.read_unread_emails(req.from_email)
    return {"emails": emails}
