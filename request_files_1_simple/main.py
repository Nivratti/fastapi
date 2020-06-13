import os
from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

UPLOAD_DIR = "uploaded"
os.makedirs(UPLOAD_DIR, exist_ok=True)
from fastapi_file_helper import save_upload_file

@app.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    filenames = [file.filename for file in files]
    dest = os.path.join(UPLOAD_DIR, filenames[0])
    save_upload_file(upload_file=files[0], destination=dest)
    return {"filenames": filenames}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file">
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)