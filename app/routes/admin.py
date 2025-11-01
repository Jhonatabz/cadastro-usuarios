from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.models.admin import Admin, AdminVerify
import app.db._connection as database

templates = Jinja2Templates(directory="app/templates/admin")

admin_router = APIRouter(prefix="/admin", tags=["Administrador"])

@admin_router.get("/login", response_class=HTMLResponse, status_code=200)
async def login_admin(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@admin_router.get("/cadastrar", response_class=HTMLResponse, status_code=200)
async def create_admin(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@admin_router.get("/usuarios", response_class=HTMLResponse, status_code=200)
async def read_users(request: Request):
    usuarios = database.buscar_usuarios()
    return templates.TemplateResponse("usuarios.html", {"request": request, "users": usuarios})


@admin_router.post('/usuarios/deletar/{user_id}')
async def delete_user(request: Request, user_id: int):
    database.deletar_usuario(user_id)
    # redirect back to the list
    return RedirectResponse(url='/admin/usuarios', status_code=302)

@admin_router.post("/login", response_class=HTMLResponse, status_code=200)
async def login_admin(request: Request,
    email: str = Form(...),
    senha: str = Form(...)
):
    admin = AdminVerify(email=email, senha=senha)
    verificacao = database.verificar_login_admin(**admin.model_dump())
    if verificacao:
        return templates.TemplateResponse("login_response.html", {"request": request})
    else: 
        return templates.TemplateResponse("login_error.html", {"request": request, "email": email})

@admin_router.post("/cadastrar", response_class=HTMLResponse, status_code=200)
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