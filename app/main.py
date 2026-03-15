from fastapi import FastAPI
from app.api.stock_api import router as stock_router

app = FastAPI()

app.include_router(stock_router)

@app.get("/")
def home():
    return {"message": "AI Engine Running"}