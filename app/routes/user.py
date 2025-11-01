from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.models.user import User, UserVerify
import app.db._connection as database
from app.routes.deps import get_current_user

templates = Jinja2Templates(directory='app/templates/user')

user_router = APIRouter(prefix="/usuario", tags=["Usu\u00e1rio"])


def _get_user_from_session(request: Request):
    email = request.session.get('user_email')
    if email:
        return {'email': email}
    return None


@user_router.get("/login", response_class=HTMLResponse, status_code=200)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "user": _get_user_from_session(request)})


@user_router.get("/cadastrar", response_class=HTMLResponse, status_code=200)
async def cadastrar_form(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request, "user": _get_user_from_session(request)})


@user_router.post("/login", response_class=HTMLResponse, status_code=200)
async def login_user(request: Request,
    email: str = Form(...),
    senha: str = Form(...)
):
    user = UserVerify(email=email, senha=senha)
    verificacao = database.verificar_login_usuario(**user.model_dump())
    if verificacao:
        # set session
        request.session['user_email'] = email
        return templates.TemplateResponse("login_response.html", {"request": request, "user": _get_user_from_session(request)})
    else:
        return templates.TemplateResponse("login_error.html", {"request": request, "email": email, "user": _get_user_from_session(request)})


@user_router.get('/logout')
async def logout(request: Request):
    request.session.pop('user_email', None)
    # redirect to login page after logout
    return RedirectResponse(url="/usuario/login", status_code=302)


@user_router.post('/cadastrar', response_class=HTMLResponse, status_code=200)
async def create_user(request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...)
):
    verificar_email = database.email_existe(email)

    if verificar_email:
        return templates.TemplateResponse("cadastro_error.html", {"request": request, "email": email, "user": _get_user_from_session(request)})
    else:
        user = User(nome=nome, email=email, senha=senha)
        # inserir_usuario espera a senha em texto e fará o hash internamente
    success = database.inserir_usuario(nome, email, senha)
    # passar o novo usuário (nome/email) para o template; para o contexto autenticado, mantemos a chave 'user'
    return templates.TemplateResponse("cadastro_response.html", {"request": request, "user": {"nome": nome, "email": email}, "user": _get_user_from_session(request)})



@user_router.get('/profile', response_class=HTMLResponse)
async def profile(request: Request, current_user: dict = Depends(get_current_user)):
    return templates.TemplateResponse('profile.html', {"request": request, "user": current_user})