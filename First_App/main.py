from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoginData(BaseModel):

    username: str
    password: str


@app.post("/login")
async def login(data: LoginData):

    return {
        "username": data.username
    }