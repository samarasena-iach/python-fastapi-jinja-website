# Tutorial : FastAPI Simple Website with Jinja2 Template
# https://www.youtube.com/watch?v=yK2Ktl6O894

from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about")
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/contact")
def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})