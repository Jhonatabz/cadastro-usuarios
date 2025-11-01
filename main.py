from fastapi import FastAPI
import uvicorn
import app.db._connection as database
from starlette.middleware.sessions import SessionMiddleware
import os


database.conectar_usuarios()
database.criar_tabela_usuarios()
database.conectar_admin()
database.criar_tabela_admin()

app = FastAPI()

# SECRET_KEY used for signing session cookies. In production, set this via environment variable.
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-change-me')
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

from app.routes import home, user, admin

app.include_router(home.home_app)
app.include_router(user.user_router)
app.include_router(admin.admin_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)