from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# Home Page
@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# Login Page
@app.get("/login")
async def login_page(request: Request):

    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )


# Login Form Submit
@app.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):

    return {
        "username": username,
        "password": password
    }