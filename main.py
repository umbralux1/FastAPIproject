from fastapi import FastAPI
from fastapi.responses import FileResponse

html_path = "index.html"
app = FastAPI()


@app.get("/")
async def roo():
    return FileResponse(html_path)

