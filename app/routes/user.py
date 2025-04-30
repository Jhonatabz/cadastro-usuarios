from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.user import User, UserPublic, UserDB, UserList
from db.database import database

templates = Jinja2Templates(directory='templates')

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def form(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@router.post('/cadastrar', response_class=HTMLResponse)
async def create_user(request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...)
):
    user = User(nome=nome, email=email, senha=senha)

    email_existe = any(user.email == email for user in database)
    if email_existe:
        return templates.TemplateResponse(
            "erro.html",
            {"request": request, "user": user},
            status_code=400
        )

    user_with_id = UserDB(
        id= len(database) + 1,
        **user.model_dump()
    )
    database.append(user_with_id)

    user_public = UserPublic(**user_with_id.model_dump(exclude={'senha'}))
    return templates.TemplateResponse("resposta.html", {"request": request, "user": user_public.model_dump()})

@router.get('/usuarios', response_class=HTMLResponse)
async def read_user(request: Request):
    users_safe = [user.model_dump(exclude={"senha"}) for user in database]
    return templates.TemplateResponse("usuarios.html", {"request": request, "users": users_safe})