from fastapi import FastAPI
import uvicorn
import app.db._connection as database

database.conectar_usuarios()
database.criar_tabela_usuarios()
database.conectar_admin()
database.criar_tabela_admin()

app = FastAPI()

from app.routes import home, user, admin

app.include_router(home.home_app)
app.include_router(user.user_app)
app.include_router(admin.admin_app)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)