import os
from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


UPLOAD_DIR = "uploaded"
os.makedirs(UPLOAD_DIR, exist_ok=True)
from fastapi_file_helper import save_upload_file

@app.post("/uploadfile/")
async def create_upload_files(file: UploadFile = File(...)):
    dest = os.path.join(UPLOAD_DIR, file.filename)
    save_upload_file(
        upload_file=file, destination=dest
    )
    filename = file.filename
    return {"filename": filename}


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
