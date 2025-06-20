from pydantic import BaseModel, EmailStr

class Admin(BaseModel):
    nome: str
    email: EmailStr
    senha: str
class AdminVerify(BaseModel):
    email: EmailStr
    senha: str