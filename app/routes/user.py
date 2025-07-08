from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.models.user import User, UserVerify
import app.db._connection as database

templates = Jinja2Templates(directory='app/templates/user')

user_router = APIRouter(prefix="/usuario", tags=["Usuário"])

@user_router.get("/login", response_class=HTMLResponse, status_code=200)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@user_router.get("/cadastrar", response_class=HTMLResponse, status_code=200)
async def cadastrar_form(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@user_router.post("/login", response_class=HTMLResponse, status_code=200)
async def login_user(request: Request,
    email: str = Form(...),
    senha: str = Form(...)
):
    user = UserVerify(email=email, senha=senha)
    verificacao = database.verificar_login_usuario(**user.model_dump())
    if verificacao:
        return templates.TemplateResponse("login_response.html", {"request": request})
    else: 
        return templates.TemplateResponse("login_error.html", {"request": request, "email": email})

@user_router.post('/cadastrar', response_class=HTMLResponse, status_code=200)
async def create_user(request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...)
):
    verificar_email = database.email_existe(email)

    if verificar_email:
        return templates.TemplateResponse("cadastro_error.html", {"request": request, "email": email})
    else:
        user = User(nome=nome, email=email, senha=senha)
        database.inserir_usuario(**user.model_dump())
        return templates.TemplateResponse("cadastro_response.html", {"request": request, "user": {"nome": nome, "email": email}})