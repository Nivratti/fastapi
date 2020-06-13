from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def main():
    # sending it as a attachment
    # specify filename to send it as attachment
    some_file_path = "dog_bgr.png"
    return FileResponse(some_file_path, filename="f.png")