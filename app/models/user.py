from pydantic import BaseModel, EmailStr

class User(BaseModel):
    nome: str
    email: EmailStr
    senha: str
class UserVerify(BaseModel):
    email: EmailStr
    senha: str