from fastapi import FastAPI
from .email_routes import router

app = FastAPI(title="ARTEMIS Mailer")

app.include_router(router, prefix="/email")

@app.get("/")
def root():
    return {"message": "ARTEMIS Mailer is online, bitch 😘"}
