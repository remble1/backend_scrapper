from typing import Union
from fastapi import FastAPI
import json
from src.tool import fetch_data, api
app = FastAPI()

# hello
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# scrapper
@app.get("/get_advice")
async def advice():
    response = await fetch_data(api)
    response = json.loads(response)
    return f"{response['activity']}"


