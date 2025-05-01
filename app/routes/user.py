from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.models.user import User, UserPublic, UserDB
from app.db.users_database import database

templates = Jinja2Templates(directory='app/templates/user')

user_app = APIRouter()

@user_app.get("/usuario/login", response_class=HTMLResponse, status_code=201)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@user_app.post("/usuario/login")
async def login_user(request: Request):
    return templates.TemplateResponse("login_response.html", {"request": request})

@user_app.get("/usuario/cadastrar", response_class=HTMLResponse, status_code=201)
async def cadastrar_form(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@user_app.post('/usuario/cadastrar', response_class=HTMLResponse, status_code=200)
async def create_user(request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...)
):
    user = User(nome=nome, email=email, senha=senha)

    email_existe = any(user.email == email for user in database)
    if email_existe:
        return templates.TemplateResponse("cadastro_error.html", {"request": request, "email": user.email}, status_code=400)

    user_with_id = UserDB(
        id= len(database) + 1,
        **user.model_dump()
    )
    database.append(user_with_id)
    user_public = UserPublic(**user_with_id.model_dump(exclude={'senha'}))
    
    return templates.TemplateResponse("cadastro_response.html", {"request": request, "user": user_public.model_dump()})