from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='app/templates/home')

home_app = APIRouter()

@home_app.get("/", response_class=HTMLResponse, status_code=200)
async def form(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})