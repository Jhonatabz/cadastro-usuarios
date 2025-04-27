from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.user import User, UserPublic, UserDB
from db.database import database

templates = Jinja2Templates(directory='templates')

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def mostrar_formulario(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@router.post('/cadastrar', response_model=UserPublic)
async def create_user(
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...)
):
    user = User(nome=nome, email=email, senha=senha)
    user_with_id = UserDB(
        id= len(database) + 1,
        **user.model_dump()
    )
    database.append(user_with_id)
    return user_with_id
