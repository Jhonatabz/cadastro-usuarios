from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from app.models.admin import Admin, AdminVerify
import app.db._connection as database

templates = Jinja2Templates(directory="app/templates/admin")

admin_app = APIRouter()

@admin_app.get("/admin/login")
async def login_admin(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@admin_app.get("/admin/cadastrar")
async def create_admin(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@admin_app.get("/admin/usuarios")
async def read_users(request: Request):
    return templates.TemplateResponse("usuarios.html", {"request": request})

@admin_app.post("/admin/login")
async def login_admin(request: Request,
    email: str = Form(...),
    senha: str = Form(...)
):
    admin = AdminVerify(email=email, senha=senha)
    verificacao = database.verificar_login_admin(**admin.model_dump())
    if verificacao:
        return templates.TemplateResponse("login_response.html", {"request": request})
    else: 
        return templates.TemplateResponse("cadastro_error.html", {"request": request, "email": email})

@admin_app.post("/admin/cadastrar")
async def create_admin(request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...)
):
    admin = Admin(nome=nome, email=email, senha=senha)
    inserir = database.inserir_admin(**admin.model_dump())
    if inserir:
        return templates.TemplateResponse("cadastro_response.html", {"request": request, "admin": {"nome": nome, "email": email}})
    else:
        return templates.TemplateResponse("cadastro_error.html", {"request": request, "email": email})