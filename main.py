from fastapi import FastAPI
from app.routes import home, user, admin
import uvicorn
import app.db.connection as database

database.conectar()
database.criar_tabela()

app = FastAPI()

app.include_router(home.home_app)
app.include_router(user.user_app)
app.include_router(admin.admin_app)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)