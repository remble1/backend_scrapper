from typing import Union

from fastapi import FastAPI

app = FastAPI()

# hello
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


# scrapper
@app.get("/hello")
def hello():
    return {"Heello": "World"}
