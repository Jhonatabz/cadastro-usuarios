from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates/admin")

admin_app = APIRouter()

@admin_app.get("/admin/login")
async def login_admin(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@admin_app.get("/admin/cadastrar")
async def create_admin(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@admin_app.get("/admin/usuarios")
async def read_user(request: Request):
    return templates.TemplateResponse("usuarios.html", {"request": request})