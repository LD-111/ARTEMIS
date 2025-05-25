from fastapi import FastAPI
from app.router import router

app = FastAPI(title="ARTEMIS AI Router")

app.include_router(router, prefix="/ai")

@app.get("/")
def root():
    return {"message": "AI router online and pumpin' reps 💪"}
