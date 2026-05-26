from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoginData(BaseModel):

    username: str
    password: str


@app.get("/")
async def home():

    return {"message": "Home Page"}


@app.post("/")
async def login(data: LoginData):

    return {
        "username": data.username
    }