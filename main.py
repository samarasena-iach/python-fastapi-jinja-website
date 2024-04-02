# Tutorial : FastAPI Simple Website with Jinja2 Template
# https://www.youtube.com/watch?v=yK2Ktl6O894

from fastapi import FastAPI, Request, Form, UploadFile, File, Depends
from fastapi.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import base64
import requests
import os

os.environ['REQUESTS_CA_BUNDLE'] = 'C:/Users/AU256UR/Downloads/Zscaler Root CA.crt'

templates = Jinja2Templates(directory="templates")

app = FastAPI(title="InfraWiz",
              docs_url="/docs",
              version="0.0.1")

app.mount("/static", StaticFiles(directory="static", html=True), name="static")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/new_project")
def new_project(request: Request):
    return templates.TemplateResponse("new_project.html", {"request": request})

@app.get("/projects_list")
def new_project(request: Request):
    return templates.TemplateResponse("projects_list.html", {"request": request})

@app.post("/projects_list")
def new_project(request: Request):
    return templates.TemplateResponse("projects_list.html", {"request": request})

@app.post("/submit_form")
async def handle_form(project_name: str = Form(...),
                      cloud_service_provider: str = Form(...),
                      description: str = Form(...),
                      file_upload: UploadFile = File(...)):
    file_content = await file_upload.read()

    with open(f"static/images/uploads/{file_upload.filename}", "wb") as f:
        f.write(file_content)

    local_path = f"static/images/uploads/{file_upload.filename}"
    img_url = await upload(local_path)
    print("IMAGE URL: ", img_url)

    return RedirectResponse("/projects_list")

async def upload(image):
    with open(image, "rb") as img:
        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key": 'e601a932b245c10cc0ecf3db7b177bdf',
            "image": base64.b64encode(img.read()),
        }
        res = requests.post(url, payload)

        img_url = ""
        if res.status_code == 200:
            json_response = res.json()
            img_url = json_response["data"]["url"]
            return img_url
        else:
            print("HTTP Error:", res.status_code)
