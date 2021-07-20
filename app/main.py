import requests
from app.src.sth_func import asd
from fastapi import FastAPI

app = FastAPI()


@app.post("/")
async def root():
    return []

@app.get("/up")
async def root():
    response = requests.post("http://localhost:8000/")
    
    return response