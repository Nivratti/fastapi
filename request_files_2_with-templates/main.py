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


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    filenames = [file.filename for file in files]
    dest = os.path.join(UPLOAD_DIR, filenames[0])
    save_upload_file(upload_file=files[0], destination=dest)
    return {"filenames": filenames}


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
