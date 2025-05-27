from fastapi import FastAPI
from app.scheduler import start_polling

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    start_polling()
