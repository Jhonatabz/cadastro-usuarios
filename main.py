from fastapi import FastAPI
from app.routes import home, user, admin

app = FastAPI()

app.include_router(home.home_app)
app.include_router(user.user_app)
app.include_router(admin.admin_app)
