from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.db.users_database import database

templates = Jinja2Templates(directory="app/templates/admin")

admin_app = APIRouter()

@admin_app.get("/admin/login")
async def login_admin(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@admin_app.get("/admin/cadastrar")
async def create_admin(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@admin_app.get('usuario/usuarios', response_class=HTMLResponse, status_code=201)
async def read_user(request: Request):
    users_safe = [user.model_dump(exclude={"senha"}) for user in database]
    return templates.TemplateResponse("usuarios.html", {"request": request, "users": users_safe})