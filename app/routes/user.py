from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.models.user import User, UserVerify
import app.db._connection as database

templates = Jinja2Templates(directory='app/templates/user')

user_app = APIRouter()

@user_app.get("/usuario/login", response_class=HTMLResponse, status_code=201)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@user_app.get("/usuario/cadastrar", response_class=HTMLResponse, status_code=201)
async def cadastrar_form(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@user_app.post("/usuario/login")
async def login_user(request: Request,
    email: str = Form(...),
    senha: str = Form(...)
):
    user = UserVerify(email=email, senha=senha)
    verificacao = database.verificar_login_usuario(**user.model_dump())
    if verificacao:
        return templates.TemplateResponse("login_response.html", {"request": request})
    else: 
        return templates.TemplateResponse("cadastro_error.html", {"request": request, "email": email})

@user_app.post('/usuario/cadastrar', response_class=HTMLResponse, status_code=200)
async def create_user(request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...)
):
    user = User(nome=nome, email=email, senha=senha)
    inserir = database.inserir_usuario(**user.model_dump())
    if inserir:
        return templates.TemplateResponse("cadastro_response.html", {"request": request, "user": {"nome": nome, "email": email}})
    else:
        return templates.TemplateResponse("cadastro_error.html", {"request": request, "email": email})